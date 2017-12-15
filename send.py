import paramiko
import sys
class ShellSender():
	def __init__(self,filepath,filename):
		self.filepath=filepath
		self.filename=filename
	def run(self):
		#上传文件到linux服务器
		client= paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(hostname='192.168.210.37', port=22, username='root', password='123456')
		sftp = client.open_sftp()
		sftp.put(self.filepath,"/opt/"+self.filename)
		sftp.close()
		stdin, stdout, stderr = client.exec_command ("bash /opt/"+self.filename)
		#后期针对服务器编码为gbk优化
		sys.stdout.write(stdout.read().decode("UTF-8"))
		sys.stderr.write(stderr.read().decode("UTF-8"))
		client.close()
	def testSys(self):
		print(sys.argv[0])
		print(sys.argv[1])
		print(sys.argv[2])




if __name__=="__main__":
	ShellSender(sys.argv[1],sys.argv[2]).run()