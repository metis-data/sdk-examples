from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemycollector import setup, MetisInstrumentor, PlanCollectType
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

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
        return {""}


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
                    "aircraft_code": aircrafts.name,
                    "model": aircrafts.model,
                    "range": aircrafts.doors
                } for aircraft in aircrafts]

            return {"count": len(results), "aircrafts": results, "message": "success"}


    # @app.route('/cars/<car_id>', methods=['GET', 'PUT', 'DELETE'])
    # def handle_car(car_id):
    #     car = CarsModel.query.get_or_404(car_id)

    #     if request.method == 'GET':
    #         response = {
    #             "name": car.name,
    #             "model": car.model,
    #             "doors": car.doors
    #         }
    #         return {"message": "success", "car": response}

    #     elif request.method == 'PUT':
    #         data = request.get_json()
    #         car.name = data['name']
    #         car.model = data['model']
    #         car.doors = data['doors']

    #         db.session.add(car)
    #         db.session.commit()
            
    #         return {"message": f"car {car.name} successfully updated"}

    #     elif request.method == 'DELETE':
    #         db.session.delete(car)
    #         db.session.commit()
            
    #         return {"message": f"Car {car.name} successfully deleted."}






    if __name__ == '__main__':
        app.run(debug=True)
