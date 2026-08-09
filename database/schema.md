# Klino Database Schema

## Overview

The Klino database stores all information related to customers, agents, bookings, payments, and reviews.

---

# Customer

Fields

- Customer ID
- First Name
- Last Name
- Email
- Phone Number
- Password (encrypted)
- Address
- Profile Photo
- Account Status
- Date Joined

---

# Agent

Fields

- Agent ID
- First Name
- Last Name
- Phone Number
- Email
- Password (encrypted)
- Government ID
- Selfie Verification
- Address
- Years of Experience
- Verification Status
- Rating
- Jobs Completed
- Earnings Balance
- Date Joined

---

# Booking

Fields

- Booking ID
- Customer ID
- Agent ID
- Service Type
- Property Type
- Address
- Date
- Time
- Notes
- Before Photos
- After Photos
- Booking Status
- Total Price

---

# Payment

Fields

- Payment ID
- Booking ID
- Customer ID
- Amount
- Payment Status
- Escrow Status
- Transaction Date

---

# Review

Fields

- Review ID
- Booking ID
- Customer ID
- Agent ID
- Rating
- Comment
- Date

---

# Admin

Fields

- Admin ID
- Name
- Email
- Role