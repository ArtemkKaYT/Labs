import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO


URL = 'https://cataas.com/cat'


def get_cat():
    btn_load.config(text="Загружаю...", state="disabled")
    root.update()

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        img_data = BytesIO(response.content)
        img = Image.open(img_data)

        img.thumbnail((800, 800))
        img_tk = ImageTk.PhotoImage(img)

        label_image.config(image=img_tk)
        label_image.image = img_tk

        root.geometry("")

    except Exception as error:
        print(f"Ошибка: {error}")

    finally:
        btn_load.config(text="Еще котика!", state="normal")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Генератор котиков:3")
    btn_load = tk.Button(
        root,
        text="Получить котика^^",
        command=get_cat,
        font=("Arial", 12, "bold"),
        bg="#ff9900",
        padx=20,
        pady=10
    )
    btn_load.pack(side="top", pady=10)
    label_image = tk.Label(root)
    label_image.pack()
    root.mainloop()
