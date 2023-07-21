# 0x00. Pagination - Back-end

## Concepts

For this project, we expect you to look at the following concept:

- Back-end concepts

## Resources

Please read or watch the following resources:

- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to paginate a dataset with simple `page` and `page_size` parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A README.md file, at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All your modules should have documentation (use `python3 -c 'print(__import__("my_module").__doc__)'`).
- All your functions should have documentation (use `python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).
- All your functions and coroutines must be type-annotated.

## Setup: Popular_Baby_Names.csv

Use this data file for your project.

## Tasks

- [Task 0](./0-simple_helper_function.py): Simple helper function.
- [Task 1](./1-simple_pagination.py): Simple pagination.
- [Task 2](./2-hypermedia_pagination.py): Hypermedia pagination.
- [Task 3](./3-hypermedia_del_pagination.py): Deletion-resilient hypermedia pagination.

