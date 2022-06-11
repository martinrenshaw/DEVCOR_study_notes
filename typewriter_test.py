import time, sys

def anything(str):


  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1)

anything("\r\rYou have woken up in a mysterious maze\r\n")

anything("\r\rThe building has five levels\n")

anything("\r\rScans show that the floors increase in size as you go down\n")