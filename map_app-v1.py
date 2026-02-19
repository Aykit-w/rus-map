import tkinter as tk
from PIL import Image, ImageTk
import pytz
from datetime import datetime

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

CITIES_COORDINATES = {
    'Москва': {
        'coordinates': (960, 540),
        'timezone': 'Europe/Moscow',
        'coat': 'moscow_coat.png'
    },
    'Санкт-Петербург': {
        'coordinates': (700, 300),
        'timezone': 'Europe/Moscow',
        'coat': 'saint_petersburg_coat.png'
    },
    'Владивосток': {
        'coordinates': (1800, 700),
        'timezone': 'Asia/Vladivostok',
        'coat': 'vladivostok_coat.png'
    },
    'Екатеринбург': {
        'coordinates': (1200, 560),
        'timezone': 'Asia/Yekaterinburg',
        'coat': 'ekaterinburg_coat.png'
    },
    'Казань': {
        'coordinates': (1050, 500),
        'timezone': 'Europe/Moscow',
        'coat': 'kazan_coat.png'
    },
    'Хабаровск': {
        'coordinates': (1700, 650),
        'timezone': 'Asia/Habarovsk',
        'coat': 'khabarovsk_coat.png'
    },
    'Новосибирск': {
        'coordinates': (1350, 600),
        'timezone': 'Asia/Novosibirsk',
        'coat': 'novosibirsk_coat.png'
    },
    'Краснодар': {
        'coordinates': (900, 650),
        'timezone': 'Europe/Moscow',
        'coat': 'krasnodar_coat.png'
    },
    'Самара': {
        'coordinates': (1100, 520),
        'timezone': 'Europe/Samara',
        'coat': 'samara_coat.png'
    },
    'Ростов-на-Дону': {
        'coordinates': (950, 680),
        'timezone': 'Europe/Moscow',
        'coat': 'rostov_on_don_coat.png'
    }
}

def get_current_time(timezone_str):
    utc_now = pytz.utc.localize(datetime.utcnow())
    local_tz = pytz.timezone(timezone_str)
    localized_time = utc_now.astimezone(local_tz)
    return localized_time.strftime('%H:%M:%S %Y-%m-%d')

class MapApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Интерактивная карта России")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)

        map_img = Image.open("map_of_russia.jpg").resize((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.map_photo = ImageTk.PhotoImage(map_img)

        self.canvas = tk.Canvas(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.map_photo)

        self.canvas.bind("<Button-1>", self.on_click)

        for city, data in CITIES_COORDINATES.items():
            x, y = data['coordinates']
            self.canvas.create_text(x, y, text=city, fill="white", font=("Arial", 12, "bold"))

        closest_city = None
        min_distance = float('inf')

        info_window = tk.Toplevel(self)
        info_window.title(closest_city)
        info_window.geometry("300x200")

if __name__ == "__main__":
    app = MapApp()
    app.mainloop()