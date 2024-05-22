'use client';
import React from 'react';
import ProductForm from '@/components/ProductForm';

export default function CreateProduct() {
  const submitProduct = () => {};
  return (
    <>
      <ProductForm {...{ submitProduct }} />
    </>
  );
}
