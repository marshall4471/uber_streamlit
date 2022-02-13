import streamlit as st
import numpy as np
import string
import pickle
import xgboost
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('model.pkl','rb'))


def main():
  st.sidebar.header("Uber fare Cost prediction")
  st.sidebar.text("This a Web app that tells you the predicted fare costs for Uber.")
  st.sidebar.header("Just fill in the information below")
  st.sidebar.text("The XGboost Regressor Model was used.")



  pickup_longitude = st.slider("Input Your Pickup Longitude", -180, 180)
  pickup_latitude = st.slider("Input your Pickup Latitude",-90,90)
  dropoff_longitude= st.slider("Input your Dropoff Longitude", -180, 180)
  dropoff_latitude= st.slider("Input your Dropoff Ltitude",-90,90)
  passenger_count= st.slider("Input your passenger Count", 1,6)

  inputs = [[pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,passenger_count]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(float)
    st.success('The your predicted fare Costs will be{}'.format(updated_res))


if __name__ =='__main__':
  main()
