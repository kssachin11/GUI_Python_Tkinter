from Gui_master import RootGUI, ComGUI
from Serial_com_ctrl import SerialCtrl

MySerial = SerialCtrl()
RootMaster = RootGUI()

# Initiate the Communication Master class that will manage all the other GUI classes
ComMaster = ComGUI(RootMaster.root, MySerial)


RootMaster.root.mainloop()
#ComMaster.root.mainloop()