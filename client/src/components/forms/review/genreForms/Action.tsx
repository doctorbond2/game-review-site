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

export function Action() {
  const form = [
    {
      id: 'action-score',
      element: (
        <>
          <h2>Action score</h2>
          <Score />
          <textarea></textarea>
        </>
      ),
    },
    {
      id: 'combat-score',
      element: (
        <>
          <h2>Combat score</h2>
          <Score />
          <textarea></textarea>
        </>
      ),
    },
  ];
  return form;
}
