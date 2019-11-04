def scratch_feedback_25_alternate(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, \
         find_question, arrange_blocks_v2, variable_check_no_space
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_4_alternate import green_flag
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_5_alternate import test_prizes, test_prizes_defined, any_conditional, four_prizes, \
        no_if_if, find_else
    tests = list()

    # Test file name
    test_filename = scratch_filename_test(filename, '2.5_alternate')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        print("scripts {}".format(scripts))
        test_question = find_question(json_data, 'door', 6)
        tests.append(test_question)
        test_prize_variables = test_prizes(json_data, 5)
        tests.append(test_prize_variables)
        if test_prize_variables['pass'] is False:
            return tests
        else:
            test_prize_values = test_prizes_defined(scripts, 5)
            tests.append(test_prize_values)
            test_flag = green_flag(scripts, 5)
            tests.append(test_flag)
            test_conditional = any_conditional(scripts, 5)
            tests.append(test_conditional)
            test_four = four_prizes(scripts, 5)
            tests.append(test_four)
            test_efficient = no_if_if(scripts, 5)
            tests.append(test_efficient)
            test_else = find_else(scripts, 5)
            tests.append(test_else)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            return tests
            
