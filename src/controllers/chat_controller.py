from app import app
from flask import request
from utils.json_response import json_response
from utils.handle_error import handle_error
import gpt_2_simple as gpt2


@app.route("/")
@handle_error
def hello():
    return "<p>Hello, World!</p>"


@app.route("/chat", methods=["POST"])
@handle_error
def chat():
    message = request.form["message"]
    message = message + "[ME]"
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name="run1")
    response = gpt2.generate(sess,
                  length=250,
                  temperature=0.8,
                  prefix=message,
                  nsamples=1,
                  batch_size=1,
                  return_as_list=True,
                  include_prefix=False
                  )
    response = response[0]
    response = response.replace(f"{message}", "")
    clean_response = ""

    for i in response:
        if i != "[":
            clean_response = clean_response + i
        else:
            break
            
    data = {
        "status": "OK",
        "message": clean_response
    }
    return json_response(data)
