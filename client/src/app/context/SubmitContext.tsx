'use client';
import React, { createContext, useContext, useState } from 'react';
import { TYPE_SubmitContext as SC } from '@/types/types_submit';
import { defaultSubmitContext } from '@/types/default_submit';

type Props = { children: React.ReactNode };
const SubmitContext = createContext<SC>(defaultSubmitContext);
function SubmitProvider({ children }: Props) {
  const [submitData, setSubmitData] = useState({});
  const useSubmit = useContext(SubmitContext);
  return (
    <>
      <SubmitContext.Provider value={{ submitData, setSubmitData }}>
        {children}
      </SubmitContext.Provider>
    </>
  );
}

export default SubmitProvider;
