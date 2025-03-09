'''
Title:    Extract MIDI from WAV File
Author:   Richard D. Pohl
Date:     March, 2025
Summary:  Project Main Function
'''

from pathlib import Path
import numpy as np
import wave

def main():
    """Version 1.0.0: Initial Release"""

    #Define report file path as befits your environment
    #this code puts the sizing_output.txt report file in the same directory as main.py
    current_working_directory = Path(__file__).resolve().parent.parent.parent
    file_pointer = str(current_working_directory) + "/Love-Song/lovesong.wav"

    try:
         with wave.open(file_pointer, 'rb') as wf:
            # Retrieve information about the WAV file
            num_channels = wf.getnchannels()
            frame_rate = wf.getframerate()
            num_frames = wf.getnframes()
            sample_width = wf.getsampwidth()

            print(f"Number of channels: {num_channels}")
            print(f"Frame rate: {frame_rate} Hz")
            print(f"Number of frames: {num_frames}")
            print(f"Sample width: {sample_width} bytes")

            # Read all frames from the WAV file
            frames = wf.readframes(num_frames)
            print(f"Data type of frames: {type(frames)}")
            print(f"Size of audio data: {len(frames)} bytes")

    except FileNotFoundError:
        print("Error: WAV file not found.")
        return None
    except wave.Error as e:
        print(f"Error opening WAV file: {e}")
        return None

     # Convert byte data to a NumPy array, handling different sample widths
    if sample_width == 1:  # 8-bit samples
        audio_array = np.frombuffer(frames, dtype=np.uint8) - 128
    elif sample_width == 2:  # 16-bit samples
        audio_array = np.frombuffer(frames, dtype=np.int16)
    elif sample_width == 4:  # 32-bit samples
        audio_array = np.frombuffer(frames, dtype=np.int32)
    else:
         print(f"Unsupported sample width: {sample_width} bytes")
         return None
    
    # If stereo, reshape the array to separate channels
    if num_channels > 1:
        audio_array = audio_array.reshape(-1, num_channels)

    wf.close()

if __name__ == '__main__' :
    main()
