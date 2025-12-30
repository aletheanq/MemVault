# Importing packages to use for this file
import numpy as np
import sounddevice as sd
import soundfile as sf


# Assigning variables for constant values used in this file
fs = 44100 # Frames per second this file is recording audio at, a standard rate of 44.1 khZ
seconds  The maximum number of seconds a person can record audio, changes according to experimentation

user_recording_input = input("How many times would you like to provide a recording file?")

for i in range (int(user_recording_input)):
    print("Starting the audio recording")
    # Used to record the audio coming from only one audio input, stores audio recording in a NumPy array
    my_recording = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
    sd.wait() # Program waits until the recording is finished

    print ("Recording done. Here's the size details of the audio recording: ", my_recording.shape)

    # Converts the NumPy array into a .wav audio file
    sf.write(f"test_recording_{i+1}.wav", my_recording, fs)
    print (f"Audio recording file saved as test_recording_{i+1}.wav")
