ch = str(input("Enter character:"))
match ch:
    case 'A' | 'a' |'E' |'e' | 'I' | 'i' |'O' |'o' |'U' | 'u':
        print("Vowel")
    case _:
        print("Not vowel")