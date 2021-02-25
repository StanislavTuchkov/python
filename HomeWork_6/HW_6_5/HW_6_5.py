class Stationary:

    def __init__(self, title='drawing'):
        self.title = title
class Pen(Stationary):
    def draw(self):
        print(f'Start {self.title} with pen...')
class Pencil(Stationary):
    def draw(self):
        print('Start drawing with pencil...')
class Handle(Stationary):
    def draw(self):
        print('Start drawing handle...')


b = Pen()
b.draw()
c = Pencil()
c.draw()
d = Handle()
d.draw()