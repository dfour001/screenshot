import keyboard
from datetime import datetime
from PIL import ImageGrab

key = "print screen"

def save_screenshot(e):
    now = datetime.now().strftime("%H_%M_%S")
    filename = f'Screen_{now}.jpg'

    img = ImageGrab.grab()
    img.save(filename)
    print(f'"{e.name}" key pressed at {now.replace("_",":")}.  Screenshot saved as {filename}')


print('Ready for screenshots.  Press the "{key}" key to save a screenshot...')
keyboard.on_press_key(key, save_screenshot)
keyboard.wait()