def check_equal(str1, str2):
    '''
    input:
    str1 -> the first input string
    str2 -> the second input string
    output:
    res -> "Same" if both strings are same, or "Not Same"
    '''
    res = ""

    if len(str1) != len(str2):
        return 'Not Same'
    count = 0

    for i in range(len(str2)):
        str2 = str2[1:]+str2[0]
        if str1 ==str2  :
            count += 1
    if count > 0 :
        return 'Same'
    else :
        return 'Not Same'

    
 