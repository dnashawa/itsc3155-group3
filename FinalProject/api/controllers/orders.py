from sqlalchemy.orm import Session
from sqlalchemy import cast, Date
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from ..models.orders import Order  # implemented 12/4 by Dylan
from datetime import datetime  # implemented 12/4 by Dylan
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.Order(
        customer_name=request.customer_name,
        order_date=request.order_date,  # implemented 12/4 by Dylan, CURRENTLY NON-FUNCTIONAL
        description=request.description,
        phone_number=request.phone_number, #lines 1, 11-15 added by abby 12/2 to fix fastAPI bugs
        address=request.address,
        order_type=request.order_type,
        order_status=request.order_status,
        promo_code_id=request.promo_code_id,
        payment_type=request.payment_type, #lines 16 - 18 added by abby 12/2 to meet requirements
        payment_status=request.payment_status,
        payment_info=request.payment_info

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
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
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
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def get_orders_between_dates(db: Session, start_date: datetime,
                             end_date: datetime):  # implemented 12/4 by Dylan, CURRENTLY NON-FUNCTIONAL
    try:
        orders = (
            db.query(Order)
            .filter(cast(Order.order_date, Date) >= start_date.date(), cast(Order.order_date, Date) <= end_date.date())
            .all()
        )
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)

    return orders
