#!/usr/bin/env python3

class Compute:

    def __init__(self) -> None:
        pass

    def addNInts(self, n) -> int: 
        sum = 0 
        for i in range(n):
            sum = sum + i
        return sum
    
    def mul2Ints(self, a, b) -> int: 
        return a*b
    

