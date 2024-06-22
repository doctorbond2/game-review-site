import React, { useEffect } from 'react';
import {
  userInstance,
  clientInstance,
  adminInstance,
} from '@/classes/axiosInstance';
import axios from 'axios';
type Props<T> = {
  data: T | null;
  error: string | Error | null;
  loading: boolean;
};

const useFetch = <T>(url: string, tier: number): Props<T> => {
  if (tier < 1 || tier > 3) throw new Error('Invalid tier');
  if (!url) throw new Error('Invalid url');
  let a = clientInstance;
  if (tier === 1) {
    a = clientInstance;
  } else if (tier === 2) {
    a = userInstance;
  } else if (tier === 3) {
    a = adminInstance;
  }

  const [data, setData] = React.useState<T | null>(null);
  const [error, setError] = React.useState<string | null>(null);
  const [loading, setLoading] = React.useState<boolean>(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await a.get(url);
        setData(res.data);
      } catch (e: any) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [a, url]);
  return { data, error, loading };
};
export default useFetch;
