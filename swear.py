def filter(fulltweet):
    a_file = open("translated_words.txt", "r")
    bad_word = {}
    for line in a_file:
        stripped_line = line.strip()
        x, y = stripped_line.split(" = ")
        bad_word[x] = y
    a_file.close()

    print(bad_word)
    for bad in bad_word:
        if bad == 'fuck':
            newtweet = fulltweet.replace(bad, bad_word[bad])
        else:
            newtweet = newtweet.replace(bad, bad_word[bad])
    print(newtweet)

    # Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    word = input("word:")
    filter(word)