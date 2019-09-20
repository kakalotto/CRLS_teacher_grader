# Inputs: p_filename, filename to search for help.
#         p_points, number of points this is worth.
# Output: dictionary of test_help
# This module finds number of pep8 errors


def filename_test(p_filename, p_lab):

    import re
#    from CRLS_APCSP_autograder.app.python_labs import YEAR
    YEAR='2019'
    
    find_year = re.search(YEAR, p_filename)
    find_lab = re.search(p_lab, p_filename)
    find_all = re.search(YEAR + r"_ .+ _ " + p_lab + r".py", p_filename, re.X | re.M | re.S)
    p_test_filename = {"name": "Testing that file is named correctly",
                       "pass": True,
                       "pass_message": "<h5 style=\"color:green;\">Pass!</h5> File name looks correct "
                                       "(i.e. something like 2019_luismartinez_" + p_lab +
                                       ".py)",
                       "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                                       "File name of submitted file does not follow required convention. "
                                       " Rename and resubmit.<br>"
                                       "File name should be like this: <br> <br>"
                                       "2019_luismartinez_" + p_lab + ".py <br><br>"
                                       "File must be python file (ends in .py).<br>" 
                                       "A Google doc with Python code copy+pasted in is not accepted <br>"
                                       " Other tests not run. They will be run after filename is fixed.<br>",
                       'points': 0,
                       }
    if find_year and find_lab and find_all:
        p_test_filename['pass'] = True
    else:
        p_test_filename['pass'] = False
    return p_test_filename
