import streamlit as st
import yfinance as yf
import streamlit.components.v1 as components
import plotly.express as px

# Define the HTML for the JavaScript widget
html_code = """
<lightning-widget
    name="Support Value For Value"
    accent="#ffffff"
    to="ctenold@strike.me"
    image="https://flyclipart.com/thumb2/bitcoin-logos-brands-and-logotypes-553473.png"
    amounts="1000,5000,10000"
    labels="1000👍,5000⭐🙏,10000🔥🚀👑"
/>

<script src="https://embed.twentyuno.net/js/app.js"></script>
"""

stock_symbols = ["MSTR: Microstrategy", "3350.T: Metaplanet", "SMLR: Semler Scientific, Inc."]#, "AMZN", "TSLA"]
treasury_urls = {"MSTR": "https://bitcointreasuries.net/entities/1", "3350.T":"https://bitcointreasuries.net/entities/176", "SMLR": "https://bitcointreasuries.net/entities/194"}
# Streamlit app
st.title("Stocks App")


# Create a dropdown menu with the list of stock symbols
symbol = st.selectbox("Select a stock symbol", stock_symbols).split(':')[0]
if st.button("Get Quote"):
  st.write(treasury_urls[symbol])
  # st.json(yf.Ticker(symbol).info)
  # Fetch the stock data for the last 5 years
  stock_data = yf.download(symbol, period="5y")

  # Reset the index to have 'Date' as a column
  stock_data.reset_index(inplace=True)

  # Plot the stock price
  fig = px.line(stock_data, x='Date', y='Close', title=f'{symbol} Daily Stock Price (Last 5 Years)', labels={'Close':'Stock Price (USD)'})

  # Display the plot in Streamlit
  st.plotly_chart(fig)
  # st.success("Done")

# Display the custom widget
components.html(html_code, height=600)
