from flask import Flask, redirect, request, render_template
import search as sr

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def home():
    return render_template('index.html')


@app.route(f'/search', methods =["GET", "POST"])
def search():
    search = request.args.get("q")
    aa=sr.search_query(search.lower())
    answer = aa
    if search==False:
        return render_template('index.html')
    if request.method == 'GET': 
        request.form.get('q')
        data={
            "title":search,
            "search":search,
            "answer":answer,
            "idlinks":list(answer["links"].keys()) 
        }
        print(str(search))
    return render_template('search.html',data=data)

@app.route('/translator', methods =["GET", "POST"])
def translatorr():
    lang = sr.languages()
    data = {
        "lang": lang,
        "langv": list(lang.keys()),
        "langse": "en",
        "langvles": "english",
        "answer": "Translation",
        "title": "Language Translator"
    } 
    if request.method == 'POST':
        query = request.form.get('question')
        select = request.form.get('comp_select')
        langvle = lang[select]
        query = str(query)
        trans_result=sr.rishabh_translate(text=query,lang=select)
        langq = trans_result.src
        data = {
            "lang": lang,
            "langv": list(lang.keys()),
            "langse": select,
            "langvles": langvle,
            "langqu": langq.lower(),
            "question": query,
            "answer": trans_result,
            "title": query
        }
    return render_template("translator.html",data=data)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
    # app.run()
