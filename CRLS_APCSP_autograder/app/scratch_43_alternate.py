def scratch_feedback_43a_alternate(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, \
        arrange_blocks_v2, free_points, variable_check_no_space
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_4_3 import one_works, songs_list, songs_list_min_items, one_looks_ok, two_looks_ok, \
        three_looks_ok, four_looks_ok, five_looks_ok, two_works, three_works, four_works, five_works, tester
    tests = list()

    # Test file name
    test_filename = scratch_filename_test(filename, '4.3a_alternate')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return tests
    else:
        unzip_sb3(filename)
        json_data = read_json_file()
        scripts = arrange_blocks_v2(json_data)

        test_spaces = variable_check_no_space(json_data['monitors'])
        tests.append(test_spaces)
        if test_spaces['pass'] is False:
            return tests
        else:
            test_songs_list = songs_list(json_data, 5)
            tests.append(test_songs_list)
            test_songs_list_min_items = songs_list_min_items(json_data, 5)
            tests.append(test_songs_list_min_items)
            if test_songs_list_min_items['pass'] is False:
                return tests
            else:
                free_points = free_points(5)
                tests.append(free_points)
                test_one_looks_ok = one_looks_ok(scripts, 5)
                tests.append(test_one_looks_ok)
                test_one_works = one_works(scripts, 5)
                tests.append(test_one_works)
                test_two_looks_ok = two_looks_ok(scripts, 5)
                tests.append(test_two_looks_ok)
                test_two_works = two_works(scripts, 5)
                tests.append(test_two_works)
                test_three_looks_ok = three_looks_ok(scripts, 5)
                tests.append(test_three_looks_ok)
                test_three_works = three_works(scripts, 5)
                tests.append(test_three_works)
                test_four_looks_ok = four_looks_ok(scripts, 5)
                tests.append(test_four_looks_ok)
                test_four_works = four_works(scripts, 5)
                tests.append(test_four_works)
                test_five_looks_ok = five_looks_ok(scripts, 5)
                tests.append(test_five_looks_ok)
                test_five_works = five_works(scripts, 5)
                tests.append(test_five_works)
                test_help = find_help(json_data, 5)
                tests.append(test_help)
                return tests

