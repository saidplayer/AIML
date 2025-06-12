# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
import joblib
from flask import Flask, request, render_template
# import numpy as np
import json

app = Flask(__name__)

# Load the model
model = joblib.load('iris_model.pkl')

# @app.route('/predict', methods=['GET'])
# def predict():
#     data = request.args["data"]
#     data = np.array(json.loads(data)).reshape(-1,4)
#     prediction = model.predict(data)
#     return "<html><title>aaa</title><h3>Model outcome: <i>" + str(prediction) + "</i></h3></html>"

@app.route('/', methods=['GET'])
def homepage():
    visible     = "hidden"
    age         = 0
    income      = 0
    costs       = 0

    if "age" in request.args:
        age     = int(request.args["age"])
        visible = "block"
    if "income" in request.args:
        income  = int(request.args["income"])
        visible = "block"
    if "costs" in request.args:
        costs   = int(request.args["costs"])
        visible = "block"

    if visible == "block":
        prediction = model.predict([[age, income, costs, 0]])[0]
    else:
        prediction = 0
    return render_template("./index.html",visible = visible, prediction = prediction, age = age, income = income, costs = costs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)