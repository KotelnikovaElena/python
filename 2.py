time = int(input('введите время в секундах:'))
hour = time // 3600
min = time / 3600 - hour
min = int(min * 60)
sec = time-hour * 3600 - min * 60
print("%02d" % hour, "%02d" % min, "%02d" % sec, sep=':')
