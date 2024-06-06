import React from 'react';

type Props = { submitProduct: () => void };

const ProductForm = ({ submitProduct }: Props) => {
  return (
    <>
      <form onSubmit={submitProduct} className="">
        <label htmlFor="name_input_field">Title of product: </label>
        <input
          type="text"
          id="name_input_field"
          className="border border-black"
        />
        <label htmlFor="expiration_date_field"> Expiration date: </label>
        <input type="date" id="expiration_date_field" />
        <button type="submit" className="bg-slate-500 border-t-neutral-400">
          Register product
        </button>
      </form>
    </>
  );
};

export default ProductForm;
