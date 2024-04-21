import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK stopwords (run this once)
nltk.download('stopwords')

def remove_stopwords(text):
    """
    Remove stop words from the text using NLTK stopwords.
    """
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    return filtered_words

def count_word_frequency(words_list):
    """
    Count the frequency of each word in the processed text.
    """
    word_freq = Counter(words_list)
    return word_freq

def main():
    # Read the file
    with open('random_paragraphs.txt', 'r') as file:
        text = file.read()

    # Remove stop words
    filtered_words = remove_stopwords(text)

    # Count word frequency
    word_freq = count_word_frequency(filtered_words)

    # Display word frequency count
    for word, count in word_freq.items():
        print(f'{word}: {count}')

if __name__ == "__main__":
    main()