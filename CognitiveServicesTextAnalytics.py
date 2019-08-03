from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
from tkinter import *
from pymsgbox import *
import display

key_phrases = []
sentiment_Polarity = []


def exit_func():
    exitClause = confirm(text="Are you sure you want to Exit?", title="Confirm Exit",
                         buttons=['Yes', 'No'])
    if exitClause == "Yes":
        exit()
    else:
        pass


def get_search_query():

    def validate_azure_credentials():
        inputVar = search_string.get()
        documents = [  # Dictionary to hold basic values for the API to evaluate
            {
                "id": "1",
                "language": "en",
                "text": inputVar
            }
        ]
        search_string.delete(first=0, last=50)
        search.withdraw()
        subscription_key = "d671436ef9ca42fb9b9205b8b209528c"  # Azure Account Subscription Key
        credentials = CognitiveServicesCredentials(subscription_key)  # Establishing Credentials
        text_analytics_url = "https://eastus.api.cognitive.microsoft.com/"  # setting the url for text analytics
        text_analytics = TextAnalyticsClient(endpoint=text_analytics_url, credentials=credentials)  # setting the endpoint and adding credentials
        sent_polarity = text_analytics.sentiment(documents=documents)  # adding a variable for sentiment polarity
        for document in sent_polarity.documents:  # for loop to search the list for docnames and scan text for polarity
            sentiment_Polarity.append("{:.4f}".format(document.score))  # appending sentiment polarity to new list

        display.display(inputVar, sentiment_Polarity)

    search = Tk()
    search.title("Azure Text Analytics Search")  # window title
    search.columnconfigure(0, weight=1)
    search.rowconfigure(0, weight=1)
    search.configure(background='blue')  # window background color
    label_term1 = Label(search, text="Enter a string of text for Azure to analyze:")
    label_term1.grid(column=2, row=0)  # labels and entry boxes
    search_string = Entry(search, width=50)
    search_string.grid(column=2, row=1)
    Azure_call = Button(search, text="Analyze", command=validate_azure_credentials)
    Azure_call.grid(column=2, row=2)
    Exit_btn = Button(search, text="Exit", command=exit_func)
    Exit_btn.grid(column=2, row=3)
    search.mainloop()


if __name__ == '__main__':     # if name = main calling main so that the file can be called without executing constantly
    get_search_query()