#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# https://docs.python-guide.org/
#
import wx
import GriduinoDialogs

class thisApp(wx.App):
    def OnInit(self):
        self.frame = GriduinoDialogs.GriduinoFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
  app = thisApp(False)  # Create a new app, don't redirect stdout/stderr to a window.
  app.MainLoop()