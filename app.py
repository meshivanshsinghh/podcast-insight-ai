import streamlit as st
import assemblyai as aai
import plotly.express as px
import pandas as pd
import os
from dotenv import load_dotenv
from utils import download_youtube_audio, analyze_podcast, display_analytics

load_dotenv()

aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')


def main():
    st.title("PodcastInsight 🎙️")
    st.subheader("AI-Powered Podcast Analytics Platform")

    os.makedirs('temp', exist_ok=True)

    # youtube input url
    youtube_url = st.text_input(
        "Enter YouTube Podcast URL:", placeholder="https://youtube.com/...")

    if youtube_url:
        with st.spinner("Processing podcast..."):
            try:
                audio_file = download_youtube_audio(youtube_url)
                if audio_file:
                    # analyze podcast
                    transcript = analyze_podcast(audio_file)
                    if transcript:
                        # display analytics
                        display_analytics(transcript)
                        # add download button for transcript
                        st.download_button(
                            "Download Transcript",
                            transcript.text,
                            file_name="transcript.txt",
                            mime="text/plain"
                        )
            except Exception as e:
                st.error(f"Error processing podcast: {str(e)}")


if __name__ == "__main__":
    main()
