'use client';
import React from 'react';
import useFetch from '@/hooks/useFetch';
import endpoints from '@/classes/endpoints';
import GameCard from '../cards/game/GameCard';
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
      {loading ? (
        <h2>Loading...</h2>
      ) : error ? (
        <h2>Error: {error}</h2>
      ) : data && Array.isArray(data) && data.length > 0 ? (
        <ul id="home-game-list">
          {data.map((game: any, index) => (
            <li key={index}>
              <GameCard game={game} />
            </li>
          ))}
        </ul>
      ) : (
        <h2>No data available</h2>
      )}
    </>
  );
}

export default GameList;
