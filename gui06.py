import wx

class wxExample(wx.Frame):
    
	def __init__(self, *args, **kwargs):
		super(wxExample, self).__init__(*args, **kwargs) 
            
		self.InitUI()
        
	def InitUI(self):    

		menubar = wx.MenuBar()    	## 메뉴바
		fileMenu = wx.Menu()       ### 파일 매뉴 
		fitem = fileMenu.Append(wx.ID_EXIT, '종료', '어플리케이션 종료') ## wx.ID_EXIT 종료버튼
		menubar.Append(fileMenu, '&파일')   ## 메뉴에 추가 하기 
		self.SetMenuBar(menubar)
		#menubar.Append(fileMenu, '&단기')   ## 메뉴에 추가 하기 
		#self.SetMenuBar(menubar)
		
		#menubar.Append(, '&파일')   ## 메뉴에 추가 하기 
        #self.SetMenuBar(menubar)
        
		self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

		self.SetSize((300, 200))
		self.SetTitle('간단한 메뉴!!! ')
		self.Centre()
		self.Show(True)
        
	def OnQuit(self, e):
		self.Close()

def main():
    
	ex = wx.App()
	wxExample(None)
	ex.MainLoop()    


if __name__ == '__main__':
	main()