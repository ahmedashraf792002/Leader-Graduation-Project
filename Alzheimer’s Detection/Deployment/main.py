from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model('model_VGG16.h5')

import cv2

def preprocess_image(image):
    img = Image.open(io.BytesIO(image))
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize((224, 224)) 
    img_array = np.array(img)
    if img_array.shape[-1] != 3:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    image = file.read()
    processed_image = preprocess_image(image)
    preds = model.predict(processed_image)

    # Convert prediction probabilities to class labels
    dic = {0: "Alzheimer's disease", 1: "Cognitively normal", 2: "Early mild cognitive impairment", 3: "Late mild cognitive impairment"}
    
    pred_class = dic[np.argmax(preds)]   # Get the class label with maximum probability
    pred_proba = str(round(float(preds[0, np.argmax(preds)]),2))+"%"  # Get the probability of the predicted class
    return  pred_class+" "+pred_proba





if __name__ == '__main__':
    app.run(debug=True)
