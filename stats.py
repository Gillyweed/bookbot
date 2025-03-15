def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    count = {}
    for char in text:
        char = char.lower()
        count[char] = count.get(char, 0) + 1
    return count

def sort_on(dict):
    return dict["count"]

def sort_count_chars(count_chars):
    sorted = []
    for elem in count_chars:
        sorted.append({"char": elem, "count": count_chars[elem]})
    sorted.sort(key=sort_on, reverse=True)
    return sorted
