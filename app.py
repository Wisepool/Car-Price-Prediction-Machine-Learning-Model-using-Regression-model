import numpy as np
import pandas as pd
import pickle as pk
import streamlit as st


regressor = pk.load(open('model.pkl' , 'rb'))
st.header('CAR PRICE PREDICTION MACHINE LEARNING MODEL')
df1 = pd.read_csv('cardetails.csv')
def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()
df1['name'] = df1['name'].apply(get_brand_name)

brand = st.selectbox('Select Car Brand' ,df1['name'].unique() )
year = st.slider('Car Manufactured Year' , 1992 , 2020)
distance = st.slider('Car Distance Driven' , 1 , 200000)
fuel = st.selectbox('Fuel Type' , df1['fuel'].unique())
owner = st.selectbox('Owner' , df1['owner'].unique())
transmission = st.selectbox('Transmission' , df1['transmission'].unique())

if st.button('Predict'):
    input_data_model = pd.DataFrame(
        [[brand, year, distance, fuel, transmission, owner]],
        columns=['name', 'year', 'km_driven', 'fuel', 'transmission', 'owner']
    )

    input_data_model['fuel'].replace(
        ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'], 
        [1, 2, 3, 4, 5], inplace=True
    )
    input_data_model['transmission'].replace(
        ['Manual', 'Automatic'], 
        [1, 2], inplace=True
    )
    input_data_model['owner'].replace(
        ['First Owner', 'Second Owner', 'Fourth & Above Owner', 'Third Owner', 'Test Drive Car'], 
        [1, 2, 3, 4, 5], inplace=True
    )
    input_data_model['name'].replace(
        ['Maruti', 'Hyundai', 'Datsun', 'Honda', 'Tata', 'Chevrolet',
         'Toyota', 'Jaguar', 'Mercedes-Benz', 'Audi', 'Skoda', 'Jeep',
         'BMW', 'Mahindra', 'Ford', 'Nissan', 'Renault', 'Fiat',
         'Volkswagen', 'Volvo', 'Mitsubishi', 'Land', 'Daewoo', 'MG',
         'Force', 'Isuzu', 'OpelCorsa', 'Ambassador', 'Kia'], 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], 
        inplace=True
    )

    input_data_model = input_data_model.apply(pd.to_numeric)

    car_price = regressor.predict(input_data_model)
    st.markdown('Car price is going to be ' + str(car_price[0]))

