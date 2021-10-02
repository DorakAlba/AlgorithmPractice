def isMatch( s: str, p: str) -> bool:
    s = s[::-1]
    p = p[::-1]
    p_in = 0
    l_p = len(p) - 1
    ascended = False
    kept = None
    for number, letter in enumerate(s):
        repeat = True
        while repeat:
            repeat = False
            if l_p >= p_in:
                if letter == p[p_in]:
                    kept = None
                    p_in+=1
                    pass
                elif p[p_in] == '.':
                    p_in+=1
                    kept = None
                    pass
                elif kept == letter:
                    pass
                elif p[p_in] == '*':
                    if p[p_in+1] == letter:
                        p_in+=2
                        kept = letter
                        pass
                    elif p[p_in+1] == '.':
                        p_in+=2
                        ascended = True
                        pass
                    elif kept == letter:
                        kept = p[p_in]
                        p_in+=2
                        pass
                    else:
                        p_in+=2
                        repeat = True
                else:
                    return False
            else:
                if ascended == True or kept == letter:
                    return True
                return False
    while p_in<= l_p:
        if p[p_in] == '*':
            p_in+=2
        elif kept ==p[p_in]:
            p_in+=1
        else:
            return False
    return True

isMatch("aasdfasdfasdfasdfas",
        "aasdf.*asdf.*asdf.*asdf.*s")