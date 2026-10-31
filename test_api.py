import requests

url = "http://127.0.0.1:5001/invocations"

# Details of a new house
data = {
    "dataframe_split": {
        "columns": [
            "longitude",
            "latitude",
            "housing_median_age",
            "total_rooms",
            "total_bedrooms",
            "population",
            "households",
            "median_income",
            "ocean_proximity"
        ],
        "data": [[
            -122.25,
            37.85,
            30,
            1500,
            300,
            800,
            250,
            7.5,
            "NEAR BAY"
        ]]
    }
}

# Send POST request
response = requests.post(url, json=data)

# Display result
print("Status Code:", response.status_code)
print("API Response:", response.json())