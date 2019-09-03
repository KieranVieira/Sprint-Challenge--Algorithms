'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    if len(word) <= 1:
        return count
    if word[0] + word[1] == "th":
        count += 1
    count += count_th(word[1:])
    return count


# takes in string word
# should return a count of how many times th occur within function

# initialize count as 0
# if word == "" or len(word) == 1
#   return count
# if word[0] + word[1] == "th"
#   count + 1
# return count += recurse(word[2:])