words = ["start", "Star", "Dummy"]

filtered = filter(lambda word: word.startswith("s"), words)

print(list(filtered))

filtered = filter(lambda word: word.startswith("D"), words)

print(list(filtered))