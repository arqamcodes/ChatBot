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
    "123456": "I'M NOT SURE WHAT YOU MEAN. CAN YOU ASK SOMETHING ELSE?",






    # Admission Test Information Lowercase

    # General Information
    "what is the admission test?": "the admission test is an exam required to assess the eligibility of students for admission to a specific course or institution.",
    "why is the admission test important?": "the admission test is important because it helps to evaluate a student's knowledge and skills, ensuring they meet the standards required by the institution.",
    "who can take the admission test?": "any student who meets the eligibility criteria set by the institution can take the admission test.",

    # Test Dates and Deadlines
    "when is the admission test?": "the admission test is typically held twice a year. exact dates vary by institution, so check the official website for details.",
    "what are the important deadlines?": "important deadlines include the application submission date, test date, and result announcement date. these are usually listed on the institution's website.",

    # Registration Process
    "how do i register for the admission test?": "you can register for the admission test online through the institution's official website. fill out the application form and pay the required fee.",
    "what documents are required for registration?": "required documents typically include a copy of your id, previous academic records, and proof of payment for the registration fee.",

    # Test Format and Content
    "what is the format of the admission test?": "the format of the admission test usually includes multiple-choice questions, essay writing, and sometimes practical assessments, depending on the course.",
    "what subjects are covered in the admission test?": "the subjects covered in the admission test vary by course but generally include mathematics, english, and general knowledge.",

    # Test Preparation
    "how should i prepare for the admission test?": "prepare for the admission test by reviewing the syllabus, practicing past papers, and studying relevant textbooks and materials.",
    "are there any recommended study materials?": "recommended study materials include textbooks, online courses, and practice tests specifically designed for the admission test.",

    # On Test Day
    "what should i bring on the test day?": "on the test day, bring your admission ticket, a valid id, and any other materials specified by the institution, such as pens or a calculator.",
    "what time should i arrive at the test center?": "arrive at the test center at least 30 minutes before the test starts to complete the check-in process and find your seat.",

    # Results and Next Steps
    "how will i receive my test results?": "test results are usually posted on the institution's website or sent to your registered email address.",
    "what should i do after receiving my test results?": "after receiving your test results, follow the instructions provided by the institution regarding the next steps in the admission process, such as attending an interview or submitting additional documents.",

    # Admission Test Information Uppercase

    # General Information
    "WHAT IS THE ADMISSION TEST?": "THE ADMISSION TEST IS AN EXAM REQUIRED TO ASSESS THE ELIGIBILITY OF STUDENTS FOR ADMISSION TO A SPECIFIC COURSE OR INSTITUTION.",
    "WHY IS THE ADMISSION TEST IMPORTANT?": "THE ADMISSION TEST IS IMPORTANT BECAUSE IT HELPS TO EVALUATE A STUDENT'S KNOWLEDGE AND SKILLS, ENSURING THEY MEET THE STANDARDS REQUIRED BY THE INSTITUTION.",
    "WHO CAN TAKE THE ADMISSION TEST?": "ANY STUDENT WHO MEETS THE ELIGIBILITY CRITERIA SET BY THE INSTITUTION CAN TAKE THE ADMISSION TEST.",

    # Test Dates and Deadlines
    "WHEN IS THE ADMISSION TEST?": "THE ADMISSION TEST IS TYPICALLY HELD TWICE A YEAR. EXACT DATES VARY BY INSTITUTION, SO CHECK THE OFFICIAL WEBSITE FOR DETAILS.",
    "WHAT ARE THE IMPORTANT DEADLINES?": "IMPORTANT DEADLINES INCLUDE THE APPLICATION SUBMISSION DATE, TEST DATE, AND RESULT ANNOUNCEMENT DATE. THESE ARE USUALLY LISTED ON THE INSTITUTION'S WEBSITE.",

    # Registration Process
    "HOW DO I REGISTER FOR THE ADMISSION TEST?": "YOU CAN REGISTER FOR THE ADMISSION TEST ONLINE THROUGH THE INSTITUTION'S OFFICIAL WEBSITE. FILL OUT THE APPLICATION FORM AND PAY THE REQUIRED FEE.",
    "WHAT DOCUMENTS ARE REQUIRED FOR REGISTRATION?": "REQUIRED DOCUMENTS TYPICALLY INCLUDE A COPY OF YOUR ID, PREVIOUS ACADEMIC RECORDS, AND PROOF OF PAYMENT FOR THE REGISTRATION FEE.",

    # Test Format and Content
    "WHAT IS THE FORMAT OF THE ADMISSION TEST?": "THE FORMAT OF THE ADMISSION TEST USUALLY INCLUDES MULTIPLE-CHOICE QUESTIONS, ESSAY WRITING, AND SOMETIMES PRACTICAL ASSESSMENTS, DEPENDING ON THE COURSE.",
    "WHAT SUBJECTS ARE COVERED IN THE ADMISSION TEST?": "THE SUBJECTS COVERED IN THE ADMISSION TEST VARY BY COURSE BUT GENERALLY INCLUDE MATHEMATICS, ENGLISH, AND GENERAL KNOWLEDGE.",

    # Test Preparation
    "HOW SHOULD I PREPARE FOR THE ADMISSION TEST?": "PREPARE FOR THE ADMISSION TEST BY REVIEWING THE SYLLABUS, PRACTICING PAST PAPERS, AND STUDYING RELEVANT TEXTBOOKS AND MATERIALS.",
    "ARE THERE ANY RECOMMENDED STUDY MATERIALS?": "RECOMMENDED STUDY MATERIALS INCLUDE TEXTBOOKS, ONLINE COURSES, AND PRACTICE TESTS SPECIFICALLY DESIGNED FOR THE ADMISSION TEST.",

    # On Test Day
    "WHAT SHOULD I BRING ON THE TEST DAY?": "ON THE TEST DAY, BRING YOUR ADMISSION TICKET, A VALID ID, AND ANY OTHER MATERIALS SPECIFIED BY THE INSTITUTION, SUCH AS PENS OR A CALCULATOR.",
    "WHAT TIME SHOULD I ARRIVE AT THE TEST CENTER?": "ARRIVE AT THE TEST CENTER AT LEAST 30 MINUTES BEFORE THE TEST STARTS TO COMPLETE THE CHECK-IN PROCESS AND FIND YOUR SEAT.",

    # Results and Next Steps
    "HOW WILL I RECEIVE MY TEST RESULTS?": "TEST RESULTS ARE USUALLY POSTED ON THE INSTITUTION'S WEBSITE OR SENT TO YOUR REGISTERED EMAIL ADDRESS.",
    "WHAT SHOULD I DO AFTER RECEIVING MY TEST RESULTS?": "AFTER RECEIVING YOUR TEST RESULTS, FOLLOW THE INSTRUCTIONS PROVIDED BY THE INSTITUTION REGARDING THE NEXT STEPS IN THE ADMISSION PROCESS, SUCH AS ATTENDING AN INTERVIEW OR SUBMITTING ADDITIONAL DOCUMENTS."








}


    def get_response(self, message):
        message = message.lower()
        return self.responses.get(message, "Sorry, I didn't understand that.")
