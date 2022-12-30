"""def cube():
    for i in range(5):
        yield i**3 #değer saklanmaz

iterator= cube()
for i in iterator:
    print(i)"""


generator = (i**4 for i in range(5))
"""print(next(generator))
"""
for i in generator:
    print(i)