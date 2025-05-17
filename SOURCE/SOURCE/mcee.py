import customtkinter as ctk
import os
import subprocess
import webbrowser
import re

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MCEE Launcher")
        self.geometry("400x450")
        self.resizable(False, False)
        self.overrideredirect(True)
        
        self.nickname = self.load_nickname()
        self.create_title_bar()
        self.create_main_frame()

    def create_title_bar(self):
        self.title_bar = ctk.CTkFrame(self, fg_color="#1a1a1a", height=30)
        self.title_bar.pack(fill="x")

        # Исправленный блок создания заголовка
        self.main_title_label = ctk.CTkLabel(
            self.title_bar,
            text="MCEE Launcher",
            text_color="#ffffff",
            font=("Arial", 12)
        )  # Закрывающая скобка добавлена
        self.main_title_label.pack(side="left", padx=5, pady=10)

        close_button = ctk.CTkButton(
            self.title_bar, 
            text=" × ",
            width=30,
            height=20,
            fg_color="transparent",
            hover_color="#ff0000",
            command=self.destroy
        )
        close_button.pack(side="right", padx=5)

        self.title_bar.bind("<B1-Motion>", self.move_window)
        self.title_bar.bind("<ButtonPress-1>", self.start_move)

    def create_child_window(self, title, width, height):
        window = ctk.CTkToplevel(self)
        window.title(title)  # Устанавливаем заголовок отдельно
        window.geometry(f"{width}x{height}")
        window.resizable(False, False)
        window.overrideredirect(True)
        window.attributes("-topmost", True)
        
        # Заголовок для дочернего окна
        child_title_bar = ctk.CTkFrame(window, fg_color="#1a1a1a", height=30)
        child_title_bar.pack(fill="x")
        
        child_title_label = ctk.CTkLabel(
            child_title_bar,
            text=title,
            text_color="#ffffff",
            font=("Arial", 10)
        )
        child_title_label.pack(side="left", padx=5, pady=10)

        close_btn = ctk.CTkButton(
            child_title_bar,
            text=" × ",
            width=20,
            height=20,
            fg_color="transparent",
            hover_color="#ff0000",
            command=window.destroy
        )
        close_btn.pack(side="right", padx=5)
        
        child_title_bar.bind("<B1-Motion>", lambda e: self.move_child_window(e, window))
        child_title_bar.bind("<ButtonPress-1>", lambda e: self.start_move(e))
        
        return window

    def move_child_window(self, event, window):
        window.geometry(f'+{event.x_root}+{event.y_root}')

    def create_main_frame(self):
        main_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        buttons = [
            ("Старт", "#00ff00", self.start_app),
            ("Сменить ник", "#0088ff", self.open_settings),
            ("О программе", "#ff8800", self.open_about),
            ("Выход", "#ff0000", self.destroy)
        ]

        for text, color, command in buttons:
            btn = ctk.CTkButton(
                main_frame,
                text=text,
                fg_color=color,
                hover_color="#333333",
                text_color="#000000",
                corner_radius=10,
                command=command
            )
            btn.pack(pady=8, padx=40, fill="x")

    def move_window(self, event):
        self.geometry(f'+{event.x_root}+{event.y_root}')

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def start_app(self):
        try:
            # Показываем окно с сообщением
            launch_window = ctk.CTkToplevel(self)
            launch_window.geometry("200x100")
            launch_window.overrideredirect(True)
        
            label = ctk.CTkLabel(
                launch_window, 
                text="Запуск...", 
                font=("Arial", 14)
            )
            label.pack(expand=True)
        
            self.update()
            subprocess.Popen(["START\\Запустить.cmd"], shell=True)
            self.after(2000, self.destroy)  # Закрытие через 2 секунды
        
        except Exception as e:
            launch_window.destroy()
            self.status_label.configure(
                text=f"Ошибка: {str(e)}", 
                text_color="red"
            )

    def open_settings(self):
        window = self.create_child_window("Настройки", 300, 200)
        
        label = ctk.CTkLabel(window, text="Введите ваш ник:")
        label.pack(pady=10)

        entry = ctk.CTkEntry(window)
        entry.insert(0, self.nickname)
        entry.pack(pady=5)

        error_label = ctk.CTkLabel(window, text="", text_color="red")
        error_label.pack()

        save_btn = ctk.CTkButton(
            window,
            text="Сохранить",
            command=lambda: self.save_nickname(entry.get(), error_label)
        )
        save_btn.pack(pady=10)

    def save_nickname(self, nickname, error_label):
        if not re.match("^[a-zA-Z0-9]+$", nickname):
            error_label.configure(text="В нике могут быть только английские буквы и цифры!", text_color="red")
            return
            
        try:
            with open("config.txt", "w") as f:
                f.write(nickname)
            
            self.save_to_minecraft(nickname)
            error_label.configure(text="Успешно сохранено!", text_color="green")
            self.nickname = nickname
        except Exception as e:
            error_label.configure(text=f"Ошибка: {str(e)}", text_color="red")

    def save_to_minecraft(self, nickname):
        path = os.path.expandvars(
            r"%USERPROFILE%\AppData\Roaming\Minecraft Education Edition" 
            r"\games\com.mojang\minecraftpe\options.txt"
        )
        
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        lines = []
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                lines = [line for line in f if not line.startswith("mp_username:")]
        
        lines.insert(0, f"mp_username:{nickname}\n")
        
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)

    def open_about(self):
        window = self.create_child_window("О программе", 400, 250)
        
        content = """
        MCEE Bypass - инструмент для обхода защиты
        Версия: 2.1
        Разработчик: FoxinaBox
        Ссылки:
        """
        label = ctk.CTkLabel(window, text=content)
        label.pack(padx=10)

        links = [
            ("GitHub", "https://github.com/Cats-coding-batch"),
            ("Telegram", "https://t.me/CatsCB")
        ]

        for text, url in links:
            link = ctk.CTkLabel(
                window,
                text=text,
                text_color="#00aaff",
                cursor="hand2")
            link.pack(pady=2)
            link.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))

    def show_error(self, message):
        window = self.create_child_window("Ошибка", 300, 100)
        label = ctk.CTkLabel(window, text=message, text_color="red")
        label.pack(pady=20)

    def load_nickname(self):
        try:
            with open("config.txt", "r") as f:
                return f.read().strip()
        except:
            return "Player"

if __name__ == "__main__":
    app = App()
    app.mainloop()
