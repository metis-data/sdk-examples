from flask import Flask, render_template, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import CheckConstraint, Column, Integer, String, Table, UniqueConstraint, TIMESTAMP, text
from sqlalchemycollector import setup, MetisInstrumentor
import os
from os.path import join, dirname
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

take_env_from_docker_file = os.environ.get('TAKE_ENV_FROM_DOCKER_FILE')

if take_env_from_docker_file and take_env_from_docker_file != 'true':
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
flights_table = Table('flights_table', Base.metadata,
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


@app.route('/')
def index():
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    

@app.route('/all_aircraft', methods=[ 'GET'])
def all_aircraft():
            # Query all records from the flights table
            all_flights = db.session.query(Flight).all()

            # Create a list to hold the data of all flights
            flight_data = []
            
            # Extract the required data from each flight and append it to the list
            for flight in all_flights:
                # print(flight)
                flight_data.append({
                    'flight_id': flight.flight_id,
                    'flight_no': flight.flight_no,
                    'scheduled_departure': str(flight.scheduled_departure),
                    'scheduled_arrival': str(flight.scheduled_arrival),
                    'status': flight.status
                })

            # Return the data as a JSON response
            return jsonify(flight_data)


if __name__ == '__main__':
        app.run(debug=True)
