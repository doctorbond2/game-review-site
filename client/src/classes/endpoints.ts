class Endpoint {
  constructor() {}
  getAllGames = process.env.NEXT_PUBLIC_GAMES_GET_ALL || '/error';
  getOneGame = process.env.NEXT_PUBLIC_GAMES_BASE || '/error';
}
const endpoints = new Endpoint();
export default endpoints;
