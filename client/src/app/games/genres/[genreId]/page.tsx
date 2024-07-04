import React from 'react';

function Genre({
  params,
}: {
  params: {
    genreId: string;
  };
}) {
  console.log(params.genreId);
  return (
    <div>
      {params.genreId}
      <div>ag d</div>
    </div>
  );
}

export default Genre;
