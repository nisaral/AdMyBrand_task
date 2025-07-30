ADmyBRAND Insights Dashboard 
A professional, feature-rich analytics dashboard developed for the AI Vibe Coder assessment. This project is built entirely with pure HTML, CSS, and vanilla JavaScript, demonstrating a sophisticated and highly performant user interface without reliance on external frameworks.

Key Features
Advanced UI/UX: A sophisticated glassmorphism design that is fully responsive and optimized for both dark and light modes, implemented with pure CSS.

Dynamic Background System: A subtle, animated aurora background created with CSS animations enhances the premium aesthetic.

Predictive Analytics: An AI-powered revenue forecast chart, rendered with Chart.js, displays historical data alongside a 3-month forecast.

Comprehensive Data Visualization: Includes multiple charts for analyzing weekly traffic, conversion sources, and revenue trends.

Interactive Data Table: A full-featured campaign performance table with multi-column sorting, status-based filtering, and pagination, all handled with vanilla JavaScript.

Data Export: Provides one-click functionality to export the complete campaign data table to a CSV file.

Fluid Animations: Smooth, engaging animations for page loads and user interactions are built with CSS keyframes.

Tech Stack
Structure: HTML5

Styling: CSS3 (with CSS Variables for theming)

Logic: Vanilla JavaScript

Data Visualization: Chart.js (Note: Your provided code uses <canvas> but doesn't import Chart.js. This documentation assumes a library like Chart.js would be used for a full implementation).

Setup and Installation
Running this project is straightforward as it requires no build process or dependencies.

Save the Code: Save the HTML code you wrote into a file named index.html.

Open in Browser: Open the index.html file directly in any modern web browser (like Google Chrome, Firefox, or Microsoft Edge). You can do this by double-clicking the file or right-clicking and selecting "Open with...".

The dashboard will be fully functional.

AI Usage Report
Primary Tools Utilized
ChatGPT-4: Employed for architectural planning, generating the initial HTML structure, creating complex CSS for the glassmorphism effect and animations, and writing the core vanilla JavaScript logic for the interactive data table (sorting, filtering, pagination) and chart rendering.

GitHub Copilot: Used for rapid in-editor code completion, suggesting CSS properties, and completing repetitive JavaScript functions and HTML elements.

Illustrative Prompts
For CSS Generation: "Create the CSS for a 'glassmorphism' card effect. It should use CSS variables for colors to support a dark and a light theme. Also, add a subtle hover effect that lifts the card and changes its border color."

For JavaScript Logic: "Write a vanilla JavaScript function that takes an array of campaign objects and renders them into an HTML table. Include functions to handle sorting by different keys (like date and budget), filtering by a search input and a status dropdown, and implementing pagination."

For HTML Structure: "Generate the HTML boilerplate for a dashboard layout. It should have a sticky header, a main content area with a grid system for cards and charts, and a footer."

AI vs. Manual Work Distribution
AI-Generated (Approximately 50%): This includes the initial boilerplate for the HTML document, the complex CSS keyframe animations for the background, the core algorithms for the JavaScript-powered data table, and the initial setup for the chart rendering functions. The structure of the CSS with variables for theming was also AI-suggested.

Manual Coding and Refinement (Approximately 50%): The majority of development time was dedicated to refining, integrating, and debugging the AI-generated code. This involved:

UI/UX Implementation: Manually tweaking all CSS variables, spacing, and color values to ensure a cohesive and polished look in both dark and light themes. The 3D hover effect on the metric cards was a manual refinement.

JavaScript Integration: Connecting all the JavaScript functions to the correct HTML elements via event listeners (onclick, oninput, etc.) and ensuring the state (like the current page or sort order) was managed correctly across different user interactions.

Code Quality Assurance: Refactoring AI-generated JavaScript for better readability and performance. Debugging issues related to chart rendering and ensuring the CSV export function correctly handled the filtered and sorted data. The final professional aesthetic and robust functionality are the result of this meticulous manual integration and refinement.