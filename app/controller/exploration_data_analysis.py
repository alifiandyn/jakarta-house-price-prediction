from flask import request, jsonify
from app.utils.exploration_data import *

def updateHeatmap():
    message = heatmap()
    data = {
        'status_code': 200, 
        'result':message,
        }
    return jsonify(data)

def updateHeatmapByPrice():
    message = heatmapByPrice()
    data = {
        'status_code': 200, 
        'result':message,
        }
    return jsonify(data)