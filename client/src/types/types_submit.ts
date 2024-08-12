export type TYPE_SubmitContext = {
  setSubmitData: any;
  submitData: any;
  resetSubmit: () => void;
  submit: (data: Record<string, any>, type: string) => void;
};
export type TYPE_loginData = {
  password?: string;
  'user-login-username-or-email'?: string;
  email?: string;
  username?: string;
};
