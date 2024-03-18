# pycharm_black_magic
## a brief demo of how pycharm magically handles your $PYTHONPATH for you

- pycharm_only solution:  
uses a generic helpers.py on level up from the solution file. PyCharm magically resolves this for us but running from the command line or even other IDEs like vscode will simply fail since the module cannot be found.

## As to pytest see https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html for explanation of imports during pytest.