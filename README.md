# Synonym script
A short, fun script to aid in rewriting sentences

Inspired by the feeling of trying to rewrite a sentence in your own words, I utilize the datamuse python library to change words in a sentence without changing the meaning of the sentence (ideally...).

_Disclaimer: This script was never meant to be used to plagairize, rather it is just a fun proof-of-concept that was sprung from a conversation between friends_

That said, here is an example output:

![synonymdemo](https://user-images.githubusercontent.com/33944844/52169230-fd9f3c80-2702-11e9-9a23-780ed7c94288.png)

If you're wondering what "feeling lucky" means, as well as what impact "how lucky?" has on the output, let me explain.

If the user isn't feeling lucky, then the script will go through the sentence word-by-word and display the top-5 most relavent synonyms for each word, and ask the user which word of the 5 they would like in the sentence. If the user is feeling lucky, the program edits the sentence automatically.

So how does "how lucky?" effect everything? Well if the user thinks they're about 1 on a scale of 5, then the program will automatically go through the sentence and replace each word with the most relavent synonym that the library returns. If the user is feeling more lucky, let's say a 4 out of 5, the script will replace the each word with a synonym somewhere between the most relavent, and the fourth-most relavent synonym that the library returns.

So essentially, the more lucky the user feels, the less likely the new sentence will have the same meaning as the old sentence.
