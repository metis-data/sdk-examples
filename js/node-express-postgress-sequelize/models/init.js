const { creds } = require("../config");
let db;

function getInstance() {
  db = {};
  const Sequelize = require("sequelize");
  db.sequelize = new Sequelize(
    creds.database,
    creds.username,
    creds.password,
    creds,
  );
  db.Sequelize = Sequelize;

  return db;
}

function initSequelize() {
  const db = getInstance();
  Object.keys(db).forEach((modelName) => {
    if (db[modelName].associate) {
      db[modelName].associate(db);
    }
  });

  return db;
}

module.exports = {
  initSequelize,
  getInstance,
};
