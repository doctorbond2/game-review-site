import axios from 'axios';
import { clientInstance, adminInstance, userInstance } from './axiosInstance';

class Instance {
  constructor() {}
  client = clientInstance;
  admin = adminInstance;
  user = userInstance;
  get = async (url: string) => {
    console.log(url);
    try {
      const res = await this.client.get(url);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  post = async (url: string, data: any) => {
    try {
      const res = await this.client.post(url, data);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  put = async (url: string, data: any) => {
    try {
      const res = await this.client.put(url, data);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  delete = async (url: string) => {
    try {
      const res = await this.client.delete(url);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  admin_get = async (url: string) => {
    try {
      const res = await this.admin.get(url);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  admin_post = async (url: string, data: any) => {
    try {
      const res = await this.admin.post(url, data);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  admin_put = async (url: string, data: any) => {
    try {
      const res = await this.admin.put(url, data);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  admin_delete = async (url: string) => {
    try {
      const res = await this.admin.delete(url);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  user_get = async (url: string) => {
    try {
      const res = await this.user.get(url);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  user_post = async <T>(url: string, data: T) => {
    try {
      const res = await this.user.post(url, data);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  user_put = async (url: string, data: any) => {
    try {
      const res = await this.user.put(url, data);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
  user_delete = async (url: string) => {
    try {
      const res = await this.user.delete(url);
      return res;
    } catch (e: any) {
      throw new Error(e.message);
    }
  };
}
const api = new Instance();
export default api;
