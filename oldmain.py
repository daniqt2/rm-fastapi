# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session
# from typing import List

# from crud import create_user, create_user_item, get_user_by_email, get_users, get_items, get_user
# from schemas import User, UserCreate, TeamCreate, Team
# from database import SessionLocal, engine
# from models import Base

# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/users/", response_model=User)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return create_user(db=db, user=user)


# @app.get("/users/", response_model=List[User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=Team)
# def create_item_for_user(
#     user_id: int, item: TeamCreate, db: Session = Depends(get_db)
# ):
#     return create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[Team])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = get_items(db, skip=skip, limit=limit)
#     return items