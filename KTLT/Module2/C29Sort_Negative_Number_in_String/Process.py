def NegativeNumberInString(s):
    #s = "abc-5xyz-12k9l--p"
    neg_numbers = []
    i = 0
    while i<len(s):
        try:
            if int(s[i])%1==0 and s[i-1] == '-':
                item = '-' + s[i]
                j = i+1
                while j<len(s):
                    try:
                        if int(s[j])%1==0:
                            item = item + s[j]
                            j+=1
                    except:
                        j = len(s)
                neg_numbers.append(item)
            i+=1
        except:
            i+=1
    return neg_numbers


