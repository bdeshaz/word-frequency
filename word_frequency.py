import re

""" Text of doc """
with open("sample.txt") as sample:
    lines = sample.readlines()

""" Removes Words from List """

def word_removal(list_o_words):

    useless_words = """a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
    because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
    for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
    it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
    not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
    since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
    twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
    would,yet,you,your"""

    clean_useless_words = re.sub(r'[^A-Za-z]', "\n", useless_words)
    useless_list = clean_useless_words.split()

    clean_list = []

    useless_set = set(useless_list)
    for word in list_o_words:
        if word not in useless_set:
            clean_list.append(word)
            
    return clean_list
    # print(clean_list)
    # return filter(lambda list_o_words: useless_list, list_o_words)


# word_removal(['a', 'dog','is','the','animal'])



def word_frequency(text):

    """ Creates List from inputed text """
    clean_text = re.sub(r'[^A-Za-z]', "\n", (' '.join(text)).lower())
    text_list = clean_text.split()

    text_list = word_removal(text_list)

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


word_frequency(lines)
