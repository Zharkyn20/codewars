def get_hints(answer, guess):
    black = 0
    white = 0
    print(answer, guess)
    try:
        for i in range(len(answer)):
            if answer[i] == guess[i]:
                black += 1
                guess[i] = ''
                answer[i] = 'j'
        for i in range(len(answer)):
            if answer[i] in guess:
                white += 1
                index = guess.index(answer[i])
                guess[index] = 'k'
    except IndexError:
        pass
    print(black, white)
    return {"black": black, "white": white}


