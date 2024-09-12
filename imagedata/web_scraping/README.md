# Scraper

## Before running

1. **Install **python****
2. **Make sure you have virtualenv installed**

    If you don't have virtaulenv run the command below:

    ```bash
    python -m pip install venv
    ```

3. **Create a virtualenv**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtualenv**

    - On linux

    ```bash
    source venv/bin/activate.sh
    ```

    - On windows

        - On cmd

        ```bat
        .\venv\Scripts\activate.bat
        ```

        - On powershell

        ```bat
        .\venv\Scripts\activate.ps1
        ```

5. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## How to run

```shell
python run.py
```

It will create a `photo` directory in your project root and stores downloaded files there.
