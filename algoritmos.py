import tkinter as tk
import random
import time

class Ordenamiento:
    def __init__(self, root):
        self.root = root
        self.root.title("ALGORITMO DE ORDENAMIENTO")
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="black")
        self.canvas.pack()
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        
        self.generate_button = tk.Button(self.button_frame, text="GENERAR LISTA ALEATORIA", 
                                         command=self.generate_list, bg="blue", fg="white", font=("Bell MT", 9, "bold"))
        self.generate_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.bubble_button = tk.Button(self.button_frame, text="METODO BUBBLE SORT", 
                                       command=self.bubble_sort, bg="blue", fg="white", font=("Bell MT", 9, "bold"))
        self.bubble_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.selection_button = tk.Button(self.button_frame, text="METODO SELECTION SORT", 
                                          command=self.selection_sort, bg="blue", fg="white", font=("Bell MT", 9, "bold"))
        self.selection_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.list_values = []
        ##self.generate_list()
    
    def toggle_buttons(self, state: bool):
        """Habilita o deshabilita los botones."""
        state_str = tk.NORMAL if state else tk.DISABLED
        self.generate_button.config(state=state_str)
        self.bubble_button.config(state=state_str)
        self.selection_button.config(state=state_str)
    
    def generate_list(self):
        """Genera una nueva lista aleatoria y la dibuja."""
        self.list_values = [random.randint(10, 300) for _ in range(20)]
        self.draw_list()
    
    def draw_list(self, highlight=[]):
        """Dibuja la lista de valores como barras en el canvas."""
        self.canvas.delete("all")
        bar_width = 600 / len(self.list_values)
        for i, value in enumerate(self.list_values):
            x0 = i * bar_width
            y0 = 400 - value
            x1 = (i + 1) * bar_width
            y1 = 400
            color = "yellow" if i in highlight else "green"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.root.update()
    
    def bubble_sort(self):
        """Ordena la lista usando el algoritmo de burbuja y bloquea botones mientras se ejecuta."""
        self.toggle_buttons(False)  # Deshabilitar botones
        n = len(self.list_values)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if self.list_values[j] > self.list_values[j + 1]:
                    self.list_values[j], self.list_values[j + 1] = self.list_values[j + 1], self.list_values[j]
                    swapped = True
                    self.draw_list([j, j+1])
                    time.sleep(0.1)
            if not swapped:
                break
            self.draw_list()
        self.toggle_buttons(True)  # Habilitar botones al finalizar
    
    def selection_sort(self):
        """Ordena la lista usando el algoritmo de selección y bloquea botones mientras se ejecuta."""
        self.toggle_buttons(False)  # Deshabilitar botones
        n = len(self.list_values)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                self.draw_list([min_index, j])  # Resaltar comparación actual
                time.sleep(0.1)
                if self.list_values[j] < self.list_values[min_index]:
                    min_index = j
                    self.draw_list([min_index])  # Resaltar el nuevo mínimo
                    time.sleep(0.1)
            self.list_values[i], self.list_values[min_index] = self.list_values[min_index], self.list_values[i]
            self.draw_list([i, min_index])  # Mostrar el intercambio final
            time.sleep(0.1)
        self.draw_list()  # Redibujar lista final ordenada
        self.toggle_buttons(True)  # Habilitar botones al finalizar

if __name__ == "__main__":
    root = tk.Tk()
    app = Ordenamiento(root)
    root.mainloop()
