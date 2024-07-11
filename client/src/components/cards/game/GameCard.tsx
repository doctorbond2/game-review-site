import React from 'react';
import { Box, Card } from '@mui/material';
import { box_basic_props } from '@/mui_props/box';
import GoToGameButton from './GoToGameButton';
type Props = {
  game: any;
};

function GameCard({ game }: Props) {
  console.log(game);
  return (
    <>
      <Box sx={box_basic_props}>
        <h2>{game.title}</h2>
        <br />
        <h3>{game.genres}</h3>
        <GoToGameButton gameId={game.id} />
      </Box>
    </>
  );
}

export default GameCard;
