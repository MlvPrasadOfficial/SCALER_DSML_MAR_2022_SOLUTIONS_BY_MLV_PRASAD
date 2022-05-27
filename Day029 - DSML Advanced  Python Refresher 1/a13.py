def bill(unit):
    ans = 0
    # YOUR CODE GOES HERE
    if unit <= 50 :
        ans += units*(0.5)
    elif  unit <= 150 :
        ans += 25
        ans += ((unit-50)*(0.75))
    elif unit <= 250 :
        ans += 25
        ans += 75
        ans += ((unit-150)*(1.20))
    else :
        ans += 25
        ans += 75
        ans += 120
        ans += ((unit-250)*(1.50))
    
    
    final = ans *1.2
    return int(final)
