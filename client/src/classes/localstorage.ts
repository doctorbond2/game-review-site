class LocalStorage {
  constructor() {}
  static STORAGE_KEY = process.env.NEXT_PUBLIC_LOCAL_STORAGE_KEY || 'error';
  static setTokens<T>(value: T) {
    localStorage.setItem(this.STORAGE_KEY, JSON.stringify(value));
  }
  static getTokens() {
    return JSON.parse(localStorage.getItem(this.STORAGE_KEY) || '{}');
  }
  static getItem(key: string) {
    localStorage.getItem(key);
  }
  static removeItem(key: string) {
    localStorage.removeItem(key);
  }
  static clear() {
    localStorage.clear();
  }
  static replace(key: string, value: string) {
    localStorage.removeItem(key);
    localStorage.setItem(key, value);
  }
}
export default LocalStorage;
