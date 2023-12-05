from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import sandwiches as model
from ..models.sandwiches import Sandwich
from  ..models.orders import Order
from ..models.order_details import OrderDetail
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from fastapi.responses import JSONResponse


def create(db: Session, request):
    new_item = model.Sandwich(
        sandwich_name=request.sandwich_name,
        price=request.price,
        calories=request.calories, # lines 10 - 11 added 12/2 to fix fastapi bug - abby
        tags=request.tags
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Sandwich).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Sandwich).filter(model.Sandwich.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Sandwich).filter(model.Sandwich.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Sandwich).filter(model.Sandwich.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def get_most_popular_sandwich(db: Session, start_date: datetime, end_date: datetime):
    try:
        subquery = (
            db.query(Sandwich.sandwich_name, func.count(Sandwich.id).label('sandwich_count')).join(OrderDetail).join(Order).filter(
                Order.order_date >= start_date, Order.order_date <= end_date).group_by(Sandwich.sandwich_name).subquery()
        )

        result = (
            db.query(subquery.c.sandwich_name).order_by(subquery.c.sandwich_count.desc()).first()
        )
        result = str(result)
        result = result[2:]
        result = result[:-3]
        json_response = {"Most Popular Food": result}

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)

    return JSONResponse(content=json_response)
