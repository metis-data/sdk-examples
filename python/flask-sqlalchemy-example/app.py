import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemycollector import setup, MetisInstrumentor, PlanCollectType
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
with app.app_context():
    DATABASE_URL = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    METIS_SERVICE_NAME = os.getenv('METIS_SERVICE_NAME')
    METIS_API_KEY = os.getenv('METIS_API_KEY')
    METIS_SERVICE_VERSION = os.getenv('METIS_SERVICE_VERSION')

    instrumentation: MetisInstrumentor = setup(METIS_SERVICE_NAME,api_key=METIS_API_KEY,service_version=METIS_SERVICE_VERSION) 

    instrumentation.instrument_app(app, db.get_engine())
    class CarsModel(db.Model):
        __tablename__ = 'cars'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String())
        model = db.Column(db.String())
        doors = db.Column(db.Integer())

        def __init__(self, name, model, doors):
            self.name = name
            self.model = model
            self.doors = doors

        def __repr__(self):
            return f"<Car {self.name}>"


    @app.route('/')
    def hello():
        return {"hello": "world"}


    @app.route('/cars', methods=['POST', 'GET'])
    def handle_cars():
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])

                db.session.add(new_car)
                db.session.commit()

                return {"message": f"car {new_car.name} has been created successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == 'GET':
            cars = CarsModel.query.all()
            results = [
                {
                    "name": car.name,
                    "model": car.model,
                    "doors": car.doors
                } for car in cars]

            return {"count": len(results), "cars": results, "message": "success"}


    @app.route('/cars/<car_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_car(car_id):
        car = CarsModel.query.get_or_404(car_id)

        if request.method == 'GET':
            response = {
                "name": car.name,
                "model": car.model,
                "doors": car.doors
            }
            return {"message": "success", "car": response}

        elif request.method == 'PUT':
            data = request.get_json()
            car.name = data['name']
            car.model = data['model']
            car.doors = data['doors']

            db.session.add(car)
            db.session.commit()
            
            return {"message": f"car {car.name} successfully updated"}

        elif request.method == 'DELETE':
            db.session.delete(car)
            db.session.commit()
            
            return {"message": f"Car {car.name} successfully deleted."}


    if __name__ == '__main__':
        port = int(os.getenv("PORT")) or 5000
        app.run(debug=True, host="0.0.0.0", port=port)
