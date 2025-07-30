### Project Overview
This project provides an intelligent way to analyse any Indian stock using the ChatGPT-4o-mini API. It loads a list of all Indian stock market symbols and lets users select a stock via an interactive selectbox. The analyser then fetches real-time data, interprets trends, and generates clear insights in natural language, helping investors make informed decisions.

# AI Powered Stock Price Analyzer 📈

An intelligent web application that analyzes stock price trends using AI-powered insights. This tool fetches real-time stock data from Yahoo Finance and provides comprehensive analysis using OpenAI's GPT-4 model, making complex financial data accessible to beginners and experienced investors alike.

## 🚀 Features

- **Real-time Stock Data**: Fetches weekly stock data from Yahoo Finance for the past year
- **AI-Powered Analysis**: Uses OpenAI's GPT-4 model to analyze stock trends and patterns
- **User-Friendly Interface**: Clean Streamlit web interface with dropdown selection
- **Comprehensive Database**: Includes thousands of stocks from the National Stock Exchange of India
- **Beginner-Friendly**: Provides easy-to-understand explanations of complex financial data
- **Return Calculations**: Automatically calculates expected returns over the analysis period

## 🛠️ Technology Stack

- **Backend**: Python 3.9+
- **Web Framework**: Streamlit
- **AI/ML**: OpenAI GPT-4 API
- **Data Scraping**: BeautifulSoup4, Requests
- **Data Processing**: Pandas
- **Environment Management**: Python-dotenv

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.9 or higher installed
- An OpenAI API key (get one from [OpenAI Platform](https://platform.openai.com/))
- Internet connection for fetching stock data

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-powered-stock-price-analyzer.git
   cd ai-powered-stock-price-analyzer
   ```

2. **Install dependencies**
   
   Using pip:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using uv (recommended):
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🚀 Usage

1. **Run the application**
   ```bash
   streamlit run main.py
   ```

2. **Access the web interface**
   - Open your browser and go to `http://localhost:8501`
   - Select a company from the dropdown menu
   - Click "Analyze" to get AI-powered stock analysis

3. **View the analysis**
   - The application will fetch the latest stock data
   - AI will analyze trends, patterns, and provide insights
   - Results include expected returns and beginner-friendly explanations

## 📁 Project Structure

```
ai-powered-stock-price-analyzer/
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── stocks.csv             # Stock database (CSV format)
├── stocks.pkl             # Stock database (pickle format)
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore file
├── README.md             # This file
└── llm/                  # Virtual environment directory
```

## 🔍 How It Works

1. **Data Fetching**: The application uses Yahoo Finance's historical data API to fetch weekly stock prices for the past year
2. **Data Processing**: Raw HTML data is parsed and cleaned using BeautifulSoup
3. **AI Analysis**: The cleaned data is sent to OpenAI's GPT-4 model for intelligent analysis
4. **Results Display**: Analysis results are formatted in Markdown and displayed in the Streamlit interface

## 📊 Sample Analysis Output

The AI provides comprehensive analysis including:
- Stock price trends and patterns
- Volatility analysis
- Support and resistance levels
- Expected returns calculation
- Beginner-friendly explanations
- Investment recommendations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and informational purposes only. It should not be considered as financial advice. Always do your own research and consult with a financial advisor before making investment decisions.

## 🐛 Troubleshooting

**Common Issues:**

1. **OpenAI API Key Error**: Make sure your `.env` file contains a valid OpenAI API key
2. **Stock Data Not Found**: Some stocks might not have sufficient historical data
3. **Network Issues**: Ensure you have a stable internet connection for data fetching

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Ensure you're using the latest version of the application

## 🔄 Updates

Stay updated with the latest features and improvements by:
- Starring this repository
- Watching for updates
- Checking the releases page

---

**Made with ❤️ for the investing community**