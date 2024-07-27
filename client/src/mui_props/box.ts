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
export const footer_box_props = {
  width: '100%',
  display: 'flex',
  justifyContent: 'space-around',
  alignItems: 'center',
  bgcolor: 'primary.main',
  position: 'fixed',
  bottom: 0,
  height: '8vh',
};
export const header_box_props = {
  width: '100%',
  display: 'flex',
  justifyContent: 'space-around',
  alignItems: 'centeer',
  bgcolor: 'primary.main',
  position: 'fixed',
  top: 0,
  height: '6vh',
  borderBottom: 1,
};
export const body_container_props = {
  backgroundColor: 'red',
  height: '100%',
};
