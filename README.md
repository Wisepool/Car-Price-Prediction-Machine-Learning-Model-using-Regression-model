# Car Price Prediction Machine Learning Model 🚗📊

This project is a machine learning-based web application that predicts the price of a used car based on user inputs like brand, year of manufacture, kilometers driven, fuel type, and more.

---

## 🔧 Project Structure

- **`Untitled.ipynb`** – Contains code for:
  - Data preprocessing  
  - Exploratory Data Analysis (EDA)  
  - Feature engineering  
  - Model training using `LinearRegression` from `scikit-learn`  
  - Model evaluation  
  - Saving the trained model to `model.pkl` using `pickle`  

- **`app.py`** – A Streamlit web app that:
  - Loads the trained model  
  - Takes user inputs from the sidebar and main interface  
  - Processes the inputs to match the trained model’s expected format  
  - Predicts the car price based on the inputs  
  - Displays the predicted price in real time  

- **`cardetails.csv`** – The dataset used for training and testing.

- **`model.pkl`** – The saved trained Linear Regression model.

---

## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/Wisepool/Car-Price-Prediction-Machine-Learning-Model.git
   cd Car-Price-Prediction-Machine-Learning-Model
   ```

2. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```
