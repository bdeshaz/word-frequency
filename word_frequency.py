import re


""" clean_text(text)/ get_words(text)


word_frequency(text)

if __name__=="__main__"
    read file
    call word_frequency
    call print_word_freq """


""" Text of doc """
with open("sample.txt") as sample:
    lines = sample.readlines()


def word_frequency(text):

    """ Creates List from inputed text """
    # text = text.lower()
    # text_on_one_line = re.split(' ',text)
    # clean_text = re.sub(r'[^A-Za-z]', "\n", (' '.join(text_on_one_line)).lower()
    clean_text = re.sub(r'[^A-Za-z]', "\n", (' '.join(text)).lower())
    text_list = clean_text.split()

    """ Create Dictionary for count """
    text_dict = {}

    for word in text_list:
        if word not in text_dict:
            text_dict[word] = 1
        else:
            text_dict[word] += 1

    """ Sort Dictionary """
    for word, count in sorted(text_dict.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(word, count)






# print(a_few_words)
word_frequency(lines)
