#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# https://docs.python-guide.org/
#
import wx
import GriduinoDialogs
import time
TIMER_ID = 2000

class thisApp(wx.App):
    def OnInit(self):
        self.frame = GriduinoDialogs.GriduinoFrame(None, wx.ID_ANY, "")
        self.frame.text_griduino_log.AppendText('---Start log---\n')

        self.timer = wx.Timer(self, id=TIMER_ID)
        self.Bind(wx.EVT_TIMER, self.timertick, self.timer)
        self.timer.Start(1000)

        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

    def timertick(self, event):
        self.frame.text_griduino_log.AppendText(time.ctime()+'\n')

# end of class MyApp

if __name__ == "__main__":
  app = thisApp(False)  # Create a new app, don't redirect stdout/stderr to a window.
  app.MainLoop()