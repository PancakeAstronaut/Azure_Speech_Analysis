from tkinter import *
import dashboard as launch
from pymsgbox import *


def prompt():

    def login_request():
        login_window.withdraw()
        usr_email = email.get()
        usr_pwd = pwd.get()
        email.delete(first=0, last=50)
        pwd.delete(first=0, last=50)
        if usr_email == "sbh5436@psu.edu" and usr_pwd == "@PSU.edu.com123#":
            launch.disp_main()
        else:
            pwd_notif = confirm(text="Password is Incorrect, Try Again...", title="Try Again",
                                buttons=['Acknowledge'])
            prompt()

    def quit_login():
        exitClause = confirm(text="Are you sure you want to Exit?", title="Confirm Exit",
                             buttons=['Yes', 'No'])
        if exitClause == "Yes":
            exit()
        else:
            pass

    login_window = Tk()
    login_window.columnconfigure(0, weight=1)
    login_window.columnconfigure(3, weight=1)
    login_window.rowconfigure(0, weight=1)
    login_window.rowconfigure(5, weight=1)
    login_window.configure(background='blue')
    instructions = Label(login_window, text="Enter your MSDN login credentials below to start: ")
    instructions.grid(column=3, row=2)
    label_email = Label(login_window, text="Azure Email: ")
    label_email.grid(column=3, row=5)
    email = Entry(login_window, width=50)
    email.grid(column=3, row=6)
    label_pwd = Label(login_window, text="Azure Password: ")
    label_pwd.grid(column=3, row=7)
    pwd = Entry(login_window, show="*", width=50)
    pwd.grid(column=3, row=8)
    text_login = Button(login_window, text="Login", command=login_request)  # buttons to call functions
    text_login.grid(column=3, row=9)
    text_login.config(height=2, width=12)
    exit_clause = Button(login_window, text="Quit", command=quit_login)
    exit_clause.grid(column=3, row=10)
    exit_clause.config(height=2, width=5)
    login_window.mainloop()


if __name__ == '__main__':
    prompt()
