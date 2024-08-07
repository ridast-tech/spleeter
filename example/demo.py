import time
import os
from spleeter.separator import Separator
from spleeter.audio import STFTBackend

current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, 'criminal_cut.mp3')
file_path_fr = os.path.join(current_directory, 'fr_cut.mp3')





def split_vocal(path_in: str):
    spleeter_dir = path_in+".spleeter"
    if not os.path.exists(spleeter_dir):
        os.mkdir(spleeter_dir)
    separator = Separator('spleeter:2stems-16kHz', multiprocess=False, stft_backend=STFTBackend.LIBROSA,) 
    separator.separate_to_file(path_in, spleeter_dir,)
    path_spleeter = spleeter_dir+"/" + \
        os.path.splitext(os.path.basename(path_in))[0]+"/vocals.wav"
    return path_spleeter

split_vocal(file_path)
split_vocal(file_path_fr)
