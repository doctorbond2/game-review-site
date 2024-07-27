import { Key } from '@mui/icons-material';

export function retrieveGenres<T extends { genres?: any }>(
  gameData: T
): any | undefined {
  return gameData.genres;
}
export function reviewFormFormatter<T>(gameData: T): any | undefined {}

export function convertFormDataFields<T extends Record<string, any>>(data: T) {
  const convertedData: Record<string, any> = {};
  Object.keys(data).forEach((key) => {
    if (key.endsWith('_score')) {
      convertedData[key] = parseInt(data[key], 10);
    }
  });
  return convertedData;
}
