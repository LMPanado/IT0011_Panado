def unique_words(statement):
    excluded_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}
    
    words = []
    word = ""
    for char in statement:
        if char.isalpha():
            word += char
        else:
            if word:
                words.append(word)
                word = ""
    if word:
        words.append(word)
    
    filtered_words = [word for word in words if word.lower() not in excluded_words]

    word_counts = {}
    for word in filtered_words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    lowercase = sorted([w for w in word_counts if w.islower()])
    uppercase = sorted([w for w in word_counts if w.istitle()])

    print("\nFiltered Word Count:")
    for word in lowercase + uppercase:
        print(f"{word.ljust(10)} - {word_counts[word]}")
    
    print(f"\nThe total words filtered: {sum(word_counts.values())}")

statement = input("Enter a string statement:\n")
unique_words(statement)