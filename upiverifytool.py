import re
import tkinter as tk
from tkinter import messagebox

def verify_upi():
    txn_id = txn_entry.get()
    amount = amount_entry.get()

    # Basic check: UPI transaction ID pattern
    upi_pattern = r"^[A-Z0-9]{8,20}(@[a-z]{3,10})?$"

    if re.match(upi_pattern, txn_id):
        messagebox.showinfo("✅ Valid", f"Transaction ID looks valid.\nAmount: ₹{amount}")
    else:
        messagebox.showerror("❌ Invalid", "Invalid UPI Transaction ID format!")

# GUI setup
root = tk.Tk()
root.title("UPI TXN Verifier")
root.geometry("300x200")

tk.Label(root, text="UPI Transaction ID:").pack(pady=5)
txn_entry = tk.Entry(root)
txn_entry.pack(pady=5)

tk.Label(root, text="Amount (₹):").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

tk.Button(root, text="Verify", command=verify_upi).pack(pady=10)

root.mainloop()
