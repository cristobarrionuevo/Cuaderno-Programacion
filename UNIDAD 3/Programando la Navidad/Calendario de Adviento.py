import tkinter as tk
import random
from datetime import datetime
import winsound

FRASES = [
    "🎄 Que la magia de la Navidad ilumine tu día",
    "🎁 Hoy es un buen día para sonreír",
    "✨ Cree en los pequeños milagros",
    "❄️ Paz, amor y alegría",
    "🔔 Se escuchan campanas de felicidad",
    "🎅 El espíritu navideño vive en ti",
    "🕯️ Un deseo se hace realidad",
    "⭐ Brilla como una estrella",
    "⛄ Sonríe, es Navidad",
    "🦌 Algo bonito viene en camino",
    "🎄 Comparte amor",
    "🎁 Disfruta este regalo",
    "✨ Todo es posible",
    "🔔 Gratitud infinita",
    "🎄 Hogar y familia",
    "🕯️ Luz y esperanza",
    "⭐ Sueños que nacen",
    "❄️ Calma y paz",
    "🎅 Navidad en el aire",
    "🎁 Detalles que importan",
    "✨ Milagros diarios",
    "🔔 Campanas felices",
    "🎄 Espíritu navideño",
    "⭐ Feliz Adviento"
]

class CalendarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎄 Calendario de Adviento 🎄")
        self.root.resizable(False, False)

        self.rectangulos = {}
        self.canvas = tk.Canvas(root, width=920, height=680, bg="#2b0f3f")
        self.canvas.pack(padx=10, pady=10)

        self.crear_titulo()
        self.crear_luces()
        self.crear_marco()
        self.crear_nieve()
        self.crear_estrellas()
        self.crear_calendario()

        self.animar_luces()
        self.animar_nieve()
        self.animar_estrellas()

    # 🎶 SONIDO
    def sonido_navideno(self):
        villancico = [
            (659,150),(659,150),(659,300),
            (659,150),(659,150),(659,300),
            (659,150),(784,150),
            (523,150),(587,150),(659,400)
        ]
        for f, d in villancico:
            winsound.Beep(f, d)

    # 🎄 DECORACIÓN
    def crear_titulo(self):
        self.canvas.create_text(
            460, 35,
            text="🎄 Calendario de Adviento 🎄",
            fill="#f5c542",
            font=("Arial", 30, "bold")
        )

    def crear_marco(self):
        self.canvas.create_rectangle(
            20, 90, 900, 650,
            outline="#f5c542",
            width=3
        )

    def crear_luces(self):
        self.luces = []
        for x in range(30, 900, 30):
            luz = self.canvas.create_oval(
                x, 70, x+14, 84,
                fill=random.choice(["#f5c542", "#ffffff", "#d7bde2", "#ff9ff3"]),
                outline=""
            )
            self.luces.append(luz)

    def animar_luces(self):
        for luz in self.luces:
            self.canvas.itemconfig(
                luz,
                fill=random.choice(["#f5c542", "#ffffff", "#d7bde2", "#ff9ff3"])
            )
        self.root.after(350, self.animar_luces)

    def crear_nieve(self):
        self.nieve = []
        for _ in range(90):
            x = random.randint(0, 920)
            y = random.randint(0, 680)
            copo = self.canvas.create_oval(
                x, y, x+4, y+4,
                fill="#f8f2ff",
                outline=""
            )
            self.nieve.append(copo)

    def animar_nieve(self):
        for copo in self.nieve:
            self.canvas.move(copo, 0, random.randint(1, 3))
            if self.canvas.coords(copo)[1] > 680:
                self.canvas.move(copo, 0, -680)
        self.root.after(60, self.animar_nieve)

    def crear_estrellas(self):
        self.estrellas = []
        for _ in range(30):
            x = random.randint(50, 880)
            y = random.randint(100, 300)
            estrella = self.canvas.create_text(
                x, y,
                text=random.choice(["✨", "⭐"]),
                font=("Arial", random.randint(12, 18)),
                fill="#fdf2c0"
            )
            self.estrellas.append(estrella)

    def animar_estrellas(self):
        for e in self.estrellas:
            self.canvas.itemconfig(
                e,
                font=("Arial", random.randint(12, 20))
            )
        self.root.after(500, self.animar_estrellas)

    # 📅 CALENDARIO
    def crear_calendario(self):
        columnas = 7
        ancho, alto, espacio = 105, 90, 12
        inicio_x, inicio_y = 30, 120
        iconos = ["🎄","🎅","🦌","🎁","❄️","⭐","🔔"]

        for dia in range(1, 25):
            fila = (dia - 1) // columnas
            col = (dia - 1) % columnas

            x1 = inicio_x + col * (ancho + espacio)
            y1 = inicio_y + fila * (alto + espacio)
            x2, y2 = x1 + ancho, y1 + alto

            rect = self.canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="#4b1c6f",
                outline="#f5c542",
                width=3
            )

            self.canvas.create_text(
                (x1+x2)/2, (y1+y2)/2,
                text=f"{iconos[col]}\n{dia}",
                fill="#fdf2c0",
                font=("Arial", 16, "bold"),
                justify="center"
            )

            self.rectangulos[dia] = rect
            self.canvas.tag_bind(
                rect, "<Button-1>",
                lambda e, d=dia: self.abrir_regalo(d)
            )

    # 🎁 LÓGICA
    def abrir_regalo(self, dia):
        hoy = datetime.now().day
        if dia > hoy:
            self.ventana_aviso("⏳ Aún no", "Este regalo todavía no puede abrirse 🎄")
            return

        self.canvas.itemconfig(self.rectangulos[dia], fill="#8e7cc3")
        self.sonido_navideno()
        self.animacion_regalo()

    # 🎁 ANIMACIÓN DE REGALO
    def animacion_regalo(self):
        top = tk.Toplevel(self.root)
        top.configure(bg="#2b0f3f")
        top.overrideredirect(True)

        cx = self.root.winfo_x() + self.root.winfo_width() // 2
        cy = self.root.winfo_y() + self.root.winfo_height() // 2
        top.geometry(f"200x200+{cx-100}+{cy-100}")

        canvas = tk.Canvas(top, bg="#2b0f3f", highlightthickness=0)
        canvas.pack(expand=True, fill="both")

        regalo = canvas.create_text(
            100, 100,
            text="🎁",
            font=("Arial", 60)
        )

        movimientos = [-6, 6] * 6

        def vibrar(i=0):
            if i < len(movimientos):
                canvas.move(regalo, movimientos[i], 0)
                top.after(60, lambda: vibrar(i+1))
            else:
                canvas.itemconfig(regalo, text="🎊✨")
                top.after(400, lambda: (top.destroy(), self.ventana_regalo()))

        vibrar()

    # 🎁 MENSAJE FINAL
    def ventana_regalo(self):
        top = tk.Toplevel(self.root)
        top.configure(bg="#2b0f3f")
        top.geometry("420x260")

        tk.Label(
            top,
            text="🎁 Regalo del Adviento 🎁",
            bg="#2b0f3f",
            fg="#f5c542",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        tk.Label(
            top,
            text=random.choice(FRASES),
            bg="#2b0f3f",
            fg="#fdf2c0",
            font=("Arial", 14),
            wraplength=340,
            justify="center"
        ).pack(pady=10)

        tk.Button(
            top,
            text="Cerrar 🎄",
            command=top.destroy,
            bg="#f5c542",
            fg="#2b0f3f",
            font=("Arial", 12, "bold"),
            relief="flat"
        ).pack(pady=10)

    def ventana_aviso(self, titulo, mensaje):
        top = tk.Toplevel(self.root)
        top.title(titulo)
        top.configure(bg="#2b0f3f")
        top.geometry("360x200")

        tk.Label(
            top,
            text=mensaje,
            bg="#2b0f3f",
            fg="#fdf2c0",
            font=("Arial", 13),
            wraplength=300,
            justify="center"
        ).pack(expand=True)

# ▶ MAIN
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarioApp(root)
    root.mainloop()
