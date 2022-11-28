const process = require("process");
const env = process.env.NODE_ENV || "development";
const defaultCredentials = require(__dirname + "/../config/config.json")[env];
const defaults = require('lodash.defaults');
const creds = {
    development: {
        username: process.env.DB_USERNAME,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_NAME,
        host: process.env.DB_HOSTNAME,
        dialect: 'postgres',
    },
    test: {
        username: process.env.DB_USERNAME,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_NAME,
        host: process.env.DB_HOSTNAME,
        dialect: 'postgres',
    },
    production: {
        username: process.env.DB_USERNAME,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_NAME,
        host: process.env.DB_HOSTNAME,
        dialect: 'postgres',
    },
};

module.exports = {
    env,
    creds: defaults(creds[env], defaultCredentials)
};
