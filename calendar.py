import tkinter as tk
from tkinter import ttk
import calendar
from hijri_converter import convert
from datetime import datetime

# Hijri month names
HIJRI_MONTHS = [
    "Muharram", "Safar", "Rabi' al-Awwal", "Rabi' al-Thani", "Jumada al-Awwal", "Jumada al-Thani",
    "Rajab", "Sha'ban", "Ramadan", "Shawwal", "Dhu al-Qi'dah", "Dhu al-Hijjah"
]

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        
        self.show_button = tk.Button(root, text="Show Current Calendar", command=self.show_calendar)
        self.show_button.grid(row=0, column=0, columnspan=2)
        
        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=1, column=0, columnspan=2, sticky="nsew")
        
        self.gregorian_frame = ttk.Frame(self.notebook)
        self.hijri_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.gregorian_frame, text='Gregorian Calendar')
        self.notebook.add(self.hijri_frame, text='Hijri Calendar')
        
        self.gregorian_text = tk.Text(self.gregorian_frame, width=40, height=20)
        self.gregorian_text.pack(expand=1, fill='both')
        
        self.hijri_text = tk.Text(self.hijri_frame, width=40, height=20)
        self.hijri_text.pack(expand=1, fill='both')
        
        # Automatically show the current month's calendar on startup
        self.show_calendar()
    
    def show_calendar(self):
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        
        # Gregorian calendar
        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_str = cal.formatmonth(year, month)
        
        # Islamic calendar
        hijri_date = convert.Gregorian(year, month, day).to_hijri()
        hijri_day = hijri_date.day
        hijri_month_name = HIJRI_MONTHS[hijri_date.month - 1]
        hijri_year = hijri_date.year
        hijri_cal_str = f"Islamic Calendar\n{hijri_day} {hijri_month_name} {hijri_year}\n\n"
        
        self.gregorian_text.delete(1.0, tk.END)
        self.gregorian_text.insert(tk.END, cal_str)
        
        self.hijri_text.delete(1.0, tk.END)
        self.hijri_text.insert(tk.END, hijri_cal_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
