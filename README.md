# pycharm_black_magic
## a brief demo of how pycharm magically handles your $PYTHONPATH for you

- pycharm_only solution:  
uses a generic helpers.py one level up from the solution file. Pycharm magically resolves this because its default setting adds the project root to the PYTHONPATH. This can be seen by printing out the sys.path once in pycharm and comparing with the result of the same command when solution.py is run in vscode or from a terminal.

see: https://stackoverflow.com/questions/71594141/modulenotfounderror-happening-in-vscode-but-not-in-pycharm

for explanation although this solution does not seem to work

- works_everywhere  
simply solves the puzzle in a python script. To demonstrate that this (non-root level) directory has been added to the PYTHONPATH (trivial though this is) a helper module is used to show that this import does work.

## running from terminal
- this will not print the highest level commands i.e. print("f{sys.modules=}")  
`python -m pycharm_only/solution.py`

- running without the -m will  
`python pycharm_only/solution.py`
