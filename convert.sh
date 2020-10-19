#!/bin/bash

cp ../CRLS_APCSP_autograder/app/routes.py CRLS_APCSP_autograder/app/
cp ../CRLS_APCSP_autograder/app/forms.py CRLS_APCSP_autograder/app/
cp ../CRLS_APCSP_autograder/app/docs_labs/docs.py CRLS_APCSP_autograder/app/docs_labs/
cp ../CRLS_APCSP_autograder/app/python_labs/python.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/__init__.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/io_test.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/find_items.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/python_2_040.py CRLS_APCSP_autograder/app/python_labs



sed -i  's/from app import app/from CRLS_APCSP_autograder import app/' CRLS_APCSP_autograder/app/routes.py
sed -i  's/from app.forms /from CRLS_APCSP_autograder.app.forms /' CRLS_APCSP_autograder/app/routes.py
sed -i  's/^@app.*//' CRLS_APCSP_autograder/app/routes.py


sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/binary_practice_v5.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/binary_practice_v5.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/encoding_black_and_white_v3.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/encoding_black_and_white_v3.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/encoding_color.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/encoding_color.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/encoding_text_v1.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/encoding_text_v1.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/encryption_1a.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/encryption_1a.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/encryption_3.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/encryption_3.py

sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/encryption_4.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/encryption_4.py
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
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw08.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw08.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw09.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw09.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw10.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw10.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw11.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw11.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw12.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw12.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/hw13.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/hw13.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/lossy_compression_v2.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/lossy_compression_v2.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/lossless_compression_v2.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/lossless_compression_v2.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/python_1020.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/python_1020.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/python_1030.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/python_1030.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/python_2021.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/python_2021.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/python_2032.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/python_2032.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/python_2040_doc.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/python_2040_doc.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/scratch_12.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/scratch_12.py

sed -i  's/from app.python_labs /from CRLS_APCSP_autograder.app.python_labs /' CRLS_APCSP_autograder/app/python_labs/python.py
sed -i  's/from app.python_labs /from CRLS_APCSP_autograder.app.python_labs /' CRLS_APCSP_autograder/app/python_labs/io_test.py

sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/anonymity_and_privacy.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/anonymity_and_privacy.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/multimedia.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/multimedia.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/proxies.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/proxies.py

sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/tor_1.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/tor_1.py
sed -i  's/from app.docs_labs.docs/from CRLS_APCSP_autograder.app.docs_labs.docs/' CRLS_APCSP_autograder/app/vpn_1.py
sed -i  's/from app.routes/from CRLS_APCSP_autograder.app.routes/' CRLS_APCSP_autograder/app/vpn_1.py

# python and routes

declare -a PythonArray=("python_1040" "python_1060" "python_2021" "python_2032a" "python_2032b" "python_2040" )
for val in ${PythonArray[@]}; do
   sed -i  's/from app.python_labs.python /from CRLS_APCSP_autograder.app.python_labs.python /' CRLS_APCSP_autograder/app/$val.py
   sed -i  's/from app.routes /from CRLS_APCSP_autograder.app.routes /' CRLS_APCSP_autograder/app/$val.py
done

# find_items
declare -a PythonArray=("python_1040" "python_1060" "python_2021" "python_2032a" "python_2032b" "python_2040")
for val in ${PythonArray[@]}; do
   sed -i  's/from app.python_labs.find_items /from CRLS_APCSP_autograder.app.python_labs.find_items /' CRLS_APCSP_autograder/app/$val.py
done

# io_test
declare -a PythonArray=("python_1040" "python_1060" "python_2021" "python_2032a" "python_2032b" )
for val in ${PythonArray[@]}; do
   sed -i  's/from app.python_labs.io_test /from CRLS_APCSP_autograder.app.python_labs.io_test /' CRLS_APCSP_autograder/app/$val.py
done

sed -i  's/from app.python_labs.name_dictionary /from CRLS_APCSP_autograder.app.python_labs.name_dictionary /' CRLS_APCSP_autograder/app/python_labs/python.py
sed -i  's/from app.python_labs.python_1_040/from CRLS_APCSP_autograder.app.python_labs.python_1_040/' CRLS_APCSP_autograder/app/python_1040.py
sed -i  's/from app.python_labs.python_2_03x /from CRLS_APCSP_autograder.app.python_labs.python_2_03x /' CRLS_APCSP_autograder/app/python_2032a.py
sed -i  's/from app.python_labs.python_2_03x /from CRLS_APCSP_autograder.app.python_labs.python_2_03x /' CRLS_APCSP_autograder/app/python_2032b.py
sed -i  's/from app.python_labs.python_2_040 /from CRLS_APCSP_autograder.app.python_labs.python_2_040 /' CRLS_APCSP_autograder/app/python_2040.py

sed -i  's/from app.python_labs.io_test /from CRLS_APCSP_autograder.app.python_labs.io_test /' CRLS_APCSP_autograder/app/python_labs/python_2_040.py

# Scratch labs

cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch_1_3.py CRLS_APCSP_autograder/app/scratch_labs
cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch.py CRLS_APCSP_autograder/app/scratch_labs
cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch_2_6.py CRLS_APCSP_autograder/app/scratch_labs

sed -i  's/from app.scratch_labs.scratch /from CRLS_APCSP_autograder.app.scratch_labs.scratch /' CRLS_APCSP_autograder/app/scratch_labs/scratch_2_6.py
sed -i  's/from app.scratch_labs.scratch/from CRLS_APCSP_autograder.app.scratch_labs.scratch /' CRLS_APCSP_autograder/app/routes.py

sed -i  's/from app.scratch_labs.scratch /from CRLS_APCSP_autograder.app.scratch_labs.scratch /' CRLS_APCSP_autograder/app/scratch_labs/scratch_1_3.py
sed -i  's/from app.scratch_labs.scratch_2_2 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2 /' CRLS_APCSP_autograder/app/scratch_labs/scratch_1_3.py
sed -i  's/from app.python_labs /from CRLS_APCSP_autograder.app.python_labs /' CRLS_APCSP_autograder/app/scratch_labs/scratch.py
sed -i  's/from app.scratch_labs.scratch_2_2 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2  /' CRLS_APCSP_autograder/app/scratch_labs/scratch.py

declare -a StringArray=("scratch_13" "scratch_15" "scratch_1x" "scratch_23a" "scratch_23b" "scratch_24" "scratch_26")

for val in ${StringArray[@]}; do
   sed -i  's/from app.scratch_labs.scratch /from CRLS_APCSP_autograder.app.scratch_labs.scratch /' CRLS_APCSP_autograder/app/$val.py
   sed -i  's/from app.routes /from CRLS_APCSP_autograder.app.routes /' CRLS_APCSP_autograder/app/$val.py
done
