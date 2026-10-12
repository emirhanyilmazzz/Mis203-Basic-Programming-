# Lab 04: Savings Goal Planner

## Testing and Reflection

### Test Case Run
- **Test Inputs:**
  - Starting Balance: `1000`
  - Monthly Deposit: `500`
  - Interest Rate: `1`
  - Savings Goal: `3000`
- **Expected & Observed Result:**
  - Goal reached in: `4 months`
  - Final Balance: `3070.80 TRY`
  - Total Interest Earned: `70.80 TRY`

### Boundary Test
- Tested `starting_balance: 3000` with `savings_goal: 3000`.
- Verified that the simulation does not print any table rows and immediately reports that the goal has already been met in 0 months.

### Change Made After Testing
- Initially, when inputting negative numbers or zero for deposit/goal, the program didn't re-prompt correctly. I updated the input validation to follow the `while condition:` re-prompt pattern to enforce strictly positive deposits and non-negative balances before starting the simulation loop.

