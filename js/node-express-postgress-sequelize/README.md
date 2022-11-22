[![metis](https://static-asserts-public.s3.eu-central-1.amazonaws.com/logo-l.png)](https://www.metisdata.io/)

# Node.js, Express.js, Sequelize.js and PostgreSQL RESTful API

Using the [DOC](https://docs.metisdata.io/metis/sdk-integration/javascript-sequelize) of [Metis](https://app.metisdata.io/) and this source code is part of [Node.js, Express.js, Sequelize.js and PostgreSQL RESTful API](https://www.djamware.com/post/5b56a6cc80aca707dd4f65a9/nodejs-expressjs-sequelizejs-and-postgresql-restful-api) tutorial.

## Setup

1 - Add **METIS_API_KEY** into `./models/index.js#L43`

2 - To run locally:

- Make sure you have install and run PostgreSQL server
- Create database with the name same as in config file
- Run `npm install` or `yarn install`
- Run `sequelize db:migrate`
- Run `nodemon` or `npm start`

### run database

`docker-compose up db`

### run express docker

`docker-compose run --rm api bash`
`docker-compose`

3 - open [localhost:3000](http://localhost:3000/api/student) you should see empty array `[ ]` because you still not add any data to PostgreSQL yet, feel free update it 😉 but any rest request will send all necessary data to Metis

4 - navigate to [Metis](https://app.metisdata.io/activities) and verify in filter that you select the **METIS_API_KEY** and result should show all yours traces

## FINISH 🎉

### PS

You can use [Metis](https://app.metisdata.io/) for **FREE**  
If you need help plz use the [DOC](https://docs.metisdata.io)
