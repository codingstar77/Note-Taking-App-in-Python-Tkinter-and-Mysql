from tkinter import *
from NoteDB import NoteDB
from dashboard import Dashboard
if __name__=="__main__":
    try:
        #Add Your Database username and password here
        db=NoteDB(username="root",password="kd99")
        Dashboard().initUI(db)
    except Exception as e:
        messagebox.showinfo("Error","Unable to establish database connection.")
        
   

    
