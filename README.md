# Complex-numbers-in-the-real-plane
the idea is that the generator generates all polinomials up to degree 10 with coefficients ranging from ranges -10 to 10, and inserts them into a file
then axDrawer uses that file to represent the roots of whatever polinomials you tell it to

The file is a dictionary where the keys are g1, g2, g3... for each degree from 1 to 10.
the values of these keys are also dictionaries, with keys c1,c2,3... for each coefficient from 1 to 10
and the value of THOSE keys, is a list of lists, where the first element holds all the real parts of the roots and the second element
holds all the imaginary parts of the roots
