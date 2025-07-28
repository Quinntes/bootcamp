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

### Create (`menu_add_data()`):

  * Add new animal patient entries with required fields: **`Animal_Name`** (Name), **`Age`** (Age), **`Animal_Type`** (Species), **`Gender`** (Gender), **`Diagnosis`**
  * Automatically generates a unique **`Animal_ID`** using the `create_auto_id()` function.
  * Includes **input validation** for proper formatting (e.g., text-only for names and species via `input_alpha_text()`, age in months/years via `input_age()`, gender selection via `input_gender()`, and general text input via `input_diagnosis()`).
  * Supports adding a single record or multiple records in one session.

### Read (`menu_view_data()`):

  * **View full data list** in a formatted table using `display_table()`.
  * **Search for specific patient data** by:
      * **ID** (`find_animal_by_id()`)
      * **Partial/full name match**
  * Filter and display targeted results with clear formatting.
  * Includes a **`display_statistics()`** function to generate summary views of patient data (total animals, counts by species, gender, diagnosis, and average age by species).
  * Patient age is intelligently displayed in years and months using `format_age_display()`.

### Update (`menu_update_data()`):

  * Modify individual fields of an existing patient record after searching by ID.
  * Field-by-field editing options (e.g., change gender, update diagnosis).
  * **Validated inputs** are used for new values, similar to the Create function.
  * Includes an option to **update diagnosis across multiple records** that share the same old diagnosis.
  * Confirmation prompts (`get_confirmation()`) are required to avoid accidental overwrites.

### Delete (`menu_delete_data()`):

  * Remove animal patient records by ID.
  * Confirmation required (`get_confirmation()`) before final deletion.
  * Includes an option to **clear all patient data** (reset the system).

-----

## Data Model

This application uses Python's **`list` of `dictionary`** objects to store data in memory. The initial data is set in the `patient_data` global variable.

Each animal patient record contains the following fields:

  * **`Animal_ID`**: (String) - Unique identifier for each patient (e.g., `H001`, `H002`)
  * **`Animal_Name`**: (String) - The name of the animal
  * **`Age`**: (Integer) - Age in months, converted and displayed in readable format (e.g., "2 tahun 3 bulan") by `format_age_display()`.
  * **`Animal_Type`**: (String) - Type/species of the animal (e.g., "Kucing", "Anjing")
  * **`Gender`**: (String) - Gender of the animal ('Jantan' or 'Betina')
  * **`Diagnosis`**: (String) - Medical condition of the animal

-----

## Usage

To run the program, ensure you have Python installed. Then, execute the script from your terminal or code editor:

```bash
python <nama_file_program>.py
```

The program will display a main menu, and you can navigate through the available operations:

1.  **Report Animal Data**: View all records, search by ID or Name, or see data statistics.
2.  **Add Animal Data**: Add new patient entries.
3.  **Update Animal Data**: Edit existing patient records or perform mass diagnosis updates.
4.  **Delete Animal Data**: Delete specific patient records or clear all data.
5.  **Exit**: Terminate the program.

-----

## Contribution

This is a beginner-friendly open-source project! Feel free to improve the code, suggest features, or report bugs by submitting an issue or creating a pull request. Your contributions are welcome!

-----

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Quinntes/Bootcamp/blob/3f044767832a246c6555e5e3d90aa248919d4538/LICENSE) file for details.
