"""This is the entry point of the program."""

from .languages import LANGUAGES

def load_languages(language_list=LANGUAGES):
    # Input: A list of dicts where within each dict in the list, the value for the key 
    #   'name' is the language and the value key 'common words' is a list of common words. 
    # Returns:  A dict with the key being the names of the lanauges and the values 
    #   a int initialized to zero.
    
    result = {}
    for lang_dict in language_list:
        result[lang_dict.get('name')] = 0
    return result

assert load_languages() == {'German': 0, 'Spanish': 0}


def detect_language(text, languages=LANGUAGES):
    # Input: A string of text with unknown language, 'text', and a list of dicts, 'langauges' 
    #    where within each dict in the list, the value for the key 'name' is the language and 
    #    the value key 'common words' is a list of common words.
    # Returns: The detected language of given text as a string.
    
    # Pre-load our results dictionary:
    results_dict = load_languages(languages)
    
    for lang_dict in languages:
        langname = lang_dict['name']
        wordlist = lang_dict['common_words']
        results_dict[langname] = len([word for word in text.lower().split() if (word in wordlist)])
    return max(results_dict, key=results_dict.get)
    




# Itereative version of detect_languages(text, languages=LANGUGAES).
# Working but not implemented:

# def detect_language(text, languages=LANGUAGES):
#     #Returns: The detected language of given text.
#     # Pre-load our results dictionary:
#     results_dict = load_languages(languages)
    
#     for langdict in languages:
#         langname = langdict['name']
#         wordlist = langdict['common_words']
#         for word in text.lower().split():
#             if word in wordlist:
#                 results_dict[langname] += 1
                
#         return max(results_dict, key=results_dict.get)