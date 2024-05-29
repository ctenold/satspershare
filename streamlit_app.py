import streamlit as st
import yfinance as yf
from streamlit_extras.chart_container import chart_container
import plotly.express as px

# Define the HTML for the JavaScript widget
html_code = """
<lightning-widget
    name="Support Value For Value"
    accent="#0E1117"
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
st.title("SatsPerShare")


# Create a dropdown menu with the list of stock symbols
symbol = st.selectbox("Select a stock symbol", stock_symbols).split(':')[0]
if st.button("Get Quote"):
  # st.write(treasury_urls[symbol])
  # st.json(yf.Ticker(symbol).info)
  # Fetch the stock data for the last 5 years
  stock_data = yf.download(symbol, period="5y")

  # Reset the index to have 'Date' as a column
  stock_data.reset_index(inplace=True)
  with chart_container(stock_data):
    # st.write("Here's a cool chart")
    # st.area_chart(chart_data)
  # Plot the stock price
    fig = px.line(stock_data, x='Date', y='Close', title=f'{symbol} Daily Stock Price (Last 5 Years)', labels={'Close':'Stock Price (USD)'})
    fig.update_layout(height=600)
    fig.add_annotation(
      text="SatsPerShare.streamlit.app",
      xref="paper", yref="paper",
      x=0.5, y=0.05,  # x, y coordinates on the plotting area, x=0.5 is center horizontally, y=0 is bottom
      xanchor='center', yanchor='top',
      showarrow=False,
      font=dict(size=14))
    st.plotly_chart(fig,use_container_width=True,height=800)
  # Display the plot in Streamlit
  # st.plotly_chart(fig)
  # st.write("Sources:" , treasury_urls[symbol])
  # st.success("Done")

# Display the custom widget
# components.html(html_code, height=350)
# st.write("Author: www.x.com/coletenold")
st.markdown(
    "Author: [ColeTenold](www.x.com/coletenold)"
)