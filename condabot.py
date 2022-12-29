from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request
# from cleaner import clean_corpus
chatbot = ChatBot("gccbot")
# CORPUS_FILE = "chat.txt"
data = open('chat.txt').read()
data.strip().split('\n')


trainer = ListTrainer(chatbot)
# cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(data)


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get("msg")
    return str(chatbot.get_response(user_text))

if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)