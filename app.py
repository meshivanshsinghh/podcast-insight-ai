import streamlit as st
import assemblyai as aai
import plotly.express as px
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')


def main():
    st.title("PodcastInsight")
    st.subheader("AI-Powered Podcast Analytics Platform")

    # youtube input url
    youtube_url = st.text_input(
        "Enter YouTube Podcast URL:", placeholder="https://youtube.com/...")

    if youtube_url:
        with st.spinner("Processing podcast..."):
            try:
                # TODO: Implement podcast processing
                # 1. Download audio from YouTube
                # 2. Send to AssemblyAI for transcription
                # 3. Process result
                pass
            except Exception as e:
                st.error(f"Error processing podcast: {str(e)}")


if __name__ == "__main__":
    main()
