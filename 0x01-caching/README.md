# 0x01. Caching

## Background Context
In this project, you will learn about different caching algorithms.

## Resources
Read or watch:
- [Cache replacement policies](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29) - FIFO
- [Cache replacement policies](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29) - LIFO
- [Cache replacement policies](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29) - LRU
- [Cache replacement policies](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29) - MRU
- [Cache replacement policies](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29) - LFU

## Learning Objectives
By the end of this project, you are expected to be able to explain the following topics without the help of Google:

**General**
- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system is
- What limits a caching system has

## Requirements
**Python Scripts**
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not just a simple word; it should be a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)

## More Info
**Parent class BaseCaching**
All your classes must inherit from the `BaseCaching` class defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data is stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item to the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

