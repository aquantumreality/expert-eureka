# Broken Sticks and Triangles

The following is a classic toy problem in probability theory, and serves as a wonderful technical interview question for Data Science and Machine Learning roles. The question is as follows:

The question we have at hand is as follows:

**You have a stick of arbitrary length. You break the stick uniformly at random along it’s length at two places, leaving you with three distinct pieces. What is the probability that you can form a triangle with the resulting three pieces?**

We will first solve this problem, and then simulate the problem to verify our findings.

**Solution**: 

Let us say the stick has unit length. Now we break the stick uniformly at random along it’s length at two places, leaving us with three pieces. Note that because we have defined the total length as 1, only two variables a and b are required to fully specify the lengths of the resulting three pieces. The first piece is of length a, second piece of length b, and third piece of length 1-a-b.

Note that each piece can range in length from 0 to 1, with the condition that the three pieces sum to 1. Now we have to check whether our three pieces form a triangle? Let us recall the geometric conditions required of all triangles: each side of a triangle is strictly less than the sum of the other two sides. Therefore we can specify three distinct boundary conditions required to form a triangle from the three pieces:

![boundary](https://github.com/aquantumreality/sticks-and-stuff/blob/main/assets/boundary-conditions.png)

Let us overlay the three boundary conditions above on our probability space to determine the values for a and b for which we can form a triangle:

![](https://github.com/aquantumreality/sticks-and-stuff/blob/main/assets/prob.png)

We can see from the figure above that the boundary conditions specify 1/4 of the total probability space. Therefore, we can conclude there is a 1/4 probability that the three broken pieces will form a triangle. Now, let us now simulate this problem computationally in python to confirm our answer.
