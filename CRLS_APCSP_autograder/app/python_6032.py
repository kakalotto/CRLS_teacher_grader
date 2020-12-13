def route_python_6_032(filename):
    from CRLS_APCSP_autograder.app.python_labs.function_test import extract_all_functions, run_unit_test, create_testing_file
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, find_loop, find_dictionary
    from CRLS_APCSP_autograder.app.python_labs.read_file_contents import read_file_contents
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=69, score_manual=11)
    test_filename = filename_test(filename, '6.032')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        filename_data = read_file_contents(filename)
        dict_help = 'https://docs.google.com/presentation/d/1-Us-Uaf_59FoYxVwcXCX1JpgcqGb6w1EHsHkfLTFazo/' \
                    'edit#slide=id.ga8ba07ecf9_0_0'
        add_assignment_help = 'https://docs.google.com/presentation/d/1C_-QMyelmSAI2NZVW5jdxIpxQhYCuuCyWvfMFPaw_nM/' \
                              'edit#slide=id.g9ff4d60f69_1_0'
        calculate_grade_help = 'https://drive.google.com/file/d/1jJkGtrb7JmSmZ_DjrJN8ZDo5GFfqZd-f/view?usp=sharing'
        tests.append(find_dictionary(filename_data, num_items=0, points=5, help_link=dict_help))
        tests.append(find_function(filename, 'add_assignment', 3, points=5))
        extract_all_functions(filename)
        create_testing_file(filename)
        tests.append(run_unit_test('6.032', 1, 5, help_link=add_assignment_help))
        tests.append(run_unit_test('6.032', 2, 5, help_link=add_assignment_help))
        tests.append(run_unit_test('6.032', 3, 5, help_link=add_assignment_help))
        tests.append(run_unit_test('6.032', 4, 5, help_link=add_assignment_help))
        test_find_function = find_function(filename, 'calculate_grade', 1, points=5)
        tests.append(test_find_function)
        tests.append(run_unit_test('6.032', 5, 5, help_link=calculate_grade_help))
        tests.append(run_unit_test('6.032', 6, 5, help_link=calculate_grade_help))
        tests.append(run_unit_test('6.032', 7, 5, help_link=calculate_grade_help))
        tests.append(find_loop(filename_data, 5))
        tests.append(pep8(filename, 14))
        tests.append(helps(filename, 5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]
