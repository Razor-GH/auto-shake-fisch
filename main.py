import pyautogui, keyboard, asyncio, autoit

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
                    await asyncio.sleep(0.1) # you can change this
                    autoit.mouse_click("left", center.x, center.y, speed=-10000)
                    await asyncio.sleep(0.23)

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
