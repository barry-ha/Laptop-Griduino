#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# https://docs.python-guide.org/

# system imports
#import time

# pip install imports
import wx       # pip install -U wxPython
import serial   # pip install -U pySerial
#from dateutil.parser import *     # pip install python-dateutil
#import calendar 

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
        self.Bind(wx.EVT_TIMER, self.timerTick, self.timer)
        self.timer.Start(100)

        self.Bind(wx.EVT_BUTTON, self.DoPortOkButton, self.frame.button_port_ok)
        self.Bind(wx.EVT_BUTTON, self.DoButtonSaveKML, self.frame.button_download_gps)
        self.Bind(wx.EVT_BUTTON, self.DoButtonSendText, self.frame.button_send_text)

        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

    def clearTextLog(self):
        self.frame.text_griduino_log.Clear()
        self.frame.text_griduino_log.AppendText("---Start log---\n")

    def timerTick(self, event):
        #self.frame.text_griduino_log.AppendText(time.ctime() + "\n")
        if (self.mySerial.is_open):
          while True:     # read from USB until data is exhausted
            data = self.mySerial.readline().decode("utf-8")
            if (data != ''):
              self.frame.text_griduino_log.AppendText(data)
              self.DoUpdateClockDialog(data)
            else:
              break 

    def DoPortOkButton(self, event):
        print("main.py - event button_port_ok")
        event.Skip()

        # read user's selection from dialog
        offset = self.frame.radiobox_port.GetSelection()
        count = self.frame.radiobox_port.GetCount()
        fullportname = self.frame.radiobox_port.GetItemLabel(offset)
        port = fullportname.split()[0]    # first word of the long port name e.g. "COM17"

        self.mySerial.close()
        self.mySerial.baudrate = 115200
        self.mySerial.timeout = 0     # non-blocking read
        self.mySerial.port = port     # be sure to test error handling with port name "bogus"
        try:
            self.mySerial.open()      # opens in binary (not text) mode
            print('Connected to port: ' + self.mySerial.name) # check which port was really opened
            self.frame.notebook_1.SetSelection(1)  # switch to new tab in notebook
            self.frame.frame_statusbar.SetStatusText("Running", 0)  # update status
            self.frame.frame_statusbar.SetStatusText(fullportname, 1)
        except:
            import sys
            (exctype, value, tb) = sys.exc_info()
            print(exctype)      # <class 'serial.serialutil.SerialException'>
            print(type(value))  # <class 'serial.serialutil.SerialException'>
            print(value)        # could not open port 'bogus': FileNotFoundError(2, 'The system cannot find the file specified.', None, 2)
            print(tb)           # <traceback object at 0x0000015A5FEE68C0>
            wx.MessageDialog(
              None,   #parent
              "Unable to open port '{0}'\n\n{1}".format(self.mySerial.name, value),
              self.frame.GetTitle(),   # message box has same window title as the UI
              wx.OK_DEFAULT + wx.ICON_INFORMATION
            ).ShowModal()

    def DoButtonSaveKML(self, event):
        print("main.py - event button_download_gps")

    def DoButtonSendText(self, event):
        print("main.py - event button_send_text")
        if (self.mySerial.is_open):
            text = self.frame.text_griduino_send.GetValue().encode("utf-8")
            self.mySerial.write(text)
            self.frame.text_griduino_send.SetValue('')
        return

    def isDateFormatISO(self, data):
        # input: data = string similar to "2022-03-02 12:34:56+00:00"
        # First filter to recognize GMT time is string length
        if (len(data) == 27):          # 27 == len("2022-01-01 22:11:00+00:00\r\n")
            #looks okay so far
            #if (data[4] == '-')
            #    if (data[7] == '-')
            return True     # indicate IS a valid ISO date
        else:
            return False    # indicate NOT an ISO date

    def DoUpdateClockDialog(self,data):
        # From: https://docs.python.org/3/library/datetime.html#datetime.datetime 
        #
        # classmethod datetime.fromisoformat(date_string)
        # Return a datetime corresponding to a date_string in one of the 
        # formats emitted by date.isoformat() and datetime.isoformat().
        # Specifically, this function supports strings in the format:
        #       YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]
        #
        # From: https://www.progress.com/blogs/understanding-iso-8601-date-and-time-format 
        # We made Griduino produce ISO 8601 date/time format strings:
        #       2022-01-01 21:49:49+00:00
        #
        # Better yet, wxPython has all the date/time parsing and formatting functions needed
        # From: https://wxpython.org/Phoenix/docs/html/wx.DateTime.html#wx.DateTime.ParseISOCombined 
        #
        if (self.isDateFormatISO(data)):
            #print("Possible ISO date: {0} ({1} bytes)".format(data, len(data)))
            # although module time provides strptime() function to parse text into timestamps,
            # it reportedly has subtle bugs so we use dateutil library instead
            # Stack overflow: https://stackoverflow.com/questions/969285/how-do-i-translate-an-iso-8601-datetime-string-into-a-python-datetime-object 
            # Replacement:    https://pypi.org/project/python-dateutil/ 
            # Code on GitHub: https://github.com/dateutil/dateutil/
            
            #now = parse("Sat Oct 11 17:13:46 UTC 2003")
            #now = parse("2022-03-02 23:23:04+00:00")
            #now = wx.DateTime.ParseISOCombined(data, " ") # exception: first argument must be DateTime object
            
            #datetime.fromisoformat()
            #if (rc):
            if (True):
                #showDate = "{0} {1}, {2}".format(now.GetMonth(wx.DateTime.UTC), now.GetDay(wx.DateTime.UTC), now.GetYear(wx.DateTime.UTC))
                #showtime = "{0} : {1} : {2} GMT".format(now.GetHour(wx.DateTime.UTC), now.GetMinute(wx.DateTime.UTC), now.GetSecond(wx.DateTime.UTC))
                #print("Griduino date stamp: %s" % showDate)
                #print("Griduino time stamp: %s\n" % showtime)

                now = wx.DateTime.Now()                     # temp debug
                now = now.MakeUTC()                         # temp debug
                showtime = now.Format('%H : %M : %S GMT')   # temp debug http://www.cplusplus.com/reference/ctime/strftime/
                showDate = now.Format('%b %e, %Y')          # temp debug http://www.cplusplus.com/reference/ctime/strftime/

                self.frame.label_gmt.SetLabel(showtime)
                self.frame.label_date.SetLabel(showDate)
            else:
                print("Did not parse date/time from: {}".format(data))

# end of class MyApp


if __name__ == "__main__":
    # Create a new app, don't redirect stdout/stderr to a window.
    app = thisApp(False)
    app.MainLoop()
