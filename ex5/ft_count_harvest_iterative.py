def ft_count_harvest_iterative() -> None:
    maxdays = int(input("Days until harvest: "))
    for i in range(1, maxdays + 1):
        print(f"Day {i}")
    print("Harvest time!")
