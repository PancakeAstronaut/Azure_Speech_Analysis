from tkinter import *
from pymsgbox import *
import CognitiveServicesTextAnalytics as Azure_Text_API
import CognitiveServicesSpeechAnalysis_Import as Azure_Speech_Import_API
import raw_voice_input as raw_wav


def disp_main():

    def azure_text_search():
        Azure_Text_API.get_search_query()

    def azure_speech_search_import():
        warning = confirm(text="Please make sure your audio file is in the\n"
                               "'Audio_Files' folder otherwise this will not work.", title="Check Files",
                          buttons=['Proceed', 'Return'])
        if warning == "Proceed":
            Azure_Speech_Import_API.handler('Audio_Files/Imported_Audio/test.wav')
        else:
            disp_main()

    def azure_speech_search_raw():
        warning = confirm(text="Please make sure your microphone is enabled\n"
                               "Speech recording will commence once you click\n"
                               "Proceed", title="Input Check",
                          buttons=['Proceed', 'Return'])
        if warning == "Proceed":
            raw_wav.main()
        else:
            disp_main()

    def speech_analysis_api_call_import():
        frame.withdraw()
        azure_speech_search_import()

    def speech_analysis_api_call_raw():
        frame.withdraw()
        azure_speech_search_raw()

    def text_analysis_api_call():
        frame.withdraw()
        azure_text_search()

    def quit_scheme():
        exitClause = confirm(text="Are you sure you want to Exit?", title="Confirm Exit",
                             buttons=['Yes', 'No'])
        if exitClause == "Yes":
            exit()
        else:
            pass

    frame = Tk()
    frame.title("Azure Text Analysis")
    frame.configure(background='blue')
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    paddingleft = Label(frame, bg='blue', text="              ")
    paddingleft.grid(column=0, row=0)
    paddingright = Label(frame, bg='blue', text="              ")
    paddingright.grid(column=5, row=0)
    paddingbottom = Label(frame, bg='blue', text="\n\n")
    paddingbottom.grid(column=3, row=15)
    paddingtop = Label(frame, bg='blue', text="\n\n")
    paddingtop.grid(column=3, row=0)
    introlbl = Label(frame, text="Welcome to the Text Analysis Tool using\n"
                                 "Microsoft Azure Cognitive Services:\n"
                                 "Text Analytics/Speech-to-Text API")
    introlbl.grid(column=3, row=1)
    text_login = Button(frame, text="Analyze Text", command=text_analysis_api_call)  # buttons to call functions
    text_login.grid(column=3, row=9)
    text_login.config(height=2, width=12)
    speech_login = Button(frame, text="Analyze Speech", command=speech_analysis_api_call_import)
    speech_login.grid(column=3, row=10)
    speech_login.config(height=2, width=12)
    speech_raw = Button(frame, text="Raw Input", command=speech_analysis_api_call_raw)
    speech_raw.grid(column=3, row=11)
    speech_raw.config(height=2, width=12)
    exit_clause = Button(frame, text="Quit", command=quit_scheme)
    exit_clause.grid(column=3, row=12)
    exit_clause.config(height=2, width=5)
    frame.mainloop()  # mainloop for tk


if __name__ == '__main__':
    disp_main()
