import random
import datetime

a = random.randint(1,10)
print(a)

now = datetime.datetime.now()
print(type(now))
print(now)
print(now.year)

print(now+datetime.timedelta(days=28))