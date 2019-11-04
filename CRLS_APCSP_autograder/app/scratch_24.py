def scratch_feedback_24_alternate(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help,\
        find_variable, find_question, find_set_variable, arrange_blocks_v2, variable_check_no_space
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_4_alternate import green_flag, test_color_change, one_question, two_question, \
        name_variable_x4, color_variables
    tests = list()

    # Test file name
    test_filename = scratch_filename_test(filename, '2.4_alternate')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        test_spaces = variable_check_no_space(json_data['monitors'])
        tests.append(test_spaces)
        if test_spaces['pass'] is False:
            return tests
        else:
            scripts = arrange_blocks_v2(json_data)
            print("scripts {}".format(scripts))
            test_question = find_question(json_data, 'name', 5)
            tests.append(test_question)
            test_name = find_variable(json_data, 'name', 5)
            tests.append(test_name)
            if test_name['pass'] is False:
                return tests
            else:
                test_flag = green_flag(scripts, 5)
                tests.append(test_flag)
                test_name_variable = find_set_variable(json_data, 'name', 'answer', points=5)
                tests.append(test_name_variable)
                test_question_color = find_question(json_data, 'color', 5)
                tests.append(test_question_color)
                test_color = find_variable(json_data, 'color', 5)
                tests.append(test_color)
                test_color_variable = color_variables(scripts, 5)
                tests.append(test_color_variable)
                test_stage = test_color_change(scripts, 5)
                tests.append(test_stage)
                test_q1 = one_question(scripts, 10)
                tests.append(test_q1)
                test_q2 = two_question(scripts, 10)
                tests.append(test_q2)
                test_name_usage = name_variable_x4(scripts, 5)
                tests.append(test_name_usage)
                test_help = find_help(json_data, 5)
                tests.append(test_help)
                return tests
            
