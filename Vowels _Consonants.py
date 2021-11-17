#BY \GURLEEN KAUR\
G = input('Enter Any Sentence: ')

vowels = [each for each in G if each in "aeiouAEIOU"]

consonants = [each for each in G if each not in "aeiouAEIOU "]

print('Number of vowel in string:', len(vowels))
print(vowels)

print('Number of consonant in string:', len(consonants))
print(consonants)
