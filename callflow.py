import datetime
import tkinter as tk
from tkinter import messagebox

class CallLogProgram:
    def __init__(self, master):
        self.master = master
        self.master.title("Call Log Program")

        self.who_label = tk.Label(master, text="Who:")
        self.who_entry = tk.Entry(master, width=50)

        self.why_label = tk.Label(master, text="Why:")
        self.why_entry = tk.Entry(master, width=50)

        self.what_label = tk.Label(master, text="What:")
        self.what_text = tk.Text(master, height=10, width=50)

        self.timestamp_button = tk.Button(master, text="Timestamp", command=self.add_timestamp)

        self.wrap_label = tk.Label(master, text="Wrap:")
        self.wrap_text = tk.Text(master, height=5, width=50)

        self.summary_button = tk.Button(master, text="Generate Summary", command=self.generate_summary)

        # Layout
        self.who_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.who_entry.grid(row=0, column=1, columnspan=3, pady=5)

        self.why_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.why_entry.grid(row=1, column=1, columnspan=3, pady=5)

        self.what_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.what_text.grid(row=2, column=1, columnspan=3, pady=5)

        self.timestamp_button.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        self.wrap_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.wrap_text.grid(row=4, column=1, columnspan=3, pady=5)

        self.summary_button.grid(row=5, column=0, columnspan=4, pady=10)

        # Initialize variables
        self.call_log = {
            'Who': '',
            'Why': '',
            'What': '',
            'Timestamps': [],
            'Wrap': ''
        }

    def add_timestamp(self):
        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] Eastern Time")
        self.call_log['Timestamps'].append(timestamp)

    def generate_summary(self):
        self.call_log['Who'] = self.who_entry.get()
        self.call_log['Why'] = self.why_entry.get()
        self.call_log['What'] = self.what_text.get("1.0", "end-1c")
        self.call_log['Wrap'] = self.wrap_text.get("1.0", "end-1c")

        summary = f"Who: {self.call_log['Who']}\n"
        summary += f"Why: {self.call_log['Why']}\n"
        summary += f"What:\n{self.call_log['What']}\n"
        summary += "Timestamps:\n"
        for timestamp in self.call_log['Timestamps']:
            summary += f"{timestamp}\n"
        summary += f"Wrap:\n{self.call_log['Wrap']}"

        messagebox.showinfo("Call Log Summary", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = CallLogProgram(root)
    root.mainloop()
