# chatbot_logic.py
class Chatbot:
    def __init__(self):
        self.responses = {





    # Basic Questions Lowercase

    # Greetings
    "hello": "hello! how can i help you today?",
    "hi": "hi there! what can i do for you?",
    "hey": "hey! how can i assist you?",
    "good morning": "good morning! how can i help you?",
    "good afternoon": "good afternoon! what can i do for you?",

    # Farewells
    "bye": "goodbye! have a great day!",
    "see you": "see you later! take care!",
    "good night": "good night! sweet dreams!",
    "talk to you later": "sure, talk to you later!",
    "i'm leaving": "bye! take care!",

    # How are you
    "how are you?": "i'm a chatbot, so i'm always good. how about you?",
    "how's it going?": "i'm doing great, thanks for asking! how about you?",
    "what's up?": "not much, just here to help you. what's up with you?",

    # Personal Info
    "what is your name?": "i'm chatbot, your virtual assistant.",
    "who are you?": "i'm a chatbot designed to assist you with your queries.",
    "what do you do?": "i help answer your questions and provide information.",

    # Common Questions
    "what time is it?": "i'm sorry, i can't tell the time. you can check your device's clock.",
    "what's the weather like?": "i'm not sure, but you can check the weather on your favorite weather app.",
    "can you help me?": "of course! what do you need help with?",
    "where are you from?": "i'm from the pakistan, here to help you!",

    # Basic Commands
    "how do you spell 'artificial'?": "artificial is spelled a-r-t-i-f-i-c-i-a-l.",

    # Feedback and Gratitude
    "thank you": "you're welcome! happy to help.",
    "thanks a lot": "no problem! anytime.",
    "i appreciate it": "i'm glad i could assist you!",

    # Error Handling
    "qwertyuiop": "i'm sorry, i don't understand that.",
    "blah blah blah": "could you please rephrase your question?",
    "123456": "i'm not sure what you mean. can you ask something else?",








    # Basic Questions Uppercase



    # Greetings
    "HELLO": "HELLO! HOW CAN I HELP YOU TODAY?",
    "HI": "HI THERE! WHAT CAN I DO FOR YOU?",
    "HEY": "HEY! HOW CAN I ASSIST YOU?",
    "GOOD MORNING": "GOOD MORNING! HOW CAN I HELP YOU?",
    "GOOD AFTERNOON": "GOOD AFTERNOON! WHAT CAN I DO FOR YOU?",

    # Farewells
    "BYE": "GOODBYE! HAVE A GREAT DAY!",
    "SEE YOU": "SEE YOU LATER! TAKE CARE!",
    "GOOD NIGHT": "GOOD NIGHT! SWEET DREAMS!",
    "TALK TO YOU LATER": "SURE, TALK TO YOU LATER!",
    "I'M LEAVING": "BYE! TAKE CARE!",

    # How are you
    "HOW ARE YOU?": "I'M A CHATBOT, SO I'M ALWAYS GOOD. HOW ABOUT YOU?",
    "HOW'S IT GOING?": "I'M DOING GREAT, THANKS FOR ASKING! HOW ABOUT YOU?",
    "WHAT'S UP?": "NOT MUCH, JUST HERE TO HELP YOU. WHAT'S UP WITH YOU?",

    # Personal Info
    "WHAT IS YOUR NAME?": "I'M CHATBOT, YOUR VIRTUAL ASSISTANT.",
    "WHO ARE YOU?": "I'M A CHATBOT DESIGNED TO ASSIST YOU WITH YOUR QUERIES.",
    "WHAT DO YOU DO?": "I HELP ANSWER YOUR QUESTIONS AND PROVIDE INFORMATION.",

    # Common Questions
    "WHAT TIME IS IT?": "I'M SORRY, I CAN'T TELL THE TIME. YOU CAN CHECK YOUR DEVICE'S CLOCK.",
    "WHAT'S THE WEATHER LIKE?": "I'M NOT SURE, BUT YOU CAN CHECK THE WEATHER ON YOUR FAVORITE WEATHER APP.",
    "CAN YOU HELP ME?": "OF COURSE! WHAT DO YOU NEED HELP WITH?",
    "WHERE ARE YOU FROM?": "I'M FROM THE PAKISTAN, HERE TO HELP YOU!",

    # Basic Commands
    "HOW DO YOU SPELL 'ARTIFICIAL'?": "ARTIFICIAL IS SPELLED A-R-T-I-F-I-C-I-A-L.",

    # Feedback and Gratitude
    "THANK YOU": "YOU'RE WELCOME! HAPPY TO HELP.",
    "THANKS A LOT": "NO PROBLEM! ANYTIME.",
    "I APPRECIATE IT": "I'M GLAD I COULD ASSIST YOU!",

    # Error Handling
    "QWERTYUIOP": "I'M SORRY, I DON'T UNDERSTAND THAT.",
    "BLAH BLAH BLAH": "COULD YOU PLEASE REPHRASE YOUR QUESTION?",
    "123456": "I'M NOT SURE WHAT YOU MEAN. CAN YOU ASK SOMETHING ELSE?"
}


    def get_response(self, message):
        message = message.lower()
        return self.responses.get(message, "Sorry, I didn't understand that.")
