from neuralaudio import play
from neuralaudio.client import NeuralAudio

from .utils import IN_GITHUB, DEFAULT_VOICE_FILE


def test_audio_isolation() -> None:
    """Test basic audio isolation."""
    client = NeuralAudio()
    audio_file = open(DEFAULT_VOICE_FILE, "rb")
    try:
        audio_stream = client.audio_isolation.audio_isolation(audio=audio_file)
        audio = b"".join(chunk for chunk in audio_stream)
        assert isinstance(audio, bytes), "Combined audio should be bytes"
        if not IN_GITHUB:
            play(audio)
    finally:
        audio_file.close()


def test_audio_isolation_as_stream():
    """Test audio isolation with streaming."""
    client = NeuralAudio()
    audio_file = open(DEFAULT_VOICE_FILE, "rb")
    try:
        audio_stream = client.audio_isolation.audio_isolation_stream(audio=audio_file)
        audio = b"".join(chunk for chunk in audio_stream)
        assert isinstance(audio, bytes), "Combined audio should be bytes"
        if not IN_GITHUB:
            play(audio)
    finally:
        audio_file.close()
