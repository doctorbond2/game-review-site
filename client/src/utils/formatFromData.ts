export function retrieveGenres<T extends { genres?: any }>(
  gameData: T
): any | undefined {
  return gameData.genres;
}
export function reviewFormFormatter<T>(gameData: T): any | undefined {}
