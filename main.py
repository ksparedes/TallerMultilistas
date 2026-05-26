from flask import Flask, render_template
from files import Files

app = Flask(__name__)

f = Files()
multilist = f.read_divipola("DIVIPOLA.csv")
multilist.print_multilist()

@app.route("/")
def root():
    markers = f.get_markers(multilist)
    return render_template("index.html", markers=markers)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)