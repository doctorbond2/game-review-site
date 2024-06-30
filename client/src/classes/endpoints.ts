class Endpoint {
  constructor() {}
  getAllGames = process.env.GAMES_GET_ALL || '/error';
}
const endpoints = new Endpoint();
export default endpoints;
