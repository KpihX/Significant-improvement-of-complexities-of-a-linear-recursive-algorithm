def evalSeqRec(n: int, seq: callable, start: int, init: list[float]) -> float:
	"""
	Evaluate a linear recursive sequence of arbitrary order using a recursive approach with O(n) time complexity and O(1) space complexity.

	Args:
		n (int): The index of the term in the sequence to evaluate.
		seq (callable): A function that takes as input a list of values representing the current term and the previous terms in the sequence, and returns the next term in the sequence.
		start (int): The index of the first term in the sequence for which the initial values are provided.
		init (List[float]): A list of the initial values of the sequence, up to the start index.

	Returns:
		float: The value of the nth term in the sequence.

	Example:
		>>> def seq_test(values):
		...     return values[0] + sum(values[1:])
		...
		>>> n = 10
		>>> init = [3, 1, 2]
		>>> evalSeqRec(n, seq_test, 2, init)
		277
	"""

	global Previous
	l = len(init)
	m = n - start

	# If n is equal to the last index of the initial values, return the last initial value
	if m == l-1:
		Previous = init[:-1]
		return init[-1]

	# If n is within the range of the initial values, return the corresponding initial value
	if 0 <= m <= l-2:
		return init[m]

	# Otherwise, recursively evaluate the sequence
	x = evalSeqRec(n-1, seq, start, init)
	y = seq([n] + Previous + [x])
	Previous = Previous[1:] + [x]
	return y

#Test

def seq_test(Values: list[float]) -> float:
	"""
	Example function that can be used as the recursive function Un = n + U(n-1) + U(n-2) + U(n-3).

	Args:
		values (List[float]): A list of values representing the current term and the previous terms in the sequence.

	Returns:
		float: The next term in the sequence.
	"""
	return sum(Values)

n = 10
init = [3, 1, 2]
print(evalSeqRec(n, seq_test, 2, init)) # output 277