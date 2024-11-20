import pyautogui, keyboard, win32api, asyncio

running = False

def toggle_running():
    global running
    running = not running

async def find(image_path, confidence: float = 0.8):
    last_location = None

    while running:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                center = pyautogui.center(location)

                if last_location != center:
                    last_location = center
                    win32api.SetCursorPos((center.x, center.y))
                    await asyncio.sleep(0.3) # you can change this
                    pyautogui.click()

        except Exception:
            await asyncio.sleep(0.1)
            return

async def main(image_path, confidence: float):
    while True:
        if running:
            await find(image_path, confidence)

if __name__ == "__main__":
    keyboard.add_hotkey('F8', toggle_running)

    try:
        asyncio.run(main("shake.png", 0.6))

    except KeyboardInterrupt:
        print("bye")
