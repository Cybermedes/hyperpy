bubblegum: int = 202
toffee: int = 118
ice_cream: int = 2250
milk_chocolate: int = 1680
doughnut: int = 1075
pancake: int = 80
income: int = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake

text: str = f'''
Earned amount:
Bubblegum: ${bubblegum}
Toffee: ${toffee}
Ice cream: ${ice_cream}
Milk chocolate: ${milk_chocolate}
Doughnut: ${doughnut}
Pancake: ${pancake}

Income: ${income}'''
print(text)
print('Staff expenses:')
staff_expenses: int = int(input())
print('Other expenses:')
other_expenses: int = int(input())
print(f'Net income: ${income - staff_expenses - other_expenses}')
