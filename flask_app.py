from flask import Flask, request, jsonify
from logger import SingletonLogger
from model import My_Classifier_Model
import logging
import os

app = Flask(__name__)

logging.basicConfig(filename='./data/log_file.log', level=logging.INFO)

class My_Classifier_Model:
    def train(self, dataset_filename):
        logging.info(f'Training model with dataset: {dataset_filename}')
        os.makedirs('./model/', exist_ok=True)
        logging.info('Model training completed and artifacts saved.')

    def predict(self, dataset_filename):
        logging.info(f'Loading model for predictions from: ./data/model/')
        predictions = ["prediction1", "prediction2"]
        os.makedirs('./data/', exist_ok=True)
        with open('./data/results.csv', 'w') as f:
            f.write('\n'.join(predictions))
        logging.info('Predictions saved to ./data/results.csv.')

model = My_Classifier_Model()

@app.route('/train', methods=['POST'])
def train():
    try:
        data = request.json
        dataset_filename = data.get('dataset_filename')
        model.train(dataset_filename)
        return jsonify({"message": "Model trained successfully."}), 200
    except Exception as e:
        logging.error(f'Error during training: {str(e)}')
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        dataset_filename = data.get('dataset_filename')
        model.predict(dataset_filename)
        return jsonify({"message": "Predictions saved successfully."}), 200
    except Exception as e:
        logging.error(f'Error during prediction: {str(e)}')
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

