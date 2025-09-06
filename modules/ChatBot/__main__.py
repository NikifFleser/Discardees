if __name__ == "__main__":
    from chatBotConnector import ChatBotConnector
    ChatBot = ChatBotConnector()
    print(ChatBot.get_response("Hello, how are you?"))