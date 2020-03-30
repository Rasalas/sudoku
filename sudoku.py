class Cell:
    content = 0
    x = 0
    y = 0

    def __init__(self, content, x, y):
        self.content = content
        self.x = x
        self.y = y
    
    def __str__(self):
        return str(self.content)

    def __repr__(self):
        return str(self.content)

class Board:
    rows, cols = (9, 9)
    cells = []
    empty = '.'

    def __init__(self):
        for x in range(self.cols):
            self.cells.append([])
            for y in range(self.rows):
                cell = Cell(self.empty, x, y)
                self.cells[x].append(cell)
    def __init__(self, arr):
        self.cells = arr

    def printBoard(self):
        s = ""
        for x in range(self.cols):
            for y in range(self.rows):
              print(str(self.cells[x][y]), end = " ")
            print('')
    
    def write(self, content, x, y):
        self.cells[y][x] = content

    def is_in_col(self,x,number):
        for y in range(self.rows):
            if(self.cells[x][y] == number):
                return True
        return False

    def is_in_row(self,y,number):
        for x in range(self.cols):
            if(self.cells[x][y] == number):
                return True
        return False

    def is_in_box(self,x,y,number):
        for i in range(3):
            for j in range(3):
                if(self.cells[x-x%3+i][y-y%3+j] == number):
                    return True
            return False

    def is_legal(self, x, y, number):
        return not self.is_in_col(x, number) and not self.is_in_row(y, number) and not self.is_in_box(x, y, number)

    def solve(self):
        return 0

    

example = [
    [0,2,4,  0,6,0,  0,0,1],
    [0,0,0,  0,0,0,  0,7,9],
    [0,7,1,  0,3,8,  0,0,0],

    [0,0,0,  0,0,3,  5,0,0],
    [0,8,6,  0,5,0,  1,3,0],
    [0,0,5,  1,0,0,  0,0,0],

    [0,0,0,  4,7,0,  6,9,0],
    [1,0,0,  0,9,0,  8,5,0],
    [6,9,0,  0,0,0,  0,0,0],
]

b = Board(example)



b.printBoard()
print(b.is_legal(0,1,5))
print(b.is_legal(0,1,6))


