import sublime
import sublime_plugin
import os
import sys




class MyShell1Command(sublime_plugin.TextCommand):
	def run(self, edit):
		sys.stdout.write("loading configuration\n")
		settings = sublime.load_settings("SublimeShell.sublime-settings")
		hostname = settings.get("host")
		port = settings.get("port")
		remotePath = settings.get("remotePath")
		user = settings.get("user")
		password = settings.get("password")
		if(hostname==None or port ==None or remotePath == None or user==None or password == None or
			hostname.strip()=='' or port.strip() =='' or remotePath.strip() == '' or user.strip()=='' or password.strip() == ''):
			sublime.message_dialog("服务器信息未配置\n配置路径Preferences->Package Settings->Send To Shell->settings")
		else:
			sys.stdout.write("load configuration sucess\n")

		TEMP=os.getenv("TEMP")
		if( self.view.is_dirty()):
			sublime.message_dialog("警告！！文件未保存")
			return
		#创建view页面的临时文件
		absolute_filepath = self.view.file_name()
		filename = absolute_filepath.split("\\")[-1]
		absolute_temppath = TEMP+ "\\" +filename
		with open(absolute_filepath,"rb") as fread :
			with open(absolute_temppath,"wb") as fwrite:
				fwrite.write(fread.read())
				sys.stdout.write("INFO:Success to create temp file\n")
		self.view.window().run_command("exec",{"cmd":"e://python3/python3.exe "+
			"\"c:\\Users\\TobbyQuinn\\AppData\\Roaming\\Sublime Text 3\\Packages\\sublime_shell\\send.py\""+" "+absolute_temppath+" "+filename+" "+
			hostname+" "+port+" "+user+" "+password+" "+remotePath})
		

# class SendToShellOpenFileCommand(sublime_plugin.ApplicationCommand):
# 	def run(file):
# 		print(file)
# 		pass

