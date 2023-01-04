<p align="center" width="100%">
<a href="https://metisdata.io">
    <img width="33%" src="https://uploads-ssl.webflow.com/62d69ddf7813e9ad935e731f/62de3b0f9e217377201a83b9_metis-logo-white.svg">
    </a>
</p>

# Prisma, Node.js, NestJs and PostgreSQL

Using the [Documentation](https://docs.metisdata.io/metis/sdk-integration/javascript-prisma/nestjs/simple) of [Metis](https://app.metisdata.io/) and this source code is part of [Prisma, Node.js, NestJs and PostgreSQL](https://github.com/TasinIshmam/blog-backend-rest-api-nestjs-prisma) tutorial.


# Sample Backend Service

A simple backend REST API for a blog built using NestJS, Prisma, PostgreSQL and Swagger.

## Prerequisites
- make sure the following are installed:
    - `nodejs@16.19.0`
    - `docker@20.10.21`
## Installation
1. Install dependencies: `npm install`
2. Start a PostgreSQL database with docker using: `docker-compose up -d`. 
    - If you have a local instance of PostgreSQL running, you can skip this step. In this case, you will need to change the `DATABASE_URL` inside the `.env` file with a valid [PostgreSQL connection string](https://www.prisma.io/docs/concepts/database-connectors/postgresql#connection-details) for your database. 
3. edit `.env` file and add the following:
    ```
    DATABASE_URL="postgres://myuser:mypassword@localhost:5432/median-db"
    METIS_API_KEY=<REPLACE_IT>
    METIS_SERVICE_NAME=<REPLACE_IT>
    METIS_SERVICE_VERSION=<REPLACE_IT>
    ```
4. Start the project:  `npm run start`
5. visit `http://localhost:3000/api` for seeing the available endpoints
6. visit a specific endpoint such: `http://localhost:3000/articles`
7. visit `https://metisdata.io/activities/<YOUR_API_KEY>`

## Your'e all set! Happy Metising!  &nbsp; 🎉🎉 🎉 



<!-- https://github.com/TasinIshmam/blog-backend-rest-api-nestjs-prisma -->