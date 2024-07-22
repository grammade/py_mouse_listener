from pynput import mouse

left_click_count = 0
right_click_count = 0
middle_click_count = 0

def on_click(x, y, button, pressed):
    global left_click_count, right_click_count, middle_click_count
    if pressed:
        if button == mouse.Button.left:
            left_click_count += 1
        elif button == mouse.Button.right:
            right_click_count += 1
        elif button == mouse.Button.middle:
            middle_click_count += 1
        print(f'M1: {left_click_count}, M2: {right_click_count}, M3: {middle_click_count}')

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
