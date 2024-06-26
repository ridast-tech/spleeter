import time
import os
from spleeter.separator import Separator

current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, 'criminal_cut.mp3')


separator = Separator('spleeter:2stems-16kHz', multiprocess=False)


def split_vocal(path_in: str):
    spleeter_dir = path_in+".spleeter"
    if not os.path.exists(spleeter_dir):
        os.mkdir(spleeter_dir)
    separator.separate_to_file(path_in, spleeter_dir,)
    path_spleeter = spleeter_dir+"/" + \
        os.path.splitext(os.path.basename(path_in))[0]+"/vocals.wav"
    return path_spleeter

split_vocal(file_path)
