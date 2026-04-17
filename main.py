import os
from dotenv import load_dotenv
from IPython.display import Markdown, display
from groq import Groq
import yfinance as yf
from datetime import datetime, timedelta
import pickle
import streamlit as st


load_dotenv()
api_key = os.getenv("Groq_API_KEY")
openai = Groq()
# Define headers for HTTP requests
# This is used to mimic a browser request to avoid being blocked by some websites.

class YahooFinanceWebsite:
    def __init__(self, stock_symbol):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.stock_symbol = stock_symbol.upper()
    def get_stock_data(self):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        weekly_data = yf.download(self.stock_symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'), interval='1wk')
        stock = yf.Ticker(self.stock_symbol)
        info = stock.info
        title = info.get('shortName', 'N/A')
        return title, weekly_data

        return title, html_table_data
def build_stock_analysis_prompt(stock_symbol, title, stock_table_data):
    sys_prompt = r"""You are an assistant that analyzes the contents of table that contains data on a specific stock.
    The table contains the date, open price, close price, low and highs aggregated for every week over one year timeframe. 
    Respond in Markdown format"""
    
    user_prompt = f"The data provided below in the table format for {stock_symbol} from the Yahoo Finances.\
    Make the explaination easy enough for a newbie to understand. \
    Analyze and Summarize the trends on this stock:\n{stock_table_data}\n\n\
    Also, calculate the total returns in percentage one could have expected over this period."
    
    return [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
def analyze_stock_trends(stock_symbol):
    stock_data_page = YahooFinanceWebsite(stock_symbol+'.NS')
    title, stock_table_data = stock_data_page.get_stock_data()
    response = openai.chat.completions.create(
        model = "openai/gpt-oss-120b",
        messages = build_stock_analysis_prompt(stock_symbol, title, stock_table_data)
    )
    return response.choices[0].message.content

def display_analysis(stock_symbol):
    display(Markdown(analyze_stock_trends(stock_symbol)))

st.header('Stock Price Analyzer')
# Load the stocks data from the pickle file
with open('stocks.pkl', 'rb') as f:
    stocks = pickle.load(f)

stocks_name = stocks['Company Name'].values
selected_stock = st.selectbox(
    "Type or select a company name from the dropdown",
    stocks_name
)
# Get the stock symbol based on the selected company name
stock_symbol = stocks[stocks['Company Name'] == selected_stock]['Symbol'].values[0]
st.session_state.stock_symbol = stock_symbol
if st.button('Analyze'):
    if stock_symbol:
        try:
            analysis = analyze_stock_trends(stock_symbol)
            st.markdown(analysis)
        except Exception as e:
            st.error(f"An error occurred while analyzing the stock: {e}")
    else:
        st.warning("Please enter a valid stock symbol.")

