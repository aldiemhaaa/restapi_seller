from typing import List, Optional
from pydantic import BaseModel
from datetime import date,datetime

class Produk(BaseModel):
    nama: str
    harga_beli: int
    harga_jual: int
    sku: str

class ProdukOut(Produk):
    nama : str
    sku : str

    class Config:
        orm_mode = True
    
class Penjualan(BaseModel):
    produk_id: int
    qty: int
    variasi_id: int
    no_pesanan: str

class PenjualanOut(Penjualan):
    produk_id: int
    qty: int
    variasi_id: int
    
    class Config:
        orm_mode = True
    
class Transaksi(BaseModel):
    nama : str
    keterangan : str
    income: int
    outcome: int
    tanggal: str
    xupdate : str

class TransaksiOut(Transaksi):
    nama : str
    tanggal: str
    
    class Config:
        orm_mode = True


class Variasi(BaseModel):
    produk_id: int
    variasi: str

class VariasiOut(Variasi):
    pass

    class Config:
        orm_mode = True

class Stok(BaseModel):
    produk_id: int
    variasi_id: int
    stok: int
    xupdate : str

class StokOut(Stok):
    produk_id: int
    variasi_id: int
    stok: int
    
    class Config:
        orm_mode = True