def strip_remove(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()



comment = "   Harry is a good boy      "
print(strip_remove(comment, " good"))