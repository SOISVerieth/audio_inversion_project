
# Audio Inversion Web App

This project is a web application that allows users to record audio or upload audio files (in WAV or MP3 format), invert the audio waveform, and visualize the original and inverted waveforms using charts.

## Features

- Record audio directly from your microphone.
- Upload audio files (supports WAV and MP3 formats).
- Invert the audio waveform.
- Visualize original and inverted waveforms using charts.

## Installation

### Requirements

- Python 3.x
- Flask
- pydub
- numpy
- ffmpeg

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SOISVerieth/audio-inversion-webapp.git
   cd audio-inversion-webapp
   ```

2. **Install dependencies:**

   ```bash
   pip install Flask pydub numpy
   ```

3. **Install ffmpeg:**

   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.
   - **macOS**: Install via Homebrew:
     ```bash
     brew install ffmpeg
     ```
   - **Ubuntu**: Install via apt:
     ```bash
     sudo apt-get update
     sudo apt-get install ffmpeg
     ```

## Usage

1. **Run the Flask server:**

   ```bash
   python app.py
   ```

2. **Open your web browser:**

   Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the application.

3. **Using the application:**

   - Click on "Start Recording" to record audio using your microphone.
   - Click on "Stop Recording" to stop recording.
   - Alternatively, click on "Choose File" to upload an audio file (in WAV or MP3 format).
   - Click on "Upload Audio" to process the uploaded audio file and see the inverted waveform and charts.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests.
