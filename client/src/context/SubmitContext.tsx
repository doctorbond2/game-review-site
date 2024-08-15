'use client';
import React, { createContext, useContext, useState } from 'react';
import {
  TYPE_SubmitContext as SC,
  TYPE_PasswordChangeData,
  TYPE_RegisterData,
} from '@/types/types_submit';
import { defaultSubmitContext } from '@/types/default_submit';
import { isEmail } from '@/utils/clientFunctions';
import { TYPE_SubmitData, TYPE_LoginData } from '@/types/types_submit';
type Props = { children: React.ReactNode };

const SubmitContext = createContext<SC>(defaultSubmitContext);

export function useSubmit() {
  const context = useContext(SubmitContext);
  if (!context) {
    throw new Error('useSubmit must be used within a SubmitProvider');
  }
  return context;
}

function SubmitProvider({ children }: Props) {
  const [submitData, setSubmitData] = useState({});

  const resetSubmit = () => setSubmitData({});

  const submit = <T extends keyof TYPE_SubmitData>(
    data: TYPE_SubmitData[T],
    type: T
  ) => {
    if (type === 'login') {
      const loginData = data as TYPE_LoginData;
      if (isEmail(loginData['user-login-username-or-email'] as string)) {
        loginData['email'] = loginData['user-login-username-or-email'];
        delete loginData['user-login-username-or-email'];
        console.log('Email');
      } else {
        loginData['username'] = loginData['user-login-username-or-email'];
        delete loginData['user-login-username-or-email'];
        console.log('Username');
      }
    }
    if (type == 'register') {
      const registerData = data as TYPE_RegisterData;
      if (isEmail(registerData.email)) {
        console.log('ok');
      }
      if (type == 'password_change') {
        const passwordChangeData = data as TYPE_PasswordChangeData;
      }
    }
  };
  // const submission = <InputData, ParsedData>(
  //   data: InputData
  // ): ParsedData | null => {
  //   return null;
  // };

  return (
    <SubmitContext.Provider
      value={{ submitData, setSubmitData, resetSubmit, submit }}
    >
      {children}
    </SubmitContext.Provider>
  );
}

export default SubmitProvider;
