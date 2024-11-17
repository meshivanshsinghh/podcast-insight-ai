import streamlit as st
import plotly.express as px
import pandas as pd
import assemblyai as aai


def display_speaker_analysis(transcript: aai.Transcript) -> None:
    """Display speaker analysis visualization"""
    if transcript.utterances:
        speaker_times = {}
        for utterance in transcript.utterances:
            speaker = f"Speaker {utterance.speaker}"
            duration = utterance.end - utterance.start
            speaker_times[speaker] = speaker_times.get(speaker, 0) + duration

        df = pd.DataFrame({
            'Speaker': list(speaker_times.keys()),
            'Speaking Time (seconds)': list(speaker_times.values())
        })

        fig = px.pie(df, values='Speaking Time (seconds)',
                     names='Speaker', title='Speaker Distribution')
        st.plotly_chart(fig)


def display_key_insights(transcript: aai.Transcript) -> None:
    """Display key insights"""
    if transcript.summary:
        st.write(transcript.summary)


def display_analytics(transcript: aai.Transcript) -> None:
    """Display all analytics"""
    if not transcript:
        return

    tab1, tab2 = st.tabs(['Speaker Analysis', 'Key Insights'])

    with tab1:
        st.subheader("Speaker Analysis")
        display_speaker_analysis(transcript)

    with tab2:
        st.subheader("Key Insights")
        display_key_insights(transcript)
