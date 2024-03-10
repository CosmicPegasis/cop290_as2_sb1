import ffmpeg
import sys
from audio import transcribe_audio
import os


def transcribe_video(video_file):
    input_file = ffmpeg.input(video_file)
    input_file.output("audio.mp3", acodec="mp3").run()
    text = transcribe_audio("audio.mp3")
    os.remove("audio.mp3")
    return text


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 video.py video.mp4 output.txt")
        sys.exit(1)

    with open(sys.argv[2], "w") as f:
        f.write(transcribe_video(sys.argv[1]))
