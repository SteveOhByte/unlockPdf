import wx
import os
import re
import subprocess
import sys
import pypdf
from pypdf import PdfReader, PdfWriter
from unlockPdf import unlockerFrame

path = ""
kind = ""
frame = None
done = False

def unlock(file):
	reader = PdfReader(file)
	writer = PdfWriter()

	if reader.is_encrypted:
		result = reader.decrypt(frame.passwordTextCtrl.GetValue())
		if not result:
			result = wx.MessageBox("Wrong password. Try again?", "Wrong password", wx.YES_NO | wx.ICON_QUESTION)
			if result == wx.YES:
				return False
			else:
				sys.exit(0)

	# Add all pages to the writer
	for page in reader.pages:
		writer.add_page(page)

	# Save the new PDF to a file
	with open(file, "wb") as f:
		writer.write(f)
	print("Unlocked " + file)
	return True

def lock(file):
	reader = PdfReader(file)
	writer = PdfWriter()

	# Add all pages to the writer
	for page in reader.pages:
		writer.add_page(page)

	# Add a password to the new PDF
	writer.encrypt(frame.passwordTextCtrl.GetValue())

	# Save the new PDF to a file
	with open(file, "wb") as f:
		writer.write(f)
	print("Locked " + file)
	return True

def setup():
	if len(sys.argv) != 3:
		print("Invalid number of arguments. Exiting...")
		sys.exit(0)

	path = sys.argv[1]
	mode = sys.argv[2]
	
	# Is the path to a file
	if os.path.isfile(path):
		# Is the file a pdf?
		if re.search(".pdf$", path):
			# Is the mode valid?
			if mode == "-lock" or mode == "-unlock":
				return path, mode, "file"
			else:
				print("Invalid mode. Exiting...")
				sys.exit(0)
		else:
			print("Invalid file type. Exiting...")
			sys.exit(0)
	else: # Is the path to a folder
		# Is the folder empty?
		if len(os.listdir(path)) == 0:
			print("Folder is empty. Exiting...")
			sys.exit(0)
		else:
			# Does the folder contain any pdf files?
			pdfFiles = [file for file in os.listdir(path) if re.search(".pdf$", file)]
			if len(pdfFiles) == 0:
				print("Folder does not contain any pdf files. Exiting...")
				sys.exit(0)
			else:
				# Is the mode valid?
				if mode == "-lock" or mode == "-unlock":
					return path, mode, "folder"
				else:
					print("Invalid mode. Exiting...")
					sys.exit(0)

def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	base_path = getattr(sys, '_MEIPASS', '.')
		
	return os.path.join(base_path, relative_path)

def unlockBtnOnClick(event):
	if kind == "file":
		if not unlock(path):
			return
	elif kind == "folder":
		for file in os.listdir(path):
			if re.search(".pdf$", file):
				if not unlock(os.path.join(path, file)):
					return
	
	result = wx.MessageBox("All files have been unlocked.", "Success", wx.OK | wx.ICON_INFORMATION)
	if result == wx.OK:
		sys.exit(0)

def lockBtnOnClick(event):
	if kind == "file":
		if not lock(path):
			return
	elif kind == "folder":
		for file in os.listdir(path):
			if re.search(".pdf$", file):
				if not lock(os.path.join(path, file)):
					return
	
	result = wx.MessageBox("All files have been locked.", "Success", wx.OK | wx.ICON_INFORMATION)
	if result == wx.OK:
		sys.exit(0)

def unlockBtnOnEnter(event):
	frame.unlockBtn.SetForegroundColour(wx.Colour(60, 60, 60))

def unlockBtnOnLeave(event):
	frame.unlockBtn.SetForegroundColour(wx.Colour(255, 255, 255))

def lockBtnOnEnter(event):
	frame.lockBtn.SetForegroundColour(wx.Colour(60, 60, 60))

def lockBtnOnLeave(event):
	frame.lockBtn.SetForegroundColour(wx.Colour(255, 255, 255))

if __name__ == "__main__":
	app = wx.App(False)
	frame = unlockerFrame(None)
	frame.SetIcon(wx.Icon(resource_path("appicon.ico"), wx.BITMAP_TYPE_ICO))

	path, mode, kind = setup()
	if mode == "-lock":
		frame.SetTitle("Lock PDF")
		frame.SetIcon(wx.Icon(resource_path("lock.ico"), wx.BITMAP_TYPE_ICO))
		frame.unlockBtn.Hide()
		frame.lockBtn.Show()
	elif mode == "-unlock":
		frame.SetTitle("Unlock PDF")
		frame.SetIcon(wx.Icon(resource_path("unlock.ico"), wx.BITMAP_TYPE_ICO))
		frame.unlockBtn.Show()
		frame.lockBtn.Hide()

	frame.filesTextCtrl.SetValue(path)

	# bindings
	frame.unlockBtn.Bind(wx.EVT_ENTER_WINDOW, unlockBtnOnEnter)
	frame.unlockBtn.Bind(wx.EVT_LEAVE_WINDOW, unlockBtnOnLeave)
	frame.unlockBtn.Bind(wx.EVT_BUTTON, unlockBtnOnClick)
	frame.lockBtn.Bind(wx.EVT_ENTER_WINDOW, lockBtnOnEnter)
	frame.lockBtn.Bind(wx.EVT_LEAVE_WINDOW, lockBtnOnLeave)
	frame.lockBtn.Bind(wx.EVT_BUTTON, lockBtnOnClick)

	frame.Show()
	app.MainLoop()