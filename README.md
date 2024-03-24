# Food Products Inventory Management System

## Introduction
The Food Products Inventory Management System is an advanced tool designed to help businesses and consumers manage food inventories more efficiently, aiming to reduce food waste and improve sustainability. This system provides real-time inventory tracking, expiration date management, and insightful analytics on food consumption patterns.

## Features
- **Inventory Tracking:** Keep an accurate record of stock levels and manage inventory in real-time.
- **Expiration Management:** Track expiration dates of food items to prioritize consumption and reduce waste.
- **Analytics Dashboard:** Gain insights into consumption trends, inventory turnover, and more to make informed decisions.
- **Notification Alerts:** Automated alerts for low stock levels and approaching expiration dates to prevent stockouts and waste.


## Technology Stack
- **Backend:** Django / Django REST Framework
- **Database:** PostgreSQL
- **Frontend:** HTML & CSS
- **Others:** Celery for asynchronous task processing, Redis for caching, and D3.js for data visualizations

## Getting Started
To get a local copy up and running, follow these simple steps.

### Prerequisites
- Python 3.x
- PostgreSQL
- Redis & Celery

### Installation
1. Clone the repository:
   ```sh
   git clone git@github.com:Irene-Busah/capstone.git
2. Navigate to the project directory:
    ```sh
   cd capstone
3. Install backend dependencies:
    ``` sh
    pip install -r requirements.txt
4. Initialize the database:
    ```sh
    python manage.py migrate
5. Start the backend server:
    ```sh
    python manage.py runserver

