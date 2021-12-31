#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# https://docs.python-guide.org/

# system imports
import time

# pip install imports
import wx       # pip install -U wxPython
import serial   # pip install -U pySerial

# project/local imports
import GriduinoDialogs

# globals
TIMER_ID = 2000

class thisApp(wx.App):
    """doc string here"""
    mySerial = serial.Serial()

    def OnInit(self):
        self.frame = GriduinoDialogs.GriduinoFrame(None, wx.ID_ANY, "")
        self.clearTextLog()

        self.timer = wx.Timer(self, id=TIMER_ID)
        self.Bind(wx.EVT_TIMER, self.timertick, self.timer)
        self.timer.Start(2000)

        self.Bind(wx.EVT_BUTTON, self.DoPortOkButton, self.frame.button_port_ok)
        self.Bind(wx.EVT_BUTTON, self.DoButtonSaveKML, self.frame.button_download_gps)
        #mySerial = serial.Serial()

        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

    def clearTextLog(self):
        self.frame.text_griduino_log.Clear()
        self.frame.text_griduino_log.AppendText("---Start log---\n")

    def timertick(self, event):
        self.frame.text_griduino_log.AppendText(time.ctime() + "\n")

    def DoPortOkButton(self, event):
        print("main.py - event button_port_ok")
        event.Skip()

        # read user's selection from dialog
        offset = self.frame.radiobox_port.GetSelection()
        count = self.frame.radiobox_port.GetCount()
        port = self.frame.radiobox_port.GetItemLabel(offset).split()[0]

        self.mySerial.close()
        self.mySerial.baudrate = 115200
        self.mySerial.port = port     # also test error handling with port name "bogus"
        try:
            # opens in binary (not text) mode
            self.mySerial.open()
            # check which port was really opened
            print('Connected to port: ' + self.mySerial.name)
            self.frame.notebook_1.SetSelection(1)  # success! switch to new tab in notebook
        except:
            import sys
            (type, value, tb) = sys.exc_info()
            print(type)     # <class 'serial.serialutil.SerialException'>
            print(value)    # could not open port 'bogus': FileNotFoundError(2, 'The system cannot find the file specified.', None, 2)
            print(tb)       # <traceback object at 0x0000015A5FEE68C0>
            wx.MessageDialog(
              None,   #parent
              "Unable to open port '{0}'\n\n{1}".format(self.mySerial.name, value),
              self.frame.GetTitle(),   # message box has same window title as the UI
              wx.OK_DEFAULT + wx.ICON_INFORMATION
            ).ShowModal()
        # todo - remember the selected port, to be used in all of our pySerial operations


    def DoButtonSaveKML(self, event):
        print("main.py - event button_download_gps")

    #def ParseTime(self,isotime):
        # From: https://docs.python.org/3/library/datetime.html#datetime.datetime 
        #
        # classmethod datetime.fromisoformat(date_string)
        # Return a datetime corresponding to a date_string in one of the 
        # formats emitted by date.isoformat() and datetime.isoformat().
        # Specifically, this function supports strings in the format:
        # YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]
        #
        # Therefore, we will make Griduino produce ISO date/time format strings
        #
        #print("ParseTime(" + isotime + ")")


# end of class MyApp


if __name__ == "__main__":
    # Create a new app, don't redirect stdout/stderr to a window.
    app = thisApp(False)
    app.MainLoop()
    #input("Press enter to exit")
    #import os
    #os.system("pause")