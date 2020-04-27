import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from URL"""
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words=line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(items):
    for item in items:
        print("This is the itme : ", item)


def main():
    url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main()