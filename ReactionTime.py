import pyautogui
import time

X_COORDINATE = 400
Y_COORDINATE = 400
GREEN = (75, 219, 106)
X_COORDINATE_SAVE = 860
Y_COORDINATE_SAVE = 740


def reactionTime():
    counter = 0
    time.sleep(3)
    pyautogui.click(X_COORDINATE, Y_COORDINATE)
    while True:
        pixel_color = pyautogui.pixel(X_COORDINATE, Y_COORDINATE)
        if pixel_color == GREEN:
            pyautogui.click(X_COORDINATE, Y_COORDINATE)
            counter += 1
            time.sleep(0.5)
            if counter == 5:
                break
            pyautogui.click(X_COORDINATE, Y_COORDINATE)
    pyautogui.click(X_COORDINATE_SAVE, Y_COORDINATE_SAVE)
