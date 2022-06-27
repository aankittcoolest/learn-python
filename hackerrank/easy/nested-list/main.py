import sys

if __name__ == '__main__':
    minimum = sys.float_info.max
    second_min = sys.float_info.max
    names = {}
    out = []
    records = [["chia", 20.0], ["beta", 50.0], ["alpha", 50.0]]
    grades = []
    for record in records:
        grades.append(record[1])
        names[record[0]] = record[1]
    grades = sorted(list(set(grades)))

    for name, value in names.items():
        if value == grades[1]:
            out.append(name)

    out.sort()
    for name in out:
        print(name)

    a = "ankit"
    a.lower()
