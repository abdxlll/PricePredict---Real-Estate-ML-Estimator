# House Price Prediction

## Overview
This project is a simulation designed to demonstrate the concept of house price prediction using machine learning. It was developed for the Bay Area Science and Engineering Fair (BASEF) and was awarded a Bronze Merit Award. The project is intended for educational purposes and is not meant to be used for actual real-world predictions or decision-making.

## Features
- Simulates house price predictions based on user-input features.
- User-friendly interface for demonstrating the model's functionality.
- Visualizations to analyze data trends and model performance.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib / Seaborn (for visualizations)
- Streamlit (for the web application)

## Getting Started
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/abdxlll/house-price-prediction.git
   cd house-price-prediction
   
2. Install the required packages
   ```bash
   pip install -r requirements.txt

3. Run the application:
   ```bash
   streamlit run modelUserInterface.py

## Adjusting File Paths
Some parts of the code use absolute file paths specific to the developer's environment. To run the project on your local machine, you may need to update these paths.

### Steps to Change File Paths

1. **Locate the Absolute Paths**: Search for absolute paths in the following files:
   - `modelBuild.ipynb`
   - `modelUserInterface.py`

2. **Update Paths**: Replace the paths with the appropriate paths for your system. For example:
   ```python
   # Original path in the code
   data = pd.read_csv('C:/Users/xxxxx/Projects/HousePricePrediction/data.csv')
   
   # Change it to your local path
   data = pd.read_csv('/path/to/your/local/data.csv')


