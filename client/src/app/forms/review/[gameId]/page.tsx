import React from 'react';
import ReviewForm from '@/components/forms/review/ReviewForm';
type Props = {
  params: {
    gameId: string;
  };
};

function newGameReview({ params }: Props) {
  const { gameId } = params;
  return (
    <>
      <h2 style={{ color: 'red' }}>Posting review for game: {gameId}</h2>
      <ReviewForm {...{ gameId }} />
    </>
  );
}

export default newGameReview;
