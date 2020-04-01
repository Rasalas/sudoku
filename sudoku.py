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

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getContent(self):
        return self.content

    def setContent(self, content):
        self.content = content

class Board:
    rows, cols = (9, 9)
    cells = []
    empty = '0'

    def __init__(self):
        for x in range(self.cols):
            self.cells.append([])
            for y in range(self.rows):
                cell = Cell(self.empty, x, y)
                self.cells[x].append(cell)

    def __init__(self, arr):
        for x in range(self.cols):
            self.cells.append([])
            for y in range(self.rows):
                self.cells[x].append(Cell(arr[y][x],x,y))


    def printBoard(self):
        for x in range(self.cols):
            for y in range(self.rows):
                s = str(self.cells[y][x])
                if s == "0" : s= "."
                print(s, end = " ")
            print('')
        print('')
    
    def getCell(self, x, y):
        return self.cells[x][y]

    def write(self, content, x, y):
        self.cells[x][y].setContent(content)

    def is_in_col(self,number, x):
        for y in range(self.rows):
            cell = self.getCell(x,y)
            if(cell.getContent() == number):
                return True
        return False

    def is_in_row(self, number, y):
        for x in range(self.cols):
            cell = self.getCell(x,y)
            if(cell.getContent() == number):
                return True
        return False

    def is_in_box(self, number, x, y):
        for i in range(3):
            for j in range(3):
                cell = self.getCell(x-x%3+i,y-y%3+j)
                if(cell.getContent() == number):
                    return True
        return False

    def is_legal(self, number, x, y):
        return not (self.is_in_col(number, x) or self.is_in_row(number, y) or self.is_in_box(number, x, y))

    def next_cell(self, cell):
        x = cell.getX()
        y = cell.getY()

        x += 1

        if(x > self.cols-1):
            x = 0
            y += 1
        
        if(y > self.rows-1):
            return None

        return self.getCell(x,y)
    
    def solve(self, cell):

        if(cell == None): 
            return True # last cell
        
        if(cell.getContent() != 0):
            return self.solve(self.next_cell(cell)) # cell not empty

        for i in range(1,self.cols+1): # go through all legal possibilities
            if(not self.is_legal(i, cell.getX(), cell.getY())): continue

            self.write(i, cell.getX(), cell.getY())
            solved = self.solve(self.next_cell(cell))
            if (solved):
                return True
            else:
                self.write(0,cell.getX(), cell.getY())
        return False
    
    def solve_it(self):
        self.solve(self.getCell(0,0))
    

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

b.solve_it()

b.printBoard()




