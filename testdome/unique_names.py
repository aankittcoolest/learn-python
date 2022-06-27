def unique_names(names1, names2):
    unique_names = {}
    items = []
    for name in names1:
        unique_names[name] = True
    for name in names2:
        unique_names[name] = True

    for key in unique_names:
        items.append(key)

    return items


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    # should print Ava, Emma, Olivia, Sophia
    print(unique_names(names1, names2))
