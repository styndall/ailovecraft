from flask import Flask, render_template, request
import gpt_2_simple as gpt2

app = Flask(__name__)

sess = None

@app.route("/", methods=['GET'])
def base_index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def base_index_post():
    text = generate_text(prefix=request.form['prefix_text'])
    return render_template("index.html", generated_text=text)

def generate_text(prefix=None):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)
    gentext = gpt2.generate(sess, prefix=prefix, length=200, nsamples=5, batch_size=5, return_as_list=True)
    return gentext
