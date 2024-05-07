import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'shift', 'n')

pyautogui.write('https://mail.google.com/')

pyautogui.press('enter')

time.sleep(4)

pyautogui.write('gustavofigueredo86@gmail.com')
pyautogui.press('enter')

time.sleep(3)
pyautogui.write('password')
pyautogui.press('enter')