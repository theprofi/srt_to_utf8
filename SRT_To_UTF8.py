# -- encoding: utf-8 --
# !/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import sys

if __name__ == "__main__":

    srts_path = sys.argv[1]  # Get the directory where it will convert SRTs to UTF-8 format

    #  Filter only SRTs that weren't converted previosly by the script
    srts_list = [f for f in listdir(srts_path) if isfile(join(srts_path, f))
                 and f.endswith('srt') and not f.startswith('UTF8')]

    for srt_file in srts_list:
        with open(srts_path + "/" + srt_file, 'r', encoding="cp1255") as original_srt:
            try:
                data = original_srt.read()
                f = open(srts_path + "/UTF8_" + srt_file, "w", encoding="utf-8")
                f.write(data)
                f.close()
            #  If the encoding of the SRT is already UTF-8 just skip it
            except UnicodeDecodeError:
                continue
