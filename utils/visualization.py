import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
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


def display_timeline(transcript: aai.Transcript) -> None:
    """Display interactive timeline visualization"""
    if not transcript.utterances:
        return

    # Create a DataFrame for the timeline
    timeline_data = []
    for utterance in transcript.utterances:
        timeline_data.append({
            'Speaker': f'Speaker {utterance.speaker}',
            'Start': utterance.start / 1000,  # Convert to seconds
            'End': utterance.end / 1000,
            'Text': utterance.text
        })

    df = pd.DataFrame(timeline_data)

    # Create the timeline figure
    fig = go.Figure()

    # Add a trace for each speaker
    for speaker in df['Speaker'].unique():
        speaker_df = df[df['Speaker'] == speaker]

        fig.add_trace(go.Bar(
            name=speaker,
            x=speaker_df['End'] - speaker_df['Start'],
            y=[speaker] * len(speaker_df),
            orientation='h',
            base=speaker_df['Start'],
            hovertemplate=(
                f"<b>{speaker}</b><br>" +
                "Time: %{base:.1f}s - %{base + x:.1f}s<br>" +
                "Duration: %{x:.1f}s<br>" +
                "<extra></extra>"
            )
        ))

    # Update layout
    fig.update_layout(
        title="Conversation Timeline",
        xaxis_title="Time (seconds)",
        yaxis_title="Speakers",
        barmode='stack',
        height=400,
        showlegend=True,
        hovermode='closest'
    )

    # Display the figure
    st.plotly_chart(fig, use_container_width=True)


def display_analytics(transcript: aai.Transcript) -> None:
    """Display all analytics"""
    if not transcript:
        return

    tab1, tab2, tab3 = st.tabs(
        ['Timeline', 'Speaker Analysis', 'Key Insights'])

    with tab1:
        st.subheader("Interactive Timeline")
        display_timeline(transcript)

    with tab2:
        st.subheader("Speaker Analysis")
        display_speaker_analysis(transcript)

    with tab3:
        st.subheader("Key Insights")
        display_key_insights(transcript)
