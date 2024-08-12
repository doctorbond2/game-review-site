'use client';
import React from 'react';
import { FormControl, FormLabel, Button } from '@mui/material';
type Props = {};

function LoginForm({}: Props) {
  return (
    <>
      <form
        id="user-login-form"
        onSubmit={() => {
          console.log('logging in');
        }}
      >
        <FormControl>
          <FormLabel>Username/Email</FormLabel>
          <input
            type="text"
            id="user-login-username-or-email"
            name="user-login-username-or-email"
          />
          <FormLabel>Password</FormLabel>
          <input
            type="password"
            id="user-login-password"
            name="user-login-password"
          />
        </FormControl>
      </form>
    </>
  );
}

export default LoginForm;
