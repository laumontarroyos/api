from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

rpvs = [ 
    {
    'numero' : '10',
    'status': 'situação 10'
    },
    {
    'numero' : '20',
    'status': 'situação 20'
    },
    {
    'numero' : '30',
    'status': 'situação 30'
    },
    {
    'numero' : '40',
    'status': 'situação 40'
    },
    {
    'numero' : '50',
    'status': 'situação 50'
    }
    
]

@app.route('/')     
def home():
    return render_template('index.html')


@app.route('/rpv', methods=['POST'])
def create_rpvs():
    request_data = request.get_json()
    new_rpv = {
        'numero': request_data['numero'],
        'status':'vazio'
    }
    rpvs.append(new_rpv)
    return jsonify(new_rpv)

@app.route('/rpv/<string:numero>')
def get_store(numero):
    for rpv in rpvs:
        if rpv['numero'] == numero:
            return jsonify({'rpv': rpv})
    return jsonify({'message': 'rpv não localizado!'})
    

@app.route('/rpvs')
def get_rpvs():
    return jsonify({'rpvs': rpvs})

#@app.route('/')     #  'http://www.google.com'
#def home():
#    return "hello, world!"

app.run(port=5000)