class NumberRestriction(Exception):
  pass

while True:
  expression = list(input('Введите выражение в польской нотации: ').split( ))
  try:
    if expression == ['q']:
      print('До свидания')
      break
    elif len(expression) != 3:
      raise NumberRestriction('! Программа выполняет вычисления только с двумя числами')
    elif int(expression[1]) < 0 or int(expression[2]) < 0:
      raise NumberRestriction('! Программа выполняет вычисления только с положительными числами')
    else:
      assert str(expression[0]) in ['+', '-', '*', '/'], '! Программа не поддерживает данный оператор'
      if expression[0] == '+':
        result = int(expression[1]) + int(expression[2])
      elif expression[0] == '-':
        result = int(expression[1]) - int(expression[2])
      elif expression[0] == '*':
        result = int(expression[1]) * int(expression[2])
      elif expression[0] == '/':
          result = int(expression[1]) / int(expression[2])
          # try:
          #   result = int(expression[1]) / int(expression[2])
          # except ZeroDivisionError as e:
          #   print(f'{e.__class__.__name__}: {e}')
      print(f'Результат вычисления: {result}')
  except (NumberRestriction, AssertionError) as e:
    print(e)
  except (ZeroDivisionError, ValueError) as e:
    print(f'{e.__class__.__name__}: {e}')