from flask import Flask, render_template, request, jsonify, send_file
import text2voice
import seepk2text
import numpy as np
import brain

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    # audio_array = np.array(data['audioData'], dtype=np.float32)
    # 现在你可以使用 audio_array 进行处理，例如传递给语音识别模块
    # 假设处理函数返回文本
    user_input = seepk2text.get_text(np.array(data['audioData'], dtype=np.float32))
    print("txt" + user_input)
    response = brain.response(user_input)
    print("response" + response)
    return text2voice.get_voice(response)

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        # 可以在这里处理音频，比如保存或者进一步处理
        # 为简单起见，这里直接返回相同的音频文件
        audio_file.save('received_audio.webm')
        return send_file('received_audio.webm', as_attachment=True)
    return 'No audio uploaded', 400


@app.route('/play', methods=['POST'])
def play_audio():
    # return send_file('tts_output.wav', as_attachment=True)
    return text2voice.get_voice("hello world, My name is coki")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)