#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0pre on Mon Dec 20 14:17:38 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import serial
import serial.tools.list_ports
# end wxGlade


class GriduinoFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: GriduinoFrame.__init__
        # --- frame ---
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((500, 300))
        self.SetTitle("GriduinoGUI")

        # --- notebook_1
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY)

        # --- panel_ports
        self.panel_ports = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.panel_ports, "Port")

        sizer_ports = wx.BoxSizer(wx.VERTICAL)

        # --- radiobox_port
        self.radiobox_port = wx.RadioBox(self.panel_ports, wx.ID_ANY, "Griduino COM port", choices=["no COM ports available", "unused", "unused", "unused"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.radiobox_port.SetSelection(0)
        # fill in ports and select current setting
        preferred_index = 0
        self.portlist = enumerate(sorted(serial.tools.list_ports.comports()))
        for n, (portname, desc, hwid) in self.portlist:
            self.radiobox_port.SetString(n, u'{} - {}'.format(portname, desc))
        for n in range(self.radiobox_port.GetCount()):
            if self.radiobox_port.GetString(n) == 'unused':
                self.radiobox_port.ShowItem(n, False)
        self.radiobox_port.SetSelection(preferred_index)
        # after radiobox_port 
        sizer_ports.Add(self.radiobox_port, 0, wx.ALL, 8)

        # --- radiobox_udp
        self.radiobox_udp = wx.RadioBox(self.panel_ports, wx.ID_ANY, "WSJT port for UDP", choices=["choice 1"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.radiobox_udp.Hide()
        self.radiobox_udp.SetSelection(0)
        sizer_ports.Add(self.radiobox_udp, 0, wx.ALL, 8)

        self.button_port_ok = wx.Button(self.panel_ports, wx.ID_ANY, "OK")
        sizer_ports.Add(self.button_port_ok, 0, wx.ALL, 8)

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_ports.Add(sizer_1, 1, wx.EXPAND, 0)

        sizer_1.Add((0, 0), 0, 0, 0)

        # --- panel_gps ---
        self.panel_gps = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.panel_gps, "GPS")

        sizer_gps = wx.BoxSizer(wx.VERTICAL)

        # --- label_grid6
        label_grid6 = wx.StaticText(self.panel_gps, wx.ID_ANY, "CN87us", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_grid6.SetFont(wx.Font(36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_gps.Add(label_grid6, 0, wx.ALL | wx.EXPAND, 13)

        # --- label_gmt
        label_gmt = wx.StaticText(self.panel_gps, wx.ID_ANY, "12 : 34 : 56 GMT", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_gmt.SetFont(wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        now = wx.DateTime.Now()
        now = now.MakeUTC()
        label_gmt.SetLabel(now.Format('%H : %M : %S GMT'))  # http://www.cplusplus.com/reference/ctime/strftime/
        # end label_gmt
        sizer_gps.Add(label_gmt, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 7)

        # --- label_date
        label_date = wx.StaticText(self.panel_gps, wx.ID_ANY, "Dec 20, 2021")
        label_date.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        now = wx.DateTime.Now()
        now = now.MakeUTC()
        label_date.SetLabel(now.Format('%b %e, %Y'))  # http://www.cplusplus.com/reference/ctime/strftime/
        sizer_gps.Add(label_date, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 8)

        sizer_set_clock = wx.BoxSizer(wx.HORIZONTAL)
        sizer_gps.Add(sizer_set_clock, 1, wx.ALL | wx.EXPAND, 4)

        self.button_plus_time = wx.Button(self.panel_gps, wx.ID_ANY, "Nudge +0.1 sec")
        sizer_set_clock.Add(self.button_plus_time, 0, wx.ALL, 4)

        self.button_set_time = wx.Button(self.panel_gps, wx.ID_ANY, "Set Computer Clock from GPS")
        sizer_set_clock.Add(self.button_set_time, 0, wx.ALL, 4)

        self.button_minus_time = wx.Button(self.panel_gps, wx.ID_ANY, "Nudge -0.1 sec")
        sizer_set_clock.Add(self.button_minus_time, 0, wx.ALL, 4)

        # --- panel_download ---
        self.panel_download = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.panel_download, "Download")

        sizer_download = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_download.Add(sizer_3, 0, wx.ALL | wx.EXPAND, 8)

        # --- button_download_gps
        label_2 = wx.StaticText(self.panel_download, wx.ID_ANY, "GPS bread crumb trail:")
        sizer_3.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_download_gps = wx.Button(self.panel_download, wx.ID_ANY, "Save KML As...")
        sizer_3.Add(self.button_download_gps, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 8)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_download.Add(sizer_2, 0, wx.ALL | wx.EXPAND, 8)

        # --- button_download_barometer
        label_1 = wx.StaticText(self.panel_download, wx.ID_ANY, "Barometer 3-day history:")
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.button_download_barometer = wx.Button(self.panel_download, wx.ID_ANY, "Save Barometer As...")
        sizer_2.Add(self.button_download_barometer, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 8)

        # --- panel_chatter ---
        self.panel_chatter = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.panel_chatter, "COM Data")

        sizer_griduino_log = wx.BoxSizer(wx.VERTICAL)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_griduino_log.Add(sizer_7, 0, wx.EXPAND, 0)

        self.text_griduino_send = wx.TextCtrl(self.panel_chatter, wx.ID_ANY, "")
        sizer_7.Add(self.text_griduino_send, 1, wx.ALL, 4)

        self.button_send_text = wx.Button(self.panel_chatter, wx.ID_ANY, "Send")
        sizer_7.Add(self.button_send_text, 0, wx.ALL, 4)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_griduino_log.Add(sizer_6, 1, wx.ALL | wx.EXPAND, 0)

        self.text_griduino_log = wx.TextCtrl(self.panel_chatter, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer_6.Add(self.text_griduino_log, 1, wx.ALL | wx.EXPAND, 4)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_griduino_log.Add(sizer_8, 0, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.panel_chatter, wx.ID_ANY, "Griduino COM Port")
        sizer_8.Add(label_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        self.checkbox_autoscroll = wx.CheckBox(self.panel_chatter, wx.ID_ANY, "Autoscroll")
        self.checkbox_autoscroll.SetValue(1)
        sizer_8.Add(self.checkbox_autoscroll, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        # --- button_clear_log
        self.button_clear_log = wx.Button(self.panel_chatter, wx.ID_ANY, "Clear output")
        sizer_8.Add(self.button_clear_log, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        self.panel_chatter.SetSizer(sizer_griduino_log)

        self.panel_download.SetSizer(sizer_download)

        self.panel_gps.SetSizer(sizer_gps)

        self.panel_ports.SetSizer(sizer_ports)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnPortOkButton, self.button_port_ok)
        self.Bind(wx.EVT_BUTTON, self.OnButtonSaveKML, self.button_download_gps)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckboxAutoscroll, self.checkbox_autoscroll)
        self.Bind(wx.EVT_BUTTON, self.OnClearOutput, self.button_clear_log)
        # end wxGlade

    def OnPortOkButton(self, event):  # wxGlade: GriduinoFrame.<event_handler>
        # when user clicks OK on the port selection, start showing the GPS window
        print("GriduinoDialogs: event button_port_ok")
        event.Skip()

    def OnClearOutput(self, event):  # wxGlade: GriduinoFrame.<event_handler>
        print("GriduinoDialogs: OnClearOutput() not implemented")
        self.text_griduino_log.Clear()
        # self.text_griduino_log.AppendText("---Start log---\n")

    def OnCheckboxAutoscroll(self, event):  # wxGlade: GriduinoFrame.<event_handler>
        # todo: find a way to stop autoscroll
        print("GriduinoDialogs: OnCheckboxAutoscroll() not implemented")
        event.Skip()

    def OnButtonSaveKML(self, event):  # wxGlade: GriduinoFrame.<event_handler>
        # nothing - the main program has the event handler using e.g.
        # self.Bind(wx.EVT_BUTTON, self.DoButtonSaveKML, self.frame.button_download_gps)
        print("GriduinoDialogs: OnButtonSaveKML() not implemented")
        event.Skip()

# end of class GriduinoFrame


class MyApp(wx.App):
    def OnInit(self):
        self.frame = GriduinoFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
