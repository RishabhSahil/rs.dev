from flask import Flask, redirect, request, render_template, jsonify
import search as sr
import random

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


@app.route('/img-picker/jkhaidkljf/jhtyulkjnsdf/wweuyiwqkbsd')
def get_random_animated_gifs():
    # Choose a random number of GIF files to return (0 to 5)
    gif_num = random.randint(0, 5)
    
    # Create a list of URLs for the chosen GIF files
    url = f'https://raw.githubusercontent.com/RishabhSahil/rs.dev/788a0c78da8b1431674157f5d2a7cb6aa50f22eb/static/animated-img/gif-{gif_num}.gif'
    
    # Return the URL
    return jsonify({'url': url})

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
    # app.run()
