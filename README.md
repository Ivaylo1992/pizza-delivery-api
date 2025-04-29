# 🍕 Pizza Delivery API

A simple API for managing pizza orders, customers, and delivery information.

---

## 🚀 Features

- Create, read, update, and delete pizza orders
- Manage customer details
- Track delivery status
- Search pizzas by type, size, and toppings
- Authentication & authorization (e.g., JWT)
- Detailed API documentation with Swagger UI

---

## 🛠️ Technologies Used

- [Django](https://www.djangoproject.com/) — high-level Python web framework
- [Django REST Framework (DRF)](https://www.django-rest-framework.org/) — toolkit for building Web APIs
- [PostgreSQL](https://www.postgresql.org/) — powerful relational database
- [Djoser](https://djoser.readthedocs.io/en/latest/) or [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) — authentication and token management
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) — automatic generation of Swagger/OpenAPI documentation


---

## ⚡ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Ivaylo1992/pizza-delivery-api.git
cd pizza-delivery-api
```

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up the Database

Set up PostgreSQL or another database of your choice:

1. Create a PostgreSQL database.
2. Configure your database connection in the `pizza_delivery/settings.py` file.
3. Apply migratinons

```bash
python manage.py migrate
```

### 4. Run the Server

To run the server, use the following command:

```bash
uvicorn main:app --reload
```

## 📖 Example API Endpoints

| Method | Endpoint              | Description                    |
|--------|-----------------------|--------------------------------|
| GET    | `/orders/`             | Retrieve all orders            |
| POST   | `/orders/`             | Create a new order             |
| GET    | `/orders/{id}`         | Retrieve a specific order      |
| PUT    | `/orders/{id}`         | Update an order                |
| DELETE | `/orders/{id}`         | Delete an order                |
| GET    | `/customers/{id}`      | Retrieve customer details      |
| POST   | `/customers/`          | Add a new customer             |
| PUT    | `/customers/{id}`      | Update customer information    |

### 📦 Example Order JSON Structure

```json
{
  "id": "uuid",
  "customer_id": "uuid",
  "pizza_type": "Margherita",
  "size": "Large",
  "toppings": ["Olives", "Mushrooms"],
  "status": "Delivered",
  "delivery_address": "123 Pizza St, Pizzaville",
  "price": 15.99
}
```

## 📦 Requirements

- Python 3.8 or newer
- Django
- Django REST framework
- djangorestframework-simplejwt or djoser (for authentication)
- PostgreSQL (or another database)
- drf-yasg (for API docs)

You can install all dependencies by running:

```bash
pip install -r requirements.txt
```

## 💬 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributions

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate for any changes made.
