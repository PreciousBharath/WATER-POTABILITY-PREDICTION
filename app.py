from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load saved Random Forest model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get input values from form
            ph = float(request.form['ph'])
            Hardness = float(request.form['Hardness'])
            Solids = float(request.form['Solids'])
            Chloramines = float(request.form['Chloramines'])
            Sulfate = float(request.form['Sulfate'])
            Conductivity = float(request.form['Conductivity'])
            Organic_carbon = float(request.form['Organic_carbon'])
            Trihalomethanes = float(request.form['Trihalomethanes'])
            Turbidity = float(request.form['Turbidity'])
            
            # Create input array
            input_features = np.array([[ph, Hardness, Solids, Chloramines, Sulfate,
                                        Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
            
            # Predict
            prediction = model.predict(input_features)[0]
            
            if prediction == 1:
                result = "Safe to Drink 💧"
            else:
                result = "Not Safe to Drink ⚠️"
            
            return render_template('result.html', result=result)
        except ValueError:
            return "Please enter valid numeric values."
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
