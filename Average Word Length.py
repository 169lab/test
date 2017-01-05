#5-10

if __name__ == '__main__':

    sentence = input("Please type out a sentence")

    words = sentence.split()
    counter = len(words)
    totalcharacter = sum( [ len(word) for word in words ] )

    print(totalcharacter/counter)







