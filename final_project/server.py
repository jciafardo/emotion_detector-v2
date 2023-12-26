from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def sent_analyzer():
    
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    dominant_emotion = response['Dominant Emotion']
    if dominant_emotion == None:
        return("Invalid text please try again")
    emotion_scores = ', '.join(f"'{emotion}': {score}" for emotion, score in response.items() if emotion != 'Dominant Emotion')
    
    output_string = f"For the given statement, the system response is {emotion_scores}. The dominant emotion is {dominant_emotion}."
    return output_string
    



@app.route('/')
def render_index_page():
    return render_template("index.html")

@app.route('/test')
def Test():
    return render_template("index.html")

app.run(host="0.0.0.0", port=5006)