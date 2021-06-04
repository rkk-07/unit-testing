#include <stdio.h>
#include <stdint.h>


typedef enum
{
  E_ERROR,
  E_VALID
}status_et;



status_et add(const int16_t i_arg1_i16,
              const int16_t i_arg2_i16,
              int16_t *const o_out_i16)
{
  status_et status_e;
  uint16_t signArg1_u8;
  uint16_t signArg2_u8;
  
  signArg1_u8 = (i_arg1_i16 < 0) ? (uint8_t)1U : 0;

  signArg1_u8 = i_arg1_i16 & 0x7FFF;
  signArg2_u8 = i_arg2_i16 & 0x7FFF;
  *o_out_i16  = i_arg1_i16 + i_arg2_i16;
  if (signArg1_u8 == signArg2_u8) 
  {
    if((*o_out_i16 & 0x7FFF) == signArg1_u8)
    {
       status_e  = E_VALID;
    }
    else
    {
       status_e  = E_ERROR;
    }
  }
  return (status_e);
}