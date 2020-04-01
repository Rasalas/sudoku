# Sudoku

This Python program is going to be able to create entirely new Sudokus and solve them.

## Solving Sudokus
To test it, you have to import the `python.py` file first. 
If you are in the same folder, just write:
```python
import sudoku
```

Now you can use this unsolved example Sudoku:

```python
>>> example = [
		[0,2,4,	 0,6,0,  0,0,1],
		[0,0,0,  0,0,0,  0,7,9],
		[0,7,1,  0,3,8,  0,0,0],

		[0,0,0,  0,0,3,  5,0,0],
		[0,8,6,  0,5,0,  1,3,0],
		[0,0,5,  1,0,0,  0,0,0],

		[0,0,0,  4,7,0,  6,9,0],
		[1,0,0,  0,9,0,  8,5,0],
		[6,9,0,  0,0,0,  0,0,0],
	]
```
Create a board:
```python
>>> b = sudoku.Board(example)
```
Print the still unsolved Sudoku board with:

```python
>>> b.printBoard()

. 2 4 . 6 . . . 1
. . . . . . . 7 9
. 7 1 . 3 8 . . .
. . . . . 3 5 . .
. 8 6 . 5 . 1 3 .
. . 5 1 . . . . .
. . . 4 7 . 6 9 .
1 . . . 9 . 8 5 .
6 9 . . . . . . .
```
Now you probably want to `solve_it`:
```python
>>> b.solve_it()
```
Now print it again to check the solved board:
```python
>>> b.printBoard()

5 2 4 7 6 9 3 8 1
3 6 8 5 1 4 2 7 9
9 7 1 2 3 8 4 6 5
7 1 9 6 4 3 5 2 8
4 8 6 9 5 2 1 3 7
2 3 5 1 8 7 9 4 6
8 5 2 4 7 1 6 9 3
1 4 7 3 9 6 8 5 2
6 9 3 8 2 5 7 1 4
```

### TODO:
- `create()` method that creates an entirely new Sudoku
- `sieve(percent)` function that deletes enough of the right cells to make the Sudoku more difficult
- function to create 'seeds' from new Sudokus
- functions to create several Sudokus from one 'seed'

#### Maybe later:
- make performance optimization
- add my own solving algorithm
- GUI
- same thing in JS for easier "installation" + animations about what is happening
