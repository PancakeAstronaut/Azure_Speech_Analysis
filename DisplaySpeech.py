from tkinter import *               # tkinter for GUI assembly
from pymsgbox import *              # for confirmation windows
import dashboard                    # calling back to the dashboard
import AzureSpeechAnalysis as clear_polarity            # for clearing the sentiment polarity index


def exit_func():
    exitClause = confirm(text="Are you sure you want to Exit?", title="Confirm Exit",
                         buttons=['Yes', 'No'])         # exit confirmation
    if exitClause == "Yes":
        exit()
    else:
        pass


def display(query, sentiment):              # display function

    def back():
        backconf = confirm(text="Are you sure you want to return to the Dashboard?", title="Back to Dashboard?",
                           buttons=['Yes', 'No'])
        if backconf == "Yes":
            disp.withdraw()
            clear_polarity.sentiment_Polarity.pop()
            dashboard.disp_main()
        else:
            pass

    polarity_analysis = round(float(sentiment[0]), 1)           # evaluates the sentiment polarity value
    if polarity_analysis > .5:
        tone = "Positive"
    elif polarity_analysis < .5:
        tone = "Negative"
    elif polarity_analysis == .5:
        tone = "Neutral"
    else:
        tone = "Couldn't Capture Tone"

    disp = Tk()         # GUI assembly
    disp.title("SpeechTone Report")
    disp.columnconfigure(0, weight=1)
    disp.rowconfigure(0, weight=1)
    disp.configure(background='blue')
    title_lbl = Label(disp, text="Azure Text Analysis of User Input Data:")
    title_lbl.grid(column=2, row=2)
    div1 = Label(disp, text="------------------------\nUser Input String")
    div1.grid(column=2, row=3)
    query_lbl = Label(disp, text=query)
    query_lbl.grid(column=2, row=4)
    div2 = Label(disp, text="------------------------\nSentiment Polarity")
    div2.grid(column=2, row=5)
    sentiment_lbl = Label(disp, text=sentiment)
    sentiment_lbl.grid(column=2, row=6)
    div3 = Label(disp, text="------------------------\nTone of Phrase")
    div3.grid(column=2, row=7)
    tone_lbl = Label(disp, text=tone)
    tone_lbl.grid(column=2, row=8)
    div4 = Label(disp, text="------------------------")
    div4.grid(column=2, row=9)
    backbtn = Button(disp, text="Return to Dashboard", command=back)
    backbtn.grid(column=2, row=10)
    exit_btn = Button(disp, text="Exit", command=exit_func)
    exit_btn.grid(column=2, row=11)
    disp.mainloop()


if __name__ == '__main__':
    display()

