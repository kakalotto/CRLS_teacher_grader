# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_2032b import route_python_2_032b as power

person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]

    
fulltext_search = '.py'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'2.032_DC_Superhero_girls_4_Buckets_KFC',
                           r'Python 2.032 DC Superhero girls KFC- Rubric',
                           p_rubric_name)
#    return p_rubric_name
    return None


value_cells = ['F22', 'F23', 'B11', 'B5', ]
rubric_sheet_name = ''

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
              scorer=power, python_lab_num='2.032b', python_rubric_suffix=' - Python 2.032 DC Superhero girls KFC- Rubric')

else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, python_lab_num='2.032b', python_rubric_suffix=' - Python 2.032 DC Superhero girls KFC- Rubric',
                  person=person)
