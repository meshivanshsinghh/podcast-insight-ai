import assemblyai as aai
import streamlit as st


def analyze_podcast(audio_file):
    try:
        config = aai.TranscriptionConfig(
            speaker_labels=True,
            summarization=True,
            language_detection=True
        )
        transcriber = aai.Transcriber(config=config)
        transcript = transcriber.transcribe(audio_file)
        if transcript.status == 'error':
            st.error(f"Transcription failed: {transcript.error}")
        return transcript

    except Exception as e:
        st.error(f"Error analyzing podcast: {str(e)}")
