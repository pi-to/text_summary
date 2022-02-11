from flask import Flask, render_template, request, url_for
from summpy.lexrank import summarize


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        sentence = request.form.get("sentence")
        num = request.form.get("num")
        sentences, debug_info = summarize(sentence, sent_limit=int(num),
                                          continuous=True, debug=True)

        return render_template("output.html", sentences=sentences)


if __name__ == "__main__":
    app.run(debug=True)
