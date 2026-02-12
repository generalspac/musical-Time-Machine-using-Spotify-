from tkinter import *
import functions
from tkinter import messagebox


def confirm():
    """for the confirm button"""
    print(entry.get())
    valeur = entry.get() #we get what we have written in the entry box
    entry.delete(0, END)  # Delete what we have written in the entry
    valid=functions.date_format(valeur) #to verify the date and create the playlist
    if valid:
        print("your playlist was created successfully")
        messagebox.showinfo(title='success',message="your playlist was created successfully")
    else: 
        entry.insert(0,valeur)




# window
window = Tk()
window.title("Connect to your Spotify")
window.configure(bg="black")

window_width = 600
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")


# label
label = Label(window, text="Spotify", fg="green", font=("Helvetica", 24, "bold"), bg="black")
label.pack(expand=True)

# Create and configure the entry box
entry = Entry(window, width=30)
entry.insert(END, string="(yyyy-mm-dd)")
entry.pack(pady=20)  # Adding some padding


# Centering elements using the pack geometry manager
label.pack(expand=True)
entry.pack(expand=True)

#Button
confirm_button = Button(window, text="Confirm",command=confirm)
confirm_button.pack(pady=10)


# Run the application
window.mainloop()
