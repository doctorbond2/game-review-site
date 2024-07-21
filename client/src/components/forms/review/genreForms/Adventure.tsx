import React from 'react';
import Score from '../Score';
type Props = {};

function Adventure() {
  return (
    <>
      <>
        <h2>Story score</h2>
        <Score />
        <textarea></textarea>
      </>

      <>
        <h2>Combat score</h2>
        <Score />
        <textarea></textarea>
      </>
    </>
  );
}
export default Adventure;
