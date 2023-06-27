import wx

class MyPrintout(wx.Printout):
    def OnPrintPage(self, page):
        dc = self.GetDC()
        dc.StartPage()
        # Perform the printing operations here
        # Draw text, images, or any other content on the device context (dc)
        dc.EndPage()
        return True

class PrintingApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Printing App")
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Print", pos=(20, 20))
        button.Bind(wx.EVT_BUTTON, self.on_print)

    def on_print(self, event):
        printer = wx.Printer()
        printout = MyPrintout()
        print_dialog = wx.PrintDialog(self)
        if print_dialog.ShowModal() == wx.ID_OK:
            printer.Print(self, printout, True)
        print_dialog.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = PrintingApp()
    frame.Show()
    app.MainLoop()
