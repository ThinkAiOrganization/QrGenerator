import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_qr_code_with_logo(url, filename, logo_path=None, logo_size_ratio=0.2):
    try:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H if logo_path else qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill='black', back_color='white').convert('RGB')

        if logo_path:
            # Load the logo image
            logo = Image.open(logo_path)

            # Calculate logo size and position
            qr_width, qr_height = img.size
            logo_size = int(qr_width * logo_size_ratio), int(qr_height * logo_size_ratio)
            logo = logo.resize(logo_size, Image.ANTIALIAS)
            logo_position = ((qr_width - logo_size[0]) // 2, (qr_height - logo_size[1]) // 2)

            # Paste the logo onto the QR code
            img.paste(logo, logo_position, logo)

        # Save the image to a file
        img.save(filename)
        return filename

    except Exception as e:
        print(f"Error: {e}")
        return None

def browse_logo():
    logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    logo_entry.delete(0, tk.END)
    logo_entry.insert(0, logo_path)

def generate_qr(with_logo):
    url = url_entry.get()
    logo_path = logo_entry.get() if with_logo else None
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    if with_logo and not logo_path:
        messagebox.showerror("Error", "Please select a logo image.")
        return

    filename = "qrcode_with_logo.png" if with_logo else "qrcode.png"
    result = generate_qr_code_with_logo(url, filename, logo_path)
    if result:
        messagebox.showinfo("Success", f"QR code saved as {filename}")
    else:
        messagebox.showerror("Error", "Failed to generate QR code.")

app = tk.Tk()
app.title("QR Code Generator")

tk.Label(app, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(app, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Select Logo (optional):").grid(row=1, column=0, padx=10, pady=10)
logo_entry = tk.Entry(app, width=50)
logo_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_logo).grid(row=1, column=2, padx=10, pady=10)

tk.Button(app, text="Generate QR Code with Logo", command=lambda: generate_qr(True)).grid(row=2, column=0, columnspan=3, pady=5)
tk.Button(app, text="Generate QR Code without Logo", command=lambda: generate_qr(False)).grid(row=3, column=0, columnspan=3, pady=5)

app.mainloop()
