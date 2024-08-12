import React from 'react';
import { FormControl } from '@mui/material';
type Props = {};

function LoginForm({}: Props) {
  return (
    <>
      <form
        id="user-login-form"
        onSubmit={() => {
          console.log('logging in');
        }}
      ></form>
    </>
  );
}

export default LoginForm;
