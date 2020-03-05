def scratch_feedback_24(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help,\
        find_variable, find_question, find_set_variable, arrange_blocks_v2, variable_check_no_space
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_3 import green_flag23b, test_color_change23b, test_school_change23b
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_4 import find_random_one_to_ten, find_ifelse, find_set_name_to_variable, \
        check_correct_number, check_wrong_number
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_4_alternate import green_flag

    tests = list()
 
    # Test file name
    test_filename = scratch_filename_test(filename, '2.4')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return render_template('feedback.html', user=user, tests=tests, filename=filename, score_info=score_info)
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        test_spaces = variable_check_no_space(json_data['monitors'])
        tests.append(test_spaces)
        scripts = arrange_blocks_v2(json_data)
        print("scripts {}".format(scripts))
        test_flag = green_flag(scripts, 2.5)
        tests.append(test_flag)
        test_name = find_variable(json_data, 'name', 2.5)
        tests.append(test_name)
        test_question = find_question(json_data, r'(name|Name)', 2.5)
        tests.append(test_question)
        test_name_to_variable = find_set_name_to_variable(scripts, 2.5)
        tests.append(test_name_to_variable)
        test_number = find_variable(json_data, 'number', 5)
        tests.append(test_number)
        test_random = find_random_one_to_ten(scripts, 10)
        tests.append(test_random)
        test_question = find_question(json_data, r'(guess|Guess)', 5)
        tests.append(test_question)
        test_ifelse = find_ifelse(scripts, 5)
        tests.append(test_ifelse)
        test_check_correct = check_correct_number(scripts, 10)
        tests.append(test_check_correct)
        test_check_wrong = check_wrong_number(scripts, 10)
        tests.append(test_check_wrong)
        
        test_help = find_help(json_data, 5)
        tests.append(test_help)
        score_info['finished_scoring'] = True
        return tests
        
            
