import random

#enable random generation

def magic_8_ball():
    """Asks a question and provides a Magic 8-Ball response."""

    question = input("Ask a yes or no question: ")

    #promt user for a question

    valid_question_words = ["were",                      #States valid question words in a list
                            "has",
                            "do",
                            "are",
                            "should",
                            "did",
                            "is",
                            "will",
                            "am",
                            "have",
                            "does",
                            "can",
                            "could",
                            "would",
                    ]
    
    if not any(question.lower().startswith(word) for word in valid_question_words):
        #Check if the user's question does not start with a valid question word from the list
        print("Please ask a question starting with Were, Has, Do, Are, Should, Did, Is, Will, Am, Have, Does, Can, Could, or Would .")
        #display message
        return
        #returns code to where function was called


    responses = [               #list of responses
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    print(random.choice(responses))
    # Generate a random response from the list

    return
    #return to where the function was called


while True:                                                             #forever loop
    magic_8_ball()                                                      #function to ask user question
    if input("Ask another question? (y/n): ").lower() != "y":           #prompts user to answer question and if question does not equal yes
        print ("goodbye.")
        break                                                           #end loop and end code


