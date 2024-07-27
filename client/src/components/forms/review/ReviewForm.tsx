'use client';
import React from 'react';
import { FormControl, FormLabel, Button } from '@mui/material';
import ReviewFormList from './ReviewFormList';
import { submitReviewForm } from '@/utils/clientFunctions';
type Props = {
  genres: string[];
};

function ReviewForm({ genres }: Props) {
  console.log(genres);

  return (
    <>
      <form onSubmit={(e) => submitReviewForm(e)}>
        <FormControl>
          <FormLabel>Game review</FormLabel>
          <ReviewFormList {...{ genres }} />
          <Button
            type={'submit'}
            id={'review-form-submit-button'}
            name={'review-form-submit-button'}
          >
            Submit form
          </Button>
        </FormControl>
      </form>
    </>
  );
}

export default ReviewForm;
