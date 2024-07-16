# Importing the requests library
import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonObj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=jsonObj, headers=headers)
    emotion_scores = json.loads(response.text)['emotionPredictions'][0]['emotion']
    sorted_scores = dict(sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True))
    dominent_emotion = list(sorted_scores)[0]
    
    output = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],          
        "dominent_emotion": dominent_emotion
    }
    
    return output