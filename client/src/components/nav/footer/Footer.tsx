import React from 'react';
import { Box, Stack } from '@mui/material';
import { footer_box_props } from '@/mui_props/box';
type Props = {};

function Footer({}: Props) {
  return (
    <>
      <Box sx={footer_box_props}>
        <Stack>Item 1</Stack>
        <Stack>Item 2</Stack>
        <Stack>Item 3</Stack>
      </Box>
    </>
  );
}

export default Footer;
