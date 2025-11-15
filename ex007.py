import tkinter as tk
from tkinter import messagebox, font

class IMCApp:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # remove decoração nativa
        self.is_maximized = False
        self._geom = '800x420+200+120'

        self.root.geometry(self._geom)
        self._create_titlebar()
        self._create_body()
        self._create_footer()
        self._bind_keys()

    def _create_titlebar(self):
        titlebar = tk.Frame(self.root, bg="#2c3e50", relief='raised', bd=0)
        titlebar.pack(fill=tk.X)

    
        titlebar.bind("<ButtonPress-1>", self.start_move)
        titlebar.bind("<B1-Motion>", self.on_move)

        title_font = font.Font(size=12, weight="bold")
        title_label = tk.Label(titlebar, text="Calculo IMC", bg="#2c3e50", fg="white", font=title_font)
        title_label.pack(side=tk.TOP, pady=6)
        #  Centralizar o titulo 
        # Criar bottões no canto superior direito (top-right) 
        btn_frame = tk.Frame(titlebar, bg="#2c3e50")
        btn_frame.place(relx=1.0, x=-6, y=6, anchor='ne')

        minimize = tk.Button(btn_frame, text="▁", width=3, command=self.minimize, bg="#95a5a6", relief='flat')
        maximize = tk.Button(btn_frame, text="▢", width=3, command=self.toggle_maximize, bg="#95a5a6", relief='flat')
        close = tk.Button(btn_frame, text="✕", width=3, command=self.root.quit, bg="#e74c3c", fg="white", relief='flat')

        minimize.pack(side=tk.LEFT, padx=(0,4))
        maximize.pack(side=tk.LEFT, padx=(0,4))
        close.pack(side=tk.LEFT)

        # allow titlelabel to also drag
        title_label.bind("<ButtonPress-1>", self.start_move)
        title_label.bind("<B1-Motion>", self.on_move)

    def _create_body(self):
        body = tk.Frame(self.root, bg="#ecf0f1", padx=20, pady=10)
        body.pack(fill=tk.BOTH, expand=True)

        lbl_font = font.Font(size=10)
        entry_style = {'bd':0, 'highlightthickness':1, 'highlightbackground':'black', 'highlightcolor':'black', 'bg':'white', 'font':lbl_font}

        # Nome
        tk.Label(body, text="Nome do Participante:", bg="#ecf0f1").grid(row=0, column=0, sticky='w', pady=(6,2))
        self.nome_entry = tk.Entry(body, **entry_style)
        self.nome_entry.grid(row=1, column=0, sticky='we', pady=(0,8), ipady=6)

        # Endereço (Texto multilinhas)
        tk.Label(body, text="Endereço do participante:", bg="#ecf0f1").grid(row=2, column=0, sticky='w', pady=(6,2))
        self.endereco_txt = tk.Text(body, height=3, wrap='word', bd=0, highlightthickness=1, highlightbackground='black', font=lbl_font)
        self.endereco_txt.grid(row=3, column=0, sticky='we', pady=(0,8))

        # Altura e Peso
        form_row = tk.Frame(body, bg="#ecf0f1")
        form_row.grid(row=4, column=0, sticky='we', pady=(4,8))

        # Altura
        alt_frame = tk.Frame(form_row, bg="#ecf0f1")
        alt_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,8))
        tk.Label(alt_frame, text="Altura (cm):", bg="#ecf0f1").pack(anchor='w')
        self.altura_entry = tk.Entry(alt_frame, **entry_style)
        self.altura_entry.pack(fill=tk.X, ipady=6, pady=(0,0))

        # Peso
        peso_frame = tk.Frame(form_row, bg="#ecf0f1")
        peso_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Label(peso_frame, text="Peso (kg):", bg="#ecf0f1").pack(anchor='w')
        self.peso_entry = tk.Entry(peso_frame, **entry_style)
        self.peso_entry.pack(fill=tk.X, ipady=6, pady=(0,0))

        # Resultado
        res_box = tk.Frame(body, bg="#ecf0f1")
        res_box.grid(row=5, column=0, sticky='we', pady=(6,8))
        tk.Label(res_box, text="Resultado:", bg="#ecf0f1").pack(anchor='w')
        self.result_label = tk.Label(res_box, text="", bg="white", anchor='w', justify='left',
                                     bd=0, highlightthickness=1, highlightbackground='black', padx=6, pady=6)
        self.result_label.pack(fill=tk.X)

        # Expandir a coluna
        body.grid_columnconfigure(0, weight=1)

    def _create_footer(self):
        footer = tk.Frame(self.root, bg="#bdc3c7")
        footer.pack(fill=tk.X)

        btn_calc = tk.Button(footer, text="Calcular", width=12, command=self.calcular, bg="#27ae60", fg="white")
        btn_reset = tk.Button(footer, text="Reiniciar", width=12, command=self.reiniciar, bg="#f39c12", fg="white")
        btn_exit = tk.Button(footer, text="Sair", width=12, command=self.root.quit, bg="#c0392b", fg="white")

        # Colocar botões no canto direito 
        btn_exit.pack(side=tk.RIGHT, padx=10, pady=8)
        btn_reset.pack(side=tk.RIGHT, padx=10, pady=8)
        btn_calc.pack(side=tk.RIGHT, padx=10, pady=8)

    def _bind_keys(self):
        # Permite que Esc feche
        self.root.bind("<Escape>", lambda e: self.root.quit())

    # Janela de manipuladoras de movimentos (handlers)
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        dx = event.x_root - self.x
        dy = event.y_root - self.y
        self.root.geometry(f'+{dx}+{dy}')

    def minimize(self):
        self.root.update_idletasks()
        self.root.iconify()

    def toggle_maximize(self):
        if not self.is_maximized:
            self._geom = self.root.geometry()
            self.root.state('zoomed')  # windows: zoomed
            self.is_maximized = True
        else:
            try:
                self.root.state('normal')
                self.root.geometry(self._geom)
            except Exception:
                self.root.geometry(self._geom)
            self.is_maximized = False

    def calcular(self):
        nome = self.nome_entry.get().strip()
        endereco = self.endereco_txt.get("1.0", "end").strip()
        altura_s = self.altura_entry.get().strip().replace(',', '.')
        peso_s = self.peso_entry.get().strip().replace(',', '.')

        if not altura_s or not peso_s:
            messagebox.showwarning("Dados incompletos", "Preencha altura e peso.")
            return
        try:
            altura_cm = float(altura_s)
            peso = float(peso_s)
            altura_m = altura_cm / 100.0
            if altura_m <= 0:
                raise ValueError
            imc = peso / (altura_m ** 2)
        except Exception:
            messagebox.showerror("Erro", "Altura e peso devem ser números válidos.")
            return

        categoria = self._classificar_imc(imc)
        resultado = f"Nome: {nome or '-'}\nEndereço: {endereco or '-'}\nAltura: {altura_cm:.1f} cm\nPeso: {peso:.1f} kg\nIMC: {imc:.2f} ({categoria})"
        self.result_label.config(text=resultado)

    def _classificar_imc(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidade"

    def reiniciar(self):
        self.nome_entry.delete(0, tk.END)
        self.endereco_txt.delete('1.0', tk.END)
        self.altura_entry.delete(0, tk.END)
        self.peso_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = IMCApp(root)
    root.mainloop()
