import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile

def extract_audio(video_path):
    """Extract audio from a video file."""
    video_clip = VideoFileClip(video_path)
    audio_path = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False).name
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    video_clip.close()
    return audio_path

def main():
    st.title("Audio Extractor from Video")
    st.write("Upload a video file to extract the audio.")

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mkv", "avi", "mov"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video_file:
            temp_video_file.write(uploaded_file.read())
            temp_video_path = temp_video_file.name

        # Step 1: Extract audio
        st.write("Extracting audio from video...")
        extracted_audio_path = extract_audio(temp_video_path)
        st.write("Audio extraction complete!")

        # Step 2: Play and Download audio
        st.audio(extracted_audio_path, format="audio/mp3")
        with open(extracted_audio_path, "rb") as audio_file:
            st.download_button(
                label="Download Extracted Audio",
                data=audio_file,
                file_name="extracted_audio.mp3",
                mime="audio/mp3"
            )

if __name__ == "__main__":
    main()
