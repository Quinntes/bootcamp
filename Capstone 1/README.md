# Python CRUD Application for Veterinary Patient Management

A comprehensive Python application for managing animal patient data in a veterinary clinic using Create, Read, Update, and Delete (CRUD) operations.

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

---

## Features

### Create:

* Add new animal patient entries with required fields:

  * `Nama Hewan` (Name), `Usia` (Age), `Jenis Hewan` (Species), `Jenis Kelamin` (Gender), `Diagnosis`
* Automatically generates a unique `ID Hewan`
* Validation rules for proper formatting (e.g., text-only for names and species, age in months or years)

### Read:

* View full data list in a formatted table
* Search for specific patient data by:

  * ID
  * Partial/full name match
* Filter and display targeted results with clear formatting

### Update:

* Modify individual fields of a patient record
* Field-by-field editing options (e.g., change gender, update diagnosis)
* Validated inputs and confirmation prompts to avoid accidental overwrites

### Delete:

* Remove animal patient records by ID
* Confirmation required before final deletion

### Reporting (Text-Based):

* Generates summary views of patient data for daily use
* Option to display entire list or filtered results

---

## Data Model

This application uses Python's `list` of `dictionary` objects to store data in memory.

Each animal patient record contains the following fields:

* **ID Hewan**: (String) - Unique identifier for each patient (e.g., H001, H002)
* **Nama Hewan**: (String) - The name of the animal
* **Usia**: (Integer) - Age in months, converted and displayed in readable format (e.g., 2 tahun 3 bulan)
* **Jenis Hewan**: (String) - Type/species of the animal (e.g., Kucing, Anjing)
* **Jenis Kelamin**: (String) - Gender of the animal ('Jantan' or 'Betina')
* **Diagnosis**: (String) - Medical condition of the animal

---

## Usage

Run the program using a terminal or code editor:

```bash
python <nama_file_program>.py
```

Available operations:

* **1. Report Data Hewan**: View all or search for specific patient records
* **2. Menambahkan Data Hewan**: Add new patient entry
* **3. Mengubah Data Hewan**: Edit existing patient record
* **4. Menghapus Data Hewan**: Delete a patient by ID
* **5. Exit**: Terminate the program

---

## Contribution

This is a beginner-friendly open-source project! Feel free to improve the code, suggest features, or report bugs by submitting an issue or contacting the author at \[your\_email\_here].

---

## License

This project is licensed under the MIT License. Feel free to use, distribute, and modify it with attribution.

