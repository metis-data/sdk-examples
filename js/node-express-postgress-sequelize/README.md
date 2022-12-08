[![metis](https://static-asserts-public.s3.eu-central-1.amazonaws.com/metis-min-logo.png)](https://www.metisdata.io/)

# Sequelize, Node.js, Express and PostgreSQL RESTful API

Using the [DOC](https://docs.metisdata.io/metis/sdk-integration/javascript-sequelize) of [Metis](https://app.metisdata.io/) and this source code is part of [Node.js, Express.js, Sequelize.js and PostgreSQL RESTful API](https://www.djamware.com/post/5b56a6cc80aca707dd4f65a9/nodejs-expressjs-sequelizejs-and-postgresql-restful-api) tutorial.

## Setup

### 1. Insert API Key
Insert your api key into `METIS_API_KEY` at `./models/index.js line:43`

### 2. Setup a local PostgreSQL Database.

<ins>Option 1</ins>: Native PostgreSLQ
- Install PostgreSQL locally.
- Create a Database with a name matching `development.test` inside `./config/config.json`.
- Run `npm install`.
- Run `sequelize db:migrate`.


<ins>Option 2</ins>: Docker Database
`docker-compose up db`

### 3. Run
<ins>Option 1</ins>: Native Express Server
- Run `npm start`.

<ins>Option 2</ins>: Docker
`docker-compose run --rm api bash`

### 3. Trigger your Database.
Open [localhost:3000](http://localhost:3000/api/student) and play around. 

### 4. Go to Metis
Navigate to [Metis](https://app.metisdata.io/activities) to view your recent activity.

## You're all set! 🎉 
Fore more info vist our - [Documentation](https://docs.metisdata.io)
