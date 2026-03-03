def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(day):
        if day > days:
            return
        print("Day", day)
        helper(day + 1)
    helper(1)
    print("Harvest time!")
