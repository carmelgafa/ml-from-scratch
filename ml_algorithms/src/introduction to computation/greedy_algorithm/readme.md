# Introduction

Resolution of 0/1 knapsack problem by using a greedy algorithm.

- each value represented by < value, weight > pair
- total weight possible is wk
- vector L of length n representing each set of available items
- boolean vector V of length n indicates whether item is taken

that is, maximize $$\sum_{i=0}^{n-1} V[i]I[i].value$$

such that  $$\sum_{i=0}^{n-1} V[i]I[i].weight \leq w$$

## Brute force

From power set, eliminate all sets greater than w and select best set.

This approach is not very practical.

## Example

Example builds a menu using having a maximum calories constraint using a couple of greedy algorithms having

- user preference (held in the value attribute)
- calories (the inverse thereof)
- a function combining the preference and calories (held in the density attribute)

## Reference

https://www.youtube.com/watch?v=C1lhuz6pZC0
