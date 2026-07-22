# Klino Database Design

## 1. Users Table

Stores all customer accounts.

Fields:

- id
- full_name
- username
- email
- phone_number
- password
- address
- profile_photo
- verification_status
- created_at


---

## 2. Agents Table

Stores cleaner accounts.

Fields:

- id
- user_id
- full_name
- phone_number
- address
- profile_photo
- government_id
- proof_of_address
- bank_details
- verification_status
- rating
- created_at


---

## 3. Services Table

Types of cleaning offered.

Fields:

- id
- service_name
- description
- base_price


Example:

- Home Cleaning
- Office Cleaning
- Deep Cleaning
- Move Cleaning


---

## 4. Bookings Table

Stores cleaning appointments.

Fields:

- id
- customer_id
- agent_id
- service_id
- address
- date
- time
- status
- total_price
- created_at


Booking Status:

- Pending
- Accepted
- In Progress
- Completed
- Cancelled


---

## 5. Photos Table

Stores before and after cleaning pictures.

Fields:

- id
- booking_id
- agent_id
- photo_type
- image_url
- uploaded_at


Photo Type:

- Before
- After


---

## 6. Payments Table

Stores money movement.

Fields:

- id
- booking_id
- customer_id
- amount
- payment_status
- escrow_status
- created_at


Payment Status:

- Pending
- Paid
- Released
- Refunded


---

## 7. Reviews Table

Stores customer ratings.

Fields:

- id
- booking_id
- customer_id
- agent_id
- rating
- comment
- created_at


---

## 8. Notifications Table

Stores alerts.

Fields:

- id
- user_id
- message
- read_status
- created_at