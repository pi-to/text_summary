from flask import Flask, render_template, request, url_for
from summpy.lexrank import summarize


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        sentence = request.form.get("sentence")
        # sentence1 = sentence.replace(' ', '\n')
        # sentence2 = sentence1.split('\n')

        # ans_list = []
        # i = 0
        # while(1):
        #     try:
        #         if sentence2[i] != "":
        #             text = ""
        #             text += sentence2[i]
        #             i += 1
        #             while(1):
        #                 if sentence2[i] != "":
        #                     text += sentence2[i]
        #                     i += 1
        #                 else:
        #                     i += 1
        #                     break
        #             ans_list.append(text)
        #         else:
        #             i += 1
        #             continue
        #     except IndexError:
        #         break

        # real_txt = "\n".join(ans_list)
        sentences, debug_info = summarize(sentence, sent_limit=5,
                                          continuous=True, debug=True)

        # title = request.form.get("title")
        return render_template("output.html", sentences=sentences)


if __name__ == "__main__":
    app.run()
