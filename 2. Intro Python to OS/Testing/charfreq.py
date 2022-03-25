def character_frequency(filename):
    """Counts the frequency of each character in the given file.

    Args:
        filename (string): a string that represents the path that belongs to the file
    """

    try:
        f = open(filename)
    except OSError:
        return "Input file error!!"

    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters
