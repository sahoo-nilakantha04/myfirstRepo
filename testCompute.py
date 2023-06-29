#!/usr/bin/env python3

from compute import Compute

n = 10 

a = 4
b = 5

comp = Compute()

# test add functionality
sum = comp.addNInts(n)
print(f"sum of first {n} int is = {sum}")

# test multiply functionality
mul = comp.mul2Ints(a, b)
print(f"Multiply of {a}x{b} = {mul}")
