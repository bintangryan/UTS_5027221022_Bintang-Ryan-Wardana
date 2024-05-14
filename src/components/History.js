import React, { useState, useEffect } from 'react';

const History = () => {
  const [jenisTransaksi, setJenisTransaksi] = useState('');
  const [filteredTransactions, setFilteredTransactions] = useState([]);
  const [allTransactions, setAllTransactions] = useState([]);

  useEffect(() => {
    // Ambil transaksi dari penyimpanan lokal saat halaman dimuat
    const transactions = JSON.parse(localStorage.getItem('transactions')) || [];
    setAllTransactions(transactions);
    setFilteredTransactions(transactions);
  }, []);

  useEffect(() => {
    // Filter transaksi berdasarkan jenis transaksi saat jenisTransaksi berubah
    setFilteredTransactions(allTransactions.filter(transaction => {
      return jenisTransaksi ? transaction.jenis === jenisTransaksi : true;
    }));
  }, [jenisTransaksi, allTransactions]);

  const handleJenisTransaksiChange = (e) => {
    setJenisTransaksi(e.target.value);
  };

  return (
    <div className="container mt-5">
      <h2 className="card-title text-success">Histori Transaksi</h2>
      <div className="row mb-3 mt-4">
        <div className="col-md-3">
          <label htmlFor="jenisTransaksi" className="form-label">Jenis Transaksi:</label>
          <select id="jenisTransaksi" className="form-select" value={jenisTransaksi} onChange={handleJenisTransaksiChange}>
            <option value="">Semua</option>
            <option value="pemasukan">Pemasukan</option>
            <option value="pengeluaran">Pengeluaran</option>
          </select>
        </div>
      </div>
      <table className="table mt-4">
        <thead>
          <tr>
            <th scope="col">Jenis</th>
            <th scope="col">Jumlah</th>
            <th scope="col">Tanggal</th>
            <th scope="col">Deskripsi</th>
          </tr>
        </thead>
        <tbody>
          {filteredTransactions.map((item, index) => (
            <tr key={index}>
              <td>{item.jenis}</td>
              <td>{item.jumlah}</td>
              <td>{item.tanggal}</td>
              <td>{item.deskripsi}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default History;
