def minion_game(wd):
    # length of the word
    len_s = len(wd)

    # index of vowel
    k_list = [s for s in range(len_s) if wd[s] in ['A','E','I','O','U']]

    # index of consonant (by subtracting index of vowel)
    s_list = list(set(range(len_s)) - set(k_list))

    # score for kevin
    k_score = sum(map(lambda x: len_s - x, k_list))

    # score for stuart
    s_score = sum(map(lambda x: len_s - x, s_list))

    # result
    if s_score > k_score:
        print("Stuart " + str(s_score))
    elif s_score < k_score:
        print("Kevin " + str(k_score))
    else:
        print("Draw")
