# used to lock screen
import ctypes
import keyboard # pip install keyboard
import time
# used to get mouse side button events
import win32api # pip install pywin32


# Constants for side mouse button states
MOUSE3 = 0x05 # left side button that is further away from your finger tips
MOUSE4 = 0x06 # left side button that is closer to your finger tips


# returns true when mouse4 is currently being pressed
def is_mouse4_pressed():
    return win32api.GetKeyState(MOUSE4) < 0


# lock screen (keyboard shortcut combination does not support windows key apparently)
def lockScreen():
    ctypes.windll.user32.LockWorkStation()


# figure out names of different keys
def print_pressed_keys(e):
    print(f'Key pressed: {e.name}')

# mute all audio
def silenceAudio():
    keyboard.press_and_release('volume mute')


# simulate play/pause button
def pausePlayback():
    keyboard.press_and_release('play/pause media')


def main():
    # Find out which names the keyboard keys have
    # keyboard.on_press(print_pressed_keys)
    # keyboard.wait('esc')  # kill program when esc is pressed
    
    start_time = None
    while True:
        # call custom action if mouse4 is held for at least 1 second
        if is_mouse4_pressed():
            if start_time is None:
                start_time = time.time()
            elif time.time() - start_time >= 1:
                # custom action
                print("Mouse4 held for 1 second. Executing custom action..")
                pausePlayback()
                #silenceAudio()
                lockScreen()
                break # you should break otherwise it would call actions multiple times
        else:
            start_time = None
        time.sleep(0.2)  # Dont overload CPU


main()
# Usage: Hold left mouse button (mouse4) for at least 2 seconds to pause all playback and lock the screen.
# Why? I only have access to bluetooth mouse while watching TV show and when I get summoned IRL I want to pause without having to walk to my keyboard.
