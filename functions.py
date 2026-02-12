from datetime import datetime
from tkinter import messagebox
import spotify


def date_format(date):
    '''this functions is here to verify if the date is correct,if it's the case, it creates the playlist'''
    year=datetime.now().year

    #date = input("which date would you like?(yyyy-mm-dd)  " )
    date_list=date.split('-')
    if len(date_list)==3 and len(date_list[0])==4 and len(date_list[1])==2 and len(date_list[2])==2:
        if int(date_list[1])<=12 and int(date_list[1])>0 and int(date_list[2])<=31 and int(date_list[2])>0 and int(date_list[0])<=year:
            spotify.creating_playlist(date)  #we create the playlist
        else:
            messagebox.showinfo(title='date',message='This date is not valid,try again(yyyy-MM-DD)')
            return False
    else:
        messagebox.showinfo(title='date', message='This date is not valid,try again(YYYY-MM-DD')
        return False
    return True