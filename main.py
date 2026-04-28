from dotenv import load_dotenv

load_dotenv()

from graph.graph import app
if __name__ == "__main__":
    question = "What is the current weather in Istanbul ?"
    result = app.invoke({"question": question})
    print(result)

