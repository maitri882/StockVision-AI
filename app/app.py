import streamlit as st
from PIL import Image
import json
import plotly.express as px
import pandas as pd

import pickle
model = pickle.load(open('model\\model.pickle','rb'))

with open("model\stock_list.json",'r') as f:
    stock_names = json.load(f)

#data = pd.read_csv('dataset/stock_data.csv')

def main():
    title = 'Stock Price Predictor'
    st.set_page_config(page_title=title, page_icon="📈") 
    st.title("Stock Price Predictor 📉")

    st.markdown("### Wanna know about trends in stock price?\n##### Start your journey from here.")
    img = Image.open('app\\Lovepik_com-611154772-Financial stock business vector illustration.png')
    st.image(img, width=450)

    st.write('')
    st.write('')

    stock_name = st.selectbox('Select the stock name', stock_names)
    high = st.number_input('Enter the high price for your stock', min_value= 0.00)
    low = st.number_input('Enter the low price for your stock',min_value=0.00)
    open = st.number_input('Enter the open price for your stock',min_value=0.00)
    volume = st.number_input('Enter the Volume of your stock',min_value=1)

    if st.button("Estimate Price"):
        try:
            Model = model
            prediction = Model.predict([[high,low,open,volume,stock_names.index(stock_name)]])
            close_price = round(prediction[0],2)
            st.success("Estimated closing price of your stock is {} INR".format(close_price))
        except:
            st.warning("Oops!! Something went wrong\nTry again")

    if st.button("Show Visualizations"):
        img1 = Image.open('eda_images\\newplot.png')
        st.image(img1, caption='Variation in opening price')

        img2 = Image.open('eda_images\\newplot (1).png')
        st.image(img2, caption='Variation in closing price')


    

if __name__ == '__main__':
    main()