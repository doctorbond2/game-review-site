import axios from 'axios';
const baseURL = process.env.NEXT_PUBLIC_API_BASE_URL;
export const clientInstance = axios.create({
  baseURL,
  timeout: 1000,
  headers: {
    'X-Custom-Header': 'foobar',
    'Content-Type': 'application/json',
  },
});
export const adminInstance = axios.create({
  baseURL,
  timeout: 1000,
  headers: {
    'X-Custom-Header': 'foobar',
    'Content-Type': 'application/json',
  },
});
export const userInstance = axios.create({
  baseURL,
  timeout: 1000,
  headers: {
    'X-Custom-Header': 'foobar',
    'Content-Type': 'application/json',
  },
});
