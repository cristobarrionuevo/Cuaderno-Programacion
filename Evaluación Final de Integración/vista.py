import tkinter as tk

class VistaIncubadora:
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root

        root.title("Incubadora Inteligente")
        root.geometry("520x420")
        root.configure(bg="#1e1e2e")

        # ===== TÍTULO =====
        tk.Label(
            root,
            text="🐣 INCUBADORA INTELIGENTE",
            font=("Segoe UI", 16, "bold"),
            fg="white",
            bg="#1e1e2e"
        ).pack(pady=10)

        # ===== CANVAS PRINCIPAL =====
        self.canvas = tk.Canvas(
            root,
            width=480,
            height=330,
            bg="#1e1e2e",
            highlightthickness=0
        )
        self.canvas.pack()

        # ===== TARJETAS =====
        self._tarjeta_temperatura()
        self._tarjeta_humedad()
        self._tarjeta_botones()
        self._tarjeta_historial()

    # ---------- TARJETA TEMPERATURA ----------
    def _tarjeta_temperatura(self):
        self.canvas.create_rectangle(20, 10, 230, 90, fill="#2a2a3d", outline="")
        self.canvas.create_text(
            125, 25, text="🌡️ TEMPERATURA",
            fill="white", font=("Segoe UI", 10, "bold")
        )
        self.txt_temp = self.canvas.create_text(
            125, 55, text="-- °C",
            fill="#ff6b6b", font=("Segoe UI", 18, "bold")
        )

    # ---------- TARJETA HUMEDAD ----------
    def _tarjeta_humedad(self):
        self.canvas.create_rectangle(250, 10, 460, 90, fill="#2a2a3d", outline="")
        self.canvas.create_text(
            355, 25, text="💧 HUMEDAD",
            fill="white", font=("Segoe UI", 10, "bold")
        )
        self.txt_hum = self.canvas.create_text(
            355, 55, text="-- %",
            fill="#4dabf7", font=("Segoe UI", 18, "bold")
        )

    # ---------- TARJETA BOTONES ----------
    def _tarjeta_botones(self):
        self.canvas.create_rectangle(20, 105, 460, 170, fill="#2a2a3d", outline="")

        btn_leer = tk.Button(
            self.root, text="📡 Leer Sensor",
            command=self.controlador.leer_sensor,
            bg="#4caf50", fg="white", relief="flat",
            font=("Segoe UI", 10, "bold")
        )
        btn_led_on = tk.Button(
            self.root, text="🔴 LED ON",
            command=self.controlador.encender_led,
            bg="#e53935", fg="white", relief="flat",
            font=("Segoe UI", 10, "bold")
        )
        btn_led_off = tk.Button(
            self.root, text="⚫ LED OFF",
            command=self.controlador.apagar_led,
            bg="#616161", fg="white", relief="flat",
            font=("Segoe UI", 10, "bold")
        )

        self.canvas.create_window(110, 138, window=btn_leer, width=140, height=35)
        self.canvas.create_window(260, 138, window=btn_led_on, width=120, height=35)
        self.canvas.create_window(390, 138, window=btn_led_off, width=120, height=35)

    # ---------- TARJETA HISTORIAL ----------
    def _tarjeta_historial(self):
        self.canvas.create_rectangle(20, 185, 460, 320, fill="#2a2a3d", outline="")
        self.canvas.create_text(
            240, 195, text="📊 HISTORIAL DE REGISTROS",
            fill="white", font=("Segoe UI", 10, "bold")
        )

        self.txt_historial = tk.Text(
            self.root,
            height=6,
            width=52,
            bg="#1e1e2e",
            fg="white",
            relief="flat",
            font=("Consolas", 9)
        )
        self.canvas.create_window(240, 255, window=self.txt_historial)

    # ===== ACTUALIZACIONES DESDE EL CONTROLADOR =====
    def actualizar_datos(self, temp, hum):
        self.canvas.itemconfig(self.txt_temp, text=f"{temp} °C")
        self.canvas.itemconfig(self.txt_hum, text=f"{hum} %")

    def mostrar_historial(self, registros):
        self.txt_historial.delete("1.0", tk.END)
        for temp, hum, fecha in registros:
            self.txt_historial.insert(
                tk.END,
                f"{fecha} | {temp} °C | {hum} %\n"
            )
