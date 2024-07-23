'use client';
import React from 'react';
import Action from './genreForms/Action';
import Adventure from './genreForms/Adventure';
import Platformer from './genreForms/Platformer';
import { Button } from '@mui/material';
type Props = {
  genres: string[];
};

function ReviewFormList({ genres }: Props) {
  if (genres) {
    const forms = genres.map((genre, index) => {
      if (genre === 'Action') {
        return (
          <>
            <Action order={index + 1} />
          </>
        );
      }
      if (genre === 'Adventure') {
        return (
          <>
            <Adventure order={index + 1} />
          </>
        );
      }
      if (genre === 'Platformer') {
        return (
          <>
            <Platformer order={index + 1} />
          </>
        );
      }
    });
    return forms;
  } else {
    return <div>forms not loading</div>;
  }
}

export default ReviewFormList;
