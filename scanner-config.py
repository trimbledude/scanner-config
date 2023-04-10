from pynput import keyboard

# This application is designed to test that the scanner is configured with the correct carriage return code.
# initialize string variable to store the key presses.
string = ""

def on_press(key):
    global string
    try:
        if key.char == "P":
            string = "P"
        elif key.char in "ASSED" and string:
            string += key.char
    except AttributeError:
        if key == keyboard.Key.down:
            print("Scanner Not Configured Successfully, please scan the carriage return code in Step 2 and try again..")
        if key == keyboard.Key.enter:
            if string == "PASSED":
                print("Scanner Configured Succesfully!")
                print("Scan another code, or press ESC to exit the application")
                string = ""
            else:
                print("Scanner Not Configured Successfully, please scan the carriage return code in Step 2 and try again..")
                string = ""
            string = ""
        else:
            string = ""

def on_release(key):
    global string
    if key == keyboard.Key.esc:
        del string
        print("Exiting the application...")
        return False

# Welcome message and prompt
print("|*************************************************************************|")
print("|**********|                                                   |**********|")
print("|**********| Welcome to the scanner configuration application! |**********|")
print("|**********|                                                   |**********|")
print("|*************************************************************************|")
print("\nPlease scan the barcode in step 2")

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
