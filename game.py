from ursina import * 

class Cube(Entity):
    def __init__(self):
        super().__init__(
            model = "cube",
            color = color.cyan,
            texture = "white_cube",
            rotation = Vec3(45, 45, 45)
        )

class Button(Button):
    def __init__(self):
        super().__init__(
            model = "cube",
            color = color.red,
            texture = "brick",
            parent = scene,
            highlight_color = color.blue,
            pressed_color = color.cyan
        )

    def input(self, key):
        if key == "left mouse down":
            print("sa")

def update():
   pass

app = Ursina()

cube = Cube()
button = Button()

app.run()