from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# for streaming of the response
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

output_form = "You are an AI assistant designed to help Dungeon " \
    "Masters create compelling NPC characters for the tabletop " \
    "role-playing game DnD 5e."

output_parser = StrOutputParser()

class ChatBotConnector:
    def __init__(self, model_name: str = "llama3.1:8b"):
        self.model = OllamaLLM(model=model_name, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature=0.7, num_ctx=8196)
        self.chat_history = []
        self.chat_history += [
            ("system", output_form)
        ]

        self.prompt = ChatPromptTemplate.from_messages(self.chat_history)
        self.npc_idea_messages = [
            ("system", "You are an AI assistant that helps create an idea for an NPC based on user input. This idea will be used to build a full character later. It shouldinclude basic traits, motivations, and a brief description."),
            ("user", "Based on the following input, generate a unique NPC idea: {input}")
        ]

        self.npc_description_messages = [
            ("system", "You are now an AI assistant that helps create a detailed NPC description. This description should include physical appearance, personality traits, and any distinguishing features."),
            ("user", "Based on the the history of the conversation, generate a detailed NPC description.")
        ]

        self.npc_backstory_messages = [
            ("system", "You are an AI assistant that helps create a compelling NPC backstory. This backstory should provide context for the NPC's motivations, relationships, history and give him a reason in the game world."),
            ("user", "Based on the the history of the conversation, generate a compelling NPC backstory.")
        ]

        self.npc_stat_block_messages = [
            ("system", "You are an AI assistant that helps create NPC stat blocks. The stat block should include all relevant stats, abilities, and traits formatted in a way that is easy to read and understand."),
            ("user", "Based on the the history of the conversation, generate a detailed NPC stat block.")
        ]

        self.reset_memory()

        self.chain = self.prompt | self.model | output_parser

        print("ChatBotConnector initialized with model:", model_name)

    def get_response(self, user_input: str) -> str:
        response = self.chain.invoke({"input": user_input})
        self.chat_history += [("user", user_input), ("system", response)]
        return response
    
    def create_npc_idea(self, user_input: str) -> str:
        self.update_prompt(self.npc_idea_messages)
        response = self.get_response(user_input)
        return response
    
    def create_npc_description(self, user_input: str) -> str:
        self.update_prompt(self.npc_description_messages)
        response = self.get_response(user_input)
        return response
        
    def create_npc_backstory(self, user_input: str) -> str:
        self.update_prompt(self.npc_backstory_messages)
        response = self.get_response(user_input)
        return response
    
    def create_npc_stat_block(self, user_input: str) -> str:
        user_input = "Please finalize the character by giving it a DnD 5e like statblock. Make sure to include all relevant stats, abilities, and traits. Format it in a way that is easy to read and understand. Use markdown formatting for better readability. Also, provide a brief explanation of the statblock."
        self.update_prompt(self.npc_idea_messages)
        response = self.get_response(user_input)
        return response
    
    # Utility functions
    def reset_memory(self):
        self.chat_history = []
    
    def update_prompt(self, new_messages: list):
        self.chat_history += new_messages
        self.prompt = ChatPromptTemplate.from_messages(self.chat_history)
        self.chain = self.prompt | self.model | output_parser
    
if __name__ == "__main__":
    pass

# Create a character in a Dungeons and dragons setting, that serves one player, who plays a dwarf, as an adversary in a cook-off.