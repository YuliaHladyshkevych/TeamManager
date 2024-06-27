# Test REST API Implementation

This project demonstrates a REST API for managing "teams" and "people in those teams" using Django Rest Framework. The API allows performing CRUD (Create, Read, Update, Delete) operations for "team" and "person" objects.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/YuliaHladyshkevych/TeamManager.git
    cd TeamManager
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # for Windows: venv\Scripts\activate
    ```

3. Install required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Populate the database with initial data (optional):
    ```sh
    python manage.py populate_data
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Using the API

### Teams

- **Get a list of teams:**
  ```http
  GET /teams/
  ```
  
- **Create a new team:**
  ```http
  POST /teams/
  ```
  Request body:
  ```json
  {
    "name": "Team Name",
    "description": "Team Description"
  }
  ```

- **Get a team by ID:**
  ```http
  GET /teams/{id}/
  ```

- **Update a team by ID:**
  ```http
  PUT /teams/{id}/
  ```
  Request body:
  ```json
  {
    "name": "Updated Team Name",
    "description": "Updated Team Description"
  }
  ```

- **Delete a team by ID:**
  ```http
  DELETE /teams/{id}/
  ```

- **Get members of a team:**
  ```http
  GET /teams/{id}/members/
  ```

- **Add a member to a team:**
  ```http
  POST /teams/{id}/add_member/
  ```
  Request body:
  ```json
  {
    "person_id": 1
  }
  ```

- **Filter members by first_name or/and last_name:**
  ```http
  GET /teams/{id}/filter_members/?first_name={first_name}&last_name={last_name}
  ```

### People

- **Get a list of people:**
  ```http
  GET /people/
  ```

- **Create a new person:**
  ```http
  POST /people/
  ```
  Request body:
  ```json
  {
    "first_name": "First Name",
    "last_name": "Last Name",
    "email": "email@example.com",
    "team": 1
  }
  ```

- **Get a person by ID:**
  ```http
  GET /people/{id}/
  ```

- **Update a person by ID:**
  ```http
  PUT /people/{id}/
  ```
  Request body:
  ```json
  {
    "first_name": "Updated First Name",
    "last_name": "Updated Last Name",
    "email": "updated.email@example.com",
    "team": 2
  }
  ```

- **Delete a person by ID:**
  ```http
  DELETE /people/{id}/
  ```
  
- **Filter persons by first_name or/and last_name:**
  ```http
  GET /people/filter_persons/?first_name={first_name}&last_name={last_name}
  ```