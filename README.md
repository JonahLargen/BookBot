# Book Bot
<img src="bookbot.jpg" width="128" alt="Book Bot parsing a book">

[boot.dev](https://boot.dev) Book Bot Project

A python application that parses a book and prints its basic information. Book Bot prints a report containing the total count of each character and the total number of words. The book content can be either a file path or text. Characters only count if they are alphabetic and their casing is ignored.

## Output

```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
...
```

## Usage

```
usage: bookbot.py [-h] [-t] content

positional arguments:
  content     The content that bookbot will read. By default, this is a file path.

options:
  -h, --help  show this help message and exit
  -t, --text  Switch to using raw text instead of a file path
```

## Examples

Reading from a file:

`python3 bookbot.py "books/frankenstein.txt"`

Reading from raw text:

`python3 bookbot.py -t "Hello, I am bookbot!"`

&nbsp;

> [!IMPORTANT]
> The repository does not come with any books pre-installed! Download your own and place them in the "books" directory. You can download [Frankenstein](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt) as a sample.
