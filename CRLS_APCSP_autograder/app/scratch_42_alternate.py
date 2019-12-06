def scratch_feedback_42_alternate(filename):
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import scratch_filename_test, unzip_sb3, read_json_file, find_help, \
        arrange_blocks_v2, variable_check_no_space
    from CRLS_APCSP_autograder.app.scratch_labs.scratch_4_2 import find_all_lists, find_all_lists_min_items, find_smash_in, \
        find_sundae_and_fancy_sundae, smash_in_works_random, smash_in_works_spacing, sundae_fancy_sundae_works,\
        add_icecreams_works, add_dry_toppings_and_wet_toppings_works, delete_two_questions, delete_works

    tests = list()

    # Test file name
    test_filename = scratch_filename_test(filename, '4.2_alternate')
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
            test_find_all_lists = find_all_lists(json_data, 5)
            tests.append(test_find_all_lists)
            test_find_all_lists_min_items = find_all_lists_min_items(json_data, 5)
            tests.append(test_find_all_lists_min_items)
            test_find_smash_in = find_smash_in(scripts, 5)
            tests.append(test_find_smash_in)
            test_find_sundae_and_fancy_sundae = find_sundae_and_fancy_sundae(scripts, 5)
            tests.append(test_find_sundae_and_fancy_sundae)
            test_smash_in_works_random = smash_in_works_random(scripts, 5)
            tests.append(test_smash_in_works_random)
            test_smash_in_works_spacing = smash_in_works_spacing(scripts, 5)
            tests.append(test_smash_in_works_spacing)
            test_sundae_fancy_sundae_works = sundae_fancy_sundae_works(scripts, 5)
            tests.append(test_sundae_fancy_sundae_works)
            test_add_icecream_works = add_icecreams_works(scripts, 5)
            tests.append(test_add_icecream_works)
            test_add_dry_toppings_and_wet_toppings_works = add_dry_toppings_and_wet_toppings_works(scripts, 10)
            tests.append(test_add_dry_toppings_and_wet_toppings_works)
            test_delete_two_questions = delete_two_questions(scripts, 5)
            tests.append(test_delete_two_questions)
            test_delete_works = delete_works(scripts, 10)
            tests.append(test_delete_works)

            test_help = find_help(json_data, 5)
            tests.append(test_help)
            return tests
