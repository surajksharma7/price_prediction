import streamlit as st
import pandas as pd
import pickle

# Load the saved model from the pickle file
with open('linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title('Placement Prediction App')

# CGPA input
cgpa_to_predict = st.number_input('Enter CGPA value to predict placement:', min_value=0.0, max_value=10.0, value=8.0, step=0.1)

# Predict placement for the input CGPA value
predicted_placement = model.predict([[cgpa_to_predict]])

# Convert prediction to scalar value
predicted_placement = round(predicted_placement[0], 2)
cgpa_to_predict = round(cgpa_to_predict,2)

# Display the prediction
if st.button('Predict'):
    st.write(f"For CGPA {cgpa_to_predict}, predicted placement status: {predicted_placement}")
