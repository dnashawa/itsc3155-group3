from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import sandwich_tags as controller
from ..schemas import sandwich_tags as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Sandwich Tags'],
    prefix="/sandwich_tags"
)


@router.post("/", response_model=schema.SandwichTag)
def create(request: schema.SandwichTagCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.SandwichTag])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.SandwichTag)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.SandwichTag)
def update(item_id: int, request: schema.SandwichTagUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)