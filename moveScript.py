import os
import shutil
import time
import getpass
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.simpledialog import askstring

def move_and_delete_files(source_folder, destination_folder, continuous):
    moved_files = set()

    while True:
        # List all .png files in the source folder
        files = [f for f in os.listdir(source_folder) if f.endswith('.png')]

        for file_name in files:
            if file_name not in moved_files:
                source_path = os.path.join(source_folder, file_name)
                destination_path = os.path.join(destination_folder, file_name)

                try:
                    shutil.move(source_path, destination_path)
                    print(f"Moved: {file_name}")
                    moved_files.add(file_name)
                except Exception as e:
                    print(f"Error moving file {file_name}: {e}")

        # List and remove all .json files in the source folder
        json_files = [f for f in os.listdir(source_folder) if f.endswith('.json')]
		  
        for file_name in json_files:
            try:
                os.remove(os.path.join(source_folder, file_name))
                print(f"Deleted: {file_name}")
            except Exception as e:
                print(f"Error deleting file {file_name}: {e}")

        if not continuous:
            break
        
        # Wait for 10 seconds before checking the folder again
        time.sleep(3)

if __name__ == "__main__":
    current_user = getpass.getuser()
    source_folder = fr"C:\Users\{current_user}\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\TempState\ScreenClip"

    # Open a file dialog to select the destination folder
    root = Tk()
    root.withdraw()  # Hide the root window
    destination_folder = askdirectory(title="Select the destination folder")

    if not destination_folder:
        print("No destination folder selected.")
    elif not os.path.exists(destination_folder):
        print(f"The destination folder {destination_folder} does not exist.")
    else:
        # Ask user for mode selection
        mode = askstring("Mode Selection", "Enter '0' for one-time move all or '1' for continuous mode:")

        if mode == "0":
            move_and_delete_files(source_folder, destination_folder, continuous=False)
        elif mode == "1":
            move_and_delete_files(source_folder, destination_folder, continuous=True)
        else:
            print("Invalid mode selected.")