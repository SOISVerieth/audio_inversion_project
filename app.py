from flask import Flask, request, jsonify, render_template
import numpy as np
from pydub import AudioSegment
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    audio_file = request.files['audio']
    if audio_file.filename.endswith('.wav') or audio_file.filename.endswith('.mp3'):
        audio = AudioSegment.from_file(audio_file)
        
        samples = np.array(audio.get_array_of_samples())
        inverted_samples = -samples
        
        inverted_audio = audio._spawn(inverted_samples.tobytes())
        
        buf = io.BytesIO()
        inverted_audio.export(buf, format="wav")
        buf.seek(0)
        
        response = {
            'original_samples': samples.tolist(),
            'inverted_samples': inverted_samples.tolist(),
            'inverted_audio': base64.b64encode(buf.read()).decode('utf-8')
        }
        
        return jsonify(response)
    else:
        return jsonify({'error': 'Unsupported file format. Please upload a WAV or MP3 file.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
