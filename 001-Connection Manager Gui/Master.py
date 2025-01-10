from Gui_master import RootGUI, ComGUI


RootMaster = RootGUI()
ComMaster = ComGUI(RootMaster.root)


RootMaster.root.mainloop()
#ComMaster.root.mainloop()