import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [jenisTransaksi, setJenisTransaksi] = useState('pengeluaran');
  const [jumlah, setJumlah] = useState('');
  const [tanggal, setTanggal] = useState('');
  const [deskripsi, setDeskripsi] = useState('');
  const [transaksi, setTransaksi] = useState([]);

  useEffect(() => {
    axios.get('/api/transaksi')
      .then(response => setTransaksi(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-md-4 mb-4">
          <div className="card bg-success text-white">
            <div className="card-body">
              <h5 className="card-title"><strong>Tambahkan Transaksi</strong></h5>
              <br />
              <form onSubmit={(e) => {
                e.preventDefault();
                const newTransaksi = {
                  type: jenisTransaksi,
                  amount: jumlah,
                  date: tanggal,
                  description: deskripsi,
                };
                axios.post('/api/transaksi', newTransaksi)
                  .then(response => {
                    setTransaksi([...transaksi, response.data]);
                    setJenisTransaksi('pengeluaran');
                    setJumlah('');
                    setTanggal('');
                    setDeskripsi('');
                  })
                  .catch(error => console.error('Error posting data:', error));
              }}>
                <div className="mb-3">
                  <label htmlFor="jenisTransaksi" className="form-label">Jenis Transaksi:</label>
                  <select id="jenisTransaksi" className="form-select" value={jenisTransaksi} onChange={(e) => setJenisTransaksi(e.target.value)}>
                    <option value="pengeluaran">Pengeluaran</option>
                    <option value="pemasukan">Pemasukan</option>
                  </select>
                </div>
                <div className="mb-3">
                  <label htmlFor="jumlah" className="form-label">Jumlah:</label>
                  <input type="number" className="form-control" id="jumlah" value={jumlah} onChange={(e) => setJumlah(e.target.value)} />
                </div>
                <div className="mb-3">
                  <label htmlFor="tanggal" className="form-label">Tanggal:</label>
                  <input type="date" className="form-control" id="tanggal" value={tanggal} onChange={(e) => setTanggal(e.target.value)} />
                </div>
                <div className="mb-3">
                  <label htmlFor="deskripsi" className="form-label">Deskripsi:</label>
                  <input type="text" className="form-control" id="deskripsi" value={deskripsi} onChange={(e) => setDeskripsi(e.target.value)} />
                </div>
                <button type="submit" className="btn btn-outline-light">Tambahkan</button>
              </form>
            </div>
          </div>
        </div>
        <div className="col-md-8 mb-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title text-success"><strong>Daftar Transaksi</strong></h5>
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
                  {transaksi.map((item, index) => (
                    <tr key={index}>
                      <td>{item.type}</td>
                      <td>{item.amount}</td>
                      <td>{item.date}</td>
                      <td>{item.description}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
