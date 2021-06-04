from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date,datetime


from .database import Base

class Produk(Base):
    __tablename__ = "produk"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    nama = Column(String)
    harga_beli = Column(Integer)
    harga_jual = Column(Integer)
    sku = Column(String)


class Penjualan(Base):
    __tablename__ = "penjualan"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    qty = Column(Integer)
    variasi_id = Column(Integer)
    no_pesanan = Column(String)
    produk_id = Column(Integer)

class Transaksi(Base):
    __tablename__ = "transaksi"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    nama = Column(String)
    keterangan = Column(String)
    income = Column(Integer)
    outcome = Column(Integer)
    tanggal = Column(String)
    xupdate = Column(String)

class Variasi(Base):
    __tablename__ = 'variasi'
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    produk_id = Column(Integer)
    variasi = Column(String)

class Stok(Base):
    __tablename__='stok'
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    produk_id = Column(Integer)
    variasi_id = Column(Integer)
    stok = Column(Integer)
    xupdate = Column(String)
