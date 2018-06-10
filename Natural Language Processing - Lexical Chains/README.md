##**TEXT SUMMARY USING LEXICAL CHAINS - NLP**##
</br>
</br>
The idea of this project is to summarize a text by forming lexical chains from the nouns used in the text. To form a lexical chain 
in this case I have decided to find the synonyms , antonyms, hyponyms and hypernyms of the nouns. 'Wordnet' is used to fetch the noun
and its related words informations [Synonym antonym hyponym and hypernym]. Scan the text, sentence by sentence [tokenize sentences],
get all the nouns [singular plural]. For every noun identified , find if is an synonymn or antonym or hyponym or hypernym of any 
existing lexical chain. If so add that noun to that chain. Else form a new chain. Finally once again scan the entire text to find 
out the sentences which has most of the words found in the longest chains. These sentences are joined together to give out a text summary.
</br>
Language used - Python. </br>
Resources used - Spyder and Wordnet
