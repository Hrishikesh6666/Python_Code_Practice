def century(year):
    if year < 0:
        return "Invalid year"
    
    if year % 100 == 0:
        century = year//100
    else:
        century = year//100+1
    print(f"Year {year} belong to the century {century} ")

print(century(year=2025))       