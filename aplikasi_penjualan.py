import tkinter as tk
from tkinter import messagebox

class SalesApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Aplikasi Penjualan")
        self.cart = []

        # Frame untuk input produk
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        self.name_label = tk.Label(self.input_frame, text="Nama Produk:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.price_label = tk.Label(self.input_frame, text="Harga Produk:")
        self.price_label.grid(row=1, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(self.input_frame)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        self.quantity_label = tk.Label(self.input_frame, text="Kuantitas:")
        self.quantity_label.grid(row=2, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(self.input_frame)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.input_frame, text="Tambah ke Keranjang", command=self.add_to_cart)
        self.add_button.grid(row=3, columnspan=2, pady=10)

        # Frame untuk keranjang belanja
        self.cart_frame = tk.Frame(root)
        self.cart_frame.pack(pady=10)

        self.cart_label = tk.Label(self.cart_frame, text="Keranjang Belanja")
        self.cart_label.pack()

        self.cart_listbox = tk.Listbox(self.cart_frame, width=50, height=10)
        self.cart_listbox.pack()

        self.total_label = tk.Label(self.cart_frame, text="Total: Rp 0")
        self.total_label.pack(pady=5)

        self.checkout_button = tk.Button(self.cart_frame, text="Checkout", command=self.checkout)
        self.checkout_button.pack(pady=10)

    def add_to_cart(self):
        name = self.name_entry.get()
        try:
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showwarning("Input Error", "Harga dan Kuantitas harus berupa angka!")
            return

        if name and price > 0 and quantity > 0:
            self.cart.append({'name': name, 'price': price, 'quantity': quantity})
            self.update_cart()
            self.name_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Semua kolom harus diisi dengan benar!")

    def update_cart(self):
        self.cart_listbox.delete(0, tk.END)
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
            self.cart_listbox.insert(tk.END, f"{item['name']} - Rp {item['price']} x {item['quantity']}")

        self.total_label.config(text=f"Total: Rp {total}")

    def checkout(self):
        if not self.cart:
            messagebox.showwarning("Keranjang Kosong", "Keranjang belanja Anda kosong!")
            return

        messagebox.showinfo("Checkout", f"Total pembayaran: Rp {self.total_label.cget('text').split(' ')[1]}")
        self.cart.clear()
        self.update_cart()

if __name__ == "_main_":
    root = tk.Tk()
    app = SalesApp(root)
    root.mainloop()