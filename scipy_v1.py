'''
Title:    Extract MIDI from WAV File
Author:   Richard D. Pohl
Date:     March, 2025
Summary:  Project Main Function
'''

from scipy.io import wavfile
from pathlib import Path
import matplotlib.pyplot as plt 
import numpy as np

def main():
    """Version 1.0.0: Initial Release"""

    #Define report file path as befits your environment
    #this code puts the sizing_output.txt report file in the same directory as main.py
    
    #iMac 
    # current_working_directory = Path(__file__).resolve().parent.parent.parent
    # file_pointer = str(current_working_directory) + "/Love-Song/lovesong.wav"

    #macbook
    current_working_directory = Path(__file__).resolve().parent
    file_pointer = str(current_working_directory) + "/lovesong_25.wav"

    duration = 5
    frequency = 440
    
    sample_rate, audio_data = wavfile.read(file_pointer)

    if len(audio_data.shape) > 1 and audio_data.shape[1] > 1:
        # Take the mean across channels to convert to mono
        audio_data = np.mean(audio_data, axis=1)

    # Create a time vector
    #time = np.linspace(0, duration, int(sample_rate duration), False)

    time = np.arange(0, len(audio_data)) / sample_rate

    # Generate a sine wave
    audio_data = np.sin(2 * np.pi * frequency * time)

    # Scale the data to 16-bit range and convert to integer
    scaled_audio_data = np.int16(audio_data * 32767)
    '''
    plt.figure(figsize=(10, 4))  
    plt.plot(time, audio_data)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Waveform of Audio')
    plt.grid(True)
    plt.show()'
    '''
    
    print(f"Sample Rate: {sample_rate} Hz")
    print(f"Audio Data Shape: {audio_data.shape}")
    print(f"Data Type: {audio_data.dtype}")    

if __name__ == '__main__' :
    main()