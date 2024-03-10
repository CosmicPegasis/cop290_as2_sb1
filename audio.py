import whisper
import sys


def transcribe_audio(audio_file):
    model = whisper.load_model("small.en")
    result = model.transcribe(audio_file)
    return result["text"]


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python audio.py audio.mp3 output.txt")
        sys.exit(1)

    with open(sys.argv[2], "w") as f:
        f.write(transcribe_audio(sys.argv[1]))
