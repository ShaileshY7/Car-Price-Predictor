from flask import Flask, render_template, request, redirect
import pandas as pd
from flask_cors import CORS, cross_origin
import pickle
import numpy as np

app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('RandomForestModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_car_new.csv')

@app.route("/")
def index():
    companies = sorted(car['company'].unique())
    car_models_dict = {}
    for company in companies:
        models = sorted(car[car['company'] == company]['name'].unique().tolist())
        car_models_dict[company] = models
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()
    return render_template('index.html',
        companies=companies,
        car_models=car_models_dict,
        years=year,
        fuel_types=fuel_type)

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    driven = int(request.form.get('kilo_driven'))

    input_df = pd.DataFrame(
        [[car_model, company, year, driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )

    prediction = model.predict(input_df)
    return str(np.round(prediction[0], 2))

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))