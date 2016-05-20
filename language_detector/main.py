"""This is the entry point of the program."""

from .languages import LANGUAGES


def load_languages(language_list=LANGUAGES):
    # Takes a list of dicts where the value for the key 'name' is the language
    # and the value key 'common words' is a list of common words. 
    
    #Returns:  a dict with the key being the names of the lanauges and the values 
    #initialized to zero
    
    result = {}
    for lang_dict in language_list:
        result[lang_dict.get('name')] = 0
    return result

assert load_languages() == {'German': 0, 'Spanish': 0}

# Itereative version:
# def detect_language(text, languages=LANGUAGES):
#     """Returns the detected language of given text."""
#     # Pre-load our results dictionary:
#     results_dict = load_languages(languages)
    
#     for langdict in languages:
#         langname = langdict['name']
#         wordlist = langdict['common_words']
#         print(wordlist)
#         print(type(wordlist))
#         for word in text.split():
#             if word in wordlist:
#                 results_dict[langname] += 1
                
#         return max(results_dict, key=results_dict.get)
    
def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    # Pre-load our results dictionary:
    results_dict = load_languages(languages)
    
    for langdict in languages:
        langname = langdict['name']
        wordlist = langdict['common_words']
        print(wordlist)
        print(type(wordlist))
        
        results_dict[langname] = len([word for word in text.split() if (word in wordlist)])
        return max(results_dict, key=results_dict.get)
    
