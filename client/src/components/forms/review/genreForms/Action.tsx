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

function Action() {
  return (
    <>
      <>
        <h2>Action score</h2>
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
export default Action;
