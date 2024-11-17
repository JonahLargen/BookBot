import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("content", help="The content that bookbot will read. By default, this is a file path.")
parser.add_argument("-t", "--text", help="Switch to using raw text instead of a file path", action="store_true")
args = parser.parse_args()

def main():
    content = args.content
    
    if (args.text):
        report(content, "Text")
    else:
        with open(content) as f:
            file_contents = f.read()
            report(file_contents, content)
   
def report(file_contents: str, report_name: str):
    word_count = count_words(file_contents)
    character_count = count_characters(file_contents)

    print(f"--- Begin report of {report_name} ---")
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