from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
from stft import stft
ws = Tk()
ws.title('Music Plagiarism Detection')
ws.geometry('300x500') 
from rabin2 import PlagiarismChecker
from os.path import dirname, join

def open_file1():
    file = askopenfile(mode='r', filetypes=[('Audio Files', '*wav')])
    if file is not None:       
        print(file.name)
        stft(file.name,'./document_a.txt')

# def open_file2():
#     file = askopenfile(mode='r', filetypes=[('Audio Files', '*wav')])
#     if file is not None:
#         print(file.name)
#         stft(file.name,'./document_b.txt')

def uploadFiles():
    pb1 = Progressbar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=5, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)

    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)

  
plagperc=0
def checkplag():
    current_dir = dirname(__file__)
    checker = PlagiarismChecker(
    join(current_dir, "./document_a.txt"),
    join(current_dir, "./document_b.txt")
    )
    print('The percentage of plagiarism held by the audio is  {0}%'.format(
    checker.get_rate()))
    plagperc=checker.get_rate()
    unique=100-plagperc
    ws.geometry('600x500')
    showplag = Label(ws, text ='The percentage of plagiarism held by the audio is  {0}% \n\t The audio is {1}% unique.'.format(
    plagperc,unique),font=("Arial", 14))
    showplag.grid(row=10, columnspan=3, pady=20)

a1 = Label(
    ws, 
    text='Upload audio file', font=("Arial", 25))
a1.grid(row=0, column=0, padx=10)

a1btn = tkinter.Button(
    ws, 
    text ='Choose File ', 
    width=10,height=3,
    command = lambda:open_file1(),
     fg='black',   bg='white',
     font=('Arial', 14)
    ) 
a1btn.grid(row=3, column=0,columnspan=1, padx=20,pady=10)

# a2 = Label(
#     ws, 
#     text='Upload audio file '
#     )
# a2.grid(row=1, column=0, padx=10)

# a2btn = Button(
#     ws, 
#     text ='Choose File ', 
#     command = lambda:open_file2()
#     ) 
# a2btn.grid(row=1, column=1)

upld =tkinter.Button(
    ws, 
    text='Upload Files', 
    width=10,height=3,
     fg='white',   bg='black',
     font=('Arial', 14),
    command=uploadFiles
    )
upld.grid(row=5, column=0, columnspan=1, padx=20,pady=10)
plag = tkinter.Button(
    ws, 
    text='Check Plagiarism', 
    width=15,height=3,
    command=checkplag,
     fg='white',   bg='purple',
     font=('Arial', 14)
    )

plag.grid(row=8, column=0,  pady=10)

# button = Button(ws, text = "Hello!", command = showplagiarism )
# button.pack()



ws.mainloop()