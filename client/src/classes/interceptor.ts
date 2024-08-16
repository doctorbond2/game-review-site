import { AxiosInstance } from 'axios';
import { userInstance } from './axiosInstance';
import { access } from 'fs';
import LocalStorage from './localstorage';
export default class Interceptor<T> {
  config: {
    headers: {};
  };
  constructor(instance: T) {
    this.config = {
      headers: {},
    };
    if (instance === 'user') {
      this.config = {
        headers: {
          Authorization: `Bearer ${LocalStorage.getItem('token')}`,
        },
      };
    }
  }
}
