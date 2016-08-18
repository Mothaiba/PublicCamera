# importing wx files
import wx

# import the newly created GUI file
import gui

# importing * : to enable writing sin(13) instead of math.sin(13)
from math import *

tungui = gui
class CalcFrame(tungui.MainFrame):
    # constructor
    def __init__(self):
        # initialize parent class
        tungui.MainFrame.__init__(self, None)

    # what to when 'Solve' is clicked
    # wx calls this function with and 'event' object
    def solveFunc(self, event):
        zz = 'text'
        try:
            # evaluate the string in 'text' and put the answer back
            ans = eval(self.__getattribute__('text').GetValue())
            self.text.SetValue(str(ans))
        except Exception:
            print 'error'

    # put a blank string in text when 'Clear' is clicked
    def clearFunc(self, event):
        self.text.SetValue(str(''))


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = CalcFrame()
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()