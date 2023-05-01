table1 = ([[1, 3, 5, 7, 9, 11, 13, 15],[17, 19, 21, 23, 25, 27, 29, 31],[33, 35, 37, 39, 41, 43, 45, 47],[49, 51, 53, 55, 57, 59]])

table2 = ([[2, 3, 6, 7, 10, 11, 14, 15],[18, 19, 22, 23, 26, 27, 30, 31],[34, 35, 38, 39, 42, 43, 46, 47],[50, 51, 54, 55, 58, 59]])

table3 = ([[4, 5, 6, 7, 12, 13, 14, 15],[20, 21, 22, 23, 28, 29, 30, 31],[36, 37, 38, 39, 44, 45, 46, 47],[52, 53, 54, 55, 60, 13]])

table4 = ([[8, 9, 10, 11, 12, 13, 14, 15],[24, 25, 26, 27, 28, 29, 30, 31],[40, 41, 42, 43, 44, 45, 46, 47],[56, 57, 58, 59, 60, 13]])

table5 = ([[16, 17, 18, 19, 20, 21, 22, 23],[24, 25, 26, 27, 28, 29, 30, 31],[48, 49, 50, 51, 52, 53, 54, 55],[56, 57, 58, 59, 60, 31]])

table6 = ([[32, 33, 34, 35, 36, 37, 38, 39],[40, 41, 42, 43, 44, 45, 46, 47],[48, 49, 50, 51, 52, 53, 54, 55],[56, 57, 58, 59, 60, 46]])

tabella1 = 1
tabella2 = 2
tabella3 = 4
tabella4 = 8
tabella5 = 16
tabella6 = 32

import tkinter as tk
from tkinter import ttk

def calculate_number():
    selections = [selection.get() for selection in checkboxes]
    total = 0
    for i, selection in enumerate(selections):
        if selection:
            total += tables_numbers[i]
    result.set(f"il numero che hai pensato è: {total}")

root = tk.Tk()
root.title("Indovina il numero")

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(expand=True, fill="both")

description = "In questo gioco, pensa a un numero tra 1 e 60. Controlla le seguenti tabelle e seleziona quelle in cui compare il tuo numero. Premi il pulsante 'Calcola il numero' per scoprire il numero a cui stavi pensando."
description_label = ttk.Label(main_frame, text=description, wraplength=450, justify="left")
description_label.pack(pady=(0, 15))

tables_frame = ttk.Frame(main_frame)
tables_frame.pack()

tables = [table1, table2, table3, table4, table5, table6]
tables_numbers = [tabella1, tabella2, tabella3, tabella4, tabella5, tabella6]

checkboxes = []
for i, table in enumerate(tables):
    table_frame = ttk.Frame(tables_frame)
    table_frame.grid(row=i//2, column=i%2, padx=(10, 10), pady=(10, 10))
    
    label = ttk.Label(table_frame, text=f"TABELLA {i+1}", font=("Arial", 10, "bold"))
    label.pack(pady=(0, 5))
    
    selection = tk.BooleanVar()
    checkboxes.append(selection)
    chk = ttk.Checkbutton(table_frame, text=str(table), variable=selection)
    chk.pack()

calculate_button = ttk.Button(main_frame, text="Calcola il numero", command=calculate_number)
calculate_button.pack(pady=(15, 0))

result = tk.StringVar()
result_label = ttk.Label(main_frame, textvariable=result, font=("Arial", 10, "bold"))
result_label.pack(pady=(15, 0))

root.mainloop()
