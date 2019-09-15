import random
import copy
import os
import time
import keyboard

SNAKE_BODY = 'o'
FOOD_CHAR = '$'

DIMENSIONS = 20
ITERATIONS = 1000
FRAMERATE = 5

# DIRECTIONS
LEFT = 'a'
RIGHT = 'd'
TOP = 'w'
BOTTOM = 's'


def clear():
    os.system('clear')


def cloneBoard(board):
    return copy.copy(board)


def generateBoard():
    board = [[None for j in range(DIMENSIONS)] for i in range(DIMENSIONS)]
    return board


def findOptimalFoodCoords(snakeX, snakeY):
    x = snakeX
    y = snakeY

    while(x is snakeX and y is snakeY):
        x = random.randint(0, DIMENSIONS - 1)
        y = random.randint(0, DIMENSIONS - 1)

    return x, y


def initBoard():
    board = generateBoard()
    midIndex = int(DIMENSIONS / 2)  # Put the snake head in the middle
    foodX, foodY = findOptimalFoodCoords(midIndex, midIndex)

    board[midIndex][midIndex] = SNAKE_BODY
    board[foodX][foodY] = FOOD_CHAR

    return board, (foodX, foodY), (midIndex, midIndex)


def renderBoard(board):
    for row in board:
        _rowStr = '|'
        for item in row:
            if item is None:
                _rowStr += '  '
            else:
                _rowStr += item + ' '

            _rowStr += ' '

        _rowStr += '|'

        print(_rowStr)


def nextFrame(board, dir, foodCoords):
    snakeXPosition = 0
    snakeYPosition = 0
    foodX = foodCoords[0]
    foodY = foodCoords[1]
    nextBoard = generateBoard()

    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):
            if board[i][j] is SNAKE_BODY:
                snakeYPosition = i
                snakeXPosition = j
                break

    nextX = snakeXPosition
    nextY = snakeYPosition

    if dir is LEFT:
        nextX = (nextX - 1) % DIMENSIONS
    elif dir is RIGHT:
        nextX = (nextX + 1) % DIMENSIONS
    elif dir is TOP:
        nextY = (nextY - 1) % DIMENSIONS
    elif dir is BOTTOM:
        nextY = (nextY + 1) % DIMENSIONS

    if nextX is foodX and nextY is foodY:
        foodX, foodY = findOptimalFoodCoords(nextX, nextY)

    nextBoard[nextY][nextX] = SNAKE_BODY
    nextBoard[foodX][foodY] = FOOD_CHAR
    return nextBoard, (foodX, foodY), (nextX, nextY)


def main():
    board, foodCoords, snakeCoords = initBoard()
    dir = BOTTOM  # Set initial direction

    i = 0
    while(i < ITERATIONS):
        try:
            if keyboard.is_pressed(LEFT):
                dir = LEFT
            elif keyboard.is_pressed(RIGHT):
                dir = RIGHT
            elif keyboard.is_pressed(TOP):
                dir = TOP
            elif keyboard.is_pressed(BOTTOM):
                dir = BOTTOM
        except:
            pass

        clear()
        print('Current DIR=' + dir + " Food coord=(" + str(foodCoords[0]) + "," + str(
            foodCoords[1]) + ")", " Snake coord=(" + str(snakeCoords[0]) + "," + str(snakeCoords[1]) + ")")
        renderBoard(board)
        board, foodCoords, snakeCoords = nextFrame(board, dir, foodCoords)
        time.sleep(1.0 / FRAMERATE)
        i += 1


if __name__ == "__main__":
    main()
