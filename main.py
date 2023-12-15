import sounddevice as sd
import numpy as np
import time

def detect_claps(data, threshold=0.7):
    # Detects claps in the audio signal
    claps = np.where(data > threshold)[0]
    return len(claps) > 0

def main():
    duration = 5  # Duration to listen (in seconds)
    rate = 44100  # Sample rate (Hz)

    clap_detected = False
    last_clap_time = None

    try:
        while True:
            # Record audio for the specified duration
            recording = sd.rec(int(duration * rate), samplerate=rate, channels=1, dtype='float64')
            sd.wait()  # Wait for recording to finish

            # Check for clap
            if detect_claps(recording, threshold=0.2):
                current_time = time.time()

                if clap_detected and last_clap_time and (current_time - last_clap_time < 2):
                    print("Hand clap!")
                    clap_detected = False
                else:
                    clap_detected = True
                    last_clap_time = current_time
            else:
                clap_detected = False

    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()
