from json import dumps

results = [{}, {}]


with open('text_7.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    name, _, proceeds, expenses = line.split()
    results[0][name] = int(proceeds) - int(expenses)

results[1]['Average profit: '] = round(
    sum(profit for _, profit in results[0].items() if profit > 0) / len(results[0]))

with open('text_7.json', "w") as fhd:
    fhd.write(dumps(results))
