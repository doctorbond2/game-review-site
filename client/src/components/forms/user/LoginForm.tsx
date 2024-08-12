'use client';
import React from 'react';
import { FormControl, FormLabel, Button } from '@mui/material';
import { useSubmit } from '@/context/SubmitContext';
type Props = {};

function LoginForm({}: Props) {
  const { submitData, setSubmitData, submit } = useSubmit();
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSubmitData({ ...submitData, [e.target.name]: e.target.value });
  };
  return (
    <>
      <form
        id="user-login-form"
        onSubmit={() => {
          submit(submitData, 'login');
        }}
      >
        <FormControl>
          <FormLabel>Username/Email</FormLabel>
          <input
            type="text"
            id="user-login-username-or-email"
            name="user-login-username-or-email"
            onChange={handleChange}
          />
          <FormLabel>Password</FormLabel>
          <input
            onChange={handleChange}
            type="password"
            id="user-login-password"
            name="password"
          />
        </FormControl>
      </form>
    </>
  );
}

export default LoginForm;
