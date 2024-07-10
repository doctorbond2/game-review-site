import { Button } from '@mui/material';
import React from 'react';
import { redirect } from 'next/navigation';
export default function NotFound() {
  //   const redirectToHome = () => {
  //     setTimeout(() => {
  //       redirect('/');
  //     }, 3000);
  //   };
  //   redirectToHome();
  return (
    <div>
      <h2>Page not found</h2>
    </div>
  );
}
