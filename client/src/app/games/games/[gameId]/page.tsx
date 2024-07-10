import React from 'react';
import { clientInstance as a } from '@/classes/axiosInstance';
import Image from 'next/image';
import api from '@/classes/api';
import endpoints from '@/classes/endpoints';
import { AxiosResponse } from 'axios';
import { Card, Box } from '@mui/material';
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
    const { data: game } = res;
    return (
      <>
        <Box>
          <Card>
            <Image src={game.image} alt={game.title} />
            <h2>{game.title}</h2>
          </Card>
        </Box>
      </>
    );
  } catch (error) {
    return <div>No game found</div>;
  }
}

export default Game;
