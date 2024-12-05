#1. Import the NUMPY package under the name np.

import numpy as np


#2. Print the NUMPY version and the configuration.

print("NumPy Version:", np.__version__)
print("NumPy Configuration:")
np.show_config()


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.rand(2, 3, 5)

print("\nArray a:\n", a)



#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5, 2, 3))

#6. Print b.

print("\nArray b:\n", b)

#7. Do a and b have the same size? How do you prove that in Python code?

same_size = a.size == b.size
print("\nDo a and b have the same size?", same_size)

#8. Are you able to add a and b? Why or why not?

try:
    c = a + b
except ValueError as e:
    print("\nAddition not possible:", e)


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1, 2, 0)
print("\nTransposed b (Array c):\n", c)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c
print("\nArray d (a + c):\n", d)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print("\nArray a:\n", a)
print("\nArray d:\n", d)
# Explanation: d is the result of adding 1 (from c) to each element of a.

#12. Multiply a and c. Assign the result to e.

e = a * c
print("\nArray e (a * c):\n", e)


#13. Does e equal to a? Why or why not?

is_equal = np.array_equal(e, a)
print("\nDoes e equal to a?", is_equal)
# Explanation: Yes, because multiplying by 1 does not change the original values.

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print("\nMax value in d:", d_max)
print("Min value in d:", d_min)
print("Mean value in d:", d_mean)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty_like(d)
print("\nEmpty array f:\n", f)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            if d[i, j, k] == d_min:
                f[i, j, k] = 0
            elif d[i, j, k] == d_max:
                f[i, j, k] = 100
            elif d_min < d[i, j, k] < d_mean:
                f[i, j, k] = 25
            elif d[i, j, k] == d_mean:
                f[i, j, k] = 50
            elif d_mean < d[i, j, k] < d_max:
                f[i, j, k] = 75




"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

print("\nArray d:\n", d)
print("\nArray f (labeled):\n", f)



"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            if d[i, j, k] == d_min:
                f_str[i, j, k] = "A"
            elif d[i, j, k] == d_max:
                f_str[i, j, k] = "E"
            elif d_min < d[i, j, k] < d_mean:
                f_str[i, j, k] = "B"
            elif d[i, j, k] == d_mean:
                f_str[i, j, k] = "C"
            elif d_mean < d[i, j, k] < d_max:
                f_str[i, j, k] = "D"

print("\nArray f (with strings):\n", f_str)