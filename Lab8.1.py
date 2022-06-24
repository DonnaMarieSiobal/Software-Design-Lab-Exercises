from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title = "Tokyo Ghoul")
        self.setResizable(False);
        imageLabel = self.addLabel(text = "",row = 0, column = 0,sticky = "NSEW")
        textLabel = self.addLabel(text = "KANEKI",row = 1, column = 0,sticky = "NSEW")
        self.image = PhotoImage(file = "200.gif")
        imageLabel["image"] = self.image
        font = Font(family = "Verdana", size = 20,slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "red"

def main():
   ImageDemo().mainloop()
if __name__ == "__main__":
   main()

