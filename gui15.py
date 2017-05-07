# sizer.py
## 텍스트 영역의 사이즈가 크기가 변경 

import wx

class wxExample(wx.Frame):
  
    def __init__(self, parent, title):
        super(wxExample, self).__init__(parent, title=title, 
            size=(260, 180))
            
        self.InitUI()
        self.Centre()
        self.Show()     
        
    def InitUI(self):
    
        menubar = wx.MenuBar()
        filem = wx.Menu()
        editm = wx.Menu()
        helpm = wx.Menu()

        menubar.Append(filem, '&File')
        menubar.Append(editm, '&Edit')
        menubar.Append(helpm, '&Help')
        self.SetMenuBar(menubar)

        wx.TextCtrl(self)


if __name__ == '__main__':
  
    app = wx.App()
    wxExample(None, title='test')
    app.MainLoop()