metro_areas = [('Tokyo', 'JP', 36.933, (35.68, 139.69)),
            ('Delhi', 'IN', 21.935, (28.61, 77.208)),
            ('Mexico', 'MX', 20.142, (19.43, -99.13)),
            ('New York', 'us', 20.104, (40.81, -74.02)),
            ('Sao Paulo', 'BR', 19.649, (-23.55, -46.64))]

print('{:15} | {:^9} | {:^9}'.format(' ', 'lat.', 'long.'))
fmt = '{:15} | {:^9.4f} | {:^9.4f}'
for name, cc, pop, (latitude, longtitude) in metro_areas:
    if longtitude <= 0:
        print(fmt.format(name, latitude, longtitude))