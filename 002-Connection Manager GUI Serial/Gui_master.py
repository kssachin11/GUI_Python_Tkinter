from tkinter import *
from tkinter import messagebox

class RootGUI:
    def __init__(self):
        self.root = Tk() #initialising the root
        self.root.title("Serial Communication")  #Title of GUI
        self.root.geometry("360x120")           # size of the GUI
        self.root.config(bg = "White")          #Background Colour
# Class to setup and create the communication manager with MCU
class ComGUI():
    def __init__(self,root, serial):
        #Frame
        self.root = root
        self.serial = serial
        self.frame = LabelFrame(root, text="Com Manager", padx=5, pady=5, bg="white") # create frame
        self.label_com =Label(self.frame, text="Available Port(s): ", bg="white", width=15, anchor="w") # create Labels
        self.label_bd =Label(self.frame, text="Baude Rate: ", bg="white", width=15, anchor="w")
        
        # Setup the Drop option menu
        self.ComOptionMenu()
        self.BaudOptionMenu()

         # Add the control buttons for refreshing the COMs & Connect
        self.btn_refresh = Button(self.frame, text="Refresh", width=10, command=self.com_refresh) #button for refresh
                                                                                                  # command is used to call a function that the buttom has to perform.

        self.btn_connect = Button(self.frame, text="Connect", width=10, state="disabled", command=self.serial_connect) #button for Connect

        self.padx = 20
        self.pady = 5
        # Put on the grid all the elements
        self.publish()

    def ComOptionMenu(self):                # for drop down menu
        '''
         Method to Get the available COMs connected to the PC
         and list them into the drop menu
        '''
       # coms = ["-","COM3","COM4", "COM5"]
        self.serial.getCOMList()  #available com ports
        self.clicked_com = StringVar() # object that allows to stock info and input informantion
        self.clicked_com.set(self.serial.com_list[0])  # drop down set
        self.drop_com = OptionMenu(self.frame, self.clicked_com, *self.serial.com_list, command =self.connect_ctrl) # dropping menu
        self.drop_com.config(width=10)


    def BaudOptionMenu(self):

        '''
         Method to list all the baud rates in a drop menu
        '''
        self.clicked_bd = StringVar()
        bds = ["-",
        "300",
        "600",
        "1200",
        "2400",
        "4800",
        "9600",
        "14400",
        "19200",
        "28800",
        "38400",
        "56000",
        "57600",
        "115200",
        "128000",
        "256000"]
        self.clicked_bd.set(bds[0])
        self.drop_baud = OptionMenu(self.frame, self.clicked_bd, *bds, command = self.connect_ctrl)
        self.drop_baud.config(width=10)

    def publish(self):      #Publish components
        '''
         Method to display all the Widget of the main frame
        '''
        #griding everything
        self.frame.grid(row=0,column=0, rowspan=3, columnspan=3, padx=5, pady=5)
        self.label_com.grid(column=1, row=2)
        self.drop_com.grid(column=2, row=2, padx=self.padx, pady=self.pady)
        self.label_bd.grid(column=1, row=3)
        self.drop_baud.grid(column=2, row=3)

        self.btn_refresh.grid(column=3, row=2)
        self.btn_connect.grid(column=3,row=3)

    def connect_ctrl(self, other):
        '''
        Method to keep the connect button disabled if all the 
        conditions are not cleared
        '''
        print("Connect Control")
        if "-" in self.clicked_bd.get() or "-" in self.clicked_com.get():   #to enable or disable connect button
            self.btn_connect["state"] = "disable"
        else:
            self.btn_connect["state"] = "active"
        
    def com_refresh(self):
        
        self.drop_com.destroy() #destroys widget
        self.ComOptionMenu()    #recreates widget
        self.drop_com.grid(column=2, row=2, padx=self.padx, pady=self.pady)
        logic = []
        self.connect_ctrl(logic)

    def serial_connect(self):
        print ("Connect")
         # If connection established move on
        if self.btn_connect["text"] in "Connect":
            #start the serial connection
            self.serial.SerialOpen(self)
            if self.serial.ser.status:
                # Update the COM manager
                self.btn_connect["text"] = "Disconnect"
                self.btn_refresh["state"] = "disable"
                self.drop_baud["state"] = "disable"
                self.drop_com["state"] = "disable"
                InfoMsg = f"Successful UART connection using {self.clicked_com.get()}"
                messagebox.showinfo("showinfo", InfoMsg)

            else:
                ErrorMsg = f"Failure to estabish UART connection using {self.clicked_com.get()} "
                messagebox.showerror("showerror", ErrorMsg)

            
        else:
            
            # Closing the Serial COM
            # Close the serial communication
            self.serial.SerialClose(self)

            InfoMsg = f"UART connection using {self.clicked_com.get()} is now closed"
            messagebox.showwarning("showinfo", InfoMsg)
            self.btn_connect["text"] = "Connect"
            self.btn_refresh["state"] = "active"
            self.drop_baud["state"] = "active"
            self.drop_com["state"] = "active"




if __name__== "__main__":
    RootGUI()
    ComGUI()