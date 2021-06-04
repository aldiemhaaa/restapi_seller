from sqlalchemy.orm import Session
from . import models, schemas

# produk
def get_produk_by_id(db: Session, id: int):
    return db.query(models.Produk).filter(models.Produk.id == id).first()

def get_produk_by_sku(db: Session, sku: str):
    return db.query(models.Produk).filter(models.Produk.sku == sku).first()

def get_all_produk(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Produk).offset(skip).limit(limit).all()

def create_produk(db: Session, produk: schemas.Produk):
    db_produk = models.Produk(nama = produk.nama,harga_beli = produk.harga_beli,harga_jual = produk.harga_jual,sku = produk.sku)
    db.add(db_produk)
    db.commit()
    db.refresh(db_produk)
    return db_produk

# penjualan
def get_penjualan_by_id(db: Session, id: int):
    return db.query(models.Penjualan).filter(models.Penjualan.id == id).first()

def get_penjualan_by_no_pesanan(db: Session, no_pesanan: str):
    return db.query(models.Penjualan).filter(models.Penjualan.no_pesanan == no_pesanan).first()

def get_all_penjualan(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Penjualan).offset(skip).limit(limit).all()

def create_penjualan(db: Session, penjualan: schemas.Penjualan):
    db_penjualan = models.Penjualan(qty = penjualan.qty,variasi_id = penjualan.variasi_id,no_pesanan = penjualan.no_pesanan,produk_id = penjualan.produk_id)
    db.add(db_penjualan)
    db.commit()
    db.refresh(db_penjualan)
    return db_penjualan

 
# transaksi 
def get_transaksi_by_id(db: Session, id: int):
    return db.query(models.Transaksi).filter(models.Transaksi.id == id).first()

def get_transaksi_by_nama(db: Session, nama: str):
    return db.query(models.Transaksi).filter(models.Transaksi.nama == nama).first()

def get_transaksi_by_tanggal(db: Session, tanggal: str):
    return db.query(models.Transaksi).filter(models.Transaksi.tanggal == tanggal).first()

def get_all_transaksi(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transaksi).offset(skip).limit(limit).all()

def create_transaksi(db: Session, transaksi: schemas.Transaksi):
    db_transaksi = models.Transaksi(nama = transaksi.nama,
    keterangan = transaksi.keterangan,
    income = transaksi.income,
    outcome = transaksi.outcome,
    tanggal = transaksi.tanggal,
    xupdate = transaksi.xupdate
    )
    db.add(db_transaksi)
    db.commit()
    db.refresh(db_transaksi)
    return db_transaksi


# variasi 
def get_variasi_by_id(db: Session, id: int):
    return db.query(models.Variasi).filter(models.Variasi.id == id).first()

def get_variasi_by_produk_id(db: Session, produk_id: int):
    return db.query(models.Variasi).filter(models.Variasi.produk_id == produk_id).first()

def get_all_variasi(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Variasi).offset(skip).limit(limit).all()

def create_variasi(db: Session, variasi: schemas.Variasi):
    db_variasi = models.Variasi(produk_id = variasi.produk_id,
    variasi = variasi.variasi
    )
    db.add(db_variasi)
    db.commit()
    db.refresh(db_variasi)
    return db_variasi


# stok 
def get_stok_by_produk_id(db: Session, produk_id: int):
    return db.query(models.Stok).filter(models.Stok.produk_id == produk_id).all()

def get_stok_by_variasi_id(db: Session, variasi_id: int):
    return db.query(models.Stok).filter(models.Stok.variasi_id == variasi_id).all()

def get_all_stok(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Stok).offset(skip).limit(limit).all()

def create_stok(db: Session, stok: schemas.Stok):
    db_stok = models.Stok(produk_id = stok.produk_id,
    variasi_id = stok.variasi_id,
    stok = stok.stok,
    xupdate = stok.xupdate
    )
    db.add(db_stok)
    db.commit()
    db.refresh(db_stok)
    return db_stok


