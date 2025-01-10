from tkinter import *

class RootGUI:
    def __init__(self):
        self.root = Tk() #initialising the root
        self.root.title("Serial Communication")  #Title of GUI
        self.root.geometry("360x120")           # size of the GUI
        self.root.config(bg = "White")          #Background Colour

class ComGUI():
    def __init__(self,root):
        #Frame
        self.root = root
        self.frame = LabelFrame(root, text="Com Manager", padx=5, pady=5, bg="white") # create frame
        self.label_com =Label(self.frame, text="Available Port(s): ", bg="white", width=15, anchor="w") # create Labels
        self.publish()

    def publish(self):      #Publish components
        #griding everything
        self.frame.grid(row=0,column=0, rowspan=3, columnspan=3, padx=5, pady=5)
        self.label_com.grid(column=1, row=2)

if __name__== "__main__":
    RootGUI()
    ComGUI()