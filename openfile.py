"""
import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n 1.Open Calculator\n 2.Open Notepad\n 3.Exit')
    choice = input('Select Menu :')

def opennotepad():
    filename = 'c:\\Windows\\SysWOW64\\notepad.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)

def open():
    filename = 'C:\\Windows\\SysWOW64\\'
"""
thisdict = {
  a:[]
}
x = input(":")
h = input(":")
k = input(":")
thisdict[2]=x+"     "+h+"     "+k
for i in range(2):
    print(thisdict[])