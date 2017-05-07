import wx

import wx

class wxExample(wx.Frame):
  
    def __init__(self, parent, title):
        super(wxExample, self).__init__(parent, title=title, 
            size=(250, 200))
            
        self.Show()


if __name__ == '__main__':
  
    app = wx.App()
    wxExample(None, title='윈도우크기')
    app.MainLoop()
	
'''	
Method	Description
Move(wx.Point point)	move a window to the given position
MoveXY(int x, int y)	move a window to the given position
SetPosition(wx.Point point)	set the position of a window
SetDimensions(x, y, width, height, sizeFlags)	set the position and the size of a window
'''
