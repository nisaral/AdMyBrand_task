import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import date, timedelta

# --- 1. DATA GENERATION ---
# We'll create a more realistic dataset for our campaigns.

# Helper function to generate random dates
def random_dates(start, end, n=10):
    start_u = start.toordinal()
    end_u = end.toordinal()
    return [date.fromordinal(np.random.randint(start_u, end_u)) for _ in range(n)]

# Generate campaign data
np.random.seed(42)
num_campaigns = 50
statuses = ['Active', 'Completed', 'Paused', 'Planning']
start_dates = random_dates(date(2023, 1, 1), date(2024, 7, 30), num_campaigns)

campaigns = []
for i in range(num_campaigns):
    start_date = start_dates[i]
    end_date = start_date + timedelta(days=np.random.randint(30, 90))
    budget = np.random.randint(2000, 15000)
    status = np.random.choice(statuses, p=[0.3, 0.4, 0.2, 0.1])
    
    if status == 'Completed':
        spend = budget
    elif status == 'Active':
        spend = np.random.uniform(0.3, 0.9) * budget
    elif status == 'Paused':
        spend = np.random.uniform(0.1, 0.5) * budget
    else: # Planning
        spend = 0
        
    # Make conversions loosely related to spend
    conversions = int(spend / np.random.uniform(20, 50))

    campaigns.append({
        'id': f'CAM{i+1:03d}',
        'name': f'Campaign {i+1} - {np.random.choice(["Brand", "Promo", "Seasonal", "Launch"])}',
        'status': status,
        'startDate': start_date.isoformat(),
        'endDate': end_date.isoformat(),
        'budget': round(budget),
        'spend': round(spend),
        'conversions': conversions,
    })

# Generate time-series data for revenue
time_series_data = []
current_date = date(2024, 1, 1)
base_revenue = 4000
for i in range(7): # 7 months of data
    month_name = current_date.strftime("%b")
    # Add some noise and trend
    revenue = base_revenue + (i * 300) + np.random.randint(-500, 500)
    time_series_data.append({
        'name': month_name,
        'revenue': round(revenue),
        'month_index': i
    })
    current_date += timedelta(days=31)


# --- 2. MODEL TRAINING & PREDICTION ---
# Train a simple model on the time-series data to forecast revenue.

df = pd.DataFrame(time_series_data)
X = df[['month_index']] # Features
y = df['revenue']       # Target

model = LinearRegression()
model.fit(X, y)

# Predict the next 3 months
future_months_indices = np.arange(7, 10).reshape(-1, 1)
future_predictions = model.predict(future_months_indices)

# Create the forecast data structure
forecast_data = []
future_month_names = ['Aug', 'Sep', 'Oct']
for i, prediction in enumerate(future_predictions):
    forecast_data.append({
        'name': future_month_names[i],
        'forecast': round(prediction),
        'month_index': 7 + i
    })

# Combine historical and forecast data for the chart
chart_data = []
for item in time_series_data:
    chart_data.append({
        'name': item['name'],
        'revenue': item['revenue'],
        'forecast': None # No forecast for historical data
    })
for item in forecast_data:
    chart_data.append({
        'name': item['name'],
        'revenue': None, # No actual revenue for future data
        'forecast': item['forecast']
    })


# --- 3. ASSEMBLE FINAL JSON OUTPUT ---
# This is the JSON object we'll copy into our React app.

final_data = {
    "metrics": [
        {"id": "revenue", "title": "Total Revenue", "value": "$324,540", "change": "+15.2%", "changeType": "increase"},
        {"id": "users", "title": "New Customers", "value": "1,230", "change": "+8.5%", "changeType": "increase"},
        {"id": "conversions", "title": "Conversion Rate", "value": "4.8%", "change": "-0.5%", "changeType": "decrease"},
        {"id": "spend", "title": "Ad Spend", "value": "$21,890", "change": "+20%", "changeType": "increase"}
    ],
    "revenueForecastData": chart_data,
    "campaigns": campaigns,
    "conversionsByChannel": [
        { "channel": 'Organic', "conversions": 4200 },
        { "channel": 'Social', "conversions": 2800 },
        { "channel": 'Referral', "conversions": 1500 },
        { "channel": 'Email', "conversions": 1200 },
        { "channel": 'Paid', "conversions": 3500 },
    ]
}

# Print the JSON output
print(json.dumps(final_data, indent=4))

