from modules.ChatBot.chatBotConnector import ChatBotConnector

def main():
    input = "Please create a normal farmer."
    ChatBot = ChatBotConnector()

    # while input.lower != "exit":

    print(ChatBot.get_response(input))

if __name__ == "__main__":
    main()