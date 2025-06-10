# Dokumentasi Workflow CI/CD Proyek

Dokumen ini menjelaskan alur Continuous Integration dan Continuous Deployment (CI/CD) untuk proyek ini, yang diimplementasikan menggunakan GitHub Actions dan MLflow. Pipeline ini mengotomatiskan proses checkout kode, instalasi dependensi, pelatihan model, pengelolaan artefak, pembuatan image Docker, dan deployment.

## Gambaran Umum Workflow

Pipeline CI/CD dijalankan saat ada push atau pull request ke branch `main`. Berikut adalah alur langkah demi langkah:

1. **Checkout Kode**
   - Menggunakan `actions/checkout@v3` untuk mengambil kode dari repositori.

2. **Setup Lingkungan Python**
   - Mengatur Python 3.12.7 menggunakan `actions/setup-python@v4`.

3. **Instal Dependensi**
   - Menginstal paket Python yang dibutuhkan, termasuk `mlflow`, `scikit-learn`, dan lainnya yang tercantum dalam proyek.

4. **Atur MLflow Tracking URI**
   - Mengonfigurasi URI pelacakan MLflow ke repositori DagsHub (`covryzne/...`).

5. **Jalankan Proyek MLflow**
   - Menjalankan `mlflow run .` untuk melatih model berikut:
     - Linear Regression
     - Random Forest
     - XGBoost
   - Mencatat ID run untuk setiap model ke `mlflow_output.log`.

6. **Ekstrak ID Run**
   - Mengurai `mlflow_output.log` untuk mendapatkan ID run dari Linear Regression, Random Forest, dan XGBoost.
   - Menyimpan ID run ke `GITHUB_ENV` untuk digunakan di langkah berikutnya.

7. **Unduh Artefak**
   - Mengunduh artefak untuk setiap ID run menggunakan `mlflow artifacts download`.
   - Menyimpan artefak ke `mlruns/0/<run_id>`.

8. **Unggah Artefak ke Git LFS**
   - Melacak `mlruns/**` menggunakan Git Large File Storage (LFS).
   - Melakukan commit dan push artefak ke branch `main`.

9. **Bangun Image Docker**
   - Membangun image Docker menggunakan `MLProject/Dockerfile`.
   - Mengatur variabel lingkungan `RUN_ID` dan `MODEL_NAME` saat pembuatan.
   - Memberi tag image sebagai `workflow-ci:latest`.

10. **Login ke Docker Hub**
    - Melakukan autentikasi ke Docker Hub menggunakan `docker/login-action@v2`.

11. **Tag dan Push Image**
    - Memberi tag image sebagai `shendyeff/workflow-ci:latest`.
    - Mengunggah image ke Docker Hub.

12. **Lokal: Tarik Image Docker**
    - Menarik image Docker secara lokal menggunakan `docker pull shendyeff/workflow-ci:latest`.

13. **Lokal: Jalankan Kontainer**
    - Menjalankan kontainer Docker dengan:
      - Pemetaan port: `-p 5005:8080`
      - Variabel lingkungan: `-e RUN_ID=<run_id>`, `-e MODEL_NAME=<model>`

14. **Lokal: Uji API**
    - Menguji API model yang di-deploy menggunakan `curl http://localhost:5005`.
    - Menyimpan tangkapan layar respons API sebagai `1.bukti_serving.png`.

## Prasyarat

- **Repositori GitHub**: Dikonfigurasi dengan GitHub Actions dan Git LFS.
- **DagsHub**: Server pelacakan MLflow diatur untuk proyek (`covryzne/...`).
- **Docker Hub**: Akun dan repositori (`shendyeff/workflow-ci`) untuk menyimpan image Docker.
- **Lingkungan Lokal**: Docker terinstal untuk menarik dan menjalankan kontainer.

## Cara Penggunaan

1. Lakukan push atau buat pull request ke branch `main` untuk memicu pipeline.
2. Pantau workflow GitHub Actions untuk melihat progres dan log.
3. Setelah pipeline selesai, tarik image Docker secara lokal:
   ```bash
   docker pull shendyeff/workflow-ci:latest
   ```
4. Jalankan kontainer:
   ```bash
   docker run -p 5005:8080 -e RUN_ID=<run_id> -e MODEL_NAME=<model> shendyeff/workflow-ci:latest
   ```
5. Uji API:
   ```bash
   curl http://localhost:5005
   ```
6. Verifikasi tangkapan layar (`1.bukti_serving.png`) sebagai bukti keberhasilan serving.

## Catatan

- Pastikan URI pelacakan MLflow dikonfigurasi dengan benar di repositori DagsHub.
- ID run dicatat dalam `mlflow_output.log` dan digunakan untuk pengambilan artefak.
- Artefak disimpan di `mlruns/0/<run_id>` dan dilacak menggunakan Git LFS.
- Image Docker dibuat dengan model dan ID run yang diperlukan untuk serving prediksi.

Untuk detail lebih lanjut, lihat file workflow GitHub Actions dan konfigurasi `MLProject`.