# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class unlockerFrame
###########################################################################

class unlockerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"(Un)Lock Pdf", pos = wx.DefaultPosition, size = wx.Size( 500,250 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 59, 59, 59 ) )

		mainSizer = wx.BoxSizer( wx.VERTICAL )


		mainSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.filesLabel = wx.StaticText( self, wx.ID_ANY, u"File(s):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.filesLabel.Wrap( -1 )

		self.filesLabel.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI" ) )
		self.filesLabel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3.Add( self.filesLabel, 0, wx.ALL, 5 )

		self.filesTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), wx.TE_CENTER|wx.TE_READONLY )
		self.filesTextCtrl.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False, "Segoe UI Semibold" ) )
		self.filesTextCtrl.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.filesTextCtrl.SetBackgroundColour( wx.Colour( 21, 21, 21 ) )

		bSizer3.Add( self.filesTextCtrl, 0, wx.ALL, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		mainSizer.Add( bSizer3, 1, wx.EXPAND, 5 )


		mainSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.passwordTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"password", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.passwordTextCtrl.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False, "Segoe UI Semibold" ) )
		self.passwordTextCtrl.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.passwordTextCtrl.SetBackgroundColour( wx.Colour( 21, 21, 21 ) )
		self.passwordTextCtrl.SetToolTip( u"The password for the pdf file(s)" )

		mainSizer.Add( self.passwordTextCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.unlockBtn = wx.Button( self, wx.ID_ANY, u"Unlock", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.unlockBtn.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI" ) )
		self.unlockBtn.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.unlockBtn.SetBackgroundColour( wx.Colour( 21, 21, 21 ) )

		bSizer2.Add( self.unlockBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lockBtn = wx.Button( self, wx.ID_ANY, u"Lock", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.lockBtn.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI" ) )
		self.lockBtn.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.lockBtn.SetBackgroundColour( wx.Colour( 21, 21, 21 ) )

		bSizer2.Add( self.lockBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		mainSizer.Add( bSizer2, 1, wx.EXPAND, 5 )


		mainSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( mainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


