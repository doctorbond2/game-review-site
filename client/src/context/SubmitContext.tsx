'use client';
import React, { createContext, useContext, useState } from 'react';
import { TYPE_SubmitContext as SC } from '@/types/types_submit';
import { defaultSubmitContext } from '@/types/default_submit';
import { isEmail } from '@/utils/clientFunctions';
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

  const submit = (data: Record<string, any>, type: string) => {
    if (type === 'login') {
      if (isEmail(data['user-login-username-or-email'])) {
        data['email'] = data['user-login-username-or-email'];
        delete data['user-login-username-or-email'];
        console.log('Email');
      } else {
        data['username'] = data['user-login-username-or-email'];
        delete data['user-login-username-or-email']; // Remove the old key if necessary
        console.log('Username');
      }
    }
  };
  return (
    <SubmitContext.Provider
      value={{ submitData, setSubmitData, resetSubmit, submit }}
    >
      {children}
    </SubmitContext.Provider>
  );
}

export default SubmitProvider;
