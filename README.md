# **Contracts for Python Functions**

Contracts can be used to validate the input or output of a function. Data flow among components can be hard to keep track or maintained, sometimes forcing us to write print statements everywhere trying to catch malformed data. This contracts library solves this by intercepting data that is piped into or out of a function and checking if they satisfy the specified requirements.


## **Getting Started**

Install contracts through pip.

```console
$ pip3 install contracts
```

Once contracts is installed, you can import the input and output contract decorators, and other convenient qualifier functions.

```py
# Imports ic (input contract) and oc (output contract) 
from contracts import ic, oc

# Examples of some qualifiers
from contracts import natural, integer
```

Refer to  Qualifiers for list of available qualifiers.


## **Contracts**
Input contract is a function decorater that takes in kwargs as a mapping of parameter names to their qualifier(s).

Output contract is another decorator that takes in a single qualifier and checks the result of calling the decorated function.

#### **Using Input Contract**
```py
from contracts import ic, natural

@ic(val = natural)
def func(val):
    return val
```
*func* takes in "val" as a parameter. *ic*'s arguments should correspond to the function's parameter names. In this case, the contract states that arguments for "val" should be natural numbers.

*ic* can take in as many arguments as the number of parameters for the decorated function. All keys should map to the correct parameter names. If the contract is violated, you will get an InputContractException error message listing out the arguments that failed and their given values.

```
contracts.exceptions.InputContractException:
Arguments that failed the contracts
val: -1
```

#### **Using Output Contract**
```py
from contracts import oc, natural

@oc(natural)
def func(val):
    return val
```
*oc* validates the result of calling a function. In this case, it checks that the result is a natural number. The decorator takes a single qualifier. If the contract is violated, the following error will be given.
```
contracts.exceptions.OutputContractException: The result of -1 broke the output contract
```

**Note:** To use both *ic* and *oc*, oc needs to be placed above ic as such:

```py
@oc(natural)
@ic(val = natural)
def func(val):
    return val
```

Otherwise, your code will break. This is definitely something to improve on.


## **Qualifiers**
Qualifiers are functions that take in a single value and return `True` if conditions are satisfied, and `False` otherwise.

For convenience, the contracts library provides a range of basic qualifiers on some data types.

* Numbers: number, positive_number, negative_number
* Integers: integer, natural, positive_integer, negative_integer
* Floats: floating_point, positive_float, negative_float

#### **Composing Multiple Qualifiers**

To compose multiple qualifiers, you can import the *compose* function and pass as many qualifiers as needed to make a single qualifier.

```py
from contracts import natural, positive_integer, compose

@ic(val = compose(natural, positive_integer))
def func(val):
    return val
```

The input contract above will check that the argument for "val" is a natural number and a positive integer.

#### **Custom Qualifiers**
Users of the library can plug in their own qualifiers as long as they adhere to the right data signature. If you're using this library throughout your code base, writing your collection of qualifiers in a separate file will keep things clean.


## **Built With**
Contracts library is built with Python 3.6. Code has been tested only in this version. Compatibility with other versions has not been tested.

Libraries used:
* [inspect](https://docs.python.org/3.6/library/inspect.html)
* [functools](https://docs.python.org/3.6/library/functools.html)
* [pytest](https://docs.pytest.org/en/latest/)


## Author
Gino Jacob - [Github](https://github.com/gvjacob)

Feedback is very much welcomed. Please write issues.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

