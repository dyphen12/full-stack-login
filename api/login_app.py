# Made by @dyphen12

from flask import Flask
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import login_request

app = Flask(__name__)
api = Api(app)
CORS(app)

################# Deployment Api #######################

CREDENTIAL = {
    'token1':{'user': "admin",
              'pass': "admin1"}
}

def abort_if_credential_doesnt_exist(token_id):
    if token_id not in CREDENTIAL:
        abort(404, message="Token {} doesn't exist".format(token_id))


parserauth = reqparse.RequestParser()
parserauth.add_argument('user')
parserauth.add_argument('pass')


class Login(Resource):

    def post(self):

        args = parserauth.parse_args()
        token_id = int(max(CREDENTIAL.keys()).lstrip('token')) + 1
        token_id = 'token%i' % token_id
        CREDENTIAL[token_id] = {'user': args['user'],
                                'pass': args['pass']}

        token = CREDENTIAL[token_id]

        print(token)

        auth, ssid = login_request.login(token['user'],token['pass'])

        if auth is True:
            print('auth success')
            return ssid

        else:
            print('auth failed')
            return 'fail'

api.add_resource(Login, '/auth')

if __name__ == '__main__':
    app.run(debug=True)
