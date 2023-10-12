import pyautogui
import time

WHITE = (255, 255, 255)
COORDINATES = [[790, 400], [950, 400], [1110, 400], [790, 570], [950, 570], [1110, 570], [790, 740], [950, 740],
               [1110, 740]]


def sequenceMemory():
    num = 1
    time.sleep(3)
    pyautogui.click(950, 700)
    while True:
        moves = []
        while True:
            screenshot = pyautogui.screenshot()
            if screenshot.getpixel((790, 400)) == WHITE:
                moves.append(0)
            elif screenshot.getpixel((950, 400)) == WHITE:
                moves.append(1)
            elif screenshot.getpixel((1110, 400)) == WHITE:
                moves.append(2)
            elif screenshot.getpixel((790, 570)) == WHITE:
                moves.append(3)
            elif screenshot.getpixel((950, 570)) == WHITE:
                moves.append(4)
            elif screenshot.getpixel((1110, 570)) == WHITE:
                moves.append(5)
            elif screenshot.getpixel((790, 740)) == WHITE:
                moves.append(6)
            elif screenshot.getpixel((950, 740)) == WHITE:
                moves.append(7)
            elif screenshot.getpixel((1110, 740)) == WHITE:
                moves.append(8)
            if len(moves) == num:
                time.sleep(0.5)
                break
            time.sleep(0.475)
        if num == 70:
            pyautogui.click(COORDINATES[(moves[0]+1) % 9][0], COORDINATES[(moves[0]+1) % 9][1])
            break

        for move in moves:
            pyautogui.click(COORDINATES[move][0], COORDINATES[move][1])
        num += 1

    pyautogui.click(880, 740)

