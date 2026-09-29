import importlib
import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    # Error handling for bad requests
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Gestion selon que le retour soit une liste ou un dictionnaire
    if isinstance(formatted_response, list):
        emotion_data = formatted_response[0]['emotionPredictions'][0]['emotion']
    else:
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']

    emotion_data = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotion_data['anger']
    disgust_score = emotion_data['disgust']
    fear_score = emotion_data['fear']
    joy_score = emotion_data['joy']
    sadness_score = emotion_data['sadness']
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }