from tkinter import *
from pymsgbox import *
import CognitiveServicesTextAnalytics as Azure_Text_API
import CognitiveServicesSpeechAnalysis as Azure_Speech_API


def disp_main():

    def azure_text_search():
        Azure_Text_API.get_search_query()

    def azure_speech_search():
        warning = confirm(text="Please make sure your audio file is in the\n"
                               "'Audio_Files' folder otherwise this will not work.", title="Check Files",
                          buttons=['Proceed', 'Return'])
        if warning == "Proceed":
            Azure_Speech_API.handler()
        else:
            disp_main()

    def speech_credentials_check():
        frame.withdraw()
        usr_email = email.get()
        usr_pwd = pwd.get()
        email.delete(first=0, last=50)
        pwd.delete(first=0, last=50)
        if usr_email == "sbh5436@psu.edu" and usr_pwd == "@PSU.edu.com123#":
            azure_speech_search()
        else:
            pwd_notif = confirm(text="Password is Incorrect, Try Again...", title="Try Again",
                                buttons=['Acknowledge'])
            disp_main()

    def text_credentials_check():
        frame.withdraw()
        usr_email = email.get()
        usr_pwd = pwd.get()
        email.delete(first=0, last=50)
        pwd.delete(first=0, last=50)
        if usr_email == "sbh5436@psu.edu" and usr_pwd == "@PSU.edu.com123#":
            azure_text_search()
        else:
            pwd_notif = confirm(text="Password is Incorrect, Try Again...", title="Try Again",
                                buttons=['Acknowledge'])
            disp_main()

    def quit_scheme():
        exitClause = confirm(text="Are you sure you want to Exit?", title="Confirm Exit",
                             buttons=['Yes', 'No'])
        if exitClause == "Yes":
            exit()
        else:
            pass

    frame = Tk()
    frame.title("Azure Text Analysis")
    frame.columnconfigure(5, weight=1)
    frame.rowconfigure(5, weight=1)
    frame.configure(background='blue')  # window background color
    introlbl = Label(frame, text="Welcome to the Text Analysis Tool using\n"
                                 "Microsoft Azure Cognitive Services:\n"
                                 "Text Analytics/Speech-to-Text API")
    introlbl.grid(column=3, row=1)
    instructions = Label(frame, text="Enter your login Microsoft Login information and choose an option below")
    instructions.grid(column=3, row=2)
    label_email = Label(frame, text="Azure Email: ")
    label_email.grid(column=3, row=5)
    email = Entry(frame, width=50)
    email.grid(column=3, row=6)
    label_pwd = Label(frame, text="Azure Password: ")
    label_pwd.grid(column=3, row=7)
    pwd = Entry(frame, show="*", width=50)
    pwd.grid(column=3, row=8)
    text_login = Button(frame, text="Analyze Text", command=text_credentials_check)  # buttons to call functions
    text_login.grid(column=3, row=9)
    text_login.config(height=2, width=12)
    speech_login = Button(frame, text="Analyze Speech", command=speech_credentials_check)
    speech_login.grid(column=3, row=10)
    speech_login.config(height=2, width=12)
    exit_clause = Button(frame, text="Quit", command=quit_scheme)
    exit_clause.grid(column=3, row=11)
    exit_clause.config(height=2, width=5)

    frame.mainloop()  # mainloop for tk


if __name__ == '__main__':
    disp_main()
