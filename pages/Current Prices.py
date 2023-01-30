import streamlit as st
import yfinance as fn


def get_ticker(name):
    company = fn.Ticker(name)
    return company


st.markdown("# Current Prices")
st.sidebar.markdown("# Current Prices")
textInput = st.text_input(
    "Company Name",
    max_chars=10,
    placeholder="Type Company Name Here!",
    label_visibility="visible"
)
startDate = st.date_input("Start Date")
endDate = st.date_input("End Date- Must be at least one day after Start Date")

c1 = get_ticker(textInput)
data = c1.history(period="3mo")

# Gets a selected company's information on button press
runButton = st.button("See Prices")
if runButton:
    try:
        stock = fn.Ticker(textInput)
        ticker = fn.download(textInput, start=startDate, end=endDate)
        st.write(ticker)
        ticker.drop(["High", "Low", "Close", "Volume"], inplace=True, axis=1)
        st.line_chart(ticker, x=None, y=None)
        price = stock.info["regularMarketPrice"]

        if price == None:
            st.write("No live price to display, markets are currently closed!")
        else:
            st.header(price)
            print(price)
    except:
        print("there was an error")
        st.write("an error occurred, make sure your format is correct")
