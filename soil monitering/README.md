# Crop Recommendation System

## Overview
This project showcases a dynamic **Flask web application** designed to recommend the most suitable crop based on specific soil and weather conditions. By leveraging a pre-trained machine learning model, it provides precise crop recommendations to optimize agricultural outcomes.

## Project Structure

- **`app.py`**: The core Flask application file responsible for routing and prediction logic.
- **`Crop_recommendation.csv`**: A comprehensive dataset containing essential soil and weather parameters alongside recommended crops.
- **`standscaler.pkl`**: The standard scaler employed to preprocess the input features for consistency.
- **`minmaxscaler.pkl`**: The min-max scaler used to normalize the input features.
- **`templates/index.html`**: A user-friendly HTML form that facilitates user input.

## Features

### 1. **Model Loading**
   - Efficiently loads a pre-trained machine learning model and associated scalers using the `pickle` module.

### 2. **Flask App Initialization**
   - Seamlessly initializes a Flask application to handle user interactions and predictions.

### 3. **Routing**
   - **Root Route (`/`)**: Serves a clean and intuitive HTML form for user input.
   - **Predict Route (`/predict`)**: Handles form submissions, processes input features, scales them, and utilizes the machine learning model to predict the recommended crop.

## How to Run

1. **Clone the Repository**: Get started by cloning the project repository to your local machine.

2. **Install Dependencies**: Ensure all required dependencies are installed by running:

   ```bash
   pip install flask numpy pandas scikit-learn
Run the Flask Application: Start the application with:


python app.py

# Usage
Input Parameters: Enter the following soil and weather parameters into the provided form:

Nitrogen (N): Nitrogen content in the soil.
Phosphorus (P): Phosphorus content in the soil.
Potassium (K): Potassium content in the soil.
Temperature: Temperature in degrees Celsius.
Humidity: Humidity percentage.
pH: Soil pH level.
Rainfall: Rainfall in millimeters.
Get Recommendations: Submit the form to receive a crop recommendation tailored to the provided conditions.

## Example Dataset
The Crop_recommendation.csv file includes data with the following columns:

N: Nitrogen content in the soil
P: Phosphorus content in the soil
K: Potassium content in the soil
Temperature: Temperature in degrees Celsius
Humidity: Humidity percentage
pH: pH level of the soil
Rainfall: Rainfall in millimeters
Crop: The recommended crop (e.g., maize)
