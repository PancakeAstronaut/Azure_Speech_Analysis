from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
from tkinter import *
from pymsgbox import *
import display
import dashboard

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

    def back_dash():
        back = confirm(text="Are you sure you want to return to the Dashboard?", title="Back to Dashboard?",
                       buttons=['Yes', 'No'])
        if back == "Yes":
            search.withdraw()
            dashboard.disp_main()
        else:
            pass

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
    search.title("SpeechTone Search")  # window title
    search.columnconfigure(0, weight=1)
    search.rowconfigure(0, weight=1)
    search.configure(background='blue')  # window background color
    label_term1 = Label(search, text="Enter text to analyze:")
    label_term1.grid(column=3, row=2)  # labels and entry boxes
    search_string = Entry(search, width=50)
    search_string.grid(column=3, row=3)
    Azure_call = Button(search, text="Analyze", command=validate_azure_credentials)
    Azure_call.grid(column=3, row=4)
    Exit_btn = Button(search, text="Exit", command=exit_func)
    Exit_btn.grid(column=3, row=5)
    backbtn = Button(search, text="Back to Dashboard", command=back_dash)
    backbtn.grid(column=1, row=0)
    paddingright = Label(search, bg='blue', text="                 ")
    paddingright.grid(column=5, row=0)
    paddingtop = Label(search, bg='blue', text="\n\n")
    paddingtop.grid(column=3, row=0)
    paddingbottom = Label(search, bg='blue', text="\n\n")
    paddingbottom.grid(column=3, row=7)
    search.mainloop()


if __name__ == '__main__':     # if name = main calling main so that the file can be called without executing constantly
    get_search_query()
