# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame4
###########################################################################

class MainFrame4 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer4 = wx.GridSizer( 2, 1, 0, 0 )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.image_1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.image_1.SetMinSize( wx.Size( 400,400 ) )
		self.image_1.SetMaxSize( wx.Size( 400,400 ) )
		
		gSizer5.Add( self.image_1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.image_2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.image_2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer4.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		gSizer6 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.image_3 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.image_3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.image_4 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.image_4, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer4.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.image_1.Bind( wx.EVT_LEFT_DCLICK, self.leftDClickFunc )
		self.image_2.Bind( wx.EVT_LEFT_DCLICK, self.leftDClickFunc )
		self.image_3.Bind( wx.EVT_LEFT_DCLICK, self.leftDClickFunc )
		self.image_4.Bind( wx.EVT_LEFT_DCLICK, self.leftDClickFunc )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def leftDClickFunc( self, event ):
		event.Skip()
	
	
	
	

###########################################################################
## Class FullImageDialog
###########################################################################

class FullImageDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.image_full = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 1600,1200 ), 0 )
		bSizer1.Add( self.image_full, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MainFrame5
###########################################################################

class MainFrame5 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer4 = wx.GridSizer( 2, 1, 0, 0 )
		
		gSizer5 = wx.GridSizer( 1, 3, 0, 0 )
		
		self.image_1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.image_1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.image_2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.image_2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.image_3 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.image_3, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer4.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		gSizer6 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.image_4 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.image_4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.image_5 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.image_5, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer4.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.image_1.Bind( wx.EVT_LEFT_DCLICK, self.leftDClickFunc )
		self.image_2.Bind( wx.EVT_LEFT_DCLICK, self.leftDClickFunc )
		self.image_3.Bind( wx.EVT_LEFT_DCLICK, self.leftDClickFunc )
		self.image_4.Bind( wx.EVT_LEFT_DCLICK, self.leftDClickFunc )
		self.image_5.Bind( wx.EVT_LEFT_DCLICK, self.leftDClickFunc )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def leftDClickFunc( self, event ):
		event.Skip()
	
	
	
	
	

