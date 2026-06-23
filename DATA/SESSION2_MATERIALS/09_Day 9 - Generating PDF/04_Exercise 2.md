# Exercise 2

Type: Exercise

Use the `reportlab` library to generate the PDF with the title page of the report:

- in a larger font, in 1/3 of the page height and with a margin on the left, place the title of the report (if you don't have an idea for it, just put "Report Title"),
- in 2/3 of the page height and with the same margin as the title, put your name,
- just below the name and surname, in smaller font, add "Copyright `[YEAR]` Company Name. All rights reserved." Do not enter a fixed year, use the `datetime` module to get the current year instead.

As before, each caption should be created with a separate call to the 'drawString' method.
