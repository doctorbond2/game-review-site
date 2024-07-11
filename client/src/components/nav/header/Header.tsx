import React from 'react';
import { header_box_props } from '@/mui_props/box';
import { Box } from '@mui/material';
type Props = {};

function Header({}: Props) {
  return (
    <>
      <Box sx={header_box_props}></Box>
    </>
  );
}

export default Header;
