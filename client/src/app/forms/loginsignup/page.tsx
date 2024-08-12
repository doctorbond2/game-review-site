import React from 'react';
import LoginForm from '@/components/forms/user/LoginForm';
import { Box } from '@mui/material';
type Props = {};

function LoginSignup({}: Props) {
  return (
    <>
      <Box>
        <LoginForm />
      </Box>
    </>
  );
}

export default LoginSignup;
