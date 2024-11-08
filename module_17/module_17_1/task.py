
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from sqlalchemy import insert
from app.schemas import CreateUser, ApdateUser, CreateTask, UpdateTask

from slugify import slugify
from sqlalchemy import select
from sqlalchemy import update



router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks():
    pass

@router.get('/task_id')
async def task_by_id():
    pass

@router.post('/create')
async def create_task():
    pass

@router.put('/update')
async def update_task():
    pass

@router.delete('/delete')
async def delete_tasks():
    pass
