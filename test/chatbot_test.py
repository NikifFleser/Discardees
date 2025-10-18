from modules.ChatBot.chatBotConnector import ChatBotConnector

def main():
    ChatBot = ChatBotConnector()
    user_input = ""

    user_input = input("You: ")
    print("ChatBot: ")
    ChatBot.create_npc_idea(user_input)
    print("\n ")

    user_input = input("You: ")
    print("ChatBot: ")
    ChatBot.create_npc_description(user_input)
    print("\n ")

    user_input = input("You: ")
    print("ChatBot: ")
    ChatBot.create_npc_backstory(user_input)
    print("\n ")

    user_input = input("You: ")
    print("ChatBot: ")
    ChatBot.create_npc_stat_block(user_input)
    print("\n ")

def main2():
    ChatBot = ChatBotConnector()
    user_input = ""
    print("Enter your message to the chatbot (type 'quit' to exit): ")
    while user_input.lower() != "quit":
        
        user_input = input("You: ")

        print("ChatBot: ")
        print(ChatBot.get_response(user_input))

if __name__ == "__main__":
    main()