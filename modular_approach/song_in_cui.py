# Import the playsound module
from playsound import playsound

# Prompt the user to enter the sound name
sound = str(input("Enter the sound name: "))

# Play the audio file based on user input using playsound module
playsound(f"D:/programming/python/modular_approach/{sound}.mp3")

# Initialize the MCI (Media Control Interface) module for more advanced audio control
import win32api

# Define a function to play sound using MCI
def play_sound_mci(sound_file):
    win32api.mciSendString(f"open \"{sound}\" alias MySound", None, 0, None)
    win32api.mciSendString("play MySound", None, 0, None)

# Call the function to play the audio file using MCI
play_sound_mci(f"D:/programming/python/modular_approach/{sound}.mp3")
