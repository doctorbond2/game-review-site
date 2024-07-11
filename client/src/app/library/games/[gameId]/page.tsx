import React from 'react';
import { clientInstance as a } from '@/classes/axiosInstance';
import api from '@/classes/api';
import endpoints from '@/classes/endpoints';
import { Box } from '@mui/material';
import { AxiosResponse } from 'axios';

const getData = async (id: string): Promise<AxiosResponse<any[]>> => {
  const res = await api.get(endpoints.getOneGame + id);

  if (res.status !== 200) {
    throw new Error('Error fetching data');
  }
  return res;
};
type Props = {
  params: {
    gameId: string;
  };
};
async function Game({ params }: Props) {
  try {
    const res: any = await getData(params.gameId);
    const { data } = res;
    return (
      <>
        <Box>
          <h2 style={{ color: 'white' }}>{data.title}</h2>
        </Box>
      </>
    );
  } catch (error) {
    return <div>No game found</div>;
  }

  return <div>page</div>;
}

export default Game;
