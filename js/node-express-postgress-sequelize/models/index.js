'use strict';

const fs = require('fs');
const path = require('path');
const Sequelize = require('sequelize');
const process = require('process');
const basename = path.basename(__filename);
const env = process.env.NODE_ENV || 'development';
const config = require(__dirname + '/../config/config.json')[env];
const { SequelizeExpressInterceptor } = require('@metis-data/sequelize-express-interceptor');
const db = {};

let sequelize;
if (config.use_env_variable) {
  sequelize = new Sequelize(process.env[config.use_env_variable], config);
} else {
  sequelize = new Sequelize(config.database, config.username, config.password, config);
}

fs.readdirSync(__dirname)
  .filter((file) => {
    return file.indexOf('.') !== 0 && file !== basename && file.slice(-3) === '.js';
  })
  .forEach((file) => {
    const model = require(path.join(__dirname, file))(sequelize, Sequelize.DataTypes);
    db[model.name] = model;
  });

Object.keys(db).forEach((modelName) => {
  if (db[modelName].associate) {
    db[modelName].associate(db);
  }
});

/**
 *  START METIS REQUIRED MIDDLEWARE
 */

const interceptor = SequelizeExpressInterceptor.create({
  serviceName: 'your-service-name', // The name of the service
  serviceVersion: '0.0.1', // The version of the service
  // exporterUrl: 'https://ingest-stg.metisdata.io',
  exporterApiKey: 'METIS_API_KEY', // The api key from https://app.metisdata.io/
});

interceptor.instrument(
  sequelize, // The Sequelize instance for getting the plan
  {
    errorHandler: console.error, // Error handler, errors are still reporterd to metis' Sentry account
    shouldCollectPlans: true, // Get the plan for each intercepted query (default to true)
    excludedUrls: [/favicon.ico/], // URLs to exclude from tracing
    printToConsole: true, // Print outgoing spans in console (default to false, passed to exporter)
  }
);

/**
 *  END METIS REQUIRED MIDDLEWARE
 */

db.sequelize = sequelize;
db.Sequelize = Sequelize;

module.exports = db;
