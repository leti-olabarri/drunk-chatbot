from app import app
from utils.json_response import json_response
from utils.handle_error import handle_error
import os
#import tensorflow as tf

@app.route("/verify")
@handle_error
def verify():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "export_basic_classification"))
    #model = tf.keras.models.load_model(path)
    return "<p>Nothing to see here</p>"