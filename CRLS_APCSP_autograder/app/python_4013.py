def route_python_4_013(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_function, function_called, find_loop, find_string
    from CRLS_APCSP_autograder.app.python_labs.function_test import run_unit_test, extract_all_functions, \
        extract_single_function, \
        create_testing_file
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8, read_file_contents
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=69, score_manual=11)
    test_filename = filename_test(filename, '4.013')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        test_find_function = find_function(filename, 'lilo_hacks', 2, points=5)
        tests.append(test_find_function)

        filename_data = read_file_contents(filename)
        extract_all_functions(filename)
        create_testing_file(filename)
        function_data = extract_single_function(filename, 'lilo_hacks')
        loop_link = 'https://docs.google.com/presentation/d/1eqIvVwHgdhgJevzVrNyLPHZEubw4hT4gX3VbJpffdDY/' \
                    'edit#slide=id.g8cb34fff74_0_0'
        tests.append(find_loop(function_data, 5,
                               description='There is a loop in the function',
                               help_link=loop_link))
        tests.append(function_called(filename, 'lilo_hacks', 2, points=5))
        run_link = 'https://docs.google.com/presentation/d/1eqIvVwHgdhgJevzVrNyLPHZEubw4hT4gX3VbJpffdDY/' \
                   'edit#slide=id.g8d4c665994_0_11'
        tests.append(run_unit_test('4.013', 1, 15,
                                   description="Calling lilo_hacks with arguments 'capture lilo and stitch now' and"
                                               "True. Function should return blank string",
                                   help_link=run_link))
        tests.append(run_unit_test('4.013', 2, 10,
                                   description="Calling lilo_hacks with arguments 'capture lilo and stitch now' and"
                                               "False. Function should return this string:<br>"
                                               "atr ioadsic o",
                                   help_link=run_link))
        call_link = 'https://docs.google.com/presentation/d/115yqVHY0APEvQFTQ0fGNbw8' \
                    '1pX4gv4kflTUfco1E_Q8/edit#slide=id.g3fda053d45_1_2'
        tests.append(find_string(filename_data, r'lilo_hacks\( .*? True \s* \)\)*$', 1, points=5,
                                 description='Testing that function is called once with argument True',
                                 help_link=call_link))
        tests.append(find_string(filename_data, r'lilo_hacks\( .*? False \s* \)\)*$', 1, points=5,
                                 description='Testing that function is called once with argument False',
                                 help_link=call_link))
        tests.append(pep8(filename, 14))
        tests.append(helps(filename, 5))
        score_info['finished_scoring'] = True
        score_info = sum_score(tests, score_info)
        return [user, tests, score_info]
