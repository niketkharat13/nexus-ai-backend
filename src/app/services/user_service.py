from fastapi import HTTPException
from pydantic import BaseModel

from app.schemas.user import UserCreateRequest

class UserService:
    def __init__(self):
        self._users: list[dict] = []
        self._next_id = 1
        
    def create_user(self, user: UserCreateRequest):
        new_user = {
            **user.model_dump(),
            "id": self._next_id
        }
        self._users.append(new_user)
        self._next_id += 1
        return new_user
        
    def get_users(self, name, sort_by, skip, limit):
        filtered = [
            u for u in self._users
            if not name or name.lower() in u['name'].lower()
        ]
        
        if sort_by:
            filtered = sorted(
                filtered,
                key=lambda u: (
                    u[sort_by].lower() if isinstance(u[sort_by], str) else u[sort_by]
                ),
            )
        return filtered[skip: skip + limit]
        
        
    
    def update_user(self, user_id, data):
        for user in self._users:
            if user['id'] == user_id:
                user.update(data.model_dump())
                return user
        raise HTTPException(status_code=404, detail="User not found")
        
    def get_user_by_id(self, user_id):
        for user in self._users:
            if user['id'] == user_id:
                return user
        raise HTTPException(status_code=404, detail="User not found")
    
    def delete_user(self, user_id):
        for user in self._users:
            if user['id'] == user_id:
                self._users = [e for e in self._users if e['id'] != user_id]
                return
        raise HTTPException(status_code=404, detail="User not found")

        

        
    