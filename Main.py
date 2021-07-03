from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        locationError.config(text=Folder_Name, fg="green")

    else:
        locationError.config(text="Please Choose Folder!!", fg="red")


def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if len(url) > 1:
        ytdError.config(text="")
        yt = YouTube(url)

        if (choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif (choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif (choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Link Not Found! try again", fg="red")

    select.download(Folder_Name)
    ytdError.config(text="Download Completed!", bg='white', fg='black', font=("Helvetica", 15, "bold"))


root = Tk()
root.configure(bg='black')
root.title("YouTube Vedio Downloader")
root.geometry("600x500")
root.columnconfigure(0, weight=1)

ytdLabel = Label(root, text="Enter The URL Link of Vedio", font=("Helvetica", 20, "bold"), bg='purple', fg='white')
ytdLabel.grid(pady=15)

ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar,)
ytdEntry.grid(padx=15)

ytdError = Label(root, text="", fg="red", font=("jost", 15), bg = 'black')
ytdError.grid()

saveLabel = Label(root, text="Select Downloading Path", font=("Helventica", 14, "bold"), bg='purple', fg='white')
saveLabel.grid(pady=15)

saveEntry = Button(root, width=15, bg="green", fg="white", text="Choose Folder", command=openLocation)
saveEntry.grid()

# Error Msg location
locationError = Label(root, text="", fg="white", font=("jost", 15),bg = 'black')
locationError.grid()

ytdQuality = Label(root, text="Select vedio Quality", font=("Helventica", 15, "italic"), bg='blue', fg='white')
ytdQuality.grid(pady=15)

choices = ["High Quality","Low Quality", "Only Audio"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid()

# donwload btn
downloadbtn = Button(root, text="Donwload!", width=15, bg="red", fg="white", command=DownloadVideo)
downloadbtn.grid(pady=20)

# developer Label
developerlabel = Label(root, text="Thank you! for Downloading with us @-Ranjan's Developers", font=("Helventica", 15),
                       bg='black', fg='white')
developerlabel.grid(pady=20)
root.mainloop()
