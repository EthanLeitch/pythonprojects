import pyautogui, time
fileInput = input("Enter a filename: ")

time.sleep(5)
f = open(fileInput, 'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
