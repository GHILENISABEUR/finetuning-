from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

template = """
answer the question below  
here is the conversation history :{context} 
Question :{question} 
answer: 
"""

model = Ollama(model="llama3")  # Use the updated import
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conv():
    context = ""
    print("Welcome to Sabrouch Chatbot")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conv()
