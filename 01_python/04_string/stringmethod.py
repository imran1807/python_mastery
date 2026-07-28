if __name__ == "__main__":
    name="artificial intelligence"
    name=name.upper()
    print(name)

    email="JOhOn@Gmial.com"
    email=email.lower()
    print(email)
    print(name.capitalize())
    text = "   Python   "
    print(text.strip())
    print(text.lstrip())
    print(text.rstrip())
    sentence = "banana"
    print(sentence.count("a"))
    sentence="i love python"
    sentecce_list=sentence.split()
    print(sentecce_list)
    print("Python".center(40))
    word=["Python","is","a","programming","language"]
    word_joined=" ".join(word)
    print(word_joined)
    case="imran Nazir"
    print(case.casefold())
    name = "Nazir"

    print("Hello {}".format(name))

    text = "Python is a programming language"
    print(text.replace("Python","Java"))
    file_name="image.png"
    print(file_name.endswith(".png"))
    text = "Python is a programming language"
    print(text.find("programming"))