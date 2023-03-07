import openai
try:
    import app.config as config
    from app.intent import intent_classifier
    from app.slot_fillings import extract_slots
except:
    import config as config
    from intent import intent_classifier
    from slot_fillings import extract_slots


openai.api_key = config.open_ai_api
model_engine = config.model_engine
chatbot_prompt = config.chatbot_prompt




def get_response(conversation_history="", user_input=""):
    prompt = chatbot_prompt.replace(
        "<conversation_history>", conversation_history).replace("<user input>", user_input)

    # Get the response from GPT-3
    response = openai.Completion.create(
        engine=model_engine, prompt=prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)

    # Extract the response from the response object
    response_text = response["choices"][0]["text"]

    chatbot_response = response_text.strip()
    # result = intent_classifier(str(user_input+conversation_history))

    return {"chatbot_response":chatbot_response}


# def main():
    
    # while True:
    #     user_input = input("> ")
    #     if user_input == "exit":
    #         break
    #     chatbot_response = get_response(conversation_history, user_input)
    #     print(f"Chatbot: {chatbot_response}")
    #     conversation_history += f"User: {user_input}\nChatbot: {chatbot_response}\n"

# main()


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = chatbot_prompt
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = openai.Completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer


get_response("what is on my calender today")