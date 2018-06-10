# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:12:07 2018

@author: Ayshwarya
"""


import nltk
from nltk.corpus import wordnet 
import re

# READ FILE Railway Station
Inputfile = open("Railway station.txt", "r")
nouns = [] 

# print sample synset
syn =  wordnet.synsets("Animal") 
print(syn[0].lemmas()[0])

# 
File = [ line for line in Inputfile ]
String = '' . join(File)
sentences = re.split(r'[.!?]', String)

# Find out all the noun words in all the sentences of the text
for sentence in sentences:
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if (pos == 'NNPS' or pos == 'NN' or pos == 'NNS' or pos == 'NNP'):
            nouns.append(word)

print("LIST OF NOUNS IN THE TEXT")
print("-------------------------")
print(nouns)           

no_punctuation_noun = []
for k in nouns:
    if ((len(k) != 1)):
        no_punctuation_noun.append(k)
 
print("LIST OF NOUNS IN THE TEXT EXCLUDING PUNCTUATIONS")
print("------------------------------------------------")       
print(no_punctuation_noun)
 
# Function to get synonyms antonyms hyponyms hypernyms of a word 
def get_Syn_Ant_Hypo_Hyper_Noun(word, nounset):
    same_word_cnt = nounset.count(word)
    same_word.append(word+"("+str(same_word_cnt)+")")
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            syno.append(lemma.name())
            if lemma.antonyms():
                anto.append(lemma.antonyms()[0].name())  
        for m in syn.hyponyms():
           hypo.append(m.name())
        for j in syn.hypernyms():
           hyper.append(j.name())
    for a in syno:
        if a in nounset and a != word:
            same_word_cnt = nounset.count(a)
            if a+"("+str(same_word_cnt)+")" not in same_word:
                same_word.append(a+"("+str(same_word_cnt)+")")
    for b in anto:
        if b in nounset and b != word:
            same_word_cnt = nounset.count(b)
            if b+"("+str(same_word_cnt)+")" not in same_word:
                same_word.append(b+"("+str(same_word_cnt)+")")
    for c in hypo:
        if c in nounset and c != word:
            same_word_cnt = nounset.count(c)
            if c+"("+str(same_word_cnt)+")" not in same_word:
                same_word.append(c+"("+str(same_word_cnt)+")")
    for d in hyper:
        if d in nounset and d != word:
            same_word_cnt = nounset.count(d)
            if d+"("+str(same_word_cnt)+")" not in same_word:
                same_word.append(d+"("+str(same_word_cnt)+")")
        
    return same_word

# form the lexical chains
i=1
Big_match = []
print(" ")
print("LEXICAL CHAINS")
print("--------------")
while(len(no_punctuation_noun) != 0):
    word = no_punctuation_noun[0]
    same_word = []
    syno  = []
    anto  = []
    hypo  = []
    hyper  = []
    same_word = get_Syn_Ant_Hypo_Hyper_Noun(word, no_punctuation_noun) 
    print ("Chain " + str(i) + ":" + ", ".join(same_word))
    i=i+1
    if(len(same_word) >= len(Big_match)):
       if(len(Big_match) != 0):
           Big_match[:] = []
       for st3 in same_word:
           index = st3.find("(")
           st2 = st3[0:index]
           Big_match.append(st2)
    
    for st in same_word:
        index = st.find("(")
        st1 = st[0:index]
        while st1 in no_punctuation_noun:
            no_punctuation_noun.remove(st1)

# Get ready to pring text summary
txtsum=""
for data in Big_match:
    for newsent in sentences:
        if data in newsent:
            if newsent not in txtsum:
                txtsum = txtsum + newsent + ". "

# print the text summary
print("Text Summary")
print("-------------------------")
print(txtsum)
    