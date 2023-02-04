f = open('words_sentences.txt', 'r')
def count_sent(f):
    symb_count = 0
    for i in f:
        if i == '.':
            symb_count += 1
            yield symb_count


for item in f:
    print(item)
