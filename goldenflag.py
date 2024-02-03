class Gold:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = -10
        self.dy = 0


    def update(self):
        self.x += self.dx
        self.y += self.dy

        return self.x, self.y 

    def move(self, x, y):
        self.x = x
        self.y = y

     


        

