from flask import Flask, send_file
from app.controller.house_price_prediction import prediction
from app.controller.exploration_data_analysis import *
from app.controller.dataset import *
from app.views import *
from app.utils.jakarta_geojson import jakartaGeoJson

app = Flask(__name__)

# Path buat api
@app.route('/api/v1/alive',methods=['GET'])
def api_alive():
    return "alive"

@app.route('/api/v1/prediction', methods=['GET'])
def api_prediction():
    return prediction()

@app.route('/api/v1/carddata', methods=['GET'])
def api_carddata():
    return cardData()

@app.route('/api/v1/dataset', methods=['GET'])
def api_dataset():
    return getDatasetArray()

# Path buat view
@app.route('/',methods=['GET'])
def view_index():
    return home('Home',api_carddata(),jakartaGeoJson())

@app.route('/dataset',methods=['GET'])
def view_dataset():
    return dataset('Dataset of model',api_dataset())

@app.route('/eda',methods=['GET'])
def view_eda():
    return eda('Exploratory Data Analysis',updateHeatmap(), updateHeatmapByPrice())

@app.route('/about',methods=['GET'])
def view_about():
    return about('About this web')

@app.route('/profile',methods=['GET'])
def view_profile():
    return profile('Profile of creator')

# Menampilkan gambar Exploration Data Analysist
@app.route('/storage/heatmap',methods=['GET'])
def show_heatmap():
    heatmap_path = '../../app/storage/heatmap.png'
    return send_file(heatmap_path, mimetype='image/png')

@app.route('/storage/heatmapbyprice',methods=['GET'])
def show_heatmapbyprice():
    heatmap_path = '../../app/storage/heatmapbyprice.png'
    return send_file(heatmap_path, mimetype='image/png')
