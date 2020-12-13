
def route_python_6_042(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, find_loop, find_dictionary, function_called
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, create_testing_file, run_unit_test, \
        extract_single_function
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=69, score_manual=11)
    test_filename = filename_test(filename, '6.042')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        filename_data = read_file_contents(filename)
        test_find_function = find_function(filename, 'worst_hit', 1, points=5)
        tests.append(test_find_function)
        if test_find_function['pass'] is False:
            return [user, tests, score_info]
        else:
            extract_all_functions(filename)
            create_testing_file(filename)
            help_link = 'https://docs.google.com/presentation/d/1VCavJb5WeAGgE59xpxtlFVPzzCVsJVKMXjoi_SQ2Z28/' \
                        'edit#slide=id.g3f4c165c50_0_43'
            tests.append(run_unit_test('6.042', 1, 5,
                                       description='Checking worst_hit works.<br>   Input dictionary: '
                                                   '{"I got a scratch story to tell": 1500, '
                                                   'mo history mo problems": 3000, The ten CRLS commandments": 3500,'
                                                   'One more AP exam": 10000, Gimme the lunch money": 15000,'
                                                   'Machine Fun Funk": 8000}. '
                                                   'Expected "I got a scratch story to tell"',
                                       help_link=help_link))
            tests.append(run_unit_test('6.042', 2, 5,
                                       description='Checking that worst_hit works.<br>   Input dictionary: '
                                                   '{"I got a scratch story to tell": 9500, '
                                                   'mo history mo problems": 3000,'
                                                   'The ten CRLS commandments": 3500,'
                                                   'One more AP exam": 10000,'
                                                   'Gimme the lunch money": 15000,'
                                                   'Machine Fun Funk": 8000 } Expected "mo history mo problems",',
                                       help_link=help_link))
            tests.append(find_function(filename, 'top_hits', 1, points=5))
            run_simulation_function = extract_single_function(filename, 'top_hits')
            tests.append(find_loop(run_simulation_function, 5,
                                   description='Looking for loop in the run_simulation function '))
            help_link = 'https://docs.google.com/presentation/d/1ElsgYqQGbg5gwxWNALhN8xU_gOeMimnuc12U_gi3Syw/' \
                        'edit#slide=id.g9166948b78_0_12'
            tests.append(run_unit_test('6.042', 3, 5,
                                       description='Checking that top_hits works.<br>   Input dictionary: <br> '
                                                   ' {"I got a scratch story to tell": 9500,'
                                                   '"mo history mo problems": 3000,'
                                                   '"The ten CRLS commandments": 3500,'
                                                   '"One more AP exam": 10000,'
                                                   '"Gimme the lunch money": 15000,'
                                                   '"Machine Fun Funk": 8000 }<br>Expected '
                                                   "['I got a scratch story to tell', 'One more AP exam', "
                                                   "'Gimme the lunch money', 'Machine Fun Funk']",
                                       help_link=help_link))
            tests.append(run_unit_test('6.042', 4, 5,
                                       description='Checking that worst_hit works.<br> Input dictionary: <br> '
                                                   '{"I got a scratch story to tell": 1500 '
                                                   '"mo history mo problems": 3000'
                                                   '"The ten CRLS commandments": 13500'
                                                   '"One more AP exam": 110000,'
                                                   '"Gimme the lunch money": 15000,'
                                                   '"Machine Fun Funk": 18000,'
                                                   '"oh holy night": 9999} <br>'
                                                   "Expected  ['The ten CRLS commandments', 'One more AP exam', "
                                                   "'Gimme the lunch money', "
                                                   "'Machine Fun Funk', 'oh holy night']",
                                       help_link=help_link))
            tests.append(find_dictionary(filename_data, num_items=6, points=5))
            tests.append(function_called(filename, 'worst_hit', 3, points=5))
            tests.append(function_called(filename, 'top_hits', 3, points=5))
            tests.append(pep8(filename, 14))
            tests.append(helps(filename, 5))
            score_info['finished_scoring'] = True
            score_info = sum_score(tests, score_info)
            return [user, tests, score_info]
