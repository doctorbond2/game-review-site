'use client';
import React from 'react';
import { Button } from '@mui/material';
import Link from 'next/link';
import library from '@/classes/libraryRouter';
type Props = {
  gameId: string;
};

function GoToGameButton({ gameId }: Props) {
  return (
    <>
      <Link href={library.goToGame(gameId)}>
        <Button> Game page</Button>
      </Link>
    </>
  );
}

export default GoToGameButton;
