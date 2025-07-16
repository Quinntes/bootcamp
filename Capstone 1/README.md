Tentu, ini *README* yang sudah direvisi dengan penambahan bagian **License** di bagian paling bawah.

-----

# Python CRUD Application for Veterinary Patient Management

A comprehensive Python application for managing animal patient data in a veterinary clinic using Create, Read, Update, and Delete (CRUD) operations.

-----

## Business Understanding

This project is designed for the veterinary healthcare industry, specifically to address the need for structured and efficient management of animal patient data. Patient data plays a crucial role in ensuring proper diagnosis, treatment tracking, and administrative management within a veterinary clinic.

### Benefits:

  * Improved data accuracy and consistency
  * Streamlined patient registration and record-keeping processes
  * Reduced errors from manual input
  * Clear, formatted data presentation for better staff coordination
  * Unique ID generation to avoid data duplication

### Target Users:

This application is ideal for:

  * Veterinary receptionists and administrative staff
  * Junior veterinary assistants
  * Clinic managers who oversee data tracking

It helps these users in recording, searching, updating, and deleting patient records efficiently.

-----

## Features

### Create (`Menu_Tambah_Data()`):

  * Add new animal patient entries with required fields: **`Nama Hewan`** (Name), **`Usia`** (Age), **`Jenis Hewan`** (Species), **`Jenis Kelamin`** (Gender), **`Diagnosis`**
  * Automatically generates a unique **`ID Hewan`** using the `Buat_ID_Otomatis()` function.
  * Includes **input validation** for proper formatting (e.g., text-only for names and species via `Input_Teks_Huruf()`, age in months/years via `Input_Usia()`, gender selection via `Input_Jenis_Kelamin()`, and general text input via `Input_Teks_Bebas()`).
  * Supports adding a single record or multiple records in one session.

### Read (`Menu_Lihat_Data()`):

  * **View full data list** in a formatted table using `Tampilkan_Tabel()`.
  * **Search for specific patient data** by:
      * **ID** (`Cari_Hewan_by_ID()`)
      * **Partial/full name match**
  * Filter and display targeted results with clear formatting.
  * Includes a **`Tampilkan_Statistik()`** function to generate summary views of patient data (total animals, counts by species, gender, diagnosis, and average age by species).
  * Patient age is intelligently displayed in years and months using `Format_Usia_Tampil()`.

### Update (`Menu_Ubah_Data()`):

  * Modify individual fields of an existing patient record after searching by ID.
  * Field-by-field editing options (e.g., change gender, update diagnosis).
  * **Validated inputs** are used for new values, similar to the Create function.
  * Includes an option to **update diagnosis across multiple records** that share the same old diagnosis.
  * Confirmation prompts (`Minta_Konfirmasi()`) are required to avoid accidental overwrites.

### Delete (`Menu_Hapus_Data()`):

  * Remove animal patient records by ID.
  * Confirmation required (`Minta_Konfirmasi()`) before final deletion.
  * Includes an option to **clear all patient data** (reset the system).

-----

## Data Model

This application uses Python's **`list` of `dictionary`** objects to store data in memory. The initial data is set in the `Data_Pasien` global variable.

Each animal patient record contains the following fields:

  * **`ID Hewan`**: (String) - Unique identifier for each patient (e.g., `H001`, `H002`)
  * **`Nama Hewan`**: (String) - The name of the animal
  * **`Usia`**: (Integer) - Age in months, converted and displayed in readable format (e.g., "2 tahun 3 bulan") by `Format_Usia_Tampil()`.
  * **`Jenis Hewan`**: (String) - Type/species of the animal (e.g., "Kucing", "Anjing")
  * **`Jenis Kelamin`**: (String) - Gender of the animal ('Jantan' or 'Betina')
  * **`Diagnosis`**: (String) - Medical condition of the animal

-----

## Usage

To run the program, ensure you have Python installed. Then, execute the script from your terminal or code editor:

```bash
python <nama_file_program>.py
```

The program will display a main menu, and you can navigate through the available operations:

1.  **Report Data Hewan**: View all records, search by ID or Name, or see data statistics.
2.  **Menambahkan Data Hewan**: Add new patient entries.
3.  **Mengubah Data Hewan**: Edit existing patient records or perform mass diagnosis updates.
4.  **Menghapus Data Hewan**: Delete specific patient records or clear all data.
5.  **Exit**: Terminate the program.

-----

## Contribution

This is a beginner-friendly open-source project\! Feel free to improve the code, suggest features, or report bugs by submitting an issue or contacting the author at `ahmadlutfi2263@gmail.com`.

-----

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Quinntes/Bootcamp/blob/3f044767832a246c6555e5e3d90aa248919d4538/LICENSE) file for details.
