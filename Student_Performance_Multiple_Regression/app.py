import streamlit as st
import pickle
import numpy as np

# Load the models
with open('maths_model.pkl', 'rb') as file:
    maths_model = pickle.load(file)

with open('portuguese_model.pkl', 'rb') as file:
    portuguese_model = pickle.load(file)

# Load the scaler
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Define the common features
common_features = ['higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc',
                   'Walc', 'health', 'absences_M']

# Function to make predictions
def predict_performance(model, features):
    features = np.array(features).reshape(1, -1)
    features = scaler.transform(features)  # Apply the scaler
    prediction = model.predict(features)
    return prediction

# Streamlit interface
st.title('Student Performance Prediction')

# Input fields for features
st.write('Enter the features:')
features = []
for feature in common_features:
    value = st.text_input(f'{feature}', value='0')
    value = int(value)  # Convert to integer
    features.append(value)

# Make predictions
if st.button('Predict'):
    maths_prediction = predict_performance(maths_model, features)
    portuguese_prediction = predict_performance(portuguese_model, features)
    
    st.write('Predicted performance for Mathematics:')
    st.write(f'G_1: {maths_prediction[0][0].round(0)}')
    st.write(f'G_2: {maths_prediction[0][1].round(0)}')
    st.write(f'G_3: {maths_prediction[0][2].round(0)}')
    
    st.write('Predicted performance for Portuguese:')
    st.write(f'G_1: {portuguese_prediction[0][0].round(0)}')
    st.write(f'G_2: {portuguese_prediction[0][1].round(0)}')
    st.write(f'G_3: {portuguese_prediction[0][2].round(0)}')