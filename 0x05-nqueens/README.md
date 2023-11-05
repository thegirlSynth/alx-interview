# N Queens

## The problem is described as follows:

The N queens puzzle is the challenge of placing `N` non-attacking queens on an `N×N` chessboard.

The program [0-nqueens.py](0-nqueens.py) solves the N queens problem.



### Requirements:

* `Usage: nqueens N`
   * If the user called the program with the wrong number of arguments, `Usage: nqueens N` is printed, followed by a new line, and the program exits with the status `1`

* where `N` must be an integer greater or equal to `4`
   * If `N` is not an integer, `N must be a number` is printed, followed by a new line, and the program exits with the status `1`
   * If `N` is smaller than `4`,  `N must be at least 4` is printed, followed by a new line, and the program exits with the status `1`

* The program should print every possible solution to the problem
   * One solution per line
   * Format: see [example](#example)
   * The solutions do not have be printed in a specific order

* Only the sys module can be imported

### [Example](#example)
```
synth@GODS-GIFT:/alx-interview/0x05-nqueens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
synth@GODS-GIFT:/alx-interview/0x05-nqueens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
synth@GODS-GIFT:/alx-interview/0x05-nqueens$
```
