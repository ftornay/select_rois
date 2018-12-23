#!/usr/bin/env python3
"""Program that presents thermographical images, lets you select
where different regions of interest are and stores the positions"""
from matplotlib import pyplot as plt
import sys, os, glob
import easygui as g
import csv, random
from split_seq import split_seq
from calc_temp import calc_temp

ROIS = ["Nariz", "Fosa_nasal_izquierda", "Fosa_nasal_derecha",
        "Dedo_izquierdo", "Dedo_derecho",
        "Ojo_izquierdo", "Ojo_derecho",
        "Boca_izquierda", "Boca_derecha",
        "Mejilla_izquierda", "Mejilla_derecha",
        "Frente_izquierda", "Frente_derecha"]
KEYS = ["z", "n", "N", "d", "D", "j", "J", "b", "B", "m", "M", "r", "R"]

INIT_FIELDS = ["dirname", "men_ver", "paradigma", "image_name",
        #"image"
        ]

class Manage_rois:
    def __init__(self, filename, init_dict, key="z"):
        assert key in KEYS
        plain, path = get_fnames(filename)
        self.csvfile = os.path.splitext(path)[0]
        self.csvfile += '.csv'
        removeImages = get_images_csv(self.csvfile)
        self.frames = {f"{plain}_{i:05}": f
                for i,f in enumerate(split_seq(path))}
        for im_name in removeImages:
            try:
                del self.frames[im_name]
            except KeyError:
                continue
        self.imgnames = list(self.frames.keys())
        if len(self.imgnames) < 1:
            msg = f"No se encuentran nuevas imágenes en {dirpath}"
            g.msgbox(msg, title="Error!")
            sys.exit(-1)
        # Randomize image list 
        random.shuffle(self.imgnames)
        self.imgnames = iter(self.imgnames)
        self.init_dict = init_dict
        self.current_key = key
        self.roi_dict = dict(zip(KEYS, ROIS))
        self.clear_coords()
        self.create_image()

    def write_csv_row(self):
        extra_dict = {}
        extra_dict["image_name"] = self.imagename
        #extra_dict["image"] = self.image.tobytes()
        for c in self.coords:
            extra_dict[c + "_x"] = self.coords[c][0]
            extra_dict[c + "_y"] = self.coords[c][1]
        data = {**self.init_dict, **extra_dict}
        with open(self.csvfile, "a+") as f:
            writer = csv.DictWriter(f, get_fields())
            writer.writerow(data)

    def create_image(self):
        self.imagename, self.image = self.get_image(next(self.imgnames))
        fig, ax = plt.subplots()
        t = self.current_roi + " " * 40 + "Pulsa h para obtener ayuda"
        self.text = plt.gcf().text(0, 0, t, fontsize=14)
        implot = ax.imshow(self.image, cmap="hot")
        plt.title(self.imagename)
        fig.canvas.mpl_connect("key_press_event", self.get_key_handler())
        implot.figure.canvas.mpl_connect("button_press_event",
                                        self.get_mouse_handler())
        plt.show()

    def update_image(self):
        plt.gcf().clear()
        self.text = plt.gcf().text(0, 0, '', fontsize=14)
        self.update_text()
        plt.imshow(self.image, cmap="hot")
        plt.title(self.imagename)
        for r in self.coords:
            if r == self.current_roi:
                plt.plot(*self.coords[r], "ro")
            else:
                plt.plot(*self.coords[r], "bo")
        plt.draw()

    def get_image(self, im_name):
        im = calc_temp(self.frames[im_name])
        return im_name, im

    @property
    def current_roi(self):
        return self.roi_dict[self.current_key]

    def clear_coords(self):
        self.coords = {}

    def update_text(self):
        roi = self.current_roi
        if roi in self.coords:
            msg = "{}: {}:{}".format(roi,
                            self.coords[roi][0],
                            self.coords[roi][1])
        else:
            msg = roi

        msg = msg + " " * 40 + "Pulsa h para obtener ayuda"

        self.text.set_text(msg)
        plt.draw()

    def get_mouse_handler(self):
        def onclick(event):
            if event.xdata != None and event.ydata != None:
                x, y = int(event.xdata), int(event.ydata)
                self.coords[self.current_roi] = (x, y)
                self.update_image()
        return onclick

    def get_key_handler(self):
        def onkey(event):
            if event.key in self.roi_dict:
                self.current_key = event.key
                self.update_image()
            elif event.key in ["h", "H"]:
                self.show_help()
            elif event.key =="enter":
                self.write_csv_row()
                try:
                    im_name = next(self.imgnames)
                except StopIteration:
                    sys.exit(0)
                self.imagename, self.image = self.get_image(im_name)
                self.clear_coords()
                self.update_image()
        return onkey

    def show_help(self):
        msg = 'Pulsa una de estas teclas para introducir la localización de cada ROI:\n\n'
        for k, r in self.roi_dict.items():
            msg += f'{k}: {r}\n'
        msg += '\nEnter: graba los datos de esta imagen y pasa a la siguiente'
        msg +='\n\nVer archivo README.md para más detalles'
        g.msgbox(msg)

def get_fnames(fname):
    plain = os.path.basename(fname)
    plain = os.path.splitext(plain)[0]
    path = os.path.abspath(fname)
    return plain, path

def get_images_csv(filename):
    """ Returns which files are already in the csv file if it exists
        Otherwise, it creates the csv file """
    files = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                files.append(row["image_name"])
    else:
        with open(filename, "w") as f:
            writer = csv.DictWriter(f, get_fields())
            writer.writeheader()
    return files

def get_fields():
    fields = INIT_FIELDS
    for r in ROIS:
        fields.append(r + '_x')
        fields.append(r + '_y')
    return fields

def create_app():
    filepath = g.fileopenbox()
    if filepath is None:
        sys.exit(0)
    filename, filepath = get_fnames(filepath)
    men_ver = g.choicebox("¿El sujeto miente o dice la verdad?",
            '¿Mentira o verdad?',
            ["mentira", "verdad", "desconocido"])
    if men_ver is None:
        sys.exit(0)
    paradigma = g.choicebox("¿Qué tipo de procedimiento es?",
            'Paradigma',
            ["ecologico", "cold_stress", "otro"])
    if paradigma is None:
        sys.exit(0)
    init_dict = {'dirname': filename,
                 'men_ver': men_ver, 'paradigma': paradigma}
    rois = Manage_rois(filepath, init_dict)

if __name__ == "__main__":
    create_app()
