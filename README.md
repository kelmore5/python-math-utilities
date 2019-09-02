# Math

Math is a small library of math utility functions compiled for personal needs. There's 
nothing too fancy nor anything you can't find from another library, but Math consists of
smaller functions to be used rather than relying on larger packages.

Functions include things like fibonacci, simple trig, triangles, some statistical math, etc.

## Personal Note

Math is only on Github because I reference it in other projects. I don't have any plans 
to maintain this project, but I will update it from time to time. 

# Install

You can install this project directly from Github via:

```bash
$ pip3.7 install git+https://github.com/kelmore5/python-math-utilities.git
```

## Dependencies

- Python 3.7

# Usage

Once installed, you can import the main class like so:

    >>> from kelmore_math import MathTools as Math
    >>>
    >>> Math.factorial(5)               # 120
    >>> Math.fibonacci(9)               # 34
    >>> Math.check.is_even(22)          # True
    >>> Math.prime.prime_factors(34)    # [2, 17]
    >>> Math.weather.to_celsius(32)     # 0
    .
    .
    .

# Documentation

To be updated