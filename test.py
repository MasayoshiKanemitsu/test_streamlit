from unittest import result
import pandas as pd

df = pd.read_csv()

a = 1
b = 5
print(a + b)

x = ['aaa',
    'bbb',
    'ccc']

def hello(x: str, y: int) -> str:
  """_summary_

  Args:
      x (str): _description_
      y (int): _description_

  Returns:
      str: _description_
  """
  return f'{x}は{y}円です'

def func1(x,y):
  return x + y

result1 = func1(1,4)
result2 = func1(1,3)