
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from sqlalchemy import insert
from app.schemas import CreateUser, ApdateUser, CreateTask, UpdateTask

from slugify import slugify
from sqlalchemy import select
from sqlalchemy import update



router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users():
    pass


@router.get('/user_id')
async def user_by_id():
    pass


@router.post('/create')
async def create_user():
    pass


@router.put('/update')
async def update_user()
    pass          


@router.delete('/delete')
async def delete_user():
    pass
