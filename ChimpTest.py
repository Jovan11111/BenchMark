import pyautogui
import cv2
import time
import numpy as np

ONE = [336, 377]
TWO = [577, 568]
THREE = [571, 564]
FOUR = [579, 545]
FIVE = [610, 609]
SIX = [692, 685]
SEVEN = [415, 414]
EIGHT = [706, 713]
NINE = [683, 680]
TEN = [965, 983]
ELEVEN = [723, 669]
TWELVE = [923, 901]
THIRTEEN = [904, 910]
FOURTEEN = [912, 891]
FIFTEEN = [955, 943]
SIXTEEN = [1031, 1025]
SEVENTEEN = [760, 748]
EIGHTEEN = [1059, 1039]
NINETEEN = [1013, 1029]
TWENTY = [1206, 1207]
TWENTY_ONE = [947, 911, 910]
TWENTY_TWO = [1142, 1147]
TWENTY_THREE = [1134, 1145]
TWENTY_FOUR = [1115, 1153]
TWENTY_FIVE = [1179, 1184]
TWENTY_SIX = [1255, 1266]
TWENTY_SEVEN = [984, 989]
TWENTY_EIGHT = [1283, 1280]
TWENTY_NINE = [1254, 1253]
THIRTY = [1204, 1210]
THIRTY_ONE = [944, 914]
THIRTY_TWO = [1146, 1144]
THIRTY_THREE = []
THIRTY_FOUR = []
THIRTY_FIVE = []
THIRTY_SIX = []
THIRTY_SEVEN = []
THIRTY_EIGHT = []
THIRTY_NINE = []
FORTY = []
NUMBERS = [ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, ELEVEN, TWELVE, THIRTEEN, FOURTEEN,
           FIFTEEN, SIXTEEN, SEVENTEEN, EIGHTEEN, NINETEEN, TWENTY, TWENTY_ONE, TWENTY_TWO,
           TWENTY_THREE, TWENTY_FOUR, TWENTY_FIVE, TWENTY_SIX, TWENTY_SEVEN, TWENTY_EIGHT,
           TWENTY_NINE, THIRTY, THIRTY_ONE]


def chimpTest():
    time.sleep(2)
    coordinates = []
    for i in range(5):
        for j in range(8):
            coordinates.append([j * 112, i * 112])
    nums = [ONE, TWO, THREE, FOUR]
    ind = 4
    pyautogui.click(950, 730)
    while True:
        grid = [0] * 5 * 8
        for x, coordinate in enumerate(coordinates):
            screenshot = pyautogui.screenshot(region=(coordinate[0] + 515, coordinate[1] + 275, 80, 80))
            screenshot_np = np.array(screenshot)
            grayPic = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
            ret, threshold = cv2.threshold(grayPic, 200, 255, cv2.THRESH_BINARY)
            grid[x] = cv2.countNonZero(threshold)
        print(grid)

        for number in NUMBERS:
            for i, el in enumerate(grid):
                if el in number:
                    if grid[i] == 910 and number == THIRTEEN:
                        grid[i] -= 1
                    pyautogui.click(coordinates[i][0] + 550, coordinates[i][1] + 290)
                    break

        nums.append(NUMBERS[ind])
        if ind < 30:
            ind += 1
        time.sleep(0.5)
        pyautogui.click(940, 730)
