from flask import Flask

from sortData import ga4_result_to_df
from fechingData import fetch_ga4_data
from flask import request, jsonify

app = Flask(__name__)

# Ruta de prueba
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'




@app.route('/report', methods=['POST'])
def get_report():
    data = request.get_json()
    if not data or 'credentials' not in data:
        return jsonify({'error': 'Missing credentials'}), 400

    credentials_dict = data['credentials']
    dimensions = request.args.get('dimensions').split(',')
    metrics = request.args.get('metrics').split(',')
    property_id = request.args.get('property_id')
    
    if not property_id:
        return jsonify({'error': 'Missing property_id'}), 400

    if not dimensions or not metrics:
        return jsonify({'error': 'Missing dimensions or metrics'}), 400
    
    response = fetch_ga4_data(property_id, credentials_dict, dimensions, metrics)
    df = ga4_result_to_df(response)
    matrix = df.values
    headers = df.columns.tolist()
    return jsonify({'headers': headers, 'data': matrix.tolist()})
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
    
    

# Documentación oficial: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries#python
# Info sobre dimensiones y métricas: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema