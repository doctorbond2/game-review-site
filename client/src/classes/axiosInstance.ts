import axios from 'axios';
const baseURL = process.env.API_BASE_URL;
export const clientInstance = axios.create({
  baseURL,
  timeout: 1000,
  headers: { 'X-Custom-Header': 'foobar' },
});
export const adminInstance = axios.create({
  baseURL,
  timeout: 1000,
  headers: { 'X-Custom-Header': 'foobar' },
});
export const userInstance = axios.create({
  baseURL,
  timeout: 1000,
  headers: { 'X-Custom-Header': 'foobar' },
});
