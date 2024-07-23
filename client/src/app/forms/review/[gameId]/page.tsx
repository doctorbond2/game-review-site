import React from 'react';
import ReviewForm from '@/components/forms/review/ReviewForm';
import { AxiosResponse } from 'axios';
import endpoints from '@/classes/endpoints';
import { getDataById } from '@/utils/serverFunctions';
import { retrieveGenres } from '@/utils/formatFromData';
type Props = {
  params: {
    gameId: string;
  };
};

async function newGameReview({ params }: Props) {
  try {
    const { gameId } = params;
    const gameData = await getDataById(endpoints.getOneGame, gameId);
    const genres = retrieveGenres(gameData.data);
    console.log(genres);
    return (
      <>
        <h2 style={{ color: 'red' }}>Posting review for game: {gameId}</h2>
        <ReviewForm {...{ genres }} />
      </>
    );
  } catch (err) {
    // fix later
    return <div>no Data</div>;
  }
}

export default newGameReview;
