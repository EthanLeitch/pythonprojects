import pyautogui, time
phraseInput = input("Enter a phrase to spam: ")

for c in range(5, 0, -1):
    print("Spamming in " + str(c))
    time.sleep(1)

while True:
	pyautogui.typewrite(phraseInput)
	pyautogui.press("enter")
