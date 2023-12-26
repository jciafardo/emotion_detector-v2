from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def sent_analyzer():
    text_to_analyze = "I love this"
    output = emotion_detector(text_to_analyze)
    return("For the given statement, the system response is ", output)


@app.route('/')
def render_index_page():
    return render_template("index.html")

app.run(host="0.0.0.0", port=5000)