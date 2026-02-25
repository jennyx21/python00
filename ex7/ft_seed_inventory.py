def ft_seed_inventory(a, b, c):
    if c == "packets":
        print(a, " seeds:", b, " Packages avalible")
    elif c == "grams":
        print(a, " seeds:", b, " grams total")
    elif c == "area":
        print(a, " seeds:", b, " square meters")
    else:
        print("no corect unit found")


# def main():
#     ft_seed_inventory("tomato", 15, "packets")
#     ft_seed_inventory("carrot", 8, "grams")
#     ft_seed_inventory("lettuce", 12, "area")


# if __name__ == "__main__":
#     main()
