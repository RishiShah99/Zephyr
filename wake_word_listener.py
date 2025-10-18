import struct
import threading
from pathlib import Path
from typing import Optional, Callable
try:
    from api_keys import ACCESS_KEY  # type: ignore
except Exception:
    ACCESS_KEY = None  # type: ignore

# Path to your Porcupine keyword file (resolve relative to this file)
KEYWORD_PATH = str((Path(__file__).parent / "Yo_Zephyr.ppn").resolve())


def listen_for_wake_word(callback: Optional[Callable[[], None]] = None, *, background: bool = False):
    """Start listening for the wake word. If background=True, starts a daemon thread.

    callback() will be called when the wake word is detected.
    """
    def _runner():
        porcupine = None
        pa = None
        audio_stream = None
        try:
            pvporcupine = __import__('pvporcupine')
            pyaudio = __import__('pyaudio')
            if not ACCESS_KEY:
                raise RuntimeError("Porcupine ACCESS_KEY not configured in api_keys.py")
            porcupine = pvporcupine.create(access_key=ACCESS_KEY, keyword_paths=[KEYWORD_PATH])
            pa = pyaudio.PyAudio()
            audio_stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length,
            )
            print("Listening for wake word...")
            while True:
                pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
                keyword_index = porcupine.process(pcm)
                if keyword_index >= 0:
                    print("Wake word detected!")
                    if callback:
                        try:
                            callback()
                        except Exception as e:
                            print(f"Wake callback error: {e}")
        except Exception as e:
            print(f"Wake word listener error: {e}")
        finally:
            if audio_stream is not None:
                audio_stream.close()
            if pa is not None:
                pa.terminate()
            if porcupine is not None:
                porcupine.delete()

    if background:
        t = threading.Thread(target=_runner, daemon=True)
        t.start()
        return t
    else:
        _runner()
