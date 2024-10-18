from flask import Flask, render_template, request
import pickle

skills_app = Flask(__name__)

# Load the model
model = pickle.load(open('housePrice_model.pkl', 'rb'))

@skills_app.route("/")
def homepage():
    return render_template('index.html')

@skills_app.route("/predict", methods=['POST'])
def predict():
    # Get the values from the form
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    floors = float(request.form['floors'])
    yr_built = int(request.form['yr_built'])

    # Make prediction
    prediction = model.predict([[bedrooms, bathrooms, floors, yr_built]])
    prediction_price = prediction[0]

    # Render the prediction template with the result
    return render_template('prediction.html', prediction=prediction_price)

if __name__ == "__main__":
    skills_app.run(debug=True, port=5000)
