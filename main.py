
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        count = count_words(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count} words found in the document\n")
        char_count = count_chars(file_contents)
        sorted_chars = sort_chars(char_count)

        for item in sorted_chars:
            print(f"The '{item["name"]}' character was found {item["count"]} times")

        print("--- End report ---")

def count_words(book):
    words = book.split()
    return len(words)

def count_chars(book):
    char_list = {}
    for char in book:
        if char.isalpha():         
            char = char.lower()
            if (char_list.get(char) == None):
                char_list[char] = 1
            else:
                char_list[char] += 1

    return char_list

def sort_chars(char_list):
    sorted = []

    for key, value in char_list.items():
        sorted.append({"name": key, "count": value})

    sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(chars):
    return chars["count"]

main()