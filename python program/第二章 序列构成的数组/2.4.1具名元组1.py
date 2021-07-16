from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.2268, (35.69, 139.69))
print(tokyo)
print(tokyo.name, tokyo.population, tokyo.country, tokyo.coordinates)
print(City._fields) # _fields属性是一个包含这个类所有字段名称的元组。
