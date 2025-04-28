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

- [FastAPI](https://fastapi.tiangolo.com/) — modern, fast (high-performance) web framework for APIs
- [Uvicorn](https://www.uvicorn.org/) — lightning-fast ASGI server
- [Pydantic](https://docs.pydantic.dev/latest/) — data validation and settings management
- [PostgreSQL](https://www.postgresql.org/) — relational database
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM for database interactions
- [JWT](https://jwt.io/) — authentication

---

## 📂 Project Structure

```bash
pizza-delivery-api/
├── main.py           # Main entry point
├── models.py         # Pydantic models (schemas) & SQLAlchemy models
├── routers/
│   └── order_router.py  # API endpoints for orders
│   └── customer_router.py  # API endpoints for customers
│   └── auth_router.py  # API endpoints for authentication
├── database.py       # Database connection and session management
├── requirements.txt  # Python dependencies
└── alembic/          # Database migrations (if using Alembic)
```

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
2. Configure your database connection in the `database.py` file.

If using Alembic for migrations:

```bash
alembic upgrade head
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
- FastAPI
- Uvicorn
- Pydantic
- PostgreSQL (or another database)
- Alembic (for database migrations)
- JWT Authentication

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
