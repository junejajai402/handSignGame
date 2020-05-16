import tkinter as tk
#import relevant Packages

window = tk.Tk() #creates a window for the gui

greeting = tk.Label(text="Hello, Tkinter") #creating tk object

greeting.pack() #tightly packs the window to surround the created object

window.mainloop() #Allows the gui to stay and listen for events
