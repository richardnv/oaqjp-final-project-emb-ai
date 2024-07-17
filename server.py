import json
from flask import Flask, jsonify, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyze  = request.args.get('textToAnalyze')
    emotion_response = emotion_detector(text_to_analyze)

    if emotion_response['dominent_emotion'] == None:
        return "Invalid text! Please try again!."
    
    output = f"For the given statement, the system serponse is"
    output += f" 'anger': {emotion_response['anger']},"
    output += f" 'disgust': {emotion_response['disgust']},"
    output += f" 'fear': {emotion_response['fear']},"
    output += f" 'joy': {emotion_response['joy']},"
    output += f" 'sadness': {emotion_response['sadness']}."          
    output += f" The dominent emotion is <b>{emotion_response['dominent_emotion']}</b>."
        
    return output
