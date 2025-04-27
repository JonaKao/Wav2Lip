import subprocess
import sys
import os

# Make sure we are in the Wav2Lip directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

subprocess.run([
    sys.executable,  # <-- automatically uses your venv python
    "inference.py",
    "--checkpoint_path", "wav2lip_gan.pth",
    "--face", "face.jpg",
    "--audio", "input.wav",
    "--outfile", "result_voice.mp4"
])
