import pvporcupine
import pyaudio
import struct
from ui import open_popup

# Replace with your actual Picovoice access key
ACCESS_KEY = "JYwZceXvxP0ikCP9vGjn33uO1EmnsRJEAY+HTtIKwK/t+cCSybbUjw=="

# Path to your Porcupine keyword file
KEYWORD_PATH = "Yo_Zephyr.ppn"

def listen_for_wake_word():
    porcupine = None
    pa = None
    audio_stream = None

    try:
        porcupine = pvporcupine.create(access_key=ACCESS_KEY, keyword_paths=[KEYWORD_PATH])
        
        pa = pyaudio.PyAudio()
        
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length)
        
        print("Listening for wake word...")
        
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake word detected!")
                open_popup()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()

        if porcupine is not None:
            porcupine.delete()

listen_for_wake_word() 