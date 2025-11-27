# 🧮 009: Memory-Efficient Arrays with the `array` Module

The `array` module provides memory-efficient, typed, homogeneous sequences for numbers. Use `array.array` when you need to store millions of numbers and memory matters, or when you need to interface with binary data or C libraries. Lists are more flexible, NumPy arrays are faster for math, but `array.array` is built-in and great for compact storage of numeric data.

## 🎯 Python Array: Practical, Tricky, and Fun Usages

```python
from array import array

def array_usages():
	# ===== 1. Basic Creation & Typecodes =====
	a = array('i', [1, 2, 3])
	b = array('f', [1.0, 2.5, 3.5])
	print(a, b)

	# Typecode reference
	typecodes = {'b': 'signed char', 'B': 'unsigned char', 'u': 'unicode', 'h': 'signed short', 'H': 'unsigned short', 'i': 'signed int', 'I': 'unsigned int', 'l': 'signed long', 'L': 'unsigned long', 'q': 'signed long long', 'Q': 'unsigned long long', 'f': 'float', 'd': 'double'}
	print(typecodes)

	# ===== 2. Accessing & Modifying =====
	print(a[0], b[-1])
	a[1] = 99
	print(a)

	# ===== 3. Methods Playground =====
	a.append(4)
	a.extend([5, 6])
	a.pop()
	a.remove(99)
	print(a)

	# ===== 4. Slicing & Iteration =====
	print(a[1:3])
	for x in a:
		print(x)

	# ===== 5. Conversion Tricks =====
	lst = a.tolist()
	print(lst)
	bytes_data = a.tobytes()
	print(bytes_data)
	a2 = array('i')
	a2.frombytes(bytes_data)
	print(a2)

	# ===== 6. Type Safety & Pitfalls =====
	try:
		a.append(3.14)  # ❌ TypeError
	except TypeError as e:
		print(e)

	# ===== 7. Memory Efficiency =====
	import sys
	big_list = list(range(10**6))
	big_array = array('i', range(10**6))
	print(sys.getsizeof(big_list), big_array.buffer_info())

	# ===== 8. Advanced Usages =====
	# Read from binary file
	# with open('data.bin', 'rb') as f:
	#     arr = array('i')
	#     arr.fromfile(f, 1000)

	# Write to binary file
	# with open('out.bin', 'wb') as f:
	#     big_array.tofile(f)

	# ===== 9. Comparison with List & NumPy =====
	# Lists: flexible, not memory efficient
	# Arrays: memory efficient, typed
	# NumPy: fast math, external lib

	# ===== 10. Fun Tricks =====
	# Reverse array
	print(a[::-1])
	# Array identity
	print(array('i') is array('i'))

array_usages()
```