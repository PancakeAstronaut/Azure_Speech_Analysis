import json                 # json to format the response information
import requests             # requests to make HTTP POST requests to Cognitive Services
import AzureSpeechAnalysis as analyze

KEY = '31efbb95e1a04281bb34a2c098a9891c'        # Azure API Key
AUDIO_INPUT = 'Audio_Files/' + 'test.wav'                        # Input File Name/Path
REGION = 'eastus'                               # Service Region
MODE = 'interactive'                            # Use Mode
LANG = 'en-US'                                  # Language Specification
FORMAT = 'simple'                               # Call Format
STORAGE = 'data_storage/speech_data.json'


def handler():                          # Service Handler
    # 1. Get an Authorization Token
    token = get_token()
    # 2. Perform Speech Recognition
    result = get_text(token=token, audio=AUDIO_INPUT)
    # 3. Store Results
    with open(STORAGE, 'w') as data_dump:
        json.dump(result, data_dump, ensure_ascii=False, indent=4)

    analyze.analyze_speech()


def get_token():                # Create and Retrieve access token from Cognitive Services.
    url = 'https://speech.platform.bing.com/synthesize'
    headers = {
        'Ocp-Apim-Subscription-Key': KEY
    }
    r = requests.post(url=url, headers=headers)
    token = r.content
    return token


def get_text(token, audio):         # Uses the Bing Speech to Text API to convert audio file to text string
    url = 'https://{0}.stt.speech.microsoft.com/speech/recognition/{1}/' \
          'cognitiveservices/v1?language={2}&format={3}'.format(REGION, MODE, LANG, FORMAT)
    headers = {
        'Accept': 'application/json',
        'Ocp-Apim-Subscription-Key': KEY,
        'Transfer-Encoding': 'chunked',
        'Content-type': 'audio/wav; codec=audio/pcm; samplerate=16000',
        'Authorization': 'Bearer {0}'.format(token)
    }
    r = requests.post(url=url, headers=headers, data=stream_audio_file(audio))
    results = json.loads(r.content)
    return results


def stream_audio_file(speech_file, chunk_size=1024):          # Stream audio data to send to the API
    # Chunk audio file
    with open(speech_file, 'rb') as f:
        while 1:
            data = f.read(1024)
            if not data:
                break
            yield data


if __name__ == '__main__':              # this is here to define main and ensures the function doesn't run endlessly
    main()
