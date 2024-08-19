import LocalStorage from './localstorage';
export default class Interceptor {
  private config: { headers: Record<string, string> };
  constructor(instance: string) {
    this.config = { headers: {} };
    if (instance === 'user') {
      const token = LocalStorage.getTokens().access_token;
      this.config.headers.Authorization = token ? `Bearer ${token}` : '';
    }
  }
}
