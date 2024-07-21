import React from 'react';
import { FormControl, FormLabel } from '@mui/material';
import api from '@/classes/api';
import endpoints from '@/classes/endpoints';
import { AxiosResponse } from 'axios';
import ReviewFormList from './ReviewFormList';
import { retrieveGenres } from '@/utils/formatFromData';
type Props = {
  gameId: string;
};

const getData = async (id: string): Promise<AxiosResponse> => {
  const res = await api.get(endpoints.getOneGame + id);
  if (res.status !== 200) {
    throw new Error('Error fetching data');
  }
  return res;
};
async function ReviewForm({ gameId }: Props) {
  try {
    const gameData = await getData(gameId);
    const genres = retrieveGenres(gameData.data);
    console.log(genres);

    return (
      <>
        <FormControl>
          <FormLabel>Game review</FormLabel>
          <ReviewFormList genres={genres} />
        </FormControl>
      </>
    );
  } catch (err) {
    return <div>Something went wrong</div>;
  }
}

export default ReviewForm;
