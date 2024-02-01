#!/usr/bin/python
import socket
import sys,time
import pyotp
import base64
import getpass
import _thread


def verify(secret_key, verifycode):
   t = pyotp.TOTP(secret_key)
   result = t.verify(verifycode)  # 对输入验证码进行校验，正确返回True
   #print("秘钥[%s]验证码[%s] 验证结果[%s]" % (secret_key, verifycode, result))
   return result

basecode="CP2411-RBe-20230403"
secretKey = base64.b32encode(basecode.encode(encoding="utf-8"))  
'''
print(secretKey)
totp = pyotp.TOTP(secretKey)
token = totp.now()
print(token)
exit()
'''
#pswd = input("Input your password:")

#print ("your password is %s" %pswd)
#exit()
if True:
    '''
    pswd = getpass.getpass("Please input your password:")
    if pswd == "2023":
        print("Welcome!")
    else:
        print("You failed!")
        exit()
    '''
    pass

else: 
    pswd = getpass.getpass("Please input your verifycode:")
    if verify(secretKey, pswd) == True:
        print("Welcome")
    else:
        print("Password is false")
        exit()

HOST='localhost'
#HOST='192.168.206.110'
#HOST='192.168.123.29'
PORT=5000
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
#s.settimeout(3)
client.connect((HOST,PORT))       #要连接的IP与端口
print("Connecting...")
'''
s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
# 套接字支持TCP_KEEPIDLE，执行if里面的语句，不支持的走else语句
if hasattr(socket, "TCP_KEEPIDLE") and hasattr(socket, "TCP_KEEPINTVL") and hasattr(socket, "TCP_KEEPCNT"):
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 2)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 3)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)
else:
    s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
'''   

'''
cmd=''
cmd = input("Please input cmd:")       #与人交互，输入命令
while cmd!="exit" or cmd!="out":
    s.sendall(cmd.encode(encoding="utf-8"))      #把命令发送给对端
    data=s.recv(1024)     #把接收的数据定义为变量   
    print(data)         #输出变量
    cmd = input("Please input cmd:")       #与人交互，输入命令
'''
data=''
recvflag = True
# 为线程定义一个函数
def receive_data(sock):
    while True:
        data = sock.recv(1024)
        data = str(data,'utf-8')
        print(data)
        

# 创建两个线程
try:
   _thread.start_new_thread( receive_data, (client,) )
   #_thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")

'''
•	(UID "Factory" <password>)
•	password: "F@c70ryS3771ng$D0n3H3r3"
•	(FCT+0003 "100000002" "CP2411-RBe" "B" "2023-04-03")
'''    
uid = '(UID "Factory" "F@c70ryS3771ng$D0n3H3r3")'
fct = '(FCT+0003 "100000002" "CP2411-RBe" "A" "2023-04-03")'
clearhours = "(DGN 99)"
print('(UID "Factory" "!@#$%^&*") sending...')
client.sendall(uid.encode(encoding="utf-8")) 

time.sleep(2)
print("DGN sending...")
client.sendall(clearhours.encode(encoding="utf-8")) 


'''
try:
    data = client.recv(1024)
    data = str(data,'utf-8')
    print(data)
except socket.timeout:
    #if len(data) == 0:
    #    print("uid no data respond")
    pass

#time.sleep(1)
print("fct sending...")

client.sendall(fct.encode(encoding="utf-8")) 
try:
    data = client.recv(1024)
    data = str(data,'utf-8')
    print(data)
except socket.timeout:
    #if len(data) == 0:
    #    print("fct no data respond")
    pass
'''
'''
time.sleep(3)
if "OK" in data:
    print("Successful!")
else:
    print("Maybe failed...")
'''
#recvflag = False
   
#client.close()   #关闭连接 

print("Finished...")


#input()





