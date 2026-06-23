# Exercise 1

Type: Exercise

With the `reportlab` library generate a PDF with a multiplication table of the numbers from0 to 10 (inclusive). Make the row and column headers - factors - in bold font; do not use bold for the multiplication products.

In this exercise each number should be drawn with an individual call of the `drawString` method. If you want, you can also draw the corresponding lines to get an array-like effect.

**Hint:**

Create nested **for** loops: outer one with the `x` variable and the inner one with `y` (or the other way round if you want). Use these variables both to calculate the results of multiplication and to calculate where on the page this number should appear.
