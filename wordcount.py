
# def find_words(file):
#     for word in file:
#         word_count[word] = word_count.get(word, 0) + 1

# def get_count(file):
#     phrase = open(file)
#     word_count = {}
#     for word in phrase:
#         word_count[word] = word_count.get(word, 0) + 1
#        # return word_count.get(word, 0)
    

#     return word_count.get(word, 0)

# print get_count("test.txt")


def get_word_count(test_file):
    test_file = open(test_file)    #open file (what the file is called)
    word_dictionary = {}
    for line in test_file:   #iterate over file:
        words = line.split()
        print words
        for word in words:
            word_dictionary[word] = word_dictionary.get(word, 0) +1
    return word_dictionary

print get_word_count("test.txt")