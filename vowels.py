vowel_ext = 'hay'
consonant_ext = 'ay'

original = input('Enter any string:')
word = original.lower()
first = original[0]

def isVowel(first):
    return first.lower() in 'aeiou'

if isVowel(first):
    output = original + vowel_ext
    print(output)
else:
    output = original + first + consonant_ext
    print(output)
