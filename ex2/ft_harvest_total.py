def ft_harvest_total() -> None:
    i = 1
    sum = 0
    while i <= 3:
        sum += int(input(f"Day {i} harvest: "))
        i += 1
    print(f"Total harvest: {sum}")
