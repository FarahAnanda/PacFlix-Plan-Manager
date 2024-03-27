# PacFlix Plan Management System

## Overview

The PacFlix Plan Management System is a Python program designed to manage user subscriptions and plans for a video streaming platform called PacFlix. This program allows users to check available plans, examine active subscriptions, upgrade their current plans, and sign up as new users with referral codes.

## Code Structure

### main.py

[`main.py`](main.py) contains the main code for the PacFlix Plan Management System. It includes the following classes and methods:

### User Class

The `User` class represents an existing user of the PacFlix platform. Each user object has attributes such as username, current plan, and duration of the subscription.

#### Methods:

- `check_benefit()`: Displays the benefits of each plan available on PacFlix.
- `check_plan(username)`: Checks the current plan and subscription duration for a given username.
- `upgrade_plan(username, upgrade_plan)`: Upgrades the user's current plan to a higher plan, calculating the total payment after discounts based on the subscription duration.

### NewUser Class

The `NewUser` class represents a new user signing up for PacFlix with a referral code. Each new user object has attributes such as username and referral code.

#### Methods:

- `get_referral_code(data)`: Retrieves referral codes from the existing user data.
- `pick_plan(new_plan, referral_code)`: Allows a new user to select a plan and calculates the total payment after discounts using a referral code.

## Usage

1. **Checking Available Plans**: Use the `check_benefit()` method to display the benefits of each plan available on PacFlix.

2. **Checking Current Plan**: Use the `check_plan(username)` method to check the current plan and subscription duration for a specific username.

3. **Upgrading Plan**: Use the `upgrade_plan(username, upgrade_plan)` method to upgrade a user's current plan to a higher plan. Provide the username and the desired upgrade plan as arguments.

4. **Signing Up as a New User**: Use the `pick_plan(new_plan, referral_code)` method to sign up as a new user with a referral code. Provide the chosen plan and referral code as arguments.
