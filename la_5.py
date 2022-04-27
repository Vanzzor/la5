

"""
The program is trying to translate a sentense captured as user input.
we first read in the text file textese.txt 
then from the text file, we create a list of strings from ea lines in the text file
Then, we create a dictionary from the list.
once the text file has been read into memory, we close the file.

we then define a function for translating which envolves splitting the user input (sentence) in an 
arrary of strings ("enjoy the excellent band tonight")
("Enjoy, "the", "excellent", "band", "tonight")

once we have the array of strings representing the user's input sentence, we
loop through each words, find the key matching the word, and returns back the value tied to the word
in our dictionary.

after each word is translated, we then
Print out the translated sentence to the user, 

"""

"""
Main():
    set sentence = input()
    set dictionary = Create_dictionary()
    translate(sentence, dictionary)

Translate(sentence, dictionary):
   words = for each of the word in the sentence

   for each words, translate the word

    print translated sentence to user


Create_dictionary():
    read in file(textese.txt)
    create list = each line from file
    close the file
    create a dict off of the list
    return the dict 

main()


"""
