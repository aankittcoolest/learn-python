def minion_game(string):
    stuart = 0
    kevin = 0
    a = list("AEIOU")
    for i in range(len(string)):
        if string[i] not in a:
            stuart += len(string) - i
        else:
            kevin += len(string) - i
    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")


if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)
