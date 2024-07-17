''' Module flask server for emotion detection app '''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    ''' Return the index page '''
    return render_template("index.html")

@app.route('/emotionDetector')
def detect_emotion():
    ''' take textToAnalyze arg from request and process it via eomtion_detector '''
    text_to_analyze  = request.args.get('textToAnalyze')
    emotion_response = emotion_detector(text_to_analyze)

    if emotion_response['dominent_emotion'] is None:
        return "Invalid text! Please try again!."
    output = "For the given statement, the system serponse is"
    output += f" 'anger': {emotion_response['anger']},"
    output += f" 'disgust': {emotion_response['disgust']},"
    output += f" 'fear': {emotion_response['fear']},"
    output += f" 'joy': {emotion_response['joy']},"
    output += f" 'sadness': {emotion_response['sadness']}"
    output += f" The dominent emotion is <b>{emotion_response['dominent_emotion']}</b>"
    return output
