from flask import Flask, abort, request

HTTP_CODE_METHOD_NOT_ALLOWED = 405

app = Flask(__name__)

@app.route('/<param>', methods=['GET', 'POST'])
def main(param):
    if request.method == 'GET':
        return 'GET'
    elif request.method == 'POST':
        return 'POST'
    else:
        abort(HTTP_CODE_METHOD_NOT_ALLOWED)
