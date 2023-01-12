from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemycollector import setup, MetisInstrumentor, PlanCollectType
app = Flask(__name__)
with app.app_context():

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Trustno1@database-2.cofhrj7zmyn4.eu-central-1.rds.amazonaws.com:5432/airbases"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    instrumentation: MetisInstrumentor = setup('cars-web-server',
                        api_key='ebdcXCeuBZ6KEjzw2nwfb5PUSyMKpxUu7B4Buxv9',
                        dsn = 'http://localhost:6000/api/store-logs',
                        service_version='1.1' 
                                            ) 

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

    @app.route('/airbases')
    def airbases():
        session = db.session
        session.execute('select * from postgres_air.boarding_pass as b where passenger_id = 4484037')
        return {"hello": "world"}

    @app.route('/airbases-query-2')
    def airbases2():
        session = db.session
        session.execute("select * from postgres_air.boarding_pass as bp join postgres_air.booking_leg as bl using (booking_leg_id) join postgres_air.flight as f using (flight_id) join postgres_air.booking b using (booking_id) join postgres_air.passenger p using (passenger_id) where (departure_airport = 'JFK' and scheduled_departure between '2020-07-10' and '2020-07-11' and last_name = 'JOHNSON') or (f.departure_airport = 'EDW' and scheduled_departure between '2020-07-10' and '2020-07-11' and last_name = 'JOHNSON')")
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
        app.run(debug=True)
