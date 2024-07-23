import api from '@/classes/api';
import endpoints from '@/classes/endpoints';
import { AxiosResponse } from 'axios';

export const getDataById = async (
  endpoint: string,
  id: string
): Promise<AxiosResponse> => {
  const res = await api.get(endpoint + id);
  if (res.status !== 200) {
    throw new Error('Error fetching data');
  }
  return res;
};
