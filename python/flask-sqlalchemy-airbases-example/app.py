from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemycollector import setup, MetisInstrumentor, PlanCollectType
import os
from os.path import join, dirname
from dotenv import load_dotenv

take_env_from_docker_file = os.environ.get('TAKE_ENV_FROM_DOCKER_FILE')

if take_env_from_docker_file and take_env_from_docker_file != 'true':
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

print(os.environ.get('DB_CONNECTION_STRING'))
print(os.environ.get('METIS_API_KEY'))

app = Flask(__name__)
with app.app_context():

    app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('DB_CONNECTION_STRING')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    instrumentation: MetisInstrumentor = setup('flask-web-server-airbases',
                        api_key= os.environ.get('METIS_API_KEY'),
                        service_version='1.1' 
                                            ) 

    instrumentation.instrument_app(app, db.get_engine())
    class AirCraftModel(db.Model):
        __tablename__ = 'aircrafts'

        aircraft_code = db.Column(db.String(3), primary_key=True)
        model = db.Column(db.Text)
        range = db.Column(db.Integer)

    def __init__(self, aircraft_code, model, range):
        self.aircraft_code = aircraft_code
        self.model = model
        self.range = range

    def __repr__(self):
        return f"<AirCraft {self.aircraft_code}>"


    @app.route('/')
    def hello():
        return {"hello": "world"}


    @app.route('/aircraft', methods=['POST', 'GET'])
    def handle_cars():
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                airCraft = AirCraftModel(aircraft_code=data['aircraft_code'], model=data['model'], range=data['range'])

                db.session.add(airCraft)
                db.session.commit()

                return {"message": f"airCraft {airCraft.aircraft_code} has been created successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == 'GET':
            aircrafts = AirCraftModel.query.all()
            results = [
                {
                    "aircraft_code": aircrafts.aircraft_code,
                    "model": aircrafts.model,
                    "range": aircrafts.doors
                } for aircraft in aircrafts]

            return {"count": len(results), "aircrafts": results, "message": "success"}


    if __name__ == '__main__':
        app.run(debug=True)
