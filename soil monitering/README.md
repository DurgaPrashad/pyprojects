Crop Recommendation System
Overview
This project is a Flask web application designed to recommend the most suitable crop to grow based on various soil and weather conditions. It uses a pre-trained machine learning model to make predictions.

Project Structure
app.py: The main Flask application file that handles routing and prediction logic.
Crop_recommendation.csv: The dataset containing soil and weather parameters along with the recommended crops.
standscaler.pkl: The standard scaler used to preprocess the input features.
minmaxscaler.pkl: The min-max scaler used to preprocess the input features.
templates/index.html: The HTML form for user input.
Features
Model Loading
Loads a pre-trained machine learning model and scalers using the pickle module.
Flask App Initialization
Initializes a Flask application.
Routes
Root Route (/): Serves an HTML form for user input.
Predict Route (/predict): Handles form submissions, processes input features, scales them, and uses the model to predict the recommended crop.
How to Run
Clone the repository.
Install the required dependencies:

Verify

Open In Editor
Edit
Copy code
pip install flask numpy pandas scikit-learn
Run the Flask application:

Verify

Open In Editor
Edit
Copy code
python app.py
Open your web browser and navigate to http://127.0.0.1:5000/.
Usage
Enter the soil and weather parameters (Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall) into the form.
Submit the form to get the recommended crop.
Example
The Crop_recommendation.csv file contains data with the following columns:

N: Nitrogen content in the soil
P: Phosphorus content in the soil
K: Potassium content in the soil
Temperature: Temperature in degrees Celsius
Humidity: Humidity percentage
pH: pH level of the soil
Rainfall: Rainfall in mm
Crop: The recommended crop (e.g., maize)
License
