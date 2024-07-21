import React from 'react';
import Action from './genreForms/Action';
import Adventure from './genreForms/Adventure';
import Platformer from './genreForms/Platformer';
type Props = {
  genres: string[];
};

function ReviewFormList({ genres }: Props) {
  if (genres) {
    const forms = genres.map((genre, index) => {
      if (genre === 'Action') {
        return (
          <>
            <Action />
          </>
        );
      }
      if (genre === 'Adventure') {
        return (
          <>
            <Adventure />
          </>
        );
      }
      if (genre === 'Platformer') {
        return (
          <>
            <Platformer />
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
