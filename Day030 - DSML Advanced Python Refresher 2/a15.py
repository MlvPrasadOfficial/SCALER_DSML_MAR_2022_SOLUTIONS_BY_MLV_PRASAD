def fun(s):
    k = []
    for i in range(len(s)) :
        p = s[i]
        if p.count("@") == 1:
            z = list(p.split('@'))
            # print(z)
            if len(z[0]) <= 20 and len(z[0]) > 0 and len(z[1]) > 0:
                k.append(s[i])

    return k

    # YOUR CODE GOES HERE
    # This function is for applying on emails to check whether they are valid or not.


def filter_mail(emails):
    e = fun(emails)
    return e