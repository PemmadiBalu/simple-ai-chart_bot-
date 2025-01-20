Simple AI Chart Bot
A lightweight and interactive bot to generate charts and provide AI-powered insights from your data. This bot allows you to upload data, visualize it using various chart types, and query the data for trends or summaries using AI.
Features
📝 Data Input: Accepts CSV, Excel, or manual data input.
📊 Chart Generation: Generates bar charts, line graphs, scatter plots, and more.
🤖 AI-Powered Analysis: Answer questions about trends, patterns, and summaries using OpenAI's API.
🌐 Web Interface: A user-friendly interface built with Flask.
🚀 Customizable: Extend the bot to support additional chart types or analysis features.
Installation
Clone this repository:
git clone https://github.com/yourusername/simple-ai-chart_bot.git
cd simple-ai-chart_bot

Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

Add your OpenAI API Key in the .env file:
OPENAI_API_KEY=your-api-key
Usage

Run the Application
Start the Flask server:
python app.py

Open your browser and go to:
http://127.0.0.1:5000
Generate Charts
Upload a CSV file or manually input data.
Choose the chart type (e.g., bar, pie, line).
View and download the generated chart.
Ask AI
Type a query like:
"What is the trend in sales?"
"Summarize the data insights."
Example Screenshot
<img src="example_chart.png" alt="Example Chart" width="600">
Technologies Used
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
Charting Libraries: Matplotlib, Plotly
AI Integration: OpenAI API
Deployment: Flask (local) or Streamlit Cloud
Contributing
Fork this repository.

Create a new branch:
git checkout -b feature-name
Make your changes and commit:

git commit -m "Add your message here"
Push to your branch:

git push origin feature-name
Create a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

