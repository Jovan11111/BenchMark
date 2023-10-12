import pyautogui
import time

levels = [2, 3, 3]
WHITE = (255, 255, 255)
"""
3x3 dva nivoa
"""
TOP_LEFT_X = 700
TOP_LEFT_Y = 325
SIZE = 495

def visualMemory():
    numWhites = 3
    grid = 3
    time.sleep(3)
    pyautogui.click(950, 700)
    while True:
        while True:
            screenshot = pyautogui.screenshot(region=(TOP_LEFT_X, TOP_LEFT_Y, SIZE, SIZE))
            width = 495 / grid
            coordinates = [[width / 2 + width * i, width / 2 + width * j] for i in range(grid) for j in
                           range(grid)]
            clicks = [0] * grid * grid
            for i, coordinate in enumerate(coordinates):
                x, y = coordinate
                pixel_color = screenshot.getpixel((x, y))
                if pixel_color == WHITE:
                    clicks[i] = 1
            if sum(clicks) == numWhites:
                break
        time.sleep(2)
        for i in range(len(clicks)):
            if clicks[i] == 1:
                pyautogui.click(coordinates[i][0] + 700, coordinates[i][1] + 325)
        numWhites += 1
        if numWhites == 5:
            grid = 4
        elif numWhites == 8:
            grid = 5
        elif numWhites == 11:
            grid = 6
        elif numWhites == 16:
            grid = 7
        elif numWhites == 21:
            grid = 8
        elif numWhites == 26:
            grid = 9
        elif numWhites == 33:
            grid = 10
        elif numWhites == 40:
            grid = 11
        elif numWhites == 47:
            grid = 12
        elif numWhites == 56:
            grid = 13
        elif numWhites > 60:
            break
        time.sleep(0.8)
