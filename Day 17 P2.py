from operator import lshift
from operator import rshift
from itertools import cycle, count

class tetris:
    def __init__(self, nums, shape, pos = 0b0010000):
        self.nums = nums
        self.len = len(self.nums)
        self.shape = shape
        self.pos = pos
    
    def shift(self, char):
        if char == '>':
            return tetris(([rshift(i, 1) for i in self.nums]), self.shape, rshift(self.pos, 1))
        elif char == '<':
            return tetris(([lshift(i, 1) for i in self.nums]), self.shape, lshift(self.pos, 1))

    def shiftpossible(self, char):
        if char == '>':
            for i in self.nums:
                if i & 0b0000001:
                    return False
        if char == '<':
            for i in self.nums:
                if i & 0b1000000:
                    return False
        return True
    
    def overlap(self, stack):
        for i, layer in zip(self.nums, stack):
            if i & layer:
                return True
        return False

minos = (
    tetris((0b0011110,), 'bar'),
    tetris((0b0001000,
            0b0011100,
            0b0001000), 'cross'),
    tetris((0b0000100,
            0b0000100,
            0b0011100), 'backL'),
    tetris((0b0010000,
            0b0010000,
            0b0010000,
            0b0010000), 'line'),
    tetris((0b0011000,
            0b0011000), 'o'))

with open('Inputs/input17') as file17:
    jets = [char for char in file17.read()]
    stack = [0] * 10000
    top, height, prev_height = 0, 0, 0

    mino = cycle(minos)
    jet = cycle(jets)
    minoCount, jetCount = 0, 0
    states = {}

    while True:
        currMino = next(mino)
        minoCount += 1
        if minoCount == 20000: #Edit this number for the amount of minos you want to check.
            break

        #Loop - We shift left or right and then down if either are possible
        for y in count(top + currMino.len + 3):
        #Move every row of the mino left or right if possible
            char = next(jet)
            #there are 10091 jets in the input
            jetCount = (jetCount + 1) % 10091


            if currMino.shiftpossible(char):
                shiftedMino = currMino.shift(char)
                if not shiftedMino.overlap(stack[0:y:-1]):
                    currMino = shiftedMino
            
        #shift the mino down the stack if it will not overlap.
            if currMino.overlap(stack[0:y:-1]) or currMino.len + y <= 0:
                for i in range(currMino.len):
                    stack[y - i] += currMino.nums[i]
                    
                break
        top = max(top, y)
        height = top

        state = (jetCount, currMino.shape, currMino.pos)
        if state in states.keys():
            oldstate = states[state]
            rockCycle =  minoCount - oldstate[0]
            heightCycle = height - oldstate[1]
            diff = 1e12 - minoCount
            quotient, remainder = divmod(diff, rockCycle)
            if remainder == 0:
                print(heightCycle * quotient + height)
                break

        else: 
            states[state] = (minoCount, height)


    
