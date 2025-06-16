Car Price Prediction Machine Learning Model 🚗📊
This project is a machine learning-based web application that predicts the price of a used car based on user inputs like brand, year of manufacture, kilometers driven, fuel type, and more.

🔧 Project Structure
Untitled.ipynb – Contains code for:

Data preprocessing

Exploratory data analysis (EDA)

Feature engineering

Model training using LinearRegression from scikit-learn

Model evaluation

Saving the trained model to model.pkl using pickle

app.py – A Streamlit web application that:

Loads the trained model

Takes user inputs from the sidebar and main interface

Processes the inputs to match the trained model’s expected format

Predicts car price based on user inputs

Displays the predicted price in real-time

cardetails.csv – The dataset used for training and testing the model.

model.pkl – The serialized trained Linear Regression model.

🚀 How to Run the Project
Clone the repository

bash
Copy
Edit
git clone https://github.com/Wisepool/Car-Price-Prediction-Machine-Learning-Model.git
cd Car-Price-Prediction-Machine-Learning-Model
Make sure you have all the required packages installed
If not, install them using:

bash
Copy
Edit
pip install -r requirements.txt
Start the web app
Just run the following command in your terminal:

bash
Copy
Edit
streamlit run app.py
