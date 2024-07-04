export type Rating = {
  id: number;
  rating: number;
};

export type Game = {
  id: number;
  title: string;
  image_url: string;
  genre: string;
  system: string;
  publisher: string;
  rating?: Rating;
};
