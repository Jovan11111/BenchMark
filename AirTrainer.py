import pyautogui
import time

BLUE = (149, 195, 232)
TOP_LEFT_X = 10
TOP_LEFT_Y = 265
WIDTH = 1880
HEIGHT = 595

REGION = (TOP_LEFT_X, TOP_LEFT_Y, WIDTH, HEIGHT)


def aimTrainer():
    cnt = 0
    time.sleep(3)
    pyautogui.click(950,500)
    screenshot = pyautogui.screenshot(region=REGION)
    while True:
        for x in range(TOP_LEFT_X, TOP_LEFT_X + WIDTH, 20):
            for y in range(TOP_LEFT_Y, TOP_LEFT_Y + HEIGHT, 20):
                pixel_color = screenshot.getpixel((x - TOP_LEFT_X, y - TOP_LEFT_Y))
                if pixel_color == BLUE:
                    pyautogui.click(x, y)
                    cnt += 1
                    if cnt == 30:
                        time.sleep(1)
                        pyautogui.click(880, 740)
                        return
                    time.sleep(0.001)
                    screenshot = pyautogui.screenshot(region=REGION)


