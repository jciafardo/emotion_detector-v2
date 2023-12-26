import requests
import json

def emotion_detector(text_to_analyze):
    print("what the fuck\n")
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    print("response   ", formatted_response[0])
    label = formatted_response['emotionPredictions']['emotion']
    score = formatted_response['documentSentiment']['anger']
    return {'label': label, 'score': score}
    