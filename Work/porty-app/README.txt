Hi there,
 
This is my first attempt at making an application directory, following a pratical-python
tutorial by @dabeaz (David Beazley) on GitHub.

The 'porty' directory is a python package of a code that is loaded through import.
It contains the following programs;

main programs:
pcost.py          # computes portfolio cost
report.py         # Makes a report
ticker.py         # Produce a real-time stock ticker

supporting modules with other functionality:
stock.py          # Stock class
portfolio.py      # Portfolio class
fileparse.py      # CSV parsing
tableformat.py    # Formatted tables
follow.py         # Follow a log file
typedproperty.py  # Typed class properties

"The 'print-report.py' program is a top-level script that
produces a report.  Try it:

shell % python3 print-report.py portfolio.csv prices.csv txt
      Name     Shares      Price     Change 
---------- ---------- ---------- ---------- 
        AA        100       9.22     -22.98 
       IBM         50     106.28      15.18 
       CAT        150      35.46     -47.98 
      MSFT        200      20.89     -30.34 
        GE         95      13.48     -26.89 
      MSFT         50      20.89     -44.21 
       IBM        100     106.28      35.84 
shell % " - @dabeaz

email: sanusimichael@yahoo.com
Mike-Femi

On windows >py print-report.py porty-app/portfolio.csv porty-app/prices.csv txt