from pynput import mouse, keyboard

left_click_count = 0
right_click_count = 0
middle_click_count = 0
mouse_listener_running = True

def on_click(x, y, button, pressed):
    global left_click_count, right_click_count, middle_click_count, mouse_listener_running
    if mouse_listener_running:
        if pressed:
            if button == mouse.Button.left:
                left_click_count += 1
            elif button == mouse.Button.right:
                right_click_count += 1
            elif button == mouse.Button.middle:
                middle_click_count += 1
            print(f'M1: {left_click_count}, M2: {right_click_count}, M3: {middle_click_count}')

def on_press(key):
    global mouse_listener_running
    try:
        if key.char == 'p':
            mouse_listener_running = not mouse_listener_running
            print(f'Mouse listener {"paused" if not mouse_listener_running else "resumed"}')
    except AttributeError:
        pass

# Collect events until released
with mouse.Listener(on_click=on_click) as mouse_listener, keyboard.Listener(on_press=on_press) as keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()