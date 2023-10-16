# Selenium BDD Framework README

This repository contains automated tests for DarkwebId login page using selenium, behave, 
pyhamcrest, invoke, 'BDD framework'.

## Prerequisites

Before you can run the tests, make sure you have the following installed:

- Python 3: You can download it from the [Python website](https://www.python.org/downloads/).
- pipenv: You can install it using pip with the following command:

  ```bash
  pip install pipenv

# Installation
## Clone the repository:
-```git clone https://github.com/AlehHpro/selenium_classic_framework.git``` 
#### or
-```git clone git@github.com:AlehHpro/selenium_bdd_framework.git```   

  cd selenium_bdd_framework

## Install necessary packages:
-```pipenv install```

# Running Tests

### NOTE: In credentials.json file change VALID_EMAIL and VALID_PASSWORD variables to a valid values.

1. Open your terminal.

2. Navigate to the project directory using the `cd` command. For example:

   ```bash
   cd */selenium_bdd_framework

3. To run the automated tests for all features together, use the following command:
   ```bash
   invoke run --browser=CH (for normal mode)
   invoke run --browser=CH_HL (for headless mode)
   or using behave
   behave (if you want to use config from behave.ini file)
   or
   behave -D browser=... (specify browser)

4. To run the automated tests for a specific scenario, use the following command specifying
   scenario name (e.g.: --tags=forgot_password_1) :
   ```bash
   invoke run --tags=forgot_password_1 --browser=CH (for normal mode)
   invoke run --tags=forgot_password_1 --browser=CH_HL (for headless mode)
   or using behave
   behave --tags=... (specify scenario) -D browser=... (specify browser)

# Test Cases
## The following selenium test cases are included:

1. Login positive/negative - login.feature
2. Forgot password - forgot_password.feature
3. Learn more about KaseyaOne - login_with_k1.feature

