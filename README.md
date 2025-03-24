# Roohi Site

Roohi Site is a **custom boutique eCommerce platform** built using **Django** and **Tailwind CSS**. It allows users to browse dresses, place custom orders, and leave reviews.

## Features

✅ **User Authentication** - Sign up, log in, and manage profiles.  
✅ **Storefront** - Display available dress designs beautifully.  
✅ **Reviews & Ratings** - Customers can add reviews and see feedback.  
✅ **Custom Order System** - Users can place orders with their specific measurements and preferences.  
✅ **Manual UPI Payments** - Customers pay via UPI and upload payment proof.  
✅ **Admin Panel** - Manage orders, update statuses, and review payments.  

## Tech Stack

- **Backend**: Django & PostgreSQL  
- **Frontend**: HTML, Tailwind CSS  
- **Authentication**: Django Auth  
- **Database**: PostgreSQL  

## Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/hishamthajudheen/roohi-site.git
   cd roohi-site
   ```

2. **Create a virtual environment & install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

- Visit `http://127.0.0.1:8000/` to browse the store.
- Sign up/log in to leave reviews and place orders.
- Fill in the custom order form and pay via UPI.
- Admins can manage orders via the Django admin panel.

## Screenshots


![Homepage](https://github.com/hishamthajudheen/roohi-site/blob/master/screenshots/store-front.png)
![Product Page](https://github.com/hishamthajudheen/roohi-site/blob/master/screenshots/product-details.png)
![User Registration](https://github.com/hishamthajudheen/roohi-site/blob/master/screenshots/signup.png)
![User Revies](https://github.com/hishamthajudheen/roohi-site/blob/master/screenshots/review-list.png) (https://github.com/hishamthajudheen/roohi-site/blob/master/screenshots/review-add.png)
## To-Do

- [ ] Improve order management in the admin panel
- [ ] Automate UPI payment verification
- [ ] Deploy to a production server

## Contributing
Feel free to submit PRs or open issues if you find any bugs or have feature suggestions.

## License
This project is **private** unless specified otherwise.

---
🚀 Built by [Hisham Thajudeen](https://github.com/hishamthajudheen)
