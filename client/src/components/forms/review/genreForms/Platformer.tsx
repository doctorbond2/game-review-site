import React from 'react';
import Score from '../Score';
type Props = {};

function Platformer({}: Props) {
  return (
    <>
      <>
        <h2>Levels score</h2>
        <Score />
        <textarea></textarea>
      </>
    </>
  );
}

export default Platformer;
