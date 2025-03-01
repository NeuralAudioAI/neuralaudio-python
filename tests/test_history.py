from neuralaudio import GetSpeechHistoryResponse, NeuralAudio


def test_history():
    client = NeuralAudio()
    page_size = 5
    history = client.history.get_all(page_size=page_size)
    assert isinstance(history, GetSpeechHistoryResponse)
