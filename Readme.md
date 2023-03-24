# Amelioration of Recursive Evaluation of Linear Sequences in terms of Complexity

This repository contains a Python implementation of a recursive function that evaluates a linear sequence up to a given order n. The function has a time complexity of O(n) and a space complexity of O(1).

## Table of Contents

- Introduction
- Principle
- Examples
- Conclusion

# Introduction

A sequence can be defined as an ordered list of numbers. Recursive functions can be used to evaluate sequences by using the previous terms to compute the next term. However, naive recursive functions can have a time complexity of O(2^n) and a space complexity of O(n) which can become unmanageable for large values of n. The evalSeqRec function presented in this repository implements a clever strategy that enables it to evaluate sequences up to a given order n in O(n) time and O(1) space.

## Principle

The function evalSeqRec(n, seq, start, init) evaluates a linear recursive sequence of arbitrary order using a recursive approach with a time complexity of O(n) and a space complexity of O(1). The function takes the following parameters as input:

- `n` (int): the index of the term in the sequence to be evaluated.
- `seq` (callable): a function that takes a list of values representing the current term and the previous terms in the sequence as input, and returns the next term in the sequence.
- `start` (int): the index of the first term in the sequence for which initial values are provided.
- `init` (List[float]): a list of initial values of the sequence, up to the starting index.

The evalSeqRec function starts by initializing a global variable Previous to an empty list. Then, the length of the init list is stored in a variable l, and the difference between n and start is stored in a variable m. If n is equal to the index of the last initial value, the last initial value is returned. If n is between 0 and l-2, the corresponding initial value is returned. Otherwise, the function recursively calls evalSeqRec to evaluate the previous term x and the seq function to compute the next term y. The Previous list is then updated with the last value of x, and y is returned.


## Example

In this example, we use the seqTest sequence which is defined as follows:
Un = n + U(n-1) + U(n-2) + U(n-3)
The function seqTest() calculates the next term in the sequence using the sum of the previous terms. The evalSeqRec() function then uses this function to recursively compute the terms of the sequence up to the nth term.

```python
def seq_test(values):
    return values[0] + sum(values[1:])

n = 10
init = [3, 1, 2]
print(evalSeqRec(n, seq_test, 2, init)) # Output: 277
```

## Conclusion

In conclusion, the evalSeqRec function presented in this repository offers a clever strategy for evaluating sequences up to a given order n in O(n) time and O(1) space complexity. The function avoids storing all previous terms in memory and instead only stores the necessary previous terms. This approach can be useful in cases where the sequence becomes unmanageable for large values of n.

It should be noted that a similar result in terms of complexity can be obtained by derecursivizing the sequence and using iterations. However, this project aimed to improve the iterative approach and present a new way of looking at the problem.

Any suggestions for improving the function or the code in general are welcome.