
# Iris Flower Prediction Application

This is a Flask web application for predicting the species of an iris flower based on its sepal and petal dimensions using a trained machine learning model.

## Features

- User-friendly web interface to input flower measurements.
- Predicts the species of iris flower using a machine learning model.
- Displays the prediction results on a separate page.

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

Make sure to have the `iris_model.sav` file in the project directory. This file should be your pre-trained model.

### Step 4: Run the Application

You can run the Flask application with the following command:

```bash
python app.py
```

### Step 5: Access the Application

Open your web browser and go to `http://127.0.0.1:5000/` to access the Iris Flower Prediction application.

## How to Use

1. Enter the sepal length, sepal width, petal length, and petal width in the provided fields.
2. Click the "Predict" button.
3. You will be redirected to a new page displaying the predicted iris flower species.

