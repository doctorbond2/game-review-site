'use client';
import React from 'react';
import {
  FormControl,
  FormControlLabel,
  FormLabel,
  RadioGroup,
  Radio,
} from '@mui/material';
import Score from '../Score';
type Props = {
  order: number;
};
function Action({ order }: Props) {
  return (
    <>
      <li id={'score-radio-' + order.toString()}>
        <h2>Action score</h2>
        <Score scoreName="action" />
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
export default Action;
