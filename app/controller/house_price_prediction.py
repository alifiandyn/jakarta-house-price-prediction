from flask import request, jsonify
from app.utils.random_forest import house_prediction

def prediction():
    kota = request.args.get('kota')
    kamarTidur = request.args.get('jumlah_kamar_tidur')
    kamarMandi = request.args.get('jumlah_kamar_mandi')
    luasTanah = request.args.get('luas_tanah')
    luasBangunan = request.args.get('luas_bangunan')
    carport = request.args.get('garasi')
    jumlahLantai = request.args.get('jumlah_lantai')
    terjangkauInternet = request.args.get('terjangkau_internet')
    message = house_prediction(kota,kamarTidur,kamarMandi,luasTanah,luasBangunan,carport,jumlahLantai,terjangkauInternet)
    data = {
        'status_code': 200, 
        'result':message,
        }
    return jsonify(data)