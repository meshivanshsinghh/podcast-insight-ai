import streamlit as st
import assemblyai as aai
import os
from dotenv import load_dotenv
from utils import (
    download_youtube_audio,
    analyze_podcast,
    display_analytics,
    cleanup_temp_file
)
from utils.transcript_cache import TranscriptCache

load_dotenv()

aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')


@st.cache_resource
def get_transcript_cache():
    return TranscriptCache()


def process_podcast(youtube_url, transcript_cache):
    """Process podcast and return transcript"""
    cached_transcript = transcript_cache.get_transcript(youtube_url)
    if cached_transcript:
        st.success("Found cached transcript! Using cached version.")

        class CachedTranscript:
            def __init__(self, data):
                self.text = data['text']
                self.utterances = [type('Utterance', (), u)
                                   for u in data['utterances']]
                self.summary = data['summary']
        return CachedTranscript(cached_transcript)

    # If not in cache, process the podcast
    audio_file = download_youtube_audio(youtube_url)
    if audio_file:
        try:
            transcript = analyze_podcast(audio_file)
            if transcript:
                # Save to cache
                transcript_cache.save_transcript(youtube_url, transcript)
                return transcript
        finally:
            cleanup_temp_file(audio_file)
    return None


def main():
    st.title("PodcastInsight 🎙️")
    st.subheader("AI-Powered Podcast Analytics Platform")

    os.makedirs('temp', exist_ok=True)
    os.makedirs('transcript_cache', exist_ok=True)

    transcript_cache = get_transcript_cache()
    processed_transcript = None

    with st.form("podcast_form"):
        youtube_url = st.text_input(
            "Enter YouTube Podcast URL:",
            placeholder="https://youtube.com/..."
        )

        submitted = st.form_submit_button("Process Podcast")

    # Process outside the form
    if submitted and youtube_url:
        with st.spinner("Processing podcast..."):
            try:
                processed_transcript = process_podcast(
                    youtube_url, transcript_cache)
            except Exception as e:
                st.error(f"Error processing podcast: {str(e)}")

    # Display results outside the form
    if processed_transcript:
        # display analytics
        display_analytics(processed_transcript)
        # add download button for transcript
        st.download_button(
            "Download Transcript",
            processed_transcript.text,
            file_name="transcript.txt",
            mime="text/plain"
        )


if __name__ == "__main__":
    main()
