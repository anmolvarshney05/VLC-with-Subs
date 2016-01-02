import subprocess
import os


class VLC:
    def __init__(self, fname):
        folder = os.path.dirname(os.path.abspath('__file__'))
        folder = os.path.join(folder, fname)
        subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe", folder])
