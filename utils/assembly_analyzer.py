import assemblyai as aai
import streamlit as st


def analyze_podcast(audio_file):
    try:
        config = aai.TranscriptionConfig(
            iab_categories=True,
            auto_chapters=True,
            content_safety=True,
            auto_highlights=True,
            sentiment_analysis=True,
            entity_detection=True,
            speaker_labels=True,
            language_detection=True
        )
        st.info("Starting transcription...")
        transcriber = aai.Transcriber(config=config)
        transcript = transcriber.transcribe(audio_file)
        return transcript

    except Exception as e:
        st.error(f"Error analyzing podcast: {str(e)}")
        return None
