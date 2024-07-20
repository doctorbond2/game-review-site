import React from 'react';
import { FormControl, FormLabel } from '@mui/material';
import { Action } from './genreForms/Action';
import api from '@/classes/api';
import endpoints from '@/classes/endpoints';
import { AxiosResponse } from 'axios';
type Props = {
  gameId: string;
};

const getData = async (id: string): Promise<AxiosResponse<any[]>> => {
  const res = await api.get(endpoints.getOneGame + id);
  if (res.status !== 200) {
    throw new Error('Error fetching data');
  }
  return res;
};
async function ReviewForm({ gameId }: Props) {
  const test = Action();
  const gameData = await getData(gameId);
  return (
    <>
      {gameData && test ? (
        <FormControl>
          <FormLabel>Game review</FormLabel>
          {test[0].element}
        </FormControl>
      ) : (
        <h2>Something went wrong</h2>
      )}
    </>
  );
}

export default ReviewForm;
