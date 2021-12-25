#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# https://docs.python-guide.org/

# system imports
import time

# pip install imports
import wx

# project/local imports
import GriduinoDialogs

# globals
TIMER_ID = 2000


class thisApp(wx.App):
    """doc string here"""

    def OnInit(self):
        self.frame = GriduinoDialogs.GriduinoFrame(None, wx.ID_ANY, "")
        self.clearTextLog()

        self.timer = wx.Timer(self, id=TIMER_ID)
        self.Bind(wx.EVT_TIMER, self.timertick, self.timer)
        self.timer.Start(2000)

        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

    def clearTextLog(self):
        self.frame.text_griduino_log.Clear()
        self.frame.text_griduino_log.AppendText("---Start log---\n")

    def timertick(self, event):
        self.frame.text_griduino_log.AppendText(time.ctime() + "\n")


# end of class MyApp


if __name__ == "__main__":
    # Create a new app, don't redirect stdout/stderr to a window.
    app = thisApp(False)
    app.MainLoop()
