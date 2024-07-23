import React from 'react';
import Score from '../Score';
type Props = {
  order: number;
};

function Platformer({ order }: Props) {
  return (
    <>
      <li id={'score-radio-' + order}>
        <h2>Levels score</h2>
        <Score scoreName="levels" />
        <textarea></textarea>
      </li>
    </>
  );
}

export default Platformer;
