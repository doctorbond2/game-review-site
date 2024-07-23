import React from 'react';
import Score from '../Score';
type Props = {
  order: number;
};

function Adventure({ order }: Props) {
  return (
    <>
      <li id={'score-radio-' + order}>
        <h2>Story score</h2>
        <Score scoreName="story" />
        <textarea></textarea>
      </li>
      <li id={'score-radio-' + (order + 1).toString()}>
        <h2>Combat score</h2>
        <Score scoreName="combat" />
        <textarea></textarea>
      </li>
    </>
  );
}
export default Adventure;
