class Library {
  constructor() {}
  BaseUrl = process.env.NEXT_PUBLIC_CLIENT_BASE_URL || '/error';
  LibraryUrl = process.env.NEXT_PUBLIC_CLIENT_LIBRARY_BASE || '/error';
  GamesUrl = process.env.NEXT_PUBLIC_CLIENT_GAMES_BASE || '/error';

  goToGame = (gameId: string) => {
    return `${this.BaseUrl + this.LibraryUrl + this.GamesUrl + gameId}`;
  };
}

const library = new Library();
export default library;
