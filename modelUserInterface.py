import streamlit as st  # Importing Streamlit for web app creation
import pandas as pd  # Importing pandas for data manipulation
import joblib  # Importing joblib for loading the trained model
from category_encoders import MEstimateEncoder  # Importing MEstimateEncoder for encoding categorical features

# Load the dataset
data = pd.read_csv('data/data.csv')

# Load the trained machine learning model
model = joblib.load('models/model.pkl')

# Mapping of city names to corresponding numerical codes
city_map = {
    "Shoreline": 1, "Seattle": 2, "Kent": 3, "Bellevue": 4, "Redmond": 5,
    "Maple Valley": 6, "North Bend": 7, "Lake Forest Park": 8, "Sammamish": 9,
    "Auburn": 10, "Des Moines": 11, "Bothell": 12, "Federal Way": 13,
    "Kirkland": 14, "Issaquah": 15, "Woodinville": 16, "Normandy Park": 18,
    "Fall City": 18, "Renton": 19, "Carnation": 20, "Snoqualmie": 21,
    "Duvall": 22, "Burien": 23, "Covington": 24, "Inglewood-Finn Hill": 25,
    "Kenmore": 26, "Newcastle": 27, "Mercer Island": 28, "Black Diamond": 29,
    "Ravensdale": 30, "Clyde Hill": 31, "Algona": 32, "Skykomish": 33,
    "Tukwila": 34, "Vashon": 35, "Yarrow Point": 36, "SeaTac": 37,
    "Medina": 38, "Enumclaw": 39, "Snoqualmie Pass": 40, "Pacific": 41,
    "Beaux Arts Village": 42, "Preston": 43, "Milton": 44
}

# Map city names in the dataset to their corresponding numerical codes
data["city_code"] = data["city"].map(city_map)

# Clean the 'statezip' column by removing alphabetical characters
data['statezip'] = data['statezip'].str.replace(r'[a-zA-Z]+', '', regex=True)

# Convert 'statezip' to float for model compatibility
data["statezip"] = data["statezip"].astype(float)

# Drop the 'city' and 'street' columns as they are no longer needed
data = data.drop('city', axis=1)
data = data.drop('street', axis=1)

# Define the features to be used for prediction
home_features = [
    "bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors",
    "waterfront", "view", "condition", "sqft_above", "sqft_basement",
    "yr_built", "yr_renovated", "city_code", "statezip"
]

# Prepare the input features (X) and the target variable (y) for the model
X = data[home_features]  # Input features
y = data["price"]  # Target variable (house price)

# Set the title and subtitle of the Streamlit app
st.title("House Price Prediction")
st.subheader("Enter the details of the house to get an estimated price:")

# User input for various house features
bedrooms = st.slider("Bedrooms", 0, 10, 1)  # Slider for number of bedrooms
bathrooms = st.slider("Bathrooms", 0, 10, 1)  # Slider for number of bathrooms
sqft_living = st.number_input("Living Area in sqft", 500, 10000, 1000)  # Input for living area
sqft_lot = st.number_input("Lot Size in sqft", 1000, 50000, 5000)  # Input for lot size
floors = st.number_input("Number of Floors", 1, 5, 1)  # Input for number of floors
waterfront = st.selectbox("Waterfront", ["No", "Yes"])  # Select box for waterfront
# Convert waterfront to binary (1 for Yes, 0 for No)
if waterfront == "Yes":
    waterfront = 1
else:
    waterfront = 0

# Select box for view rating
view = st.selectbox("View", [0, 1, 2, 3, 4])
# Select box for condition rating
condition = st.selectbox("Condition", [1, 2, 3, 4, 5])
# Input for above ground living area
sqft_above = st.number_input("Above Ground Living Area in sqft", 500, 10000, 1000)
# Input for basement living area
sqft_basement = st.number_input("Basement Living Area in sqft", 0, 10000, 0)
# Input for the year built
yr_built = st.number_input("Year Built", 1900, 2030, 1990)
# Input for the year renovated
yr_renovated = st.number_input("Year Renovated", 1901, 2040, 2001)

# Select box for city name
city_code = st.selectbox("City", [
    "Shoreline", "Seattle", "Kent", "Bellevue", "Redmond", "Maple Valley",
    "North Bend", "Lake Forest Park", "Sammamish", "Auburn", "Des Moines",
    "Bothell", "Federal Way", "Kirkland", "Issaquah", "Woodinville",
    "Normandy Park", "Fall City", "Renton", "Carnation", "Snoqualmie",
    "Duvall", "Burien", "Covington", "Inglewood-Finn Hill", "Kenmore",
    "Newcastle", "Mercer Island", "Black Diamond", "Ravensdale", "Clyde Hill",
    "Algona", "Skykomish", "Tukwila", "Vashon", "Yarrow Point", "SeaTac",
    "Medina", "Enumclaw", "Snoqualmie Pass", "Pacific", "Beaux Arts Village",
    "Preston", "Milton"
])

# Map the selected city name to its corresponding numerical code
city_code = city_map[city_code]
# Input for zip code
statezip = st.number_input("Zipcode", 98001, 99999, 98133)
statezip = float(statezip)  # Convert zip code to float

# Button for submitting the prediction request
submit_button = st.button("Predict Price")

# When the button is pressed, make a prediction
if submit_button:
    # Create a dictionary of input features
    input_dict = {
        'bedrooms': bedrooms, 'bathrooms': bathrooms, 'sqft_living': sqft_living,
        'sqft_lot': sqft_lot, 'floors': floors, 'waterfront': waterfront,
        'view': view, 'condition': condition, 'sqft_above': sqft_above,
        'sqft_basement': sqft_basement, 'yr_built': yr_built,
        'yr_renovated': yr_renovated, 'city_code': city_code, 'statezip': statezip
    }
    
    # Initialize the MEstimateEncoder and fit it on the training data
    encoder = MEstimateEncoder(cols=['city_code'], m=7.0)
    encoder.fit(X, y)  # Fit encoder on input features and target
    
    # Transform the input features using the fitted encoder
    input_transformed = encoder.transform(pd.DataFrame(input_dict, index=[0]))

    # Predict the house price using the model
    predicted_price = model.predict(input_transformed)[0]

    # Display the predicted price to the user
    st.write("The estimated price of this house is $", round(predicted_price, 2))
