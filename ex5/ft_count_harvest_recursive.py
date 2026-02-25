def ft_count_harvest_recursive():
    days = int(input("Days until Harvest:"))
    ft_count(days)
    print("Harvest time!")


def ft_count(days):
    if days > 1:
        ft_count(days - 1)
    print("Day", days)


# def main():
#     ft_count_harvest_recursive()


# if __name__ == "__main__":
#     main()
