# Instructions to Run `main.py` from `mcdonaldsAutomation` Repository

To run the `main.py` script from the `mcdonaldsAutomation` repository, follow these steps:

## Prerequisites

1. **Install PyCharm**
   - Download and install PyCharm from [JetBrains](https://www.jetbrains.com/pycharm/download/?section=windows).

2. **Install Python**
   - Download and install the most recent version of Python from the [official Python website](https://www.python.org/downloads/).

## Steps to Run `main.py`

1. **Clone the Repository**
   - Open a terminal (Command Prompt, PowerShell, or Git Bash).
   - Clone the repository using the following command:
     ```sh
     git clone https://github.com/sashaKorovkina/mcdonaldsAutomation.git
     ```
   - Navigate to the cloned repository:
     ```sh
     cd mcdonaldsAutomation
     ```

2. **Open the Project in PyCharm**
   - Launch PyCharm.
   - Open the cloned repository as a new project:
     - Click on `File` > `Open`.
     - Navigate to the directory where you cloned the repository.
     - Select the repository folder and click `OK`.

3. **Configure the Python Interpreter**
   - Set up the Python interpreter to point to your installed Python version:
     - Go to `File` > `Settings` (or `PyCharm` > `Preferences` on macOS).
     - Navigate to `Project: <your_project_name>` > `Python Interpreter`.
     - Click the gear icon and select `Add...`.
     - Choose `System Interpreter` and select your installed Python version.
     - Click `OK` to apply the changes.

4. **Install Required Packages**
   - Open the `requirements.txt` file in the project.
   - Right-click on `requirements.txt` and select `Install Package`.
   - PyCharm will automatically install all the required dependencies.

5. **Run `main.py`**
   - Locate `main.py` in the Project tool window (usually on the left side).
   - Right-click on `main.py` and select `Run 'main'`.

## Additional Notes

- Ensure you have an active internet connection for cloning the repository and installing dependencies.
- If you encounter any issues with dependencies, you can manually install them using:
  ```sh
  pip install -r requirements.txt
  ```

By following these steps, you should be able to successfully run the `main.py` script from the `mcdonaldsAutomation` repository using PyCharm.
