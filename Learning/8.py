# Errors and Exception Handling in Python 















# video 1 :Errors

#print("hello world"  # invalid Syntax error 
# print("hello) # scanning string literal 
# If x > 10: # indentation error
#     print("x is greater than 10")  # usbing both tab and space 

















# video 2 : Exception 

# print(int("basith")) # ValueError
# print("15" + 2) # TypeError
# print (a+b ) # NameError
# a = 5
# b = 10











# video 3 : Built-in Exceptions


# BaseException
#  ├── BaseExceptionGroup
#  ├── GeneratorExit
#  ├── KeyboardInterrupt
#  ├── SystemExit
#  └── Exception
#       ├── ArithmeticError
#       │    ├── FloatingPointError
#       │    ├── OverflowError
#       │    └── ZeroDivisionError
#       ├── AssertionError
#       ├── AttributeError
#       ├── BufferError
#       ├── EOFError
#       ├── ExceptionGroup [BaseExceptionGroup]
#       ├── ImportError
#       │    └── ModuleNotFoundError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── MemoryError
#       ├── NameError
#       │    └── UnboundLocalError
#       ├── OSError
#       │    ├── BlockingIOError
#       │    ├── ChildProcessError
#       │    ├── ConnectionError
#       │    │    ├── BrokenPipeError
#       │    │    ├── ConnectionAbortedError
#       │    │    ├── ConnectionRefusedError
#       │    │    └── ConnectionResetError
#       │    ├── FileExistsError
#       │    ├── FileNotFoundError
#       │    ├── InterruptedError
#       │    ├── IsADirectoryError
#       │    ├── NotADirectoryError
#       │    ├── PermissionError
#       │    ├── ProcessLookupError
#       │    └── TimeoutError
#       ├── ReferenceError
#       ├── RuntimeError
#       │    ├── NotImplementedError
#       │    ├── PythonFinalizationError
#       │    └── RecursionError
#       ├── StopAsyncIteration
#       ├── StopIteration
#       ├── SyntaxError
#       │    └── IndentationError
#       │         └── TabError
#       ├── SystemError
#       ├── TypeError
#       ├── ValueError
#       │    └── UnicodeError
#       │         ├── UnicodeDecodeError
#       │         ├── UnicodeEncodeError
#       │         └── UnicodeTranslateError
#       └── Warning
#            ├── BytesWarning
#            ├── DeprecationWarning
#            ├── EncodingWarning
#            ├── FutureWarning
#            ├── ImportWarning
#            ├── PendingDeprecationWarning
#            ├── ResourceWarning
#            ├── RuntimeWarning
#            ├── SyntaxWarning
#            ├── UnicodeWarning
#            └── UserWarning




                                           # common errors
# SyntaxError — Raised when a statement uses the wrong syntax.

# TypeError — Raised when an operation or function is applied to an object of an inappropriate type.

# ValueError — Raised when an operation or function receives an argument with an inappropriate value.

# OSError — Raised when a system function returns a system-related error.

# ImportError — Raised when the imported library or module is not found.

# EOFError — Raised when input() reaches end-of-file without reading any data.

# NameError — Raised when a local or global name is not found.

# IndexError — Raised when a sequence subscript is out of range.




















# video 4 : Exception Handling 






integer = "value"

# print(int(integer)) # error is ahppening


# so we use try except method 


try:


    print(int(integer)) # error is ahppening

except ValueError as e: # cleanly manager error 
    
    
     # we can also use except Exception as e: to handle all types of errors
    print(e)
    # pass # it will ignore the error and continue the program

else: 
    print("else block") # it will execute if there is no error and if try works
finally: 
    print("finally block") # it will always execute