from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient      # Azure API imports
from msrest.authentication import CognitiveServicesCredentials
import DisplaySpeech            # display module import
import json             # json to read the storage file for audio input

key_phrases = []
sentiment_Polarity = []


def analyze_speech():

    def parse_input():               # parses the input from json and uses the API to analyze it
        STORAGE = 'data_storage/speech_data.json'
        with open(STORAGE) as speech_data:
            data = json.load(speech_data)
            for i in data:
                inputVar = data['DisplayText']
        documents = [  # Dictionary to hold basic values for the API to evaluate
            {
                "id": "1",
                "language": "en",
                "text": inputVar
            }
        ]

        subscription_key = "d671436ef9ca42fb9b9205b8b209528c"  # Azure Account Subscription Key
        credentials = CognitiveServicesCredentials(subscription_key)  # Establishing Credentials
        text_analytics_url = "https://eastus.api.cognitive.microsoft.com/"  # setting the url for text analytics
        text_analytics = TextAnalyticsClient(endpoint=text_analytics_url, credentials=credentials)  # setting the endpoint and adding credentials
        sent_polarity = text_analytics.sentiment(documents=documents)  # adding a variable for sentiment polarity
        for document in sent_polarity.documents:  # for loop to search the list for docnames and scan text for polarity
            sentiment_Polarity.append("{:.4f}".format(document.score))  # appending sentiment polarity to new list

        DisplaySpeech.display(query=inputVar, sentiment=sentiment_Polarity)

    parse_input()


if __name__ == '__main__':     # if name = main calling main so that the file can be called without executing constantly
    analyze_speech()
