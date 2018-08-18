Python CLI tools
================

pyclitools is a set of command line utilities that allow you to map/reduce your input with a Python one liner, line by line.


Installing:
-----------

    sudo pip install pyclitool


Usage:
------

    Here are some powerful examples of what you can do with the `pmap` and `preduce` command line utilities.

    Calculate the length of the file names in your current directory:
    ```
    ls | py "len(x)"
    ```

    Sum a list of numbers using a reduce function:
    ```
    echo -n "1\n2\n3\n4\n5\n" | py -r "int(x)+int(y)"
    ```

    Filter only lines from a CSV which the sixth column is greater than 3, skipping the header row of the CSV
    ```
    cat wine_data.csv | py -s -f "float(x.split(',')[5]) > 3.0"
    ```


Author:
-------

    Ron Reiter <ron.reiter@gmail.com>

