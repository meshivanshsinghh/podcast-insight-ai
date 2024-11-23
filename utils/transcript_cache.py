# import chromadb
# from chromadb.config import Settings
# import hashlib
# import assemblyai as aai
# import json
# import streamlit as st


# class TranscriptCache:
#     def __init__(self):
#         self.client = chromadb.Client(Settings(
#             persist_directory='./transcript_cache',
#             is_persistent=True
#         ))

#         self.collection = self.client.get_or_create_collection(
#             "podcast_transcripts")

#     def _generate_video_id(self, url: str) -> str:
#         """Generate a unique ID for the video URL"""
#         return hashlib.md5(url.encode()).hexdigest()

#     def get_transcript(self, video_url: str):
#         """retrieve transcript from cache if it exists"""
#         video_id = self._generate_video_id(video_url)
#         try:
#             results = self.collection.get(
#                 ids=[video_id],
#                 include=['metadatas']
#             )
#             if results and results['ids']:
#                 transcript_data = results['metadatas'][0]
#                 # Parse the JSON string back to a list
#                 if 'utterances' in transcript_data:
#                     transcript_data['utterances'] = json.loads(
#                         transcript_data['utterances'])
#                 if 'chapters' in transcript_data:
#                     transcript_data['chapters'] = json.loads(
#                         transcript_data['chapters']
#                     )
#                 return transcript_data
#             return None
#         except Exception as e:
#             st.error(f"Cache error: {str(e)}")
#             return None

#     def save_transcript(self, video_url: str, transcript: aai.Transcript):
#         """Save transcript to cache"""
#         video_id = self._generate_video_id(video_url)
#         chapters_data = []
#         if transcript.chapters:
#             chapters_data = [{
#                 'headline': ch.headline,
#                 'start': ch.start,
#                 'end': ch.end,
#                 'summary': ch.summary,
#             } for ch in transcript.chapters]

#         # Safely handle entities
#         entities = []
#         if hasattr(transcript, 'entities') and transcript.entities:
#             try:
#                 entities = [
#                     {'text': e.text, 'entity_type': e.entity_type}
#                     for e in transcript.entities
#                     if hasattr(e, 'text') and hasattr(e, 'entity_type')
#                 ]
#             except Exception as e:
#                 st.warning(f"Error processing entities: {str(e)}")

#         transcript_data = {
#             'text': transcript.text or "",
#             'utterances': json.dumps([{
#                 'speaker': u.speaker,
#                 'start': u.start,
#                 'end': u.end,
#                 'text': u.text or ""
#             } for u in transcript.utterances]),
#             'summary': transcript.summary or "",
#             'chapters': json.dumps(chapters_data),
#             'entities': entities,
#             'sentiment': getattr(transcript, 'sentiment', None)
#         }

#         self.collection.upsert(
#             ids=[video_id],
#             metadatas=[transcript_data],
#             documents=[transcript.text or ""]
#         )
