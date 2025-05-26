AI Logo Generator
=================

This is a simple AI-powered logo generator built with Python and the Diffusers library.
It uses the Stable Diffusion model to generate logos based on user input like brand name,
style, industry, and more. A simple GUI is provided using Tkinter.

How it Works
------------
The script prompts the user for brand-related inputs, then uses a Stable Diffusion pipeline
to generate a logo image based on the provided prompt. The resulting logo is saved as a PNG
file and previewed in the GUI.

Features
--------
- Tkinter GUI for user input and preview
- Custom input for brand, slogan, style, colors, industry
- Font family and icon dropdown menus
- Option for transparent background
- Image preview in-app
- Automatic file saving

Requirements
------------
See `requirements.txt` for required packages. Ensure you have:
- Python 3.9 or higher
- At least 8GB RAM (GPU optional)
- Diffusers-compatible model checkpoint access

Installation
------------
1. Clone the repository or copy the script to a folder.
    bash``
   git clone https://github.com/rishabhkarnwal04/AI-LOGO-GENERATOR.git
   cd AI-LOGO-GENERATOR
    ``
   
2. Install dependencies:
    bash``
    pip install -r requirements.txt
        ``
3. Run the app:
    bash``
    python logo_gen.py
    ``
   
Note:
-----
- If you're using a CPU-only machine, make sure not to use `torch_dtype=torch.float16`
  as it will throw an error.
- This version uses `runwayml/stable-diffusion-v1-5` which runs slowly on CPU. GPU recommended.

Author
------
Developed by Rishabh Karnwal
