def group_by_owners(files):
    items = {}
    for key, value in files.items():
        if value in items:
            items[value].append(key)
        else:
            items[value] = [key]

    return items


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))
