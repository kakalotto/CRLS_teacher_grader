def scratch_feedback_22(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, \
        find_help, arrange_blocks, arrange_blocks_v2
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_2_2 import press_zero, press_one, press_two, press_three, press_four

    tests = list()
    test_filename = scratch_filename_test(filename, '2.2')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        print("scripts {}".format(scripts))
        test_zero = press_zero(scripts, 15)
        tests.append(test_zero)
        if test_zero['pass'] is False:
            return tests
        else:
            test_one = press_one(scripts, 10)
            tests.append(test_one)
            test_two = press_two(scripts, 10)
            tests.append(test_two)
            test_three = press_three(scripts, 15)
            tests.append(test_three)
            test_four = press_four(scripts, 15)
            tests.append(test_four)
            test_help = find_help(json_data, 5)
            tests.append(test_help)
            return tests
