from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import warnings
from sklearn.exceptions import InconsistentVersionWarning
from flask import Flask, request, jsonify
warnings.simplefilter("ignore", InconsistentVersionWarning)
from flask_cors import CORS

app = Flask(__name__)
# CORS(app, origins=["http://127.0.0.1:5000/"])
cors = CORS(app, resources={r"/predict": {"origins": "*"}})

#app = Flask(__name__)

# Load the trained model
model_path = "model.pkl"  # Ensure the model is saved in this file
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/")
def home():
    #return "Welcome to Gear Fault Predictor API! Use /predict to make a prediction."
    return render_template('index2.html')

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # data = request.json
        data = request.get_json()
        a1 = float(data.get("a1", 0))
        a2 = float(data.get("a2", 0))
        a3 = float(data.get("a3", 0))
        
        # Make prediction
        prediction = model.predict(np.array([[a1, a2, a3]]))
       # print(f"{prediction[0]}")
        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(debug=True)

