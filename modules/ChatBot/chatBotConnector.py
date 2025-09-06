from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

output_form = "The endgoal is to produce a JSON object with the " \
"following keys: visual_description, personality_traits, " \
"background_story, stat_block." \
"The stat_block should be structures as in Dungeons and Dragons. If " \
"the stat_block contains any spells or equipment that are not " \
"included in the standard rules of Dungeons and Dragons, please also " \
"include the description of these things in a seperate JSON object." \

class ChatBotConnector:
    def __init__(self, model_name: str = "smollm2:1.7b"):
        self.model = OllamaLLM(model=model_name)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant in creating "
            "meaningful NPC characters for a table top RPG. " + 
            output_form),
            ("user", "{input}")
        ])
        self.chain = self.prompt | self.model

    def get_response(self, user_input: str) -> str:
        response = self.chain.invoke({"input": user_input})
        return response
    
if __name__ == "__main__":
    pass