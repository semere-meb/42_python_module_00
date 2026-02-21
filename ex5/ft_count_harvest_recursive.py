def rec(day, maxdays):
    if day > maxdays:
        return
    print(f"Day {day}")
    day += 1
    rec(day, maxdays)


def ft_count_harvest_recursive():
    maxdays = int(input("Days until harvest: "))
    rec(1, maxdays)
    print("Harvest time!")
