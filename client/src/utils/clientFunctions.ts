import api from '@/classes/api';
export const submitForm = async (e: React.FormEvent<HTMLFormElement>) => {
  e.preventDefault();
  const formData = new FormData(e.currentTarget);
  const data = Object.fromEntries(formData);
  try {
    await api.user_post(data);
  } catch (err: any) {
    throw Error(err);
  }
  console.log(data);
};
