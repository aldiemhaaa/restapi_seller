from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# produk
@app.post("/create_produk", response_model=schemas.ProdukOut)
def create_user(produk: schemas.Produk, db: Session = Depends(get_db)):
    db_user = crud.get_produk_by_sku(db, sku=produk.sku)
    if db_user:
        raise HTTPException(status_code=400, detail="Produk already registered")
    return crud.create_produk(db=db, produk=produk)


@app.get("/get_all_produk", response_model=List[schemas.ProdukOut])
def get_all_produk(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    produk = crud.get_all_produk(db = db, skip=skip, limit=limit)
    return produk


@app.get("/get_produk_by_id/{id}",response_model=schemas.ProdukOut)
def get_produk_by_id(id: int,db:Session = Depends(get_db)):
    db = crud.get_produk_by_id(db = db,id=id)
    return db

@app.get("/get_produk_by_sku/{sku}",response_model=schemas.ProdukOut)
def get_produk_by_sku(sku: str,db:Session = Depends(get_db)):
    db = crud.get_produk_by_sku(db = db,sku=sku)
    return db

# penjualan
@app.post("/create_penjualan", response_model=schemas.PenjualanOut)
def create_penjualan(penjualan: schemas.Penjualan, db: Session = Depends(get_db)):
    db_user = crud.get_penjualan_by_no_pesanan(db, sku=penjualan.no_pesanan)
    if db_user:
        raise HTTPException(status_code=400, detail="Penjualan already registered")
    return crud.create_penjualan(db=db, penjualan=penjualan)

@app.get("/get_penjualan_by_id/{id}",response_model=schemas.PenjualanOut)
def get_penjualan_by_id(id: int,db:Session = Depends(get_db)):
    db = crud.get_penjualan_by_id(db = db,id=id)
    return db
    
@app.get("/get_penjualan_by_no_pesanan/{no_pesanan}",response_model=schemas.PenjualanOut)
def get_penjualan_by_no_pesanan(no_pesanan: str,db:Session = Depends(get_db)):
    db = crud.get_penjualan_by_no_pesanan(db = db,no_pesanan=no_pesanan)
    return db

@app.get("/get_all_penjualan", response_model=List[schemas.PenjualanOut])
def get_all_penjualan(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    penjualan = crud.get_all_penjualan(db, skip=skip, limit=limit)
    return penjualan

# transaksi
@app.get("/get_transaksi_by_id/{id}",response_model=schemas.TransaksiOut)
def get_transaksi_by_id(id: int,db:Session = Depends(get_db)):
    db = crud.get_transaksi_by_id(db = db,id=id)
    return db

@app.get("/get_transaksi_by_nama/{nama}",response_model=schemas.TransaksiOut)
def get_transaksi_by_nama(nama: str,db:Session = Depends(get_db)):
    db = crud.get_transaksi_by_nama(db = db,nama=nama)
    return db
    
@app.get("/get_transaksi_by_tanggal/{tanggal}",response_model=schemas.TransaksiOut)
def get_transaksi_by_tanggal(tanggal: str,db:Session = Depends(get_db)):
    db = crud.get_transaksi_by_tanggal(db = db,tanggal=tanggal)
    return db

@app.get("/get_all_transaksi", response_model=List[schemas.TransaksiOut])
def get_all_transaksi(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transaksi = crud.get_all_transaksi(db, skip=skip, limit=limit)
    return transaksi

@app.post("/create_transaksi", response_model=schemas.TransaksiOut)
def create_transaksi(transaksi: schemas.Transaksi, db: Session = Depends(get_db)):
    return crud.create_transaksi(db=db, transaksi=transaksi)

# variasi
@app.get("/get_variasi_by_id/{id}",response_model=schemas.VariasiOut)
def get_variasi_by_id(id: int,db:Session = Depends(get_db)):
    db = crud.get_variasi_by_id(db = db,id=id)
    return db

@app.get("/get_variasi_by_produk_id/{produk_id}",response_model=schemas.VariasiOut)
def get_variasi_by_produk_id(produk_id: int,db:Session = Depends(get_db)):
    db = crud.get_variasi_by_produk_id(db = db,produk_id=produk_id)
    return db

@app.get("/get_all_variasi", response_model=List[schemas.VariasiOut])
def get_allcreate_variasi_variasi(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db = crud.get_all_variasi(db, skip=skip, limit=limit)
    return db

@app.post("/create_variasi", response_model=schemas.VariasiOut)
def create_variasi(variasi: schemas.Variasi, db: Session = Depends(get_db)):
    return crud.create_variasi(db=db, variasi=variasi)


# stok
@app.get("/get_stok_by_produk_id/{produk_id}",response_model=schemas.StokOut)
def get_stok_by_produk_id(produk_id: int,db:Session = Depends(get_db)):
    db = crud.get_stok_by_produk_id(db = db,produk_id=produk_id)
    return db

@app.get("/get_stok_by_variasi_id/{variasi_id}",response_model=schemas.StokOut)
def get_stok_by_variasi_id(variasi_id: int,db:Session = Depends(get_db)):
    db = crud.get_stok_by_variasi_id(db = db,variasi_id=variasi_id)
    return db

@app.get("/get_all_stok", response_model=List[schemas.StokOut])
def get_all_stok(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stok = crud.get_all_stok(db, skip=skip, limit=limit)
    return stok
    
@app.post("/create_stok", response_model=schemas.StokOut)
def create_stok(transaksi: schemas.Stok, db: Session = Depends(get_db)):
    return crud.create_transaksi(db=db, transaksi=transaksi)








# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
