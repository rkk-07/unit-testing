#include <unity.h>
#include "calc.c"

/**
 * @brief This function executes before each test case function
 */
void
setUp(void)
{

}

/**
 * @brief This function executes after each test case function
 */
void
tearDown(void)
{

}

void
test_addtest(void)
{
/* ----------------------------- SETUP TEST DATA ---------------------------- */
    int16_t out_i16;
/* ------------------------------ PRECONDITION ------------------------------ */
  
/* ------------------------ SETUP EXPECTED CALL CHAIN ----------------------- */

/* ------------------------ CALL FUNCTION UNDER TEST ------------------------ */
    add(100, 200, &out_i16);
/* --------------------------- VERIFY TEST RESULTS -------------------------- */
  TEST_ASSERT_EQUAL(300, out_i16);
}