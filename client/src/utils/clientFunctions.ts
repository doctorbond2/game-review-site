import api from '@/classes/api';
import endpoints from '@/classes/endpoints';
import { convertFormDataFields } from './formatFromData';
export const submitReviewForm = async (e: React.FormEvent<HTMLFormElement>) => {
  e.preventDefault();
  const formData = new FormData(e.currentTarget);
  const data = Object.fromEntries(formData);
  const preparedData = convertFormDataFields(data);
  console.log(preparedData);
  try {
    await api.user_post(endpoints.postOneReview, preparedData);
  } catch (err: any) {
    throw Error(err);
  }
  console.log(data);
};
