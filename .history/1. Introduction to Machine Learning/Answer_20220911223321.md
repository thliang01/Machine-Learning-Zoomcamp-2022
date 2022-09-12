### Set up the environment

### Question 1

What's the version of NumPy that you installed?

You can get the version information using the __version__ field:

* 1.21.6

### Question 2

How many records are in the dataset?

Here you need to specify the number of rows.

* 11914

### Question 3

Who are the most popular car manufacturers (top-3) according to the dataset?

* Chevrolet, Ford, Volkswagen

### Question 4

What's the number of unique Audi car models in the dataset?

* 26

### Question 5

How many columns in the dataset have missing values?

* 5

### Question 6

* Find the median value of "Engine Cylinders" column in the dataset.
* Next, calculate the most frequent value of the same "Engine Cylinders".
* Use the fillna method to fill the missing values in "Engine Cylinders" with the most frequent value from the previous step.
* Now, calculate the median value of "Engine Cylinders" once again.

Has it changed?

> Hint: refer to existing mode and median functions to complete the task.

* Yes
### Question 7

* Select all the "Lotus" cars from the dataset.
* Select only columns "Engine HP", "Engine Cylinders".
* Now drop all duplicated rows using `drop_duplicates` method (you should get a dataframe with 9 rows).
* Get the underlying NumPy array. Let's call it `X`.
* Compute matrix-matrix multiplication between the transpose of `X` and `X`. To get the transpose, use `X.T`. Let's call the result `XTX`.
* Invert `XTX`.
* Create an array `y` with values `[1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800]`.
* Multiply the inverse of `XTX` with the transpose of `X`, and then multiply the result by `y`. Call the result `w`.
* What's the value of the first element of `w`?

> **Note**: You just implemented linear regression. We'll talk about it in the next lesson.


* 4.5949
