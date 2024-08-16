import axios from 'axios';
const baseURL = process.env.NEXT_PUBLIC_API_BASE_URL;
const clientInstance = axios.create({
  baseURL,
  timeout: 1000,
  headers: {
    'X-Custom-Header': 'foobar',
    'Content-Type': 'application/json',
  },
});
const adminInstance = axios.create({
  baseURL,
  timeout: 1000,
  headers: {
    'X-Custom-Header': 'foobar',
    'Content-Type': 'application/json',
  },
});
const userInstance = axios.create({
  baseURL,
  timeout: 1000,
  headers: {
    'X-Custom-Header': 'foobar',
    'Content-Type': 'application/json',
  },
});
userInstance.interceptors.request.use();
userInstance.interceptors.response.use();

adminInstance.interceptors.request.use();
adminInstance.interceptors.response.use();

clientInstance.interceptors.request.use();
clientInstance.interceptors.response.use();
export { clientInstance, adminInstance, userInstance };
