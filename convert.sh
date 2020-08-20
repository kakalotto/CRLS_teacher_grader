#!/bin/bash

cp ../CRLS_APCSP_autograder/app/routes.py CRLS_APCSP_autograder/app/
cp ../CRLS_APCSP_autograder/app/forms.py CRLS_APCSP_autograder/app/
sed -i  's/from app import app/from CRLS_APCSP_autograder import app/' CRLS_APCSP_autograder/app/routes.py
sed -i  's/from app.forms /from CRLS_APCSP_autograder.app.forms /' CRLS_APCSP_autograder/app/routes.py
sed -i  's/^@app.*//' CRLS_APCSP_autograder/app/routes.py

sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw01.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw01.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw02.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw02.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw03.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw03.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw04.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw04.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw05.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw05.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw06.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw06.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw07.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw07.py


sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/python_1020.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/python_1020.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/python_1030.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/python_1030.py
