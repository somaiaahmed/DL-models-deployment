
# House Price Prediction Application

This is a Flask web application that predicts house prices based on various features such as the number of bedrooms, bathrooms, floors, and the year the house was built, using a trained machine learning model.

## Features

- User-friendly web interface to input house details.
- Predicts house prices based on the input features using a machine learning model.
- Displays the prediction result on a separate page.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Pickle**: For loading the trained machine learning model.
- **HTML/CSS**: For the front-end user interface.

## Installation

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### Step 2: Install Required Packages

You can create a virtual environment and install the necessary dependencies:

```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install Flask
pip install Flask
```

### Step 3: Place the Model File

Make sure to have the `housePrice_model.pkl` file in the project directory. This file should be your pre-trained model.

### Step 4: Run the Application

You can run the Flask application with the following command:

```bash
python app.py
```

### Step 5: Access the Application

Open your web browser and go to `http://127.0.0.1:5000/` to access the House Price Prediction application.

## How to Use

1. Enter the number of bedrooms, bathrooms, floors, and the year built in the provided fields.
2. Click the "Predict" button.
3. You will be redirected to a new page displaying the predicted house price.

