import os
from flask import Flask

app = Flask( __name__ )

@app.route('request')
def recieve_request( request_params ):
    pass

