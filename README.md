# Discardees

## Summary
*Cemal: ToDo*

## Test functions
### LLM:
```
python -i -m test.chatbot_test
```

## Github Pages
(https://nikiffleser.github.io/Discardees/)

## Setup
### Virtual Environment
Create virtual environment:
```console
python -m venv venv
```
Activate virtual environment:
```console
./venv/Scripts/activate
```

Save modules to requirements
```console
pip freeze > requirements.txt
```
Load modules from requirements
```console
pip install -r requirements.txt
```

### Setup LLM Models
1. Install ollama (https://ollama.com/download)
2. Open a command prompt
3. Type 
```
ollama pull smollm2:1.7b
```