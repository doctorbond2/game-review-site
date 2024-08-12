export type TYPE_SubmitContext = {
  setSubmitData: any;
  submitData: any;
  resetSubmit: () => void;
  submit: (data: Record<string, any>, type: string) => void;
};
