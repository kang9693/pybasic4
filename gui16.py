## 텍스트 영역의 사이즈가 크기가 변경 

# border.py
# 라인섹을 처리 

import wx

class Example(wx.Frame):
  
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(260, 180))
            
        self.InitUI()
        self.Centre()
        self.Show()     
        
    def InitUI(self):
    
        panel = wx.Panel(self)

        panel.SetBackgroundColour('#4f5049')   ## panel  색 지정
        vbox = wx.BoxSizer(wx.VERTICAL)

        midPan = wx.Panel(panel) 
        midPan.SetBackgroundColour('#ededed')  ## panel 색 지정

        vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(vbox)   # 패널 크기 사이즈 조정


if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='Border')
    app.MainLoop()