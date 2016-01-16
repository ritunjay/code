"""
Info about this doc
"""
print globals()
#{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', 
#'__file__': '/home/user/workspace/code/modules/global_and_local.py', 
#'__doc__': '\nInfo about this doc\n', '__package__': None}

i = 1
def fun():
    print "fun"
print globals() 
#{'__builtins__': <module '__builtin__' (built-in)>,'__name__': '__main__', 
#'__file__': '/home/user/workspace/code/modules/global_and_local.py', 
#'__doc__': '\nInfo about this doc\n','__package__': None, 
### ** ###'i': 1, 'fun': <function fun at 0x7f5bf0be2f50>, 
# }

del i
print globals()
#{'__builtins__': <module '__builtin__' (built-in)>, 
#'__file__': '/home/user/workspace/code/modules/globals_var.py', 
#'__package__': None, 
#'fun': <function fun at 0x7fc38ea73f50>, 
#'__name__': '__main__', '__doc__': '\nInfo about this doc\n'}
del fun
print globals()
#{'__builtins__': <module '__builtin__' (built-in)>, 
#'__file__': '/home/user/workspace/code/modules/globals_var.py', 
#'__package__': None, '__name__': '__main__', 
#'__doc__': '\nInfo about this doc\n'}








#### __builtins__
dir(globals()['__builtins__'])
#['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 
#'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 
#'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 
#'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 
#'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 
#'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 
#'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 
#'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 
#'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 
#'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 
#'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__',
# '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 
#'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 
#'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 
#'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 
#'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 
#'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 
#'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 
#'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 
#'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 
#'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
from info_module import info
info(globals()['__builtins__'],html=1, file_name="builtins.html")

