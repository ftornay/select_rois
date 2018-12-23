#!/usr/bin/env python3
import sys
import subprocess
from io import BytesIO
from PIL import Image
import numpy as np
import json
from math import exp

def get_raw(frame):
    # Extract raw values using exiftool
    try:
        result = subprocess.run(["exiftool",
                "-b", "-RawThermalImage", "-"],
            input = frame,
            stdout = subprocess.PIPE)
    except FileNotFoundError:
        result = subprocess.run(["C:/Windows/exiftool.exe",
                "-b", "-RawThermalImage", "-"],
            input = frame,
            stdout = subprocess.PIPE)
    # Read thermal image into matrix
    img_file = BytesIO(result.stdout)
    raw = np.array(Image.open(img_file))
    return raw

def get_exif(frame):
    # Get exif info with exiftool
    result = subprocess.run(["exiftool", "-j", "-"],
        input = frame,
        stdout = subprocess.PIPE)
    exif = json.loads(result.stdout.decode())
    return exif[0]

def calc_temp(frame):
    """ Calculates temperature from FLIR frame
    using program exiftool to extract data from the frame
    The temperature formulae were found in
    http://u88.n24.queensu.ca/exiftool/forum/index.php/topic,4898.msg23972.html#msg23972
    """
    exif = get_exif(frame)
    raw = get_raw(frame)
        
    R1 = exif["PlanckR1"]
    B = exif["PlanckB"]
    F = exif["PlanckF"]
    O = exif["PlanckO"]
    R2 = exif["PlanckR2"]
    emis = exif["Emissivity"]

    if emis == 1:
        temps = B / np.log(R1/(R2*(raw+O))+F)
    elif emis < 1:
        RAT = float(exif["ReflectedApparentTemperature"].split(' ')[0])
        RAT += 273.15
        refl = R1/(R2*(exp(B/RAT)-F))-O
        rad = (raw-(1-emis)*refl)/emis
        temps = B / np.log(R1/(R2*(rad+O))+F)
    else:
        raise ValueError("Emissivity greater than 1")
    return temps

if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        frame = f.read()
        temps = calc_temp(frame)
        np.save("temps.npy", temps)
