import uuid
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from diffusers import StableDiffusionPipeline
import torch
import os

# Load the Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("cpu")

def build_prompt(brand, slogan, style, colors, industry, font, icon, transparent):
    prompt = f"Logo for a {style} {industry} company named '{brand}'"
    if slogan:
        prompt += f" with slogan '{slogan}'"
    prompt += f", using {colors} colors, clean and professional design."
    prompt += f" Use font style '{font}' and include an icon related to '{icon}'."
    if transparent:
        prompt += " Logo should have a transparent background."
    return prompt

def generate_and_save_logo(brand, slogan, style, colors, industry, font, icon, transparent):
    prompt = build_prompt(brand, slogan, style, colors, industry, font, icon, transparent)
    image = pipe(prompt).images[0]
    filename = f"logo_{uuid.uuid4().hex}.png"
    image.save(filename)
    return filename

def display_preview(image_path):
    img = Image.open(image_path).resize((256, 256))
    tk_img = ImageTk.PhotoImage(img)
    preview_label.config(image=tk_img)
    preview_label.image = tk_img

def on_generate():
    brand = brand_entry.get().strip()
    slogan = slogan_entry.get().strip()
    style = style_entry.get().strip() or "modern"
    colors = colors_entry.get().strip() or "blue and white"
    industry = industry_entry.get().strip() or "tech"
    font = font_var.get()
    icon = icon_var.get()
    transparent = transparent_var.get()

    if not brand:
        messagebox.showerror("Input Error", "Brand name is required.")
        return

    status_label.config(text="Generating logo...")
    app.update()

    try:
        filename = generate_and_save_logo(brand, slogan, style, colors, industry, font, icon, transparent)
        display_preview(filename)
        status_label.config(text=f"✅ Logo saved as {filename}")
    except Exception as e:
        status_label.config(text="❌ Failed to generate logo")
        messagebox.showerror("Error", str(e))

# GUI Setup
app = tk.Tk()
app.title("AI Logo Generator")
app.geometry("420x750")

# Input Fields
tk.Label(app, text="Brand Name").pack()
brand_entry = tk.Entry(app)
brand_entry.pack()

tk.Label(app, text="Slogan (optional)").pack()
slogan_entry = tk.Entry(app)
slogan_entry.pack()

tk.Label(app, text="Style (e.g., minimalist, vintage)").pack()
style_entry = tk.Entry(app)
style_entry.pack()

tk.Label(app, text="Preferred Colors").pack()
colors_entry = tk.Entry(app)
colors_entry.pack()

tk.Label(app, text="Industry").pack()
industry_entry = tk.Entry(app)
industry_entry.pack()

# Font Family Dropdown
tk.Label(app, text="Font Style").pack()
font_var = tk.StringVar(app)
font_var.set("sans-serif")  # default value
font_dropdown = tk.OptionMenu(app, font_var, "sans-serif", "serif", "monospace", "handwritten", "modern")
font_dropdown.pack()

# Icon Pack Dropdown
tk.Label(app, text="Icon Theme").pack()
icon_var = tk.StringVar(app)
icon_var.set("technology")  # default value
icon_dropdown = tk.OptionMenu(app, icon_var, "technology", "nature", "finance", "fashion", "sports")
icon_dropdown.pack()

# Transparent Background Option
tk.Label(app, text="Transparent Background").pack()
transparent_var = tk.BooleanVar()
transparent_checkbox = tk.Checkbutton(app, text="Enable", variable=transparent_var)
transparent_checkbox.pack()

# Generate Button
tk.Button(app, text="Generate Logo", command=on_generate).pack(pady=10)

# Preview Label
preview_label = tk.Label(app)
preview_label.pack(pady=10)

# Status Label
status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
