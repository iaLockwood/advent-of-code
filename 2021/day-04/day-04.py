#!/usr/bin/env python3
import sys

class Board:
    """A Bingo Board"""
    def __init__(self, numbers):
        self.rowscols = []
        self.gridmap = {}
        for y in range(len(numbers)):
            row = list(numbers[y].split())
            for x in range(len(row)):
                self.gridmap[row[x]] = (y, x, False)
            self.rowscols.append(row)

    def __str__(self):
        s = 'Board __str__\n'
        for row in self.rowscols:
            annotatedrow = list(row)
            for x in range(len(annotatedrow)):
                (bla, blah, maybemarked) = self.gridmap[row[x]]
                if maybemarked == True:
                    annotatedrow[x] = 'X'
            s += str(row) + '    ' + str(annotatedrow) + '\n'
        s += str(self.gridmap)
        return s

    def number_called(self, n):
        if n not in self.gridmap:
            return -1
        (y, x, marked) = self.gridmap[n]
        self.gridmap[n] = (y, x, True)
        if self.check_for_bingo(n) == True:
            return self.sum_unmarked()
        else:
            return -1

    def check_for_bingo(self, n):
        (y, x, marked) = self.gridmap[n]
        if self.row_bingo(n) == True:
            print('BINGO row')
            return True
        elif self.col_bingo(n) == True:
            print('BINGO column')
            return True
        else:
            return False

    def row_bingo(self, n):
        (y, x, marked) = self.gridmap[n]
        for square in self.rowscols[y]:
            (bla, blah, maybemarked) = self.gridmap[square]
            if maybemarked == False:
                return False
        return True

    def col_bingo(self, n):
        (y, x, marked) = self.gridmap[n]
        for row in self.rowscols:
            (bla, blah, maybemarked) = self.gridmap[row[x]]
            if maybemarked == False:
                return False
        return True

    def sum_unmarked(self):
        total = 0
        for n in self.gridmap.keys():
            (y, x, marked) = self.gridmap[n]
            if marked != True:
                total += int(n)
        return total

def parse_input(filename):
    rawdata = list(map(str.strip, open(filename)))
    drawliststring = rawdata[0:1:]
    drawlist = drawliststring[0].split(',')
#    print(drawlist)
    rawboards = rawdata[1::]
#    print(rawboards)
    x = 0
    boardlist = []
#    print(boardlist)
    while x < len(rawboards):
        boardlist.append(Board(rawboards[x+1:x+6:]))
        x+=6
#    for board in boardlist:
#        print(board)
#        print(board.sum_unmarked())
    return (drawlist, boardlist)

def draw_and_score_first(drawlist, boardlist):
    for n in drawlist:
#        print('...DREW ' + n)
        for b in boardlist:
#            print(b)
            retval = b.number_called(n)
            if retval != -1:
                print(n)
                print(retval)
                finalscore = int(n) * retval
                print('final score: ' + str(finalscore))
                return finalscore
    print('ERROR')
    return 0

def test_example_1(drawlist, boardlist):
    print('...test_example_1: ')
    assert 4512 == draw_and_score_first(drawlist, boardlist)

def part_a(drawlist, boardlist):
    print('...part a: ')
    draw_and_score_first(drawlist, boardlist)

def draw_and_score_last(drawlist, boardlist):
    boardIndex = 0
    maxDraws = 0
    maxDrawsBoardIndex = 0
    savedSum = 0
    for b in boardlist:
        drawIndex = 0
        for n in drawlist:
#            print('...DRAW ' + str(drawIndex) + ' DREW ' + n)
            uncalledSum = b.number_called(n)
            if uncalledSum != -1:
                if drawIndex > maxDraws:
                    maxDraws = drawIndex
                    maxDrawsBoardIndex = boardIndex
                    savedSum = uncalledSum
#                print('maxDraws ' + str(maxDraws))
#                print('maxDrawsBoardIndex ' + str(maxDrawsBoardIndex))
                break
            drawIndex += 1
        boardIndex += 1

    return int(drawlist[maxDraws]) * savedSum

def test_example_2(drawlist, boardlist):
    print('...test_example_2: ')
    assert 1924 == draw_and_score_last(drawlist, boardlist)

def part_b(drawlist, boardlist):
    print('...part b: ... let the squid win ... ')
    print(draw_and_score_last(drawlist, boardlist))

def main():
    (test_drawlist, test_boardlist)= parse_input('day-04-example.txt')
    test_example_1(test_drawlist, test_boardlist)

    (drawlist, boardlist)= parse_input('day-04-input.txt')
    part_a(drawlist, boardlist)
    test_example_2(test_drawlist, test_boardlist)
    part_b(drawlist, boardlist)

    print('done.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
