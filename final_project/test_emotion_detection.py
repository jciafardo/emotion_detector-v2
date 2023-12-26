from emotion_detection.emotion_detection import emotion_detector
statements = ['I am glad this happend', "I am really mad about this", "I feel disgusted just hearing about this", "I am so sad about this", "I am really afraid that this will happen"]
output = []

for statement in statements:
    result = emotion_detector(statement), statement
    output.append(result)

print(output)