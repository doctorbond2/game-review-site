class Library {
  constructor() {}
  BaseUrl = process.env.NEXT_PUBLIC_CLIENT_BASE_URL || '/error';
  GamesBaseUrl = process.env.NEXT_PUBLIC_CLIENT_GAMES_BASE || '/error';
  goToGame = (gameId: string) => {
    return `${this.BaseUrl + this.GamesBaseUrl + gameId}`;
  };
}

const library = new Library();
export default library;
