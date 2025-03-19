def get_num_words(input):
    word_list = input.split()
    print(f"Found {len(word_list)} total words")

def get_num_chars(input):
    char_count = {}
    for char in input.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    sorted_char = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    for k,v in sorted_char.items():
        if k.isalpha():
            print(f"{k}: {v}")
