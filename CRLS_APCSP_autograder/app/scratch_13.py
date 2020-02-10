def scratch_feedback_13(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, arrange_blocks_v2
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_1_3 import press_zero, press_one, press_two, press_four, press_five

    tests = list()

    # Test file name
    test_filename = scratch_filename_test(filename, '1.3')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)
        test_zero = press_zero(scripts, 10)
        tests.append(test_zero)
        test_one = press_one(scripts, 10)
        tests.append(test_one)
        test_two = press_two(scripts, 10)
        tests.append(test_two)
        test_four = press_four(scripts, 15)
        tests.append(test_four)
        test_five = press_five(scripts, 15)
        tests.append(test_five)
        test_help = find_help(json_data, 5)
        tests.append(test_help)
        return tests



