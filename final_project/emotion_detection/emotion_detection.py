import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(URL, json = myobj, headers=header)
    formatted_response = json.loads(response.text)


    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
    emotion_predictions['Dominant Emotion'] = dominant_emotion

    return emotion_predictions