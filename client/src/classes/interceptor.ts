import { AxiosInstance } from 'axios';
import { userInstance } from './axiosInstance';
import { access } from 'fs';

class Interceptor<T> {
  config: any;
  constructor(instance: T) {
    if (instance === 'user') {
      this.config = {
        accessToken: '',
        refreshToken: '',
      };
    }
  }
}
const userInterceptor = new Interceptor('user');
export { userInterceptor };
