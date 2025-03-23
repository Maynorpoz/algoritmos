import tkinter as tk
import random
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Algoritmos de Ordenamiento")
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        
        self.generate_button = tk.Button(self.button_frame, text="Generar Lista", command=self.generate_list)
        self.generate_button.pack(side=tk.LEFT)
        
        self.bubble_button = tk.Button(self.button_frame, text="Bubble Sort", command=self.bubble_sort)
        self.bubble_button.pack(side=tk.LEFT)
        
        self.selection_button = tk.Button(self.button_frame, text="Selection Sort", command=self.selection_sort)
        self.selection_button.pack(side=tk.LEFT)
        
        self.list_values = []
        self.generate_list()
    
    def generate_list(self):
        self.list_values = [random.randint(10, 300) for _ in range(20)]
        self.draw_list()
    
    def draw_list(self, highlight=[]):
        self.canvas.delete("all")
        bar_width = 600 / len(self.list_values)
        for i, value in enumerate(self.list_values):
            x0 = i * bar_width
            y0 = 400 - value
            x1 = (i + 1) * bar_width
            y1 = 400
            color = "red" if i in highlight else "blue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.root.update()
    
    def bubble_sort(self):
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
    
    def selection_sort(self):
        n = len(self.list_values)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.list_values[j] < self.list_values[min_index]:
                    min_index = j
            self.list_values[i], self.list_values[min_index] = self.list_values[min_index], self.list_values[i]
            self.draw_list([i, min_index])
            time.sleep(0.1)

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
