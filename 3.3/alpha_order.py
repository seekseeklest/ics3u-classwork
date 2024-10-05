before_pairs = [("apple", "banana"), ("cat", "dog"), ("elephant", "giraffe"), 
                ("kite", "lion"), ("orange", "pear")]

after_pairs = [("zebra", "antelope"), ("unicorn", "tiger"), ("mountain", "hill"), 
               ("peach", "apple"), ("sunflower", "rose")]

for word1, word2 in before_pairs:
    if word1 < word2:
        print(f"{word1} < {word2}: True")
    else:
        print(f"{word1} < {word2}: False")

for word1, word2 in after_pairs:
    if word1 > word2:
        print(f"{word1} > {word2}: True")
    else:
        print(f"{word1} > {word2}: False")
