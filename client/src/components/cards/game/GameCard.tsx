import React from 'react';
import { Box } from '@mui/material';
import { box_basic_props } from '@/mui_props/box';
type Props = {
  game: any;
};

function GameCard({ game }: Props) {
  return (
    <>
      <Box sx={box_basic_props}>
        <h2>{game.title}</h2>
      </Box>
    </>
  );
}

export default GameCard;
