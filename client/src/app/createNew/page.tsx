'use client';
import React, { useEffect, useState } from 'react';
import ProductForm from '@/components/ProductForm';
import axios from 'axios';
export default function CreateProduct() {
  const [data, setData] = useState();
  const submitProduct = async (data: any) => {
    if (!data) {
      return;
    }
    try {
      const response = await axios.get('http://127.0.0.1:5000/test');
      if (response.data) {
        alert('bra');
        console.log(response.data);
      }
    } catch (err: any) {
      console.log(err.message);
    }
  };
  const testFetch = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/test');
      if (response.data) {
        console.log(response.data);
        setData(response.data);
      }
    } catch (err: any) {
      console.log(err.message);
    }
  };
  useEffect(() => {
    testFetch();
  }, []);
  return (
    <>
      <ProductForm {...{ submitProduct }} />
    </>
  );
}
