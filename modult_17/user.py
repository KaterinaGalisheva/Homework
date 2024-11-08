
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models import *
from sqlalchemy import insert
from app.schemas import CreateCategory, CreateProduct

from slugify import slugify
from sqlalchemy import select
from sqlalchemy import update



router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    products = db.scalars(select(Product).where(Product.is_active == True, Product.stock > 0)).all()
    if products is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no product'
        )
    return products


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)]):
    products = db.scalars(select(Product).where(Product.is_active == True, Product.stock > 0)).all()
    if products is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no product'
        )
    return products


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_product: CreateProduct):
    db.execute(insert(Product).values(name=create_product.name,
                                      description=create_product.description,
                                      price=create_product.price,
                                      image_url=create_product.image_url,
                                      stock=create_product.stock,
                                      category_id=create_product.category,
                                      rating=0.0,
                                      slug=slugify(create_product.name)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }



@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], product_slug: str,
                         update_product_model: CreateProduct):
    product_update = db.scalar(select(Product).where(Product.slug == product_slug))
    if product_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no product found'
        )

    db.execute(update(Product).where(Product.slug == product_slug)
               .values(name=update_product_model.name,
                       description=update_product_model.description,
                       price=update_product_model.price,
                       image_url=update_product_model.image_url,
                       stock=update_product_model.stock,
                       category_id=update_product_model.category,
                       slug=slugify(update_product_model.name)))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Product update is successful'
    }

@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], product_id: int):
    product_delete = db.scalar(select(Product).where(Product.id == product_id))
    if product_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no product found'
        )
    db.execute(update(Product).where(Product.id == product_id).values(is_active=False))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Product delete is successful'
    }
