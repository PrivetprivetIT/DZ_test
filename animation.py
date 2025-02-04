import tkinter as tk
from random import randint


# Создаем базовый класс для всех фигур
class Shape:
    def __init__(self, canvas, x, y, size, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    # Метод для обновления позиции фигуры
    def update_position(self, dx, dy):
        self.x += dx
        self.y += dy

    # Абстрактный метод для рисования фигуры
    def draw(self):
        raise NotImplementedError("Метод draw() должен быть реализован в подклассах")


# Класс для круга
class Circle(Shape):
    def __init__(self, canvas, x, y, size, color='blue'):
        super().__init__(canvas, x, y, size, color)

    def draw(self):
        return self.canvas.create_oval(
            self.x - self.size,
            self.y - self.size,
            self.x + self.size,
            self.y + self.size,
            fill=self.color,
            outline=""
        )


# Класс для квадрата
class Square(Shape):
    def __init__(self, canvas, x, y, size, color='green'):
        super().__init__(canvas, x, y, size, color)

    def draw(self):
        return self.canvas.create_rectangle(
            self.x - self.size,
            self.y - self.size,
            self.x + self.size,
            self.y + self.size,
            fill=self.color,
            outline=""
        )


# Функция для запуска анимации
def animate():
    for shape in shapes:
        shape.update_position(randint(-10, 10), randint(-10, 10))
        canvas.coords(shape.id, shape.x - shape.size, shape.y - shape.size, shape.x + shape.size, shape.y + shape.size)
    root.after(100, animate)


# Создание окна приложения
root = tk.Tk()
root.title("Animation with Tkinter")

# Создание холста для рисования
canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Список фигур
shapes = []

# Добавление фигур на холст
for _ in range(20):
    x = randint(50, canvas_width - 50)
    y = randint(50, canvas_height - 50)
    size = randint(10, 30)
    if randint(0, 1) == 0:
        shape = Circle(canvas, x, y, size)
    else:
        shape = Square(canvas, x, y, size)
    shape.id = shape.draw()
    shapes.append(shape)

# Запуск анимации
animate()

# Запуск главного цикла
root.mainloop()