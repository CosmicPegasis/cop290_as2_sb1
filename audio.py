from faster_whisper import WhisperModel
import sys


def transcribe_audio(audio_file):
    model = WhisperModel("small")
    segments, _ = model.transcribe(audio_file)
    s = ""
    for segment in segments:
        s += "[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text) + "\n"
    return s


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python audio.py audio.mp3 output.txt")
        sys.exit(1)

    with open(sys.argv[2], "w") as f:
        f.write(transcribe_audio(sys.argv[1]))
