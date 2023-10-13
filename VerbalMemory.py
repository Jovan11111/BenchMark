import pyautogui
import time

WHITE = (255, 255, 255)


def verbalMemory():
    allWords = []
    cntr = 0
    time.sleep(3)
    pyautogui.click(960, 740)
    while True:
        screenshot = pyautogui.screenshot(region=(770, 500, 355, 60))
        word = [[0] * screenshot.width] * screenshot.height
        for y in range(screenshot.height):
            for x in range(screenshot.width):
                pixel_color = screenshot.getpixel((x, y))
                if pixel_color == WHITE:
                    word[y][x] = 1

        if word in allWords:
            pyautogui.click(870, 635)
        else:
            allWords.append(word)
            pyautogui.click(1050, 635)
        cntr += 1
        if cntr > 500:
            for i in range(10):
                pyautogui.click(1050, 635)
            break
        time.sleep(0.1)

    pyautogui.click(865, 740)
