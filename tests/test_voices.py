from neuralaudio import Voice, VoiceSettings, NeuralAudio
from .utils import DEFAULT_VOICE


def test_get_voice():
    client = NeuralAudio()
    voice_id = DEFAULT_VOICE

    voice = client.voices.get(voice_id)
    assert isinstance(voice, Voice)

    assert voice.voice_id == voice_id
    if voice.settings is not None:
        assert isinstance(voice.settings, VoiceSettings)


def test_get_voices():
    client = NeuralAudio()
    response = client.voices.get_all()

    assert len(response.voices) > 0

    for voice in response.voices:
        assert isinstance(voice, Voice)
