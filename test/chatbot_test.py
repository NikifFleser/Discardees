from modules.ChatBot.chatBotConnector import ChatBotConnector

def main():
    ChatBot = ChatBotConnector()
    user_input = ""
    print("Enter your message to the chatbot (type 'quit' to exit): ")
    while user_input.lower() != "quit":
        
        user_input = input("You: ")

        print("ChatBot: ")
        print(ChatBot.get_response(user_input))

if __name__ == "__main__":
    main()