from concurrent.futures import ThreadPoolExecutor

def task_1():
  print("Task 1 is executed")

def task_2():
  print("Task 2 is executed")

with ThreadPoolExecutor() as executor:
  future1 = executor.submit(task_1)
  future2 = executor.submit(task_2)