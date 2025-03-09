'''
Title:    Extract MIDI from WAV File
Author:   Richard D. Pohl
Date:     March, 2025
Summary:  Project Main Function
'''

from scipy.io import wavfile
from pathlib import Path
import numpy as np

def main():
    """Version 1.0.0: Initial Release"""

    #Define report file path as befits your environment
    #this code puts the sizing_output.txt report file in the same directory as main.py
    current_working_directory = Path(__file__).resolve().parent.parent.parent
    file_pointer = str(current_working_directory) + "/Love-Song/lovesong.wav"

    duration = 5
    frequency = 440
    
    sample_rate, audio_data = wavfile.read(file_pointer)

    # Create a time vector
    time = np.linspace(0, duration, int(sample_rate * duration), False)

    # Generate a sine wave
    audio_data = np.sin(2 * np.pi * frequency * time)

    # Scale the data to 16-bit range and convert to integer
    scaled_audio_data = np.int16(audio_data * 32767)

    print(f"Sample Rate: {sample_rate} Hz")
    print(f"Audio Data Shape: {audio_data.shape}")
    print(f"Data Type: {audio_data.dtype}")    

if __name__ == '__main__' :
    main()