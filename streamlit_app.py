# *********** Step 01: Import all the required libraries and module *******************

# Streamlit for user interface
import streamlit as st
# For Numerical calculations
import numpy as np
# To use the saved and downloaded model
import joblib
# To interact with operating system
import os
# *************************************************************************************

# ************ Step 02: Load the trained model, encoder and scaler ********************

# Load the downloaded trained model
model = joblib.load('rf_iris_model.pkl')

# Load the downloaded leber_encoder
le = joblib.load("lebel_encoder.pkl")

# Load the downloaded scaler
scaler = joblib.load('scaler.pkl')

# **************************************************************************************

############### Code to show the image of the predicted lebel (Optional)###############

# Function to show species image
def show_species_image(species_name):
    image_path = f"{species_name}.jpg" # it will check image names i.e (Iris-setosa, Iris-versicolor, Iris-virginica)
    if os.path.exists(image_path):
        st.image(image_path, caption=species_name, use_container_width=True)
    else:
        st.warning(f"No image found for {species_name}")


#######################################################################################

# ************* Step 03: Build the streamlit app ***************************************
# Streamlit app title
st.title("Iris Species Classification App")

st.write("Enter the following features to predict its specie")

# Input fields for all features
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0)

# A button and its work to predict
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    scaled_input = scaler.transform(input_data) # will scale the input data, as the fetures during training were scaled
    prediction = model.predict(scaled_input) # It will predict the encoded classes i.e (0,1,2)
    # To transform the encoded classes again to its original form i.e (Iris-setosa, Iris-versicolor, Iris-virginica)
    species_name = le.inverse_transform([prediction[0]])[0]
    st.success(f"Predicted Iris Specie is: {species_name}")

    # Show the corresponding image of the predicted class, (Optional)
    show_species_image(species_name)

# *************************************************************************************