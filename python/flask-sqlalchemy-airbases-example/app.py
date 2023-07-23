from click import DateTime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import CheckConstraint, Column, Integer, String, Table, UniqueConstraint, TIMESTAMP, text
from sqlalchemycollector import setup, MetisInstrumentor, PlanCollectType
import os
from os.path import join, dirname
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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


Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'
    flight_id = Column(Integer, primary_key=True, autoincrement=True)
    flight_no = Column(String(6), nullable=False)
    scheduled_departure = Column(TIMESTAMP(timezone=True), nullable=False)
    scheduled_arrival = Column(TIMESTAMP(timezone=True), nullable=False)
    departure_airport = Column(String(3), nullable=False)
    arrival_airport = Column(String(3), nullable=False)
    status = Column(String(20), nullable=False)
    aircraft_code = Column(String(3), nullable=False)
    actual_departure = Column(TIMESTAMP(timezone=True))
    actual_arrival = Column(TIMESTAMP(timezone=True))

    def __repr__(self):
        return f"<Flight(flight_id={self.flight_id}, flight_no='{self.flight_no}', scheduled_departure='{self.scheduled_departure}', scheduled_arrival='{self.scheduled_arrival}', status='{self.status}')>"

# Define the Table and constraints outside the model
flights_table = Table('flights_1', Base.metadata,
    Column('flight_id', Integer, primary_key=True, autoincrement=True),
    Column('flight_no', String(6), nullable=False),
    Column('scheduled_departure', TIMESTAMP(timezone=True), nullable=False),
    Column('scheduled_arrival', TIMESTAMP(timezone=True), nullable=False),
    Column('departure_airport', String(3), nullable=False),
    Column('arrival_airport', String(3), nullable=False),
    Column('status', String(20), nullable=False),
    Column('aircraft_code', String(3), nullable=False),
    Column('actual_departure', TIMESTAMP(timezone=True)),
    Column('actual_arrival', TIMESTAMP(timezone=True)),
    CheckConstraint(text("scheduled_arrival > scheduled_departure"), name='flights_check'),
    CheckConstraint(text("(actual_arrival IS NULL OR (actual_departure IS NOT NULL AND actual_arrival IS NOT NULL AND actual_arrival > actual_departure))"), name='flights_check1'),
    UniqueConstraint('flight_no', 'scheduled_departure', name='flights_flight_no_scheduled_departure_key')
)

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
def metis_example():
        return {"Metis Example": "Enter the command 127.0.0.1:5000/all_aircraft"}
    

@app.route('/all_aircraft', methods=[ 'GET'])
def all_aircraft():
            # Query all records from the flights table
            all_flights = db.session.query(Flight).all()

            # Printing the results
            for flight in all_flights:
                print(flight)


@app.route('/aircraft', methods=['POST', 'GET'])
def handle_aircraft():
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
                    "aircraft_code": aircraft.aircraft_code,
                    "model": aircraft.model,
                    "range": aircraft.range
                } for aircraft in aircrafts]

            return {"count": len(results), "aircrafts": results, "message": "success"}


if __name__ == '__main__':
        app.run(debug=True)
