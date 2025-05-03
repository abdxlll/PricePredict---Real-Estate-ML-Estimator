# House Price Prediction

## Overview
This project demonstrates house price prediction using machine learning. It utilizes a dataset with house features to predict house prices. The model is built using **scikit-learn** and serves predictions through a **Streamlit web application**.

## Features
- Predicts house prices based on user-provided features like bedrooms, bathrooms, square footage, etc.
- **Streamlit** web interface for interactive use.
- Displays visualizations to help analyze data trends and model performance.
- Built for educational purposes with a simple user interface to demonstrate the capabilities of machine learning.

## Technologies Used
- **Python**
- **Pandas** (for data manipulation)
- **NumPy** (for numerical computations)
- **Scikit-Learn** (for machine learning models)
- **Matplotlib** / **Seaborn** (for data visualizations)
- **Streamlit** (for building the interactive web application)

## Getting Started

Follow these steps to run this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/abdxlll/house-price-prediction.git
   cd house-price-prediction
   
2. Install the required packages
   ```bash
   pip install -r requirements.txt

3. Run the application:
   To launch the Streamlit web app, run:
   ```bash
   streamlit run modelUserInterface.py

## Notes
- **Model File:** The trained model is saved as model.pkl and is used to make predictions in the web app.

- **Streamlit Interface:** The Streamlit interface allows you to input house feature values and receive a price prediction in real-time.



