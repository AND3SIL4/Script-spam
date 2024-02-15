import pyautogui as spam
import webbrowser as web
import time

limit = input('Amount of messages: ')
message = input('Write the message: ')
phone = input('Enter the phone number: ')

web.open(f'https://web.whatsapp.com/send?phone=+{phone}')

count = 0

time.sleep(20)

while count<int(limit):
  spam.typewrite(message)
  spam.press('enter')

  count += 1
