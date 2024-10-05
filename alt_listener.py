from pynput import keyboard
import os
import subprocess


def on_press(key):
    if key == keyboard.Key.alt_l:
        os.system("nerd-dictation resume")


def on_release(key):
    if key == keyboard.Key.alt_l:
        os.system("nerd-dictation suspend")


if __name__ == "__main__":
    # Start nerd-dictation in the background and get its PID
    nerd_dictation_pid = (
        subprocess.check_output("nerd-dictation begin & echo $!", shell=True)
        .decode()
        .strip()
    )
    print(f"Started nerd-dictation with PID: {nerd_dictation_pid}")

    os.system("nerd-dictation suspend")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        finally:
            # Ensure nerd-dictation is stopped when the script exits
            subprocess.run(["nerd-dictation", "end"])
            print("Stopped nerd-dictation")
