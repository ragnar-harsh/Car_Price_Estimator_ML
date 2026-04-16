
from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np



app = Flask(__name__)

cars = pd.read_csv('./Datasets/Cleaned_Car_Data.csv')
predict_model = pickle.load(open('./Notebook/LinearRegressionModel.pkl', 'rb'))




@app.route('/')
def index():

    companies = sorted(cars['company'].unique())
    car_models = sorted(cars['name'].unique())
    year = sorted(cars['year'].unique(), reverse=True)
    fuel_type = cars['fuel_type'].unique()

    return render_template('index.html', company_list = companies, car_model_list = car_models, year_list = year, fuel_type_list = fuel_type)


@app.route('/predict', methods=['POST'])
def predict():

    company = request.form.get('company')
    model = request.form.get('model')
    year = int(request.form.get('year'))
    fuel = request.form.get('fuel')
    km_driven = int(request.form.get('kms_driven'))

    est_price = predict_model.predict(pd.DataFrame([[model, company, year, km_driven, fuel]], columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))



    return str(np.round(est_price[0], 2))
    



if __name__ == '__main__':
    app.run(debug=True)

