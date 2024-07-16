import json, requests
from flask import Flask, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetection', methods=['POST'])
def fetect_emotion():
    data = requests.get_data().__getattribute__('q')
    text_to_analyze = data['text']
    emotion_detection_result = emotion_detector(text_to_analyze)
    
    output = f"For the given statement, the system serponse is"
    output += f" 'anger': {emotion_scores['anger']},"
    output += f" 'disgust': {emotion_scores['disgust']},"
    output += f" 'fear': {emotion_scores['fear']},"
    output += f" 'joy': {emotion_scores['joy']},"
    output += f" 'sadness': {emotion_scores['sadness']}."          
    output += f" The dominent emotion is <b>{dominent_emotion}</b>."
        
    return output
