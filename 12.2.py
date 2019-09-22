#prog 12.2
fin = open('words.txt')
def is_anagram(text):
    sorted_dict = dict()
    for line in text:
        original_word = line.strip()
        sorting_word = ''.join(sorted(list(original_word.lower()))) 
        sorted_word = sorting_word
        sorted_dict.setdefault(sorted_word, []).append(original_word)
    
    anagrams = []


    for k,v in sorted_dict.items():
        l = len(v)
        if l > 1:
            anagrams.append((l,k,v))
    return anagrams

def longest_list_anagrams(text):
    anagrams = is_anagram(text)
    longest_list_anagrams = []

    for l,k,v in reversed(sorted(anagrams)):
        longest_list_anagrams.append((l,k,v))
    return longest_list_anagrams

longest_list_anagrams = longest_list_anagrams(fin)
print(longest_list_anagrams[:5
