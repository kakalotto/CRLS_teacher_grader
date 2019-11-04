def feedback_4026(filename):

    from CRLS_APCSP_autograder.app.python_labs.pep8 import pep8
    from CRLS_APCSP_autograder.app.python_labs.helps import helps
    from CRLS_APCSP_autograder.app.python_labs.filename_test import filename_test
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_loop, find_string
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, create_testing_file, extract_single_function, \
        run_unit_test
    from CRLS_APCSP_autograder.app.python_labs.python_4_026 import case_1, case_2, case_3, case_4

    tests = list()

    # Test 1: file name
    test_filename = filename_test(filename, '4.026')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        # extract functions and create python test file
        extract_all_functions(filename)
        create_testing_file(filename)
        play_tournament_function = extract_single_function(filename, 'play_tournament')

        test_function_1 = run_unit_test('4.026', 1, 15)
        test_function_1['name'] += "Testing animate_dead function.  " \
                                   "2000 runs should give between 18000 and 21000 raised dead "
        tests.append(test_function_1)

        if test_function_1['pass'] is False:
            return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
        else:
            print("trying 2")
            test_function_2 = run_unit_test('4.026', 2, 10)
            test_function_2['name'] += "Testing raise_army function.  " \
                                       "100 runs of raise_army should print out how many Atwood raises in each cemetary<br>" \
                                       "For each cemetary, Atwood will either 'raises and control' or else " \
                                       "'raises but loses control' <br>" \
                                       "See test output for debugging info.  IF YOU ARE PERIOD 1 2019 S1 APCSP, "\
                                       " LOOK AT ANNOUNCEMENT IN GOOGLE CLASSROOM FOR CORRECTION OF WHAT IT SHOULD PRINT <br>"
            tests.append(test_function_2)

            test_function_3 = run_unit_test('4.026', 3, 10)
            test_function_3['name'] += "Testing raise_army function.  " \
                                       "5 runs of raise_army should give correct undead_data."
            tests.append(test_function_3)

            test_function_4 = run_unit_test('4.026', 4, 15)
            test_function_4['name'] += "Testing dance function.  500 runs of dance should print out correct info AND" \
                                       "should also return correct p_sim." \
                                       "  <br>" \
                                       "Check instructions in the '4 possible outcomes' section to " \
                                       "see what it should print.<br>"
            tests.append(test_function_4)

            test_function_5 = run_unit_test('4.026', 5, 10)
            test_function_5['name'] += "Testing data analysis. Give it a list [25, 50, 75, 3] and 200 simulations.<br>" \
                                       "  Spacing matters (i.e. 50.0% not 50.0 %).  This test ist mostly checking" \
                                       "that you can do math. "
            tests.append(test_function_5)


            run_simulation_function = extract_single_function(filename, 'run_simulation')
            test_run_sim = find_loop(run_simulation_function, 5)
            test_run_sim['name'] = "Looking for loop in the run_simulation function (5 points).<br>"
            tests.append(test_run_sim)

            test_run_sim_data_analysis = find_string(run_simulation_function, r'\s*data_analysis\(', 1, points=5)
            test_run_sim_data_analysis['name'] = "Checking that run_simulation calls data_analysis (5 points).<br>"
            tests.append(test_run_sim_data_analysis)

            test_function_6 = run_unit_test('4.026', 6, 5)
            test_function_6['name'] = " Testing data_analysis through run_simulation function.  Verifying that if you call it with" \
                                      "p_num_simulations of 13, the printout shows 13 runs. <br>" \
                                      "Program looks for the string 'out of 13 simulations' (assuming you ran 13 sims)." \
                                      "Requires a working data_analysis that prints out how many simulations you ran (5 points).<br>"
            tests.append(test_function_6)

            # IO tests
            test_io_1 = case_1(filename)
            tests.append(test_io_1)
            test_io_2 = case_2(filename)
            tests.append(test_io_2)
            test_io_3 = case_3(filename)
            tests.append(test_io_3)
            test_io_4 = case_4(filename)
            tests.append(test_io_4)

            # Find number of PEP8 errors and helps
            test_pep8 = pep8(filename, 14)
            tests.append(test_pep8)
            test_help = helps(filename, 5)
            tests.append(test_help)
            return tests
        


