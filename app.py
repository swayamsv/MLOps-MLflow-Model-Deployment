
import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

API_URL = "http://127.0.0.1:5001/invocations"

st.title("🏠 House Price Prediction")
st.caption("Powered by MLflow Model Serving")

st.info("Enter house details to get a prediction from our registered Gradient Boosting model.")

col1, col2 = st.columns(2)

with col1:
    longitude = st.number_input("Longitude", value=-122.25)
    latitude = st.number_input("Latitude", value=37.85)
    housing_median_age = st.number_input(
        "Housing Median Age", value=30, min_value=0
    )
    total_rooms = st.number_input("Total Rooms", value=1500, min_value=1)
    total_bedrooms = st.number_input("Total Bedrooms", value=300, min_value=0)

with col2:
    population = st.number_input("Population", value=800, min_value=0)
    households = st.number_input("Households", value=250, min_value=1)
    median_income = st.number_input("Median Income", value=7.5, min_value=0.0)
    ocean_proximity = st.selectbox(
        "Ocean Proximity",
        ["NEAR BAY", "INLAND", "NEAR OCEAN", "<1H OCEAN", "ISLAND"]
    )

if st.button("Predict House Price", type="primary"):

    columns = [
        "longitude",
        "latitude",
        "housing_median_age",
        "total_rooms",
        "total_bedrooms",
        "population",
        "households",
        "median_income",
        "ocean_proximity"
    ]

    values = [[
        longitude,
        latitude,
        housing_median_age,
        total_rooms,
        total_bedrooms,
        population,
        households,
        median_income,
        ocean_proximity
    ]]

    payload = {
        "dataframe_split": {
            "columns": columns,
            "data": values
        }
    }

    try:
        response = requests.post(
            API_URL,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            prediction = result["predictions"][0]

            st.success("Prediction generated successfully!")

            st.metric(
                "Estimated House Price",
                f"${prediction:,.2f}"
            )

            st.write("API Status:", response.status_code)
            st.json(result)

        else:
            st.error(f"API Error: {response.status_code}")
            st.code(response.text)

    except requests.exceptions.RequestException as e:
        st.error("Unable to connect to MLflow Model Serving.")
        st.write(str(e))
