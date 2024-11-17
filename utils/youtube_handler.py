import streamlit as st
import yt_dlp
import os
import uuid


def download_youtube_audio(url):
    """Download audio from YouTube video"""
    # Generate unique filename using UUID
    file_id = str(uuid.uuid4())
    temp_path = f"temp/{file_id}"

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{temp_path}.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)
            mp3_path = f"{temp_path}.mp3"

            # Return path to the MP3 file
            return mp3_path

    except Exception as e:
        st.error(f"Error downloading YouTube audio: {str(e)}")
        return None

    finally:
        # Cleanup any potential .webm files
        try:
            webm_path = f"{temp_path}.webm"
            if os.path.exists(webm_path):
                os.remove(webm_path)
        except Exception:
            pass


def cleanup_temp_file(file_path):
    """Clean up temporary audio file"""
    try:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        st.warning(f"Error cleaning up temporary file: {str(e)}")
