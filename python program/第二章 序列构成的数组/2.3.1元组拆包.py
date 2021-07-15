# 洛杉矶国际机场的经纬度
lax_coordinates = (33.65, -118.25)
# 东京市的一些信息：市名、年份、人口（单位：百万）、人口变化（单位：百分比）和面积（单位：平方千米）。
city, year, pop, chg, area = ('Tokyo', 2033, 32450, 0.66, 8014)
# 一个元组列表，元组的形式为(country_code, passport_number)。
travelers_ids = [('USA', '33250'), ('BRA', '45892'), ('ESP', '75624')]

for passport in sorted(travelers_ids):  # 在迭代的过程中，passport变量被绑定到每个元组上。
    print("%s %s" % passport)

for country, _ in travelers_ids:  # for循环可以分别提取元组里的元素，也叫作拆包（unpacking）。因为元组中第二个元素对我们没有什么用，所以它赋值给“_”占位符。
    print(country)

latitude, longitude = lax_coordinates  # 平行赋值，最容易辨认的元组拆包形式
print(latitude, longitude)
