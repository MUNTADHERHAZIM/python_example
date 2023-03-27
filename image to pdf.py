import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Image to PDF Converter")


def convert_to_pdf():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    img = Image.open(filepath)
    
    pdf_type = pdf_choice.get()
    save_location = filedialog.asksaveasfilename(defaultextension=pdf_type, initialfile="converted.pdf", filetypes=[("PDF Files", f"*.{pdf_type}")])
    img.save(save_location, format=pdf_type.upper())


image_label = tk.Label(root, text="Choose image file to convert")

image_label.pack()

browse_btn = tk.Button(root, text="Browse", command=convert_to_pdf)

browse_btn.pack()

pdf_label = tk.Label(root, text="Select PDF file type to save as")

pdf_label.pack()

pdf_choice = tk.StringVar(value="pdf")
pdf_radio1 = tk.Radiobutton(root, text="PDF", variable=pdf_choice, value="pdf")
pdf_radio1.pack()
pdf_radio2 = tk.Radiobutton(root, text="PNG", variable=pdf_choice, value="png")
pdf_radio2.pack()

root.mainloop()