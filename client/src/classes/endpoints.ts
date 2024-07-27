class Endpoint {
  constructor() {}
  getAllGames = process.env.NEXT_PUBLIC_GAMES_GET_ALL || '/error';
  getOneGame = process.env.NEXT_PUBLIC_GAMES_GET_ONE_BY_ID || '/error';

  postOneReview = process.env.NEXT_PUBLIC_GAMES_USER_POST_REVIEW || '/error';
}
const endpoints = new Endpoint();
export default endpoints;
