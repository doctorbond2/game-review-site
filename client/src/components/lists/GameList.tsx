'use client';
import React from 'react';
import useFetch from '@/hooks/useFetch';
import endpoints from '@/classes/endpoints';
type Props = {};

function GameList({}: Props) {
  const { data, loading, error } = useFetch(endpoints.getAllGames, 1) as {
    data: any[];
    loading: boolean;
    error: string;
  };

  return (
    <>
      <h2>Game list</h2>
      {data ? (
        <ul id="home-game-list">
          {data.map((item: any, index) => (
            <>{item.title}</>
          ))}
        </ul>
      ) : loading ? (
        <h2>{loading.toString()}</h2>
      ) : error ? (
        <h2>{error.toString()}</h2>
      ) : (
        <h2>No data</h2>
      )}
    </>
  );
}

export default GameList;
