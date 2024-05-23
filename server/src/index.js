import app from './api/app.js';
import startDatabase from './database/dbConfig.js';
const port = process.env.PORT || 3000;
console.log(port);
startDatabase();

app.listen(port, '0.0.0.0', () => {
  console.log(port);
  console.log('Listening to port ' + port);
});
