def reverse_words(s):
    split_words = s.split(' ')
    list_words = split_words[::-1]
    new_text = ' '.join(list_words)

    return new_text
print (reverse_words("the greatest victory is that which requires no battle" ))