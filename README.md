# NeuralAudioAI Python SDK

![LOGO](https://storage.googleapis.com/crypto-utils-1/Header%20with%20Pattern.png)

[![Website](https://img.shields.io/badge/🌎-NeuralAudioAI-white.svg)](https://www.neuralaudio.solutions)
[![Twitter](https://badgen.net/badge/black/NeuralAudioAI/icon?icon=twitter&label)](https://x.com/NeuralAudioAI)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-huggingface-black.svg)](https://huggingface.co/NeuralAudioAI)

Python SDK for [NeuralAudioAI](https://www.neuralaudio.solutions/). NeuralAudioAI is a gamechanger, introducing the new quality standards and prices of TTS services.

## Installation

```bash
pip install neural_audio
```

## 🎤 Usage

[![Open in Spaces](https://img.shields.io/badge/🤗 -Open%20in%20Spaces-blue.svg)](https://huggingface.co/spaces/)

### Models

1. **NA_base** (`na_base_v1`)

   - Solid baseline, suits for most cases
   - Support of 15 languages
   - Real-time speed

2. **NA_pro** (`na_pro_v1`)
   - Highest quality
   - Best shot for PROs & Businesses
   - Support of 52 languages

3. **NA_vic** (`na_vic`) - comming soon...

```py
from neural_audio import NeuralAudio

client = NeuralAudio(
    api_key="YOUR_API_KEY",
)

client.text_to_speech.convert(
    voice_id="32dcdovdplsmcos",
    model_id="base_v1",
    text="Hello world!",
)
```

<details> <summary> Hear the voice of the future </summary>

**Test us!** Want to see what we can? Visit the [NeuralAudioAI](https://www.neuralaudio.solutions) to test our models, hear their voices or  create your own!

</details>

## Voice clonning

Effortlessly recreate your voice with cutting-edge AI. Instantly generate a lifelike clone and explore the possibilities of voice transformation!

```py
from neural_audio import NeuralAudio

client = NeuralAudio(
  api_key="YOUR_API_KEY",
)

voice = client.clone_voice(
    name="Alex",
    description="A well-known male actor in his 50s, with a touch of excitement in his tone and a subtle sense of urgency in his delivery.",
    sample="./sample_0.wav" # or ["./sample_0.wav", "./sample_1.mp3", "./sample_2.mkv"],
)
```

## ⚡️ Real-time Streaming

Let your agents have real converstions with real-time audio streams. Both inside and out.

### Output streaming
```py
from neural_audio import NeuralAudio

streaming_client = NeuralAudio.streaming_client(
  api_key="YOUR_API_KEY",
)

audio_stream = streaming_client.text_to_speech.convert(
    text="Hi! How may I help you?",
    voice="Adam",
    model="na_pro_v1"
)

stream(audio_stream)
```

### Input streaming

Stream text chunks into audio as it's being generated, with <1s latency. Note: if chunks don't end with space or punctuation (" ", ".", "?", "!"), the stream will wait for more text.

```py
from neural_audio import NeuralAudio

streaming_client = NeuralAudio.streaming_client(
  api_key="YOUR_API_KEY",
)

def audio_stream():
    with open("live_audio_input.wav", "rb") as audio:
        while chunk := audio.read(4096): 
            yield chunk

audio_stream = streaming_client.conversation(
    audio=audio_stream(),
    voice="Adam",
    llm="gpt-4o", # OPENAI_API_KEY required
    model="na_pro_v1"
)

stream(audio_stream)
```
