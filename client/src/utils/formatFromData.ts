function retrieveGenres<T extends { genre?: any }>(
  gameData: T
): any | undefined {
  return gameData.genre;
}
export function reviewFormFormatter<T>(gameData: T): any | undefined {}
