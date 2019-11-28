# Closest to zero
[![codecov](https://codecov.io/gh/zbgn/GoJob_Test/branch/master/graph/badge.svg)](https://codecov.io/gh/zbgn/GoJob_Test)
[![Build Status](https://travis-ci.org/zbgn/GoJob_Test.svg?branch=master)](https://travis-ci.org/zbgn/GoJob_Test)

Write a function “closestToZero” described by the following specification:

given an array of positive and negative integers, it returns the closest number to zero
if the closest number in input could be either negative or positive, the function returns the positive one
if the input array is undefined or empty, the function returns 0

Examples:

```
when input is [8, 5, 10] it must returns 5
when input is [5, 4, -9, 6, -10, -1, 8] it must return -1
when input is [8, 2, 3, -2] it must return 2
```