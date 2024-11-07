s1 = input("Enter the first String")
s2 = input("Enter the second string")

if len(s1) != len(s2):
    print("Not Anagram")
else:
    for x in s1:
        if x not in s2:
            print("Not Anagram")
            break;

    else:
        print("The String is Anagram")
