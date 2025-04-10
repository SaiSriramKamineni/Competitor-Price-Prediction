# competitor_price_app.py
import streamlit as st
import joblib

model = joblib.load('D:/2/competitor_price_prediction_model.pkl')

st.title("💹 Competitor Price Prediction")

features = ['Market_Price_per_ton', 'Demand_Index', 'Supply_Index',
            'Economic_Indicator', 'Weather_Impact_Score', 'Seasonal_Factor', 'Consumer_Trend_Index']

inputs = [st.number_input(f"Enter {f}:", value=0.0) for f in features]

if st.button("Predict Competitor Price"):
    prediction = model.predict([inputs])[0]
    st.success(f"Predicted Competitor Price per ton: ₹{prediction:.2f}")
