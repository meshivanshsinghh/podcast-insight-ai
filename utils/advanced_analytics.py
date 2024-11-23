import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from collections import Counter
import assemblyai as aai


def analyze_entities(transcript: aai.Transcript):
    """Analyze and display detected entities"""
    if not hasattr(transcript, 'entities') or not transcript.entities:
        st.info("No entities detected in the transcript.")
        return

    try:
        st.write("Debug: Starting entity analysis")
        st.write(f"Total entities found: {len(transcript.entities)}")

        # group entities by type
        entity_groups = {}
        for idx, entity in enumerate(transcript.entities):
            try:
                if not hasattr(entity, 'entity_type') or not hasattr(entity, 'text'):
                    st.warning(f"Entity {idx} missing attributes: {entity}")
                    continue

                st.write(
                    f"Processing entity: Type={entity.entity_type}, Text={entity.text}")

                if entity.entity_type not in entity_groups:
                    entity_groups[entity.entity_type] = []
                entity_groups[entity.entity_type].append(entity.text)
            except Exception as e:
                st.error(f"Error processing entity {idx}: {str(e)}")

        if not entity_groups:
            st.info("No valid entities found in the transcript.")
            return

        # display entities
        st.subheader('Entity Detection')
        cols = st.columns(min(len(entity_groups), 4))  # Limit to 4 columns max

        for i, (entity_type, entities) in enumerate(entity_groups.items()):
            with cols[i % 4]:  # Use modulo to wrap to new row
                st.write(f"***{entity_type.title()}***")
                entity_count = Counter(entities)
                df = pd.DataFrame(
                    {'Entity': list(entity_count.keys()),
                     'Count': list(entity_count.values())}
                ).sort_values('Count', ascending=False)

                if not df.empty:
                    fig = px.bar(df, x="Entity", y="Count",
                                 title=f"Top {entity_type.title()} Mentions")
                    st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Error analyzing entities: {str(e)}")
        st.error("Entity analysis stack trace:", exc_info=True)


def analyze_speaker_style(transcript: aai.Transcript):
    """Analyze speaker style patterns"""
    if not transcript.utterances:
        return

    st.subheader("Speaker Style Analysis")

    speaker_metrics = {}

    for utterance in transcript.utterances:
        speaker = f"Speaker {utterance.speaker}"

        if speaker not in speaker_metrics:
            speaker_metrics[speaker] = {
                'word_counts': [],
                'durations': [],
                'sentiments': []
            }

        # calculating words per minute
        duration_minutes = (utterance.end - utterance.start) / \
            60000  # ms to minutes
        word_count = len(utterance.text.split())

        if duration_minutes > 0:
            speaker_metrics[speaker]['word_counts'].append(
                word_count)
            speaker_metrics[speaker]['durations'].append(duration_minutes)

        # checking sentiment analysis too
        if hasattr(utterance, 'sentiment') and utterance.sentiment:
            speaker_metrics[speaker]['sentiments'].append(utterance.sentiment)

    # displaying metric for each speaker
    for speaker, metrics in speaker_metrics.items():
        st.write(f"### {speaker}")

        total_words = sum(metrics['word_counts'])
        total_duration = sum(metrics['durations'])

        if total_duration > 0:
            avg_pace = total_words / total_duration
            st.metric("Average Speaking Pace", f"{avg_pace:.0f} words/minute")

        # displaying sentiment distribution

        if (metrics['sentiment']):
            sentiment_df = pd.DataFrame(metrics['sentiment'])
            fig = px.pie(sentiment_df, names='sentiment',
                         title=f"Sentiment Distribution for {speaker}")
            st.plotly_chart(fig)


def display_advanced_analytics(transcript: aai.Transcript):
    """Displaying all analytics"""
    tab1, tab2 = st.tabs(['Entity Analysis', 'Speaker Styles'])

    with tab1:
        analyze_entities(transcript)

    with tab2:
        analyze_speaker_style(transcript)
