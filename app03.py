import wx
import wx.grid
import os
import sqlite3
import re
import string
import gettext

cwd = os.path.abspath(os.curdir)

def connect():#this is the sqlite3 connection
    #con_str=cwd + '/Data/esm_event.db'
	#con_str=cwd + 'esm_event.db'
	con_str='esm_event.db'
	cnn = sqlite3.connect(con_str)
	return cnn
	cnn.close()

def data_rows_count():# to count the rows in the database
	con = connect()
	#print( con)
	cur=con.cursor()
    #cur.execute("SELECT * FROM Phone")
	cur.execute("select id, mgr_time, title, slocation, src_info, to_attack_info, src_port, alt_level, org_alert_level, info_status, agent_name from esm_event")
	rows=cur.fetchall()
	#for row in c.execute('SELECT src_info FROM esm_event where mgr_time like \'%2016-09-08%\''):
	#for row in c.execute('SELECT * FROM event_desc'):
	#	print (row[0])
	i=0
	for r in rows:
		i+=1
		
	return i

def fmtstr(fmt, strr):# to format some string!!!
    res = []
    i = 0
    s=re.sub(r'[^\w]','',strr)
    for c in fmt:
        if c == '#':
            res.append(s[i:i+1])
            i = i+1
        else:
            res.append(c)
    res.append(s[i:])
    return string.join(res)

def titling(name):# to display the names and surnames in uppercase for 1st letter
    return name.title()

def single_quote_remover(text):# to remove single quotes from entry to prevent SQL crash
    return text.replace ("'","/")

def single_quote_returner(text):# to display the single quote for the user ex: cote d'or as chocolat:)))
    return text.replace("/","'")
	
class MyFrame(wx.Frame):
#class MyDialog1(wx.Dialog):# this is the PhoneBook dialog box...

	#self.WinName = WinName
	def __init__(self, *args, **kwds):
		#kwds["style"] = wx.DEFAULT_DIALOG_STYLE		
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Dialog.__init__(self, *args, **kwds)
		self.label_10 = wx.StaticText(self, -1, _("ID"))
		self.txtID = wx.TextCtrl(self, -1, "")
		
		self.label_11 = wx.StaticText(self, -1, _("Detect Time"))
		self.txtNAME = wx.TextCtrl(self, -1, "")
		
		self.label_12 = wx.StaticText(self, -1, _("탐지명"))
		self.txtSURNAME = wx.TextCtrl(self, -1, "")
		
		self.label_13 = wx.StaticText(self, -1, _("탐지장비"))
		self.txtNUMBER = wx.TextCtrl(self, -1, "")
		
		self.label_14 = wx.StaticText(self, -1, _("Src-IP"))
		self.txtSRCIP = wx.TextCtrl(self, -1, "")
		
		self.label_15 = wx.StaticText(self, -1, _("Dst-IP"))
		self.txtDSTIP = wx.TextCtrl(self, -1, "")
		
		self.label_16 = wx.StaticText(self, -1, _("Src Port"))
		self.txtSRCPORT = wx.TextCtrl(self, -1, "")
		
		self.label_17 = wx.StaticText(self, -1, _("위험도"))
		self.txtRISKLEVEL = wx.TextCtrl(self, -1, "")
		
		self.label_18 = wx.StaticText(self, -1, _("회수"))
		self.txtEVENTCOUNT = wx.TextCtrl(self, -1, "")
		
		self.label_19 = wx.StaticText(self, -1, _("info"))
		self.txtEVENTINFO = wx.TextCtrl(self, -1, "")
		
		self.label_20 = wx.StaticText(self, -1, _("장비명"))
		self.txtUNITNAME = wx.TextCtrl(self, -1, "")
		
		self.button_6 = wx.Button(self, -1, _("UPDATE"))
		self.button_5 = wx.Button(self, -1, _("ADD"))
		self.button_7 = wx.Button(self, -1, _("DELETE"))
		self.button_8 = wx.Button(self, -1, _("LOAD"))
		
		self.grid_1 = wx.grid.Grid(self, -1, size=(1, 1))
		
		#self.grid_1.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK,
        #              self.showPopupMenu)

		self.label_14 = wx.StaticText(self, -1, _("  Search Name:"))
		self.txtSearch = wx.TextCtrl(self, -1, "")
		self.button_9 = wx.Button(self, -1, _(" Go"))
		self.button_10 = wx.Button(self, -1, _("Renumber"))
		self.txtNAME.SetFocus()
		self.button_6.Enabled=False
		self.txtID.Enabled=False
		
		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self.clk_add, self.button_5)
		self.Bind(wx.EVT_BUTTON, self.clk_update, self.button_6)
		self.Bind(wx.EVT_BUTTON, self.clk_delete, self.button_7)
		self.Bind(wx.EVT_BUTTON, self.clk_load, self.button_8)
		self.Bind(wx.EVT_BUTTON, self.clk_go, self.button_9)
		self.Bind(wx.EVT_BUTTON, self.clk_renumber, self.button_10)
		
		self.grid_1.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.showPopupMenu)
        
	def refresh_data(self):
		cnn =connect()
		cur = cnn.cursor()
		cur.execute('select id, mgr_time, title, slocation, src_info, to_attack_info, src_port, alt_level, org_alert_level, info_status, agent_name from esm_event order by id desc')
		rows=cur.fetchall()
		for i in range (0,len(rows)):
			for j in range(0,11):
				cell = rows[i]
				#print(cell)
				self.grid_1.SetCellValue(i,j,str(cell[j]))

	def __set_properties(self):
		self.SetTitle(_("Event"))
		self.SetSize((1024, 720))
		self.txtID.SetMinSize((120, 27))
		self.txtNAME.SetMinSize((120, 27))
		self.txtSURNAME.SetMinSize((120, 27))
		self.txtNUMBER.SetMinSize((120, 27))
		r=data_rows_count()
		self.grid_1.CreateGrid(r, 11)#this is to create the grid with same rows as database
		self.grid_1.SetColLabelValue(0, _("ID"))
		self.grid_1.SetColSize(0, 12)
		self.grid_1.SetColLabelValue(1, _("Detect Time"))
		self.grid_1.SetColSize(1, 150)
		self.grid_1.SetColLabelValue(2, _("탐지명"))
		self.grid_1.SetColSize(2, 150)
		self.grid_1.SetColLabelValue(3, _("탐지장비"))
		self.grid_1.SetColSize(3, 150)
		self.grid_1.SetColLabelValue(4, _("SRC_IP"))
		self.grid_1.SetColSize(3, 150)
		self.grid_1.SetColLabelValue(5, _("DST_IP"))
		self.grid_1.SetColSize(3, 150)
		self.grid_1.SetColLabelValue(6, _("Src Port "))
		self.grid_1.SetColSize(3, 150)
		self.grid_1.SetColLabelValue(7, _("위험도"))
		self.grid_1.SetColSize(3, 150)
		self.grid_1.SetColLabelValue(8, _("회수"))
		self.grid_1.SetColSize(3, 150)
		self.grid_1.SetColLabelValue(9, _("info"))
		self.grid_1.SetColSize(3, 150)
		self.grid_1.SetColLabelValue(10, _("장비명"))
		self.grid_1.SetColSize(3, 150)
		self.txtSearch.SetMinSize((100, 27))
		self.refresh_data()

	def __do_layout(self):
		sizer_4 = wx.BoxSizer(wx.VERTICAL)
		grid_sizer_4 = wx.GridSizer(1, 4, 0, 0)
		grid_sizer_3 = wx.GridSizer(11, 4, 0, 0)
		sizer_4.Add((20, 20), 0, 0, 0)
		grid_sizer_3.Add(self.label_10, 0, 0, 0)
		grid_sizer_3.Add(self.txtID, 0, 0, 0)
		grid_sizer_3.Add(self.button_5, 0, 0, 0)
		grid_sizer_3.Add(self.label_11, 0, 0, 0)
		grid_sizer_3.Add(self.txtNAME, 0, 0, 0)
		grid_sizer_3.Add(self.button_6, 0, 0, 0)
		grid_sizer_3.Add(self.label_12, 0, 0, 0)
		grid_sizer_3.Add(self.txtSURNAME, 0, 0, 0)
		grid_sizer_3.Add(self.button_7, 0, 0, 0)
		grid_sizer_3.Add(self.label_13, 0, 0, 0)
		grid_sizer_3.Add(self.txtNUMBER, 0, 0, 0)
		
		#SRC_IP
		grid_sizer_3.Add(self.label_14, 0, 0, 0)
		grid_sizer_3.Add(self.txtSRCIP, 0, 0, 0)

		grid_sizer_3.Add(self.label_15, 0, 0, 0)
		grid_sizer_3.Add(self.txtDSTIP, 0, 0, 0)		
		
		grid_sizer_3.Add(self.label_16, 0, 0, 0)
		grid_sizer_3.Add(self.txtSRCPORT, 0, 0, 0)
		
		grid_sizer_3.Add(self.label_17, 0, 0, 0)
		grid_sizer_3.Add(self.txtRISKLEVEL, 0, 0, 0)		
		
		grid_sizer_3.Add(self.label_18, 0, 0, 0)
		grid_sizer_3.Add(self.txtEVENTCOUNT, 0, 0, 0)	
		
		grid_sizer_3.Add(self.label_19, 0, 0, 0)
		grid_sizer_3.Add(self.txtEVENTINFO, 0, 0, 0)		
		#
		grid_sizer_3.Add(self.label_20, 0, 0, 0)
		grid_sizer_3.Add(self.txtUNITNAME, 0, 0, 0)		
		
		
		grid_sizer_3.Add(self.button_8, 0, 0, 0)
		sizer_4.Add(grid_sizer_3, 1, wx.EXPAND, 0)
		sizer_4.Add(self.grid_1, 1, wx.EXPAND, 0)
		sizer_4.Add((20, 20), 0, 0, 0)
		grid_sizer_4.Add(self.label_14, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		grid_sizer_4.Add(self.txtSearch, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		grid_sizer_4.Add(self.button_9, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		grid_sizer_4.Add(self.button_10, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		
		sizer_4.Add(grid_sizer_4, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_4)
		self.Layout()

	def clear_grid(self):
		self.txtID.Value=""
		self.txtNAME.Value=""
		self.txtSURNAME.Value=""
		self.txtNUMBER.Value=""
		self.txtSRCIP.Value=""
		self.txtDSTIP.Value=""
		self.txtSRCPORT.Value=""
		self.txtRISKLEVEL.Value=""
		self.txtEVENTCOUNT.Value=""
		self.txtEVENTINFO.Value=""
		self.txtUNITNAME.Value=""
		#self.txtDSTIP.Value=""
		#self.txtDSTIP.Value=""
		#self.txtDSTIP.Value=""

	def auto_number(self):
		j=data_rows_count()
		return j+1  

	def clk_add(self, event):
		if self.txtNAME.Value == "" or self.txtSURNAME.Value == "" or self.txtNUMBER.Value == "":
			wx.MessageBox("Some Fields Are Empty!")
		else:
			the_id=str(self.auto_number())
			the_name=single_quote_remover(str(self.txtNAME.Value))
			the_surname=single_quote_remover(str(self.txtSURNAME.Value))
			num=fmtstr('##-######',(str(self.txtNUMBER.Value)))#set the format here to the country u want
			name=titling(the_name)
			surname=titling(the_surname)
			self.grid_1.AppendRows(1)
			cnn = connect()
			cursor = cnn.cursor()
			add_many = "INSERT INTO esm_event(ID,name,surname,telephone) VALUES("+(the_id)+",'"+(name)+"','"+(surname)+"','"+(num)+"')"
			cursor.execute(add_many)
			cnn.commit()
			cnn.close()
			self.refresh_data()
			self.clear_grid()
			self.txtNAME.SetFocus()
		event.Skip()

	def clk_update(self, event):
		try:
			num=fmtstr('##-######',str(self.txtNUMBER.Value))
			the_name=single_quote_remover(str(self.txtNAME.Value))
			the_surname=single_quote_remover(str(self.txtSURNAME.Value))
			name=titling(the_name)
			surname=titling(the_surname)
			row_index = self.grid_1. GetSelectedRows()[0]
			c=self.grid_1.GetCellValue(row_index,0)
			cnn=connect()
			cur=cnn.cursor()
			cur.execute("UPDATE Phone SET name = "+ "'"+(name)+"'" + " ,surname="+ "'"+(surname)+"'" +",telephone=" + "'" +(num) + "'" + "WHERE ID="+"'" + str(c) + "'")
			cnn.commit()
			cnn.close()
			self.refresh_data()
			cnn.close()
			self.clear_grid()
			self.button_6.Enabled=False
			self.button_5.Enabled=True
			self.txtNAME.SetFocus()
			event.Skip()
		except IndexError:
			wx.MessageBox("you have lost focus on the row you wanted to edit")

	def clk_delete(self, event):
		try:
			lst = self.grid_1. GetSelectedRows()[0]
			c=self.grid_1.GetCellValue(lst,0)
			cnn=connect()
			cur=cnn.cursor()
			cur.execute("DELETE FROM esm_event WHERE ID="+"'" + str(c) + "'")
			cnn.commit()
			cnn.close()
			self.grid_1.DeleteRows(lst,1)
			self.refresh_data()
			self.txtNAME.SetFocus()
		except IndexError:
			wx.MessageBox("You Did Not Select Any Row To Delete!")
		event.Skip()

	def clk_load(self, event):
		try:
			row_index = self.grid_1.GetSelectedRows()[0]
			cell_value=[]
			for i in range(0,11):
				cell_value.append(self.grid_1.GetCellValue(row_index,i))
				self.txtID.Value= str(cell_value[0])
				self.txtNAME.Value=str(cell_value[1])
				self.txtSURNAME.Value=str(cell_value[2])
				self.txtNUMBER.Value=str(cell_value[3])
				self.txtSRCIP.Value=str(cell_value[4])
				self.txtDSTIP.Value=str(cell_value[5])
				self.txtSRCPORT.Value=str(cell_value[6])
				self.txtRISKLEVEL=str(cell_value[7])
				self.txtEVENTCOUNT.Value=str(cell_value[8])
				self.txtRISKINFO.Value=str(cell_value[9])
				self.txtUNITNAME.Value=str(cell_value[10])
				#self.txtSRCIP.Value=str(cell_value[4])				
				self.button_6.Enabled=True
				self.button_5.Enabled=False
				self.txtNAME.SetFocus()
				event.Skip()
		except IndexError:
			wx.MessageBox("You Did Not Select Any Row To Load")
            

	def clk_go(self, event):
		r=data_rows_count()
		for e in range(0,r):
			for f in range(0,10):
				self.grid_1.SetCellValue(e,f,"")
				
		
		if (self.txtSearch.Value==""):
			wx.MessageBox("검색ip를 넣어주세요")
			
		else:		
			cnn=connect()
			cursor=cnn.cursor()
			cursor.execute("select id, mgr_time, title, slocation, src_info, to_attack_info, src_port, alt_level, org_alert_level, info_status, agent_name from esm_event WHERE id LIKE '%"+self.txtSearch.Value+"%'") 
			cnn.commit()
			rows=cursor.fetchall()			
			for i in range(len(rows)):
				for j in range(0,10):
					cell=rows[i]
					self.grid_1.SetCellValue(i,j,str(cell[j]))
			cnn.close()
			self.txtSearch.SetFocus()
		
		event.Skip()

	def clk_renumber(self, event):
		Backup_Messasse=wx.MessageDialog(None, "It Is Preferable To Backup Your Database Before You Continue! Do You Wish To Proceed?",'Caution!',wx.YES_NO | wx.ICON_QUESTION)
		Response=Backup_Messasse.ShowModal()
		if(Response==wx.ID_NO):
			Backup_Messasse.Destroy()
		if(Response==wx.ID_YES):
			cnn = connect()
			cur = cnn.cursor()
			cur.execute("SELECT * FROM esm_event")
			rows=cur.fetchall()
			i=0
			m=()
			for r in rows:
				i+=1
				s=str(r).replace(str(r[0]),str(i))
				t=s.replace ("u'","'")
				x=eval(t)
				m+=(x,)
				cur.execute("DELETE FROM esm_event")
				add_many="INSERT INTO esm_event VALUES(?,?,?,?)"
				cur.executemany(add_many,m)
			wx.MessageBox("Renumbering Successful!")
			cur.execute("select id, mgr_time, title, slocation, ext1, src_info, to_attack_info, src_port, alt_level, org_alert_level, info_status, agent_name from esm_event order by id desc")
			TheRows = cur.fetchall()
			for i in range(len(TheRows)):
				for j in range(0,4):
					cell=TheRows[i]
					self.grid_1.SetCellValue(i,j,str(cell[j]))
			cnn.commit()
			cnn.close()
			self.txtNAME.SetFocus()
			event.Skip()
			
		def buttonClick(self, event):
			""" handle button click event and output text from entry area"""
			print('test')
			pass
			
	def showPopupMenu(self, event):
		"""
		Create and display a popup menu on right-click event
		"""
		
		if not hasattr(self, "popupID1"):
			self.popupID1 = wx.NewId()
			self.popupID2 = wx.NewId()
			self.popupID3 = wx.NewId()
			# make a menu
 
		menu = wx.Menu()
		# Show how to put an icon in the menu
		item = wx.MenuItem(menu, self.popupID1,"이벤트보고서")			
		menu.AppendItem(item)
		self.Bind(wx.EVT_MENU, self.OnItem1, item)
		
		item = wx.MenuItem(menu, self.popupID2, "Item One")
		menu.Append(self.popupID2, "Two")
		self.Bind(wx.EVT_MENU, self.OnItem2, item)
		
		item = wx.MenuItem(menu, self.popupID3, "Item Three")
		menu.Append(self.popupID3, "Three")
		self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
	 
		# Popup the menu.  If an item is selected then its handler
		# will be called before PopupMenu returns.
		self.PopupMenu(menu)
		menu.Destroy()

	### 사용법에 대한 확인 필요 
	def OnPopupItemSelected(self, event):
		item = self.popupmenu.FindItemById(event.GetId())
		text = item.GetText()
		wx.MessageBox("You selected item '%s'" % text)
		
		
	def OnItem1(self, event):
		#재사용이 가능한가.		
		#text = item.GetText()
		wx.MessageBox("You selected item '%s'" %event)
		print ("Item One selected in the %s window") #% self.WinName)

	def OnItem2(self, event):
		print ("Item Two selected in the %s window") #%self.WinName)

	def OnItem3(self, event):
		print ("Item Three selected in the %s window") #%self.WinName)

		
	def YesNo(parent, question, caption = 'Yes or no?'):
		dlg = wx.MessageDialog(parent, question, caption, wx.YES_NO | wx.ICON_QUESTION)
		result = dlg.ShowModal() == wx.ID_YES
		dlg.Destroy()
		return result
	def Info(parent, message, caption = 'Insert program title'):
		dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()
	def Warn(parent, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()
        
	#Scrolled Message Dialog
	def InfoText(parent, message, caption='Information !'):
		dlg = wx.ScrolledMessageDialog(parent, message, caption)
		dlg.ShowModal()
		

if __name__ == "__main__":
	gettext.install("app")
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frame_1 = MyFrame(None, wx.ID_ANY, "")
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()
