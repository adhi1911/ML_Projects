import streamlit as st
import pickle
import numpy as np

# Loading models and scaler
with open('maths_model.pkl', 'rb') as file:
    maths_model = pickle.load(file)
with open('portuguese_model.pkl', 'rb') as file:
    portuguese_model = pickle.load(file)
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


common_features = {
    'higher': 'wants to take higher education (binary: yes or no)',
    'internet': 'Internet access at home (binary: yes or no)',
    'romantic': 'with a romantic relationship (binary: yes or no)',
    'famrel': 'quality of family relationships (numeric: from 1 - very bad to 5 - excellent)',
    'freetime': 'free time after school (numeric: from 1 - very low to 5 - very high)',
    'goout': 'going out with friends (numeric: from 1 - very low to 5 - very high)',
    'Dalc': 'workday alcohol consumption (numeric: from 1 - very low to 5 - very high)',
    'Walc': 'weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)',
    'health': 'current health status (numeric: from 1 - very bad to 5 - very good)',
    'absences_M': 'number of school absences (numeric: from 0 to 93)'
}

#Predicting the performance
def predict_performance(model, features):
    features = np.array(features).reshape(1, -1)
    features = scaler.transform(features)  # Apply the scaler
    prediction = model.predict(features)
    return prediction

# Streamlit app
st.title('Student Performance Prediction')

#Feature INput
st.write('Enter the features:')
features = []
for feature, description in common_features.items():
    if feature in ['higher', 'internet', 'romantic']:
        value = st.selectbox(f'{feature} ({description})', ['yes', 'no'])
        value = 1 if value == 'yes' else 0  # Convert to numerical
    else:
        value = st.text_input(f'{feature} ({description})', value='0')
        value = int(value)  # Convert to integer
    features.append(value)

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