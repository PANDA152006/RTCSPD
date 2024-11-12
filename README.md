# 📈 Stock Candlestick Chart with Pattern Detection and Chatbot Integration

This project offers an interactive web-based platform for visualizing stock candlestick charts, detecting chart patterns, and interacting through a chatbot interface. The frontend is hosted on **Netlify**, and the backend runs on a **VPS** using **Flask**.

## ✨ Features

- 🔥 **Real-Time Candlestick Charting**: Visualizes stock prices with up-to-date candlestick data.
- 🔍 **Pattern Detection**: Automatically recognizes common candlestick patterns (e.g., Doji, Hammer, Engulfing).
- 🔎 **Stock Search Suggestions**: Get autocomplete suggestions for stock ticker symbols.

## 🏗️ Architecture

The project is divided into:

- **Frontend**: Hosted on **Netlify** using HTML, CSS, and JavaScript.
- **Backend**: Hosted on a **VPS** using **Flask** for real-time data retrieval and pattern detection.

For an in-depth look at the architecture, refer to the `component_diagram.png` in the root directory.

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+** for backend
- **Node.js and npm** (optional for frontend development)
- **Netlify** and **VPS** accounts

### Backend Setup (VPS)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/stock-candlestick-chart.git
   cd stock-candlestick-chart/backend
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Flask App**:
   ```bash
   python main.py
   ```

4. **Access the App**: Use your VPS IP address to access the backend.

### Frontend Deployment (vultr)
2. **Update Backend URL**: Modify `<iframe>` and API calls in `index.html` to point to the VPS backend.

## 📂 Project Structure

```
stock-candlestick-chart/
├── backend/
│   ├── main.py               # Flask API for stock data retrieval
│   ├── requirements.txt       # Backend dependencies
│   └── component_diagram.png  # Architecture diagram
├── frontend/
│   ├── index.html             # Main HTML file
│   ├── style.css              # Stylesheet
│   └── app.js                 # JavaScript logic
└── README.md                  # Project documentation
```

## 🛠️ Technologies Used

- **Backend**: 🐍 Python, Flask, yfinance, TA-Lib, NumPy, Matplotlib
- **Frontend**: 🌐 HTML5, CSS3, JavaScript, Netlify
- **Pattern Recognition**: TA-Lib for candlestick pattern analysis

## 🌍 Deployment

1. **Frontend**: Deploy to vultr.
2. **Backend**: Host on a VPS and run `main.py`.
3. **Link Frontend to Backend**: Update the API URL in `index.html` to point to your VPS backend.

## 📖 Usage

1. **Open the Web App**: Access via the Netlify-deployed link.
2. **Enter Stock Symbol**: Use the search bar to fetch candlestick data.
3. **View Patterns**: Identified patterns will be highlighted on the chart.
4. **Chatbot Interaction**: Use the chatbot for help and further insights.

## 📜 License

This project is licensed under the [MIT License](LICENSE).
