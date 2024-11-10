import csv
from datetime import datetime
import time
from pynput import keyboard

def getCSV():
    print("Please choose a name for the csv file returned.\n")
    user = input("Enter here: ")
    # date = datetime.now().strftime("%Y/%m/%d_%H:%M:%S%f")
    return f'key_log_{user}.csv'

def press(key, start_time, csv_file):
    timestamp = time.time() - start_time;
    try:
        key_pressed = key.char
    except AttributeError:
        key_pressed = str(key)

    with open(csv_file, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, key_pressed])

def release(key):
    if(key == keyboard.Key.esc):
        return False


if __name__ == "__main__":
    csvFile = getCSV()

    with open(csvFile, mode='w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Seconds elapsed", "Key"])

    cur_time = time.time()

    with keyboard.Listener(on_press=lambda key : press(key, cur_time, csvFile), on_release=release) as listener:
        listener.join()