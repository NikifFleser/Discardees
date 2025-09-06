from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class ChatBotConnector:
    def __init__(self, model_name: str = "smollm2:1.7b"):
        self.model = OllamaLLM(model=model_name)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant in creating "
            "meaningful NPC characters for a table top RPG. This "
            "includes the visual appearance, personality and role "
            "of this NPC in the game world. Additionally, the NPC "
            "should have a DND-style stat block fitting to their role. "
            "Please return the NPC description in markdown format."),
            ("user", "{input}")
        ])

    def get_response(self, user_input: str) -> str:
        formatted_prompt = self.prompt.format_messages(input=user_input)
        response = self.model.predict_messages(formatted_prompt)
        return response.content
    
if __name__ == "__main__":
    pass