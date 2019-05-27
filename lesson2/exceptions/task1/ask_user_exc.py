

questions_template = {
    "How are you?": "Good",
    "What are you doing?": "Programming",
    "What is the sense of life?": "Cats",
    "How old are you?" : "Enough",
    "Do you like coconuts?" : "Yeees:)"
}


def ask_user():
    answ = ""
    print("Hi! Let's speak!")
    while True:
        try:
            answ = str(input("You: "))

            if answ.lower() == "bue":
                print("Program: Bue!")
                break
            elif answ in questions_template:
                print("Program: {}".format(questions_template[answ]))
            else:
                print("Program: What???")
        except KeyboardInterrupt:
            print("Program: Bue!")
            break

ask_user()
