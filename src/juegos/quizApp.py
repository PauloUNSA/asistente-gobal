import tkinter as tk
from PIL import Image, ImageTk
from utils_audio import texto_a_audio
class ComputerStructureQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JUEGO: ESTRUCTURA DE UN COMPUTADOR")

        self.question_label = tk.Label(root, text="¿Qué componente almacena datos de manera temporal en la CPU?")
        self.question_label.pack()

        self.image_frame = tk.Frame(root)
        self.image_frame.pack()

        self.image_labels = []
        for _ in range(4):
            image_label = tk.Label(self.image_frame, image=None)
            image_label.pack(side=tk.LEFT, padx=10)
            image_label.bind("<Button-1>", self.check_answer)
            self.image_labels.append(image_label)

        self.correct_answer = 0  # Índice de la respuesta correcta
        self.load_question()

    def load_question(self):
        # Cargar la pregunta y las imágenes aquí
        question = "¿Qué componente almacena datos de manera temporal en la CPU?"
        options = ["RAM", "GPU", "HDD", "CPU"]
        
        self.question_label.config(text=question)
        self.correct_answer = 0  # Respuesta correcta en la posición 0 (RAM)

        for i in range(4):
            image_path = f"img/option_{i+1}.png"
            image = Image.open(image_path)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)
            self.image_labels[i].config(image=photo)
            self.image_labels[i].image = photo

    def check_answer(self, event):
        clicked_label = event.widget
        clicked_index = self.image_labels.index(clicked_label)
        
        if clicked_index == self.correct_answer:
            print("¡Respuesta correcta!")
            texto_a_audio("Respuesta correcta.")
        else:
            print("Respuesta incorrecta.")
            texto_a_audio("Respuesta incorrecta.")
        self.load_question()
