import tkinter as tk
import random
from PIL import Image, ImageTk


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
PADX = 5
PADY = 10
KEY_WIDTH = 30
DEC_WIDTH = 6


def keygen(dec):
    dec = str(dec)
    block1 = ''.join(random.choice(ALPHABET) for _ in range(5))
    block2 = ''
    for letter in range(len(block1[:-1])):
        index = ALPHABET.find(block1[letter])
        if index+(int(dec[0])) >= len(ALPHABET):
            index = abs(len(ALPHABET) - (index + int(dec[0])))
            block2 += ALPHABET[index]
        else:
            block2 += ALPHABET[index + int(dec[0])]
    block3 = ''
    for letter in range(len(block2[:-1])):
        index = ALPHABET.find(block2[letter])
        block3 += ALPHABET[index - int(dec[1])]
    block4 = ''
    for letter in range(len(block3[:-1])):
        index = ALPHABET.find(block3[letter])
        if index+(int(dec[2])) >= len(ALPHABET):
            index = abs(len(ALPHABET) - (index + int(dec[2])))
            block4 += ALPHABET[index]
        else:
            block4 += ALPHABET[index + int(dec[2])]
    return f'{block1}-{block2}-{block3}-{block4}'


def init_frames(root):
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    bg_img = Image.open('Xd5VZO2rH.png')
    bg_img = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(main_frame, image=bg_img)
    bg_label.image = bg_img
    bg_label.place(relwidth=1, relheight=1)
    dec_frame = tk.Frame(main_frame)
    dec_frame.pack(side=tk.TOP, pady=PADY)
    key_frame = tk.Frame(main_frame)
    key_frame.pack(side=tk.TOP, pady=PADY)
    bg_frame = tk.Frame(main_frame)
    bg_frame.pack()
    return main_frame, dec_frame, key_frame, bg_frame


def init_input_frame(dec_frame, key_frame):
    dec_lbl = tk.Label(dec_frame, text='Enter DEC (3 digits):')
    dec_lbl.pack(side=tk.LEFT)
    entry_dec = tk.Entry(dec_frame, width=DEC_WIDTH)
    entry_dec.pack(side=tk.LEFT, padx=PADX)
    btn_gen = tk.Button(dec_frame, text='Generate key')
    btn_gen.pack(side=tk.LEFT, padx=PADX)
    entry_key = tk.Entry(key_frame, width=KEY_WIDTH, justify='center')
    entry_key.pack()
    return entry_dec, entry_key, btn_gen


def gen(entry_dec, entry_key):
    dec = entry_dec.get()
    if len(dec) != 3:
        entry_key.delete(0, tk.END)
        entry_key.insert(0, "DEC must be 3 digits")
        return
    key = keygen(dec)
    entry_key.delete(0, tk.END)
    entry_key.insert(0, key)


def init_guy():
    root = tk.Tk()
    root.title("Cyberpunk 2077 Keygen")
    root.geometry('904x504')
    frames = init_frames(root)
    dec_frame = frames[1]
    key_frame = frames[2]
    entry_dec, entry_key, btn_gen = init_input_frame(dec_frame, key_frame)
    btn_gen.config(command=lambda: gen(entry_dec, entry_key))
    return root


if __name__ == '__main__':
    root = init_guy()
    root.mainloop()
