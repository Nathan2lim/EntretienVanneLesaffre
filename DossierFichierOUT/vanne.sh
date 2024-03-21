#!/bin/bash
# Install Python
if ! command -v python3 &> /dev/null; then
    apt-get install python3
fi

# Install Django if not already installed
if ! pip show django &> /dev/null; then
    pip install django
fi

cd Users/nathangilbert/Documents/IUT/BUT 3/STAGE_S6/EntretienVanneLesaffre/DossierFichierOUT/
# Change directory to the desired location
cd ../

# Activate the virtual environment
source env/bin/activate

ls

cd EntretienVannes/

# Run the Django server
python3 manage.py runserver
