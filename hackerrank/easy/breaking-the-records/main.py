def breakingRecords(scores):
    min_counts = 0
    max_counts = 0
    min = scores[0]
    max = scores[0]

    for x in scores:
        if x < min:
            min_counts = min_counts + 1
            min = x
        if x > max:
            max_counts = max_counts + 1
            max = x
    return max_counts, min_counts


if __name__ == '__main__':
    breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
    print("ok")
