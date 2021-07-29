dial_codes = [(86, 'China'), (91, 'India'),
              (1, 'United States'), (55, 'Brazil'), (81, 'Japan')]
country_code = {country: code for code, country in dial_codes}
print(country_code)
