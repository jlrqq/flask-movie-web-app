from flask import Flask, render_template
import requests

app = Flask(__name__) 

app.config["DEBUG"] = True

@app.route("/homepage")
def show_landing_page():
    return render_template("landing-page.html")


@app.route("/search", methods=["POST"])
def form_submit():
    user_query = request.form['search_query']
    redirect_url = url_for('.search.imdb', query_string=user_query)
    return redirect(redirect_url)


@app.route("/search/<query_string>", methods=['GET'])
def search_imdb(query_string):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    querystring = {"q":query_string}
    headers = {
        'x-rapidapi-key': "6d23a422dbmsh15b6f2cbe983f89p13c88ejsn2db1959201ca",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        return render_template("search-result.html", data=data)
    except:
        return render_template("error404.html")


if __name__ == "__main__":
    app.run(host="localhost", port="5000")
