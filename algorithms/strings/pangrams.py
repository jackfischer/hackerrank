
s = input().strip()

letters = set(s.lower())
letters.discard(' ')

if len(letters) == 26:
    print("pangram")
else:
    print("not pangram")