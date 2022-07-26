def count_unique_words(inp):
    ans = None
    # YOUR CODE GOES HERE
    ans = 0
    arr = list(inp.split())
    for word in arr:
        if len(set(word)) == len(word) and len(word) > 3:
            ans += 1
    return ans



