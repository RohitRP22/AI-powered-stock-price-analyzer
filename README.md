# AI Powered Stock Price Analyzer 📈

A Streamlit-based stock analysis app that uses Yahoo Finance data and Groq's chat completion API to generate natural-language trend summaries and return calculations for Indian stocks.

## 🔎 What this app does

- Loads a list of companies from `stocks.pkl`
- Lets you select a company name using a Streamlit dropdown
- Fetches weekly historical stock data for the past year from Yahoo Finance using `yfinance`
- Sends the stock table to Groq's chat API for AI-powered analysis
- Displays the resulting Markdown analysis in the Streamlit app

## 🚀 Features

- Weekly stock data retrieval for the last 12 months
- Indian stock symbol support via `.NS` suffix
- Company lookup from a preloaded `stocks.pkl` file
- AI-generated insights and summary
- Total return estimation over the selected period

## 🧩 Dependencies

The app relies on:

- Python 3.9+
- `streamlit`
- `yfinance`
- `groq`
- `python-dotenv`
- `pandas`
- `bs4`
- `requests`
- `ipython`
- `ipykernel`

These are defined in `requirements.txt` and `pyproject.toml`.

## ⚙️ Setup

1. Clone the repository:

```bash
git clone https://github.com/RohitRP22/AI-powered-stock-price-analyzer.git
cd "AI Powered Stock Price Analyzer"
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your Groq API key to a `.env` file in the project root:

```env
Groq_API_KEY=your_groq_api_key_here
```

## ▶️ Run the app

```bash
streamlit run main.py
```

Then open the Streamlit URL shown in the terminal (typically `http://localhost:8501`).

## 🧠 How it works

1. The app initializes a `Groq` client with the API key from `.env`.
2. `stocks.pkl` is loaded to populate the company dropdown.
3. When you click `Analyze`, the app:
   - resolves the stock symbol for the selected company
   - appends `.NS` to target the Indian exchange
   - downloads weekly historical prices for the past 365 days
   - builds a prompt describing the stock table and analysis request
   - sends the prompt to Groq's chat completion endpoint
   - renders the returned Markdown in the Streamlit UI

## 🧪 Notes

- The app uses `stock_symbol + '.NS'` for Indian NSE tickers.
- If `stocks.pkl` is missing or the ticker has no historical data, the app may raise an error.
- The prompt asks the AI to analyze weekly open/high/low/close trends and calculate percentage returns.

## 📁 Project files

- `main.py` — application entrypoint and analysis workflow
- `requirements.txt` — Python dependency list
- `pyproject.toml` — package metadata
- `stocks.csv` — stock list source (if present)
- `stocks.pkl` — pickle file loaded by the app
- `.env` — local environment variables (not committed)

## ⚠️ Disclaimer

This project is for educational purposes only. It is not financial advice. Always verify investment decisions with your own research and seek professional guidance before trading.
