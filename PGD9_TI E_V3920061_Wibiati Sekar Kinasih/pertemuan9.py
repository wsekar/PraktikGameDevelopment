from direct.showbase.ShowBase import ShowBase


class Window(ShowBase):
    def __init__(self):
        super().__init__()

        asteroid = self.loader.loadModel("models/nik-dragon")
        asteroid.setPos(0, 10, 0)
        asteroid.setScale(0.2, 0.2, 0.2)
        asteroid.reparentTo(self.render)


game = Window()
game.run()
