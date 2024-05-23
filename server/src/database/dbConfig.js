import mongoose from 'mongoose';
const db_uri = process.env.MONGODB_URI || '';
console.log(db_uri);
const startDatabase = async () => {
  if (db_uri === '') {
    console.log('No database uri provided...');
    return;
  }
  await mongoose
    .connect(db_uri)
    .then((data) => {
      console.log('connected to database.');
    })
    .catch((err) => {
      console.log(err.message);
    });
};
export default startDatabase;
