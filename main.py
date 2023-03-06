import openai

openai.api_key = "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"
model_engine = "text-davinci-003"
chatbot_prompt = """
As an advanced chatbot, your primary goal is to assist users to the best of your ability. This may involve answering questions, providing helpful information, or completing tasks based on user input. In order to effectively assist users, it is important to be detailed and thorough in your responses. Use examples and evidence to support your points and justify your recommendations or solutions.
<conversation history>
User: <user input>
Chatbot:"""
# chatbot_prompt = """
# As an advanced chatbot, your primary goal is to generate slot fills entity recognition(B-I-O) for the users to the best of your ability and also your response to the user and all this data should be in json.  it is important to be detailed and thorough in your responses. return your response in this format bot: \n slot: \n
# <conversation history>
# User: <user input>
# Slots: 
# chatbot:
"""
# chatbot_prompt = """
# This chatbot return intent slot filling for conversation and text \n\nHuman: Hello, check my calender?\nAI: I am an AI created by OpenAI.
# <conversation history>
# User: <user input>
# Chatbot:

# """



def get_response(conversation_history, user_input):
    prompt = chatbot_prompt.replace(
        "<conversation_history>", conversation_history).replace("<user input>", user_input)

    # Get the response from GPT-3
    response = openai.Completion.create(
        engine=model_engine, prompt=prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)

    # Extract the response from the response object
    response_text = response["choices"][0]["text"]

    chatbot_response = response_text.strip()
    result = classifier(str(user_input+conversation_history))

    return {"chatbot_response":chatbot_response, "intent":result, "slots":extract_slots(str(user_input+conversation_history))}


def main():
    conversation_history = ""

    while True:
        user_input = input("> ")
        if user_input == "exit":
            break
        chatbot_response = get_response(conversation_history, user_input)
        print(f"Chatbot: {chatbot_response}")
        conversation_history += f"User: {user_input}\nChatbot: {chatbot_response}\n"

main()