import openai
import speech_recognition as sr

API_KEY = input("Insert API KEY: ")

openai.api_key = API_KEY
listener = sr.Recognizer()
endConversation = False
conversationEnders = ["End Conversation", "I don't want to talk", "Shut down", "No more conversation", "End", "end"]

def listening():
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
    try:
        said = listener.recognize_google(audio)
        print(f"You said: {said}")
        return said
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""

def sendResponseToAI(api_key, user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

while not endConversation:
    userResponse = listening()
    AIResponse = sendResponseToAI(API_KEY, userResponse)
    print("AI said:", AIResponse)
    if any(ender in userResponse for ender in conversationEnders):
        endConversation = True
    else:
        continue
