class Endpoint {
  constructor() {}
  getAllGames = process.env.NEXT_PUBLIC_GAMES_GET_ALL || '/error';
}
const endpoints = new Endpoint();
export default endpoints;
