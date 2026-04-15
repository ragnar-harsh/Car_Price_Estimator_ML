
from flask import Flask, render_template
import pandas as pd



app = Flask(__name__)

cars = pd.read_csv('./Datasets/Cleaned_Car_Data.csv')




@app.route('/')
def index():

    companies = sorted(cars['company'].unique())
    car_models = sorted(cars['name'].unique())
    year = sorted(cars['year'].unique(), reverse=True)
    fuel_type = cars['fuel_type'].unique()

    return render_template('index.html', company_list = companies, car_model_list = car_models, year_list = year, fuel_type_list = fuel_type)


if __name__ == '__main__':
    app.run(debug=True)

