#!/bin/bash

cp ../CRLS_APCSP_autograder/app/routes.py CRLS_APCSP_autograder/app/
cp ../CRLS_APCSP_autograder/app/forms.py CRLS_APCSP_autograder/app/
cp ../CRLS_APCSP_autograder/app/docs_labs/docs.py CRLS_APCSP_autograder/app/docs_labs/
cp ../CRLS_APCSP_autograder/app/python_labs/python.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/__init__.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/io_test.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/find_items.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/python_2_040.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/python_2_05x.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/python_3_011.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/python_3_020.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/python_4_03x.py CRLS_APCSP_autograder/app/python_labs
cp ../CRLS_APCSP_autograder/app/python_labs/python_4_028.py CRLS_APCSP_autograder/app/python_labs

cp ../CRLS_APCSP_autograder/app/python_labs/function_test.py CRLS_APCSP_autograder/app/python_labs


sed -i  's/from app.python_labs.read_file_contents /from CRLS_APCSP_autograder.app.python_labs.read_file_contents / ' CRLS_APCSP_autograder/app/python_labs/find_items.py
sed -i  's/from app.python_labs /from CRLS_APCSP_autograder.app.python_labs / ' CRLS_APCSP_autograder/app/python_labs/function_test.py

sed -i  's/from app import app/from CRLS_APCSP_autograder import app/' CRLS_APCSP_autograder/app/routes.py
sed -i  's/from app.forms /from CRLS_APCSP_autograder.app.forms /' CRLS_APCSP_autograder/app/routes.py
sed -i  's/^@app.*//' CRLS_APCSP_autograder/app/routes.py

declare -a DocsArray=("binary_practice_v5" "cybersecurity" "encoding_black_and_white_v3" "encoding_color" "encoding_text_v1" "encryption_1a"  \
                      "encryption_3" "encryption_4" "hw01" "hw02" "hw03" "hw04" "hw05" "hw06" "hw07" "hw08" "hw09" "hw10" "hw11"\
                   "hw12" "hw13" "hw16" "hw17" "hw18" "hw19a" "hw20" "hw21" "how_unique_are_you" "internet_2_v3" "ip_addressing_dns" \
                   "lossless_compression_v2" "lossy_compression_v2" "privacy_policies" "programming_errors" "python_1020" "python_1030"\
                    "python_2021" "python_2032" "python_2040" "python_2050" \
                   "research_yourself" "routers_and_redundancy" "scratch_12" "tcp_worksheet" "visualization_exploring_trends")
for val in ${DocsArray[@]}; do
   sed -i  's/from app.docs_labs.docs /from CRLS_APCSP_autograder.app.docs_labs.docs /' CRLS_APCSP_autograder/app/$val.py
   sed -i  's/from app.routes /from CRLS_APCSP_autograder.app.routes /' CRLS_APCSP_autograder/app/$val.py
done

# IT2
declare -a DocsArray=("anonymity_and_privacy" "multimedia" "network_protocols_revisited" "nmap_1" "nmap_2" "nmap_3_vs_firewall"\
                      "passive_recon" "proxies" "stealing_password_from_unsecured_system" "tor_1" "vpn_1")
for val in ${DocsArray[@]}; do
   sed -i  's/from app.docs_labs.docs /from CRLS_APCSP_autograder.app.docs_labs.docs /' CRLS_APCSP_autograder/app/$val.py
   sed -i  's/from app.routes /from CRLS_APCSP_autograder.app.routes /' CRLS_APCSP_autograder/app/$val.py
done




sed -i  's/from app.python_labs /from CRLS_APCSP_autograder.app.python_labs /' CRLS_APCSP_autograder/app/python_labs/python.py
sed -i  's/from app.python_labs /from CRLS_APCSP_autograder.app.python_labs /' CRLS_APCSP_autograder/app/python_labs/io_test.py



# python and routes

declare -a PythonArray=("python_1040" "python_1060" "python_2021" "python_2032a" "python_2032b" "python_2040" \
                        "python_2051a" "python_2051b" "python_3011" "python_3020" "python_3027" "python_4013" \
                        "python_4021" "python_4028" "python_4031" "python_6022" "python_6032" "python_6042")
for val in ${PythonArray[@]}; do
   sed -i  's/from app.python_labs.python /from CRLS_APCSP_autograder.app.python_labs.python /' CRLS_APCSP_autograder/app/$val.py
   sed -i  's/from app.routes /from CRLS_APCSP_autograder.app.routes /' CRLS_APCSP_autograder/app/$val.py
done

# find_items
declare -a PythonArray=("python_1040" "python_1060" "python_2021" "python_2032a" "python_2032b" "python_2040" \
                        "python_2051a" "python_2051b" "python_labs/python_2_05x" "python_3011"
                        "python_labs/python_3_011" "python_3020" "python_3027" "python_4013" "python_4021" \
                        "python_4028" "python_6022" "python_6032" "python_6042")
for val in ${PythonArray[@]}; do
   sed -i  's/from app.python_labs.find_items /from CRLS_APCSP_autograder.app.python_labs.find_items /' CRLS_APCSP_autograder/app/$val.py
done

# io_test
declare -a PythonArray=("python_1040" "python_1060" "python_2021" "python_2032a" "python_2032b"  "python_2051b" \
                        "python_labs/python_2_05x" "python_labs/python_3_011"  "python_3020" \
                        "python_labs/python_3_020" "python_labs/python_4_028")
for val in ${PythonArray[@]}; do
   sed -i  's/from app.python_labs.io_test /from CRLS_APCSP_autograder.app.python_labs.io_test /' CRLS_APCSP_autograder/app/$val.py
done

# function_test
declare -a PythonArray=("python_3020" "python_3027" "python_4013" "python_4021" "python_4028" \
                        "python_4031" "python_labs/python_4_03x" "python_6022" "python_6032" "python_6042")
for val in ${PythonArray[@]}; do
   sed -i  's/from app.python_labs.function_test /from CRLS_APCSP_autograder.app.python_labs.function_test /' CRLS_APCSP_autograder/app/$val.py
done

# read_file_contents
declare -a PythonArray=( "python_6032"  "python_6042")
for val in ${PythonArray[@]}; do
   sed -i  's/from app.python_labs.read_file_contents /from CRLS_APCSP_autograder.app.python_labs.read_file_contents /' CRLS_APCSP_autograder/app/$val.py
done

sed -i  's/from app.python_labs.name_dictionary /from CRLS_APCSP_autograder.app.python_labs.name_dictionary /' CRLS_APCSP_autograder/app/python_labs/python.py
sed -i  's/from app.python_labs.python_1_040/from CRLS_APCSP_autograder.app.python_labs.python_1_040/' CRLS_APCSP_autograder/app/python_1040.py
sed -i  's/from app.python_labs.python_2_03x /from CRLS_APCSP_autograder.app.python_labs.python_2_03x /' CRLS_APCSP_autograder/app/python_2032a.py
sed -i  's/from app.python_labs.python_2_03x /from CRLS_APCSP_autograder.app.python_labs.python_2_03x /' CRLS_APCSP_autograder/app/python_2032b.py
sed -i  's/from app.python_labs.python_2_040 /from CRLS_APCSP_autograder.app.python_labs.python_2_040 /' CRLS_APCSP_autograder/app/python_2040.py
sed -i  's/from app.python_labs.python_2_05x /from CRLS_APCSP_autograder.app.python_labs.python_2_05x /' CRLS_APCSP_autograder/app/python_2051a.py
sed -i  's/from app.python_labs.python_3_011 /from CRLS_APCSP_autograder.app.python_labs.python_3_011 /' CRLS_APCSP_autograder/app/python_3011.py
sed -i  's/from app.python_labs.python_3_020 /from CRLS_APCSP_autograder.app.python_labs.python_3_020 /' CRLS_APCSP_autograder/app/python_3020.py
sed -i  's/from app.python_labs.python_4_03x /from CRLS_APCSP_autograder.app.python_labs.python_4_03x /' CRLS_APCSP_autograder/app/python_4031.py
sed -i  's/from app.python_labs.python_4_028 /from CRLS_APCSP_autograder.app.python_labs.python_4_028 /' CRLS_APCSP_autograder/app/python_4028.py
sed -i  's/from app.python_labs.io_test /from CRLS_APCSP_autograder.app.python_labs.io_test /' CRLS_APCSP_autograder/app/python_labs/python_2_040.py


# Scratch labs

cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch_1_3.py CRLS_APCSP_autograder/app/scratch_labs
cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch.py CRLS_APCSP_autograder/app/scratch_labs
cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch_2_2.py CRLS_APCSP_autograder/app/scratch_labs
cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch_2_6.py CRLS_APCSP_autograder/app/scratch_labs
cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch_3_5.py CRLS_APCSP_autograder/app/scratch_labs
cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch_3_2.py CRLS_APCSP_autograder/app/scratch_labs
cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch_3_4.py CRLS_APCSP_autograder/app/scratch_labs
cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch_4_2.py CRLS_APCSP_autograder/app/scratch_labs
cp ../CRLS_APCSP_autograder/app/scratch_labs/scratch_4_3.py CRLS_APCSP_autograder/app/scratch_labs


sed -i  's/from app.scratch_labs.scratch /from CRLS_APCSP_autograder.app.scratch_labs.scratch /' CRLS_APCSP_autograder/app/scratch_labs/scratch_2_6.py
sed -i  's/from app.scratch_labs.scratch/from CRLS_APCSP_autograder.app.scratch_labs.scratch /' CRLS_APCSP_autograder/app/routes.py

sed -i  's/from app.scratch_labs.scratch /from CRLS_APCSP_autograder.app.scratch_labs.scratch /' CRLS_APCSP_autograder/app/scratch_labs/scratch_1_3.py
sed -i  's/from app.scratch_labs.scratch_2_2 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2 /' CRLS_APCSP_autograder/app/scratch_labs/scratch_1_3.py
sed -i  's/from app.python_labs /from CRLS_APCSP_autograder.app.python_labs /' CRLS_APCSP_autograder/app/scratch_labs/scratch.py
sed -i  's/from app.scratch_labs.scratch_2_2 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2  /' CRLS_APCSP_autograder/app/scratch_labs/scratch.py
sed -i  's/from app.scratch_labs.scratch_2_2 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2  /' CRLS_APCSP_autograder/app/scratch_labs/scratch_3_2.py


declare -a StringArray=("scratch_13" "scratch_15" "scratch_1x" "scratch_22" "scratch_23a" "scratch_23b" "scratch_24"\
                        "scratch_26" "scratch_35" "scratch_32" "scratch_labs/scratch_3_2" "scratch_34" \
                        "scratch_labs/scratch_3_4" "scratch_labs/scratch_3_5" "scratch_42" "scratch_labs/scratch_4_2"\
                        "scratch_43a" "scratch_labs/scratch_4_3" "scratch_43b" )

for val in ${StringArray[@]}; do
   sed -i  's/from app.scratch_labs.scratch /from CRLS_APCSP_autograder.app.scratch_labs.scratch /' CRLS_APCSP_autograder/app/$val.py
   sed -i  's/from app.routes /from CRLS_APCSP_autograder.app.routes /' CRLS_APCSP_autograder/app/$val.py
done

sed -i  's/from app.scratch_labs.scratch_2_2 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2 /' CRLS_APCSP_autograder/app/scratch_22.py
sed -i  's/from app.scratch_labs.scratch_3_5 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_3_5 /' CRLS_APCSP_autograder/app/scratch_35.py
sed -i  's/from app.scratch_labs.scratch_3_2 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_3_2  /' CRLS_APCSP_autograder/app/scratch_32.py
sed -i  's/from app.scratch_labs.scratch_3_4 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_3_4  /' CRLS_APCSP_autograder/app/scratch_34.py
sed -i  's/from app.scratch_labs.scratch_4_2 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_4_2  /' CRLS_APCSP_autograder/app/scratch_42.py
sed -i  's/from app.scratch_labs.scratch_4_3 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_4_3  /' CRLS_APCSP_autograder/app/scratch_43a.py
sed -i  's/from app.scratch_labs.scratch_4_3 /from CRLS_APCSP_autograder.app.scratch_labs.scratch_4_3  /' CRLS_APCSP_autograder/app/scratch_43b.py
