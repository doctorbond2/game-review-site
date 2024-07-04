import { Translate } from '@mui/icons-material';
import { transform } from 'next/dist/build/swc';

export const box_basic_props = {
  justifyContent: 'center',
  border: 1,
  borderColor: 'primary.main',
  borderRadius: 1,
  p: 2,
  m: 2,
  bgcolor: 'primary.light',
  color: 'white',
  width: '40vw',
  height: '10vh',
  display: 'flex',
  alignItems: 'center',
  textAlign: 'center',
  fontSize: '1.5rem',
  fontWeight: 'bold',
  fontFamily: 'Roboto',
  boxShadow: 3,
  '&:hover': {
    bgcolor: 'primary.dark',
    cursor: 'pointer',
    Translate: 'transform 0.5s',
    transform: 'scale(1.03)',
  },
};
