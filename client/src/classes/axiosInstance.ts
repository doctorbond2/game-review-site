import axios from 'axios';

export const clientInstance = axios.create({
  baseURL: 'http://localhost:3000',
  timeout: 1000,
  headers: { 'X-Custom-Header': 'foobar' },
});
export const adminInstance = axios.create({
  baseURL: 'http://localhost:3000',
  timeout: 1000,
  headers: { 'X-Custom-Header': 'foobar' },
});
export const userInstance = axios.create({
  baseURL: 'http://localhost:3000',
  timeout: 1000,
  headers: { 'X-Custom-Header': 'foobar' },
});
