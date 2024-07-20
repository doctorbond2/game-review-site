import React from 'react';
import ReviewForm from '@/components/forms/review/ReviewForm';
type Props = {
  params: {
    gameId: string;
  };
};

function newGameReview({ params }: Props) {
  return (
    <>
      <h2 style={{ color: 'red' }}>Posting review for game: {params.gameId}</h2>
      <ReviewForm />
    </>
  );
}

export default newGameReview;
