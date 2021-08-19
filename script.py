from sys import argv

name, work_in_hours, rate_per_hour, prize = argv
print('Выработка в часах: ', work_in_hours)
print('Ставка в часах: ', rate_per_hour)
print('Премия: ', prize)
print('Заработная плата сотрудника: ', (int(work_in_hours)*int(rate_per_hour)) + int(prize))
