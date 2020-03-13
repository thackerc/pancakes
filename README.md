# Revenge of the Pancakes

## Challenge Description

The Revenge of the Pancakes challenge description can be found [here](./challenge.pdf).

## Explanation

A simple way to describe an optimal algorithm for flipping all pancakes to be face up is to view the stack as 1 or more groups of pancakes all facing in the same direction. Groups are defined by 1) edges - the top/bottom of the stack, or 2) boundaries - between two pancakes that face opposite directions (i.e., a sequence  of "-+" or "+-").

To accomplish the task of getting all the pancakes facing up we start at the top of the stack and move down until we find the first boundary. By flipping this top group we effectively merge the first and second group of pancakes. We continue by simply repeating this process of flipping top group to merge it with the next group until we have only one group, i.e., the whole stack.

If the resulting stack is facing up we are done. Otherwise we give the full stack on final flip. One way to eliminate this final step is to simply add a face up pancake to the bottom of the stack before any flips have been performed. Doing this will ensure that all the pancakes are face up without explicitly checking for that state, and will not change the total number of flips required to accomplish the task.

The assignment is to calculate this number of flips needed to get all the pancakes face up. Given the above algorithm I would do this by adding a face up pancake "+" to the bottom of each stack and then counting the number group boundaries in the stack. This sum is the same as the number of flips need to serve a happy stack of pancakes all facing up.

## Running the Solution

From the root of the project directory run [pancakes.py](./pancakes.py) on the command line by:

```
cat input/basic.in | python3 pancakes.py
```

## Disclaimer

This assignment is [Problem B](https://code.google.com/codejam/contest/6254486/dashboard#s=p1&a=1) taken from the 2016 Google Code Jam. The method I used is informed by the work done by others. Code and explanation are my own.
