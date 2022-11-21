# Documentation that is also being unit tested.

Documentation can get out of sync since developers are mainly focused on delivering features.
To solve this issue, I added `mktestdocs` to test out code.

## How to create such blocks?

You have to provide a self-contained example (Import everything that you need).

(Hint: View Raw .md file to see how you can add python documentation)

```python

a = 3
b = 5

assert a + b == 8

```

## How to test ?

Run `pytest tests/test_docs`