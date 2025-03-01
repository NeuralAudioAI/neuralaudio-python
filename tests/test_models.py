from neuralaudio import Model
from neuralaudio.client import NeuralAudio


def test_models_get_all():
    client = NeuralAudio()
    models = client.models.get_all()
    assert len(models) > 0
    assert isinstance(models[0], Model)
