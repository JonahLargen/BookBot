import sys

def main():
    book_path = sys.argv[1]
    with open(book_path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)

        print(f"--- Begin report of {book_path} ---")
        print(f"{word_count} words found in the document")
        print()

        l = []
        for k in character_count:
            if str.isalpha(k):
                v = character_count[k]
                l.append({"char": k, "num": v})
           
        l.sort(reverse=True, key=sort_on)
        
        for i in l:
            print(f"The '{i["char"]}' character was found {i["num"]} times")
        
def count_words(file_contents: str):
    return len(file_contents.split())

def count_characters(file_contents: str):
    d = {}
    for c in file_contents:
        c = c.lower()
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def sort_on(dict):
    return dict["num"]

main()