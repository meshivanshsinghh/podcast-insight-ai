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
            duration = utterance.end - utterance.start / 1000
            speaker_times[speaker] = speaker_times.get(speaker, 0) + duration

        df = pd.DataFrame({
            'Speaker': list(speaker_times.keys()),
            'Speaking Time (minutes)': [round(t/60, 2) for t in speaker_times.values()]
        })

        fig = px.pie(df,
                     values='Speaking Time (minutes)',
                     names='Speaker',
                     title='Speaker Distribution',
                     hover_data={'Speaking Time (minutes)': ':.2f'})
        st.plotly_chart(fig)


def display_key_insights(transcript: aai.Transcript) -> None:
    """Display key insights"""
    if transcript.summary:
        st.header("Summary")
        st.write(transcript.summary)

    if transcript.chapters:
        st.header("Chapter Breakdown")
        for i, chapter in enumerate(transcript.chapters, 1):
            # Convert milliseconds to minutes and seconds
            start_mins = int(chapter.start / 60000)
            start_secs = int((chapter.start % 60000) / 1000)
            end_mins = int(chapter.end / 60000)
            end_secs = int((chapter.end % 60000) / 1000)

            st.subheader(f"Chapter {i}: {chapter.headline}")
            st.text(
                f"Time: {start_mins:02d}:{start_secs:02d} - {end_mins:02d}:{end_secs:02d}"
            )
            if chapter.summary:
                st.write(f"**Summary:** {chapter.summary}")
            st.divider()  # Add visual separation between chapters


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
            'Text': utterance.text,
            # duration in seconds
            'Duration': (utterance.end - utterance.start) / 1000
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
            text=speaker_df['Text'],
            customdata=speaker_df[['Start', 'End', 'Duration']],
            hovertemplate=(
                "<b>%{y}</b><br>" +
                "Start: %{customdata[0]:.1f}s<br>" +
                "End: %{customdata[1]:.1f}s<br>" +
                "Duration: %{customdata[2]:.1f}s<br>" +
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
