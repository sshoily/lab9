""" 
Team:
Joelle Waugh, Manuel Manrique Lopez, Ricardo Rudin, Sadia Shoily

Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_pokemon_info

# Create the main window
root = Tk()
root.title("Pokemon Information")
root.resizable(False, False)

# Frames
frm_input = ttk.Frame(root)
frm_input.grid(row=0, column=0, columnspan=2, pady=(20, 10))

frm_info = ttk.LabelFrame(root, text="Info")
frm_info.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky=N)

frm_stats = ttk.LabelFrame(root, text="Stats")
frm_stats.grid(row=1, column=1, padx=(10, 20), pady=(10, 20), sticky=N)

# User Input Frame
lbl_name = ttk.Label(frm_input, text="Pokemon Name:")
lbl_name.grid(row=0, column=0, padx=(10, 5), pady=10)

enter_name = ttk.Entry(frm_input)
enter_name.insert(0, "Diglett")
enter_name.grid(row=0, column=1)

btn_get_info = ttk.Button(frm_input, text="Get Info", command=lambda: handle_btn_get_info())
btn_get_info.grid(row=0, column=2, pady=10, sticky=E)

# Info Frame Widgets
lbl_height = ttk.Label(frm_info, text="Height:")
lbl_height.grid(row=0, column=0, padx=(20, 10), pady=(10, 5), sticky=W)

lbl_height_val = ttk.Label(frm_info, width=20)
lbl_height_val.grid(row=0, column=1, padx=(10, 20), pady=(10, 5), sticky=E)

lbl_weight = ttk.Label(frm_info, text="Weight:")
lbl_weight.grid(row=1, column=0, padx=(20, 10), pady=(5, 10), sticky=W)

lbl_weight_val = ttk.Label(frm_info, width=20)
lbl_weight_val.grid(row=1, column=1, padx=(10, 20), pady=(5, 10), sticky=E)

lbl_type = ttk.Label(frm_info, text="Type:")
lbl_type.grid(row=2, column=0, padx=(20, 10), pady=(5, 10), sticky=W)

lbl_type_val = ttk.Label(frm_info, width=20)
lbl_type_val.grid(row=2, column=1, padx=(10, 20), pady=(5, 10), sticky=E)

# Stats Frame Widgets
MAX_STAT = 255
PRG_BAR_LENGTH = 200

stats = [
    ("HP:", 0),
    ("Attack:", 1),
    ("Defense:", 2),
    ("Special Attack:", 3),
    ("Special Defense:", 4),
    ("Speed:", 5)
]

bars = {}

for i, (label_text, idx) in enumerate(stats):
    lbl = ttk.Label(frm_stats, text=label_text)
    lbl.grid(row=i, column=0, padx=(10, 5), pady=5, sticky=E)

    bar = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGTH, maximum=MAX_STAT)
    bar.grid(row=i, column=1, padx=(0, 10), pady=5)
    bars[idx] = bar

# Event Handlers
def handle_btn_get_info():
    poke_name = enter_name.get().strip()
    if not poke_name:
        return

    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        lbl_height_val['text'] = f"{poke_info['height']} dm"
        lbl_weight_val['text'] = f"{poke_info['weight']} hg"

        types_list = [t['type']['name'].capitalize() for t in poke_info['types']]
        lbl_type_val['text'] = ', '.join(types_list)

        # Update stats bars
        for idx, bar in bars.items():
            bar['value'] = poke_info['stats'][idx]['base_stat']
    else:
        messagebox.showinfo(title='Error', message=f'Unable to fetch information for {poke_name} from the PokeAPI.', icon='error')

root.mainloop()
