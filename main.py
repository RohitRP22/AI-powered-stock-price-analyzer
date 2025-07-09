import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI
from urllib.parse import urlencode
import datetime
import pickle
import streamlit as st


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI()
# Define headers for HTTP requests
# This is used to mimic a browser request to avoid being blocked by some websites.
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class YahooFinanceWebsite:
    def __init__(self, stock_symbol):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.stock_symbol = stock_symbol.upper()
    def __build_url(self, params):
        base_url = f"https://finance.yahoo.com/quote/{self.stock_symbol}/history/"
        query_string = urlencode(params)
        return f"{base_url}?{query_string}"
    def get_stock_data(self):
        datetime_now = datetime.datetime.now()
        datetime_year_ago = datetime_now - datetime.timedelta(days=365)
        params = {"frequency": "1wk", "period1": datetime_year_ago.timestamp(), "period2": datetime_now.timestamp()}
        url = self.__build_url(params)
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()

        html_table_data = soup.find("table")

        return title, html_table_data
def build_stock_analysis_prompt(stock_symbol, title, stock_table_data):
    sys_prompt = r"""You are an assistant that analyzes the contents of HTML formated table that contains data on a specific stock.
    The HTML table contains the date, open price, close price, low and highs aggregated for every week over one year timeframe.
    Ignoring text, tags or html attributes that might be navigation related. 
    Respond in Markdown format"""
    
    user_prompt = f"The data provided below in the HTML table format for {stock_symbol} from the Yahoo Finances.\
    Make the explaination easy enough for a newbie to understand. \
    Analyze and Summarize the trends on this stock:\n{stock_table_data}\n\n\
    Also, calculate the total returns in percentage one could have expected over this period."
    
    return [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}]
    
def analyze_stock_trends(stock_symbol):
    stock_data_page = YahooFinanceWebsite(stock_symbol)
    title, stock_table_data = stock_data_page.get_stock_data()
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
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

