Python CLI tools
================

pyclitool is a command line utility that allow you to map/filter/reduce your input with a Python one liner, line by line.


Installing:
-----------

    sudo pip install pyclitool


Usage:
------

Here are some powerful examples of what you can do with the `py` command line utility.

Calculate the length of the file names in your current directory:

    ```bash
    ls | py "len(x)"
    ```

Sum a list of numbers using a reduce function:

    ```bash
    echo -n "1\n2\n3\n4\n5\n" | py -r "int(x)+int(y)"
    ```

Filter only lines from a CSV which the sixth column is greater than 3, skipping the header row of the CSV

    ```bash
    cat wine_data.csv | py -s -f "float(x.split(',')[5]) > 3.0"
    ```


Author:
-------

    Ron Reiter <ron.reiter@gmail.com>

