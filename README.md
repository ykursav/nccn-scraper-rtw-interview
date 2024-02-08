# nccn-scraper-rtw-interview

Interview question repository

## How to run?

1. Please create virtual environment inside of the repository folder. (Can be named .venv)

   ```bash
   virtualenv .venv
   ```

1. Please active the virtualenv. It depends windows or linux.
   Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   Linux:

   ```bash
   source venv/bin/activate
   ```

1. Then install requirements like below:

   ```bash
   pip install -r requirements.txt
   ```

1. Then basically run python script under src/main.py. It should populate database called research.db under repository folder.
   ```bash
   python src/main.py
   ```

**Note:** I am using my bolilerplate can be requirements not used or additional due to time constraint, I couldn't cleanup.
