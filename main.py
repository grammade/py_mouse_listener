from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            print('M1 pressed')
        elif button == mouse.Button.right:
            print('M2 pressed')
        elif button == mouse.Button.middle:
            print('Middle pressed')

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
