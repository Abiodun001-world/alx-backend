# 0x02. i18n

## Project Description
This project is part of the curriculum at ALX Africa using the Holberton School curriculum. The project is called "0x02. i18n" and is focused on back-end development. The project is about internationalization and localization of web applications.

## Learning Objectives
- Learn how to parametrize Flask templates to display different languages.
- Learn how to infer the correct locale based on URL parameters, user settings, or request headers.
- Learn how to localize timestamps.

## Resources
Read or watch the following resources to prepare for the project:

- [Flask-Babel](https://flask-babel.tkte.ch/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](https://pytz.sourceforge.net/)

## Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
- All your files should end with a new line.
- Your code should use the pycodestyle style (version 2.5).
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- All your *.py files should be executable.
- All your modules should have documentation (run `python3 -c 'print(__import__("my_module").__doc__)'`).
- All your classes should have documentation (run `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All your functions and methods should have documentation (run `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).
- All your functions and coroutines must be type-annotated.

## Project Structure
Please follow this structure for your project:

```
0x02.i18n/
├── models/
│   ├── base.py
│   ├── user.py
│   └── __init__.py
├── main.py
├── templates/
│   ├── 5-index.html
│   └── base.html
└── README.md
```

## How to Run the Project
1. Clone the repository.
2. Navigate to the root of the project folder.
3. Execute `python3 main.py` to run the Flask application.

## How to Test the Project
1. Ensure all the project dependencies are installed.
2. Run the Flask application using `python3 main.py`.
3. Access the application in your web browser.
4. Verify that the application displays different languages based on URL parameters or request headers.
5. Check if the timestamps are localized correctly.

## About the Author
Emmanuel Turlay is a Staff Software Engineer at Cruise. He is an experienced developer with expertise in back-end development and has contributed to the development of this project.

*This project is part of the curriculum at ALX Africa, using the Holberton School curriculum.*
