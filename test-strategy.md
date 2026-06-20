# HRMS QA Test Strategy

## Objective
To verify the HRMS payroll system works correctly and prevents incorrect salary processing.

## Critical Flows

### 1. Payroll Calculation
Risk:
Wrong salary calculation.

Impact:
Employees may receive incorrect payment.

Coverage:
Test salary, overtime, deductions, attendance impact.

Prevention:
Add functional and automation tests.

### 2. Employee Management
Risk:
Incorrect employee information.

Impact:
Wrong payroll data.

Coverage:
Test employee creation, update and validation.

Prevention:
Add input validation.

### 3. Attendance and Leave
Risk:
Wrong attendance records.

Impact:
Incorrect salary deduction.

Coverage:
Test attendance, leave approval and payroll connection.

Prevention:
Add regression testing.