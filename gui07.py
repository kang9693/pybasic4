import wx

## 아이콘 추가 ## 

APP_EXIT = 1

class wxExample(wx.Frame):
    
	def __init__(self, *args, **kwargs):
		super(wxExample, self).__init__(*args, **kwargs) 
            
		self.InitUI()
        
	def InitUI(self):

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
		qmi.SetBitmap(wx.Bitmap('icon.png'))
		fileMenu.AppendItem(qmi)

		self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)

		self.SetSize((250, 200))
		self.SetTitle('아이콘 , 바로 가기')
		self.Centre()
		self.Show(True)
        
	def OnQuit(self, e):   ## 종료 메뉴 
		self.Close()

def main():
    
	ex = wx.App()
	wxExample(None)
	ex.MainLoop()    


if __name__ == '__main__':
	main()