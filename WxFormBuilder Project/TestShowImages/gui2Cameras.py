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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 320,180 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer4 = wx.GridSizer( 2, 1, 0, 0 )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.image_1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.image_1.SetMinSize( wx.Size( 400,400 ) )
		
		gSizer5.Add( self.image_1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.image_2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.image_2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer4.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		gSizer6 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.image_3 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.image_3, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer4.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

