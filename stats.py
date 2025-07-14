def get_book_word_count(filecontents):
    return len(filecontents.split())


def get_book_letter_count(filecontents):
    count_table = []
    words = filecontents.split()
    for word in words:
        for character in word:
            current_character = character.lower()
            result = [d for d in count_table if d.get("char") == current_character]
            if result:
                result[0]["num"] += 1
            else:
                new_dict = {"char": current_character, "num": 1}
                count_table.append(new_dict)

    return count_table


def sort_on(items):
    return items["num"]


def sort_book_letter_count(letter_count_list):
    letter_count_list.sort(reverse=True, key=sort_on)
