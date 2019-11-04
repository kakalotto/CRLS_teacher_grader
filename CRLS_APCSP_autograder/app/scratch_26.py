def scratch_feedback_26(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, \
         arrange_blocks_v2, variable_check_no_space
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_6 import green_flag, test_top_1, test_fall, test_hit_ground, test_random_x, \
        platform_or_ground
    tests = list()

    # Test file name
    test_filename = scratch_filename_test(filename, '2.6')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        test_flag = green_flag(scripts, 15)
        tests.append(test_flag)
        test_top_1 = test_top_1(scripts, 10)
        tests.append(test_top_1)
        if test_top_1['pass'] is False:
            return tests
        else:
            test_falling = test_fall(scripts, 10)
            tests.append(test_falling)
            test_ground = test_hit_ground(scripts, 20)
            tests.append(test_ground)
            test_x = test_random_x(scripts, 5)
            tests.append(test_x)
            test_both = platform_or_ground(scripts, 5)
            tests.append(test_both)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            
            return tests
        

