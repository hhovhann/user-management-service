# user-management-service
User Management Service Python Demo Application
- This setup provides a robust foundation for a user management backend using FastAPI and SQLAlchemy with PostgreSQL, including Docker deployment and email notifications. 

## Running the Application

- Build and Start Docker Containers `docker-compose up --build`
- Migrate Database (if needed) Depending on the tooling you use for database migrations (e.g., Alembic), make sure to run migrations to set up your database schemas.
- Access the Application Open your browser and navigate to http://localhost:8000.


## Testing the Application

- User Registration
```
curl -X POST "http://localhost:8000/api/users/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"email":"test@example.com", "password":"testpassword"}'
```

- Authentication
```
curl -X POST "http://localhost:8000/token" -d "username=test@example.com&password=testpassword"
```


