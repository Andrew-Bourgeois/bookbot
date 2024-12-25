
char_counts = {
    "a":0, 
    "b":0, 
    "c":0, 
    "d":0, 
    "e":0, 
    "f":0, 
    "g":0, 
    "h":0, 
    "i":0, 
    "j":0, 
    "k":0, 
    "l":0, 
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0
    }

path = "books/frankenstein.txt"

# ------------ Functions --------------
def count_words(string):
    words = string.split()
    return len(words)


def sort_on(dict):
    return dict["num"]


def count_chars(string):
    dict_list = []
    for char in string:
        if char.lower() in char_counts.keys():
            # print(char_counts[char.lower()])
            char_counts[char.lower()] = char_counts[char.lower()] + 1
    
    # create new dict
    for key, value in char_counts.items():
        dict_list.append({"name":key, "num":value})
    
    return dict_list

    


# -------- Main Function --------------
with open(path) as f:
    file_contents = f.read()
    w_count = count_words(file_contents)
    c_count = count_chars(file_contents)
    c_count.sort(reverse=True, key=sort_on)
    print(f"""
--- Begin report of {path} ---
{w_count} words were found in document\n
""")
    for _ in c_count:
        name = _["name"]
        num = _["num"]
        print(f"The '{name}' character was found {num} times")
    print("--- End Report ---")
    



