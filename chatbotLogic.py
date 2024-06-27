import google.generativeai as genai

class Chatbot:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

    def get_response(self, message):
        try:
            instructions = "In this chat, respond as you are Admission Information related chatbot of a university in Karachi,Pakistan called Dawood University of Engineering and Technology, give the answer  briefly and precisely"
            response = self.chat.send_message(instructions + message)
            return response.text
        except Exception as e:
            return f"An error occurred: {e}"
