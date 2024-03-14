import ffmpeg
import sys
from audio import transcribe_audio
import os


def transcribe_video(video_file):
    text = transcribe_audio(video_file)
    return text


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 video.py video.mp4 output.txt")
        sys.exit(1)

    with open(sys.argv[2], "w") as f:
        f.write(transcribe_video(sys.argv[1]))
