import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pyautogui import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://elgoog.im/t-rex/')
driver.implicitly_wait(10)
frame = driver.find_element(By.ID, value='t')
frame.send_keys(Keys.SPACE)
print('sent')


def get_pixel(img, x, y):
    px = img.load()
    print(px[x, y], x, y)
    return px[x, y]


def colors_are_close(color1, color2, tolerance=10):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))


x, y, width, height = 0, 102, 1920, 870
y_search1, y_search2, y_search3, x_start, x_end = 730, 720, 710, 625, 740
# y_search_for_bird = 460
game = True
while game:
    img = pyautogui.screenshot(region=(x, y, width, height))
    bg_color = get_pixel(img, 200, 200)
    for i in reversed(range(x_start, x_end)):
        if not colors_are_close(get_pixel(img, i, y_search1), bg_color) or not colors_are_close(get_pixel(img, i, y_search2), bg_color) or not colors_are_close(get_pixel(img, i, y_search3), bg_color):
            frame.send_keys(Keys.SPACE)
            print('found!!!')
            break
        # if get_pixel(img, i, y_search_for_bird) != bg_color:
        #     frame.send_keys(Keys.DOWN)
        #     print('founddd')
        #     break
