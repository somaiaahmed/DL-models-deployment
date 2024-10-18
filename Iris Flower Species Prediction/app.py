from flask import Flask, render_template, request
import pickle

skills_app = Flask(__name__)

# Load the model
model = pickle.load(open('iris_model.sav', 'rb'))

@skills_app.route("/")
def homepage():
    return render_template('index.html')

@skills_app.route("/predict", methods=['POST'])
def predict():
    # Get the values from the form
    sl = float(request.form['sepal_length'])
    sw = float(request.form['sepal_width'])
    pl = float(request.form['petal_length'])
    pw = float(request.form['petal_width'])

    # Make prediction
    prediction = model.predict([[sl, sw, pl, pw]])

    # Render the prediction result in a new template
    return render_template('prediction.html', prediction=prediction[0])

if __name__ == "__main__":
    skills_app.run(debug=True, port=5000)
