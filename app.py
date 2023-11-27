import streamlit as st
import pickle
import pandas as pd

# Load( the Random Forest model)
rf_model = pickle.load(open("svm", "rb"))

# Load (the ordinal encoder)
enc = pickle.load(open("transformer1", "rb"))

def predict_price(features):

    # Then convert features to a DataFrame
    features_df = pd.DataFrame([features], columns=["age", "hp_kW", "km", "Gearing_Type", "make_model"])

    # Apply the ordinal encoder to the categorical features
    features_df[["Gearing_Type", "make_model"]] = enc.transform(features_df[["Gearing_Type", "make_model"]])

    # Make predictions using the Random Forest model
    predicted_price = svm.predict(features_df)
    return predicted_price

def main():

    st.set_page_config(
        page_title="Car Price Prediction App",
        page_icon="🚗",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.title("Car Price Prediction App")

    # manually enter values
    st.write("### Enter the car details Please:")
    age = st.slider("Car's Age", min_value=1, max_value=20, value=5)
    hp_kW = st.slider("Horsepower (kW)", min_value=50, max_value=500, value=100)
    km = st.slider("Kilometers driven", min_value=0, max_value=200000, value=50000)

    # choose Gearing Type and Car Model from a list
    gearing_type_options = ["Automatic", "Manual", "Semi-automatic"]
    selected_gearing_type = st.selectbox("Gearing Type", gearing_type_options)

    make_model_options = ["Audi A3", "Audi A1", "Opel Insignia", "Opel Astra", "Opel Corsa", "Renault Clio", "Renault Espace", "Renault Duster", "Audi A2"]
    selected_make_model = st.selectbox("Car Model", make_model_options)

    # input features
    features = {
        "age": age,
        "hp_kW": hp_kW,
        "km": km,
        "Gearing_Type": selected_gearing_type,
        "make_model": selected_make_model
    }

    # Make prediction
    if st.button("Predict Price", key="predict_button"):
        predicted_price = predict_price([features["age"], features["hp_kW"], features["km"], features["Gearing_Type"], features["make_model"]])
        st.success(f"### Predicted Price: {predicted_price[0]:,.2f} USD")

if __name__ == "__main__":
    main()










