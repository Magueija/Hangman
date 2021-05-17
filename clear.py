import os

def clear_screen():
   # for mac and linux
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows
      _ = os.system('cls')

def clear_idle():
   for i in range(50):
      print ("\n")
