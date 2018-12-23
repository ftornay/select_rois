#!/usr/bin/env python3
import sys, os

# Magical bytes that separate the different frames in the SEQ file
# FLIR camera E40
PAT_E40 = b'FFF\x00\x00\x00'
# Flir Tools
PAT_FTOOLS = b'FFF\x00CAP'
# Flir Thermacam researcher
PAT_RES = b'FFF\x00CAMCTRL'

def split_seq(infile):
    """ Splits a FLIR .SEQ file into different frame files
     which can be converted into images containing raw thermal values
     through, e.g:
     exiftool framefile.fff -b -RawThermalImage > outfile.tif
     The script is based on a perl script from
     http://u88.n24.queensu.ca/exiftool/forum/index.php/topic,5279.0.html
     Read .SEQ file """
    with open(infile, "rb") as f:
        content = f.read()

    # Find out .SEQ version
    if content.startswith(PAT_RES):
        pat = PAT_RES
    elif content.startswith(PAT_FTOOLS):
        pat = PAT_FTOOLS
    elif content.startswith(PAT_E40):
        pat = PAT_E40
    else:
        raise ValueError("Unknown file format")

    # Split the SEQ file into frames
    # Each frame begins with the magic bytes
    frames = content.split(pat)
    # Splitting gives a first empty frame that must be discarded
    # and the leading magical bytes must be restored in front
    frames = [pat + f for f in frames[1:]]
    return frames

if __name__ == "__main__":
    # Write each frame as a separate file
    frames = split_seq(sys.argv[1])
    basefilename = os.path.splitext(sys.argv[1])[0]
    for i, frame in enumerate(frames):
        with open('{}_{:03d}.fff'.format(basefilename, i+1), "wb") as f:
            f.write(frame)

