import React from 'react';
import { FormControl, FormLabel } from '@mui/material';
import Score from './Score';
type Props = {};

function ReviewForm({}: Props) {
  return (
    <>
      <FormControl>
        <FormLabel>Game review</FormLabel>
        <Score />
      </FormControl>
    </>
  );
}

export default ReviewForm;
