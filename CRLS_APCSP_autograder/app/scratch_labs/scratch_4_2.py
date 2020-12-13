def find_all_lists(p_json, p_points):
    """
    verifies the 3 lists are there
    :param p_json: json of scratch file (dict)
    :param p_points: points this is worth (int)
    :return: a test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_list
    p_test = {"name": "Checking that there are three lists that exist: ice_cream_list, dry_list, wet_list "
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The lists ice_cream_list, dry_list, wet_list exist .<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The lists ice_cream_list, dry_list, wet_list do not all exist.<br>"
                              "The lists must be named exactly correct (capitalization matters).<br>"
                              "<h5 style=\"color:purple;\">",
              "points": 0
              }
    find_ice_cream_list = find_list(p_json, 'ice_cream_list', 0)
    if find_ice_cream_list['pass'] is False:
        p_test['fail_message'] += 'Did not find this list in your code: ice_cream_list<br>'
    find_wet_list = find_list(p_json, 'wet_list', 0)
    if find_wet_list['pass'] is False:
        p_test['fail_message'] += 'Did not find this list in your code: wet_list<br>'
    find_dry_list = find_list(p_json, 'dry_list', 0)
    if find_dry_list['pass'] is False:
        p_test['fail_message'] += 'Did not find this list in your code: dry_list<br>'
    p_test['fail_message'] += 'See example in presentation: <a href="https://docs.google.com/presentation/d/' \
                              '1_GvsbbOnGSE6lCdZvMb1Ji7wjfLd5NDSbeYdBVZ9uLQ/edit#slide=id.g4608b21e0f_0_116"' \
                              'target="_blank">' \
                              '<br>Link to page in presentation </a></h5>'
    if find_ice_cream_list['pass'] and find_wet_list['pass'] and find_dry_list['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def find_all_lists_min_items(p_json, p_points):
    """
    verifies the 3 lists are there with minium number of items
    :param p_json: json of scratch file (dict)
    :param p_points: points this is worth (int)
    :return: a test dictionary
    """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_list
    p_test = {"name": "Checking three lists have minimum 3 items each"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The lists ice_cream_list, dry_list, wet_list all have 3+ items .<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The lists ice_cream_list, dry_list, wet_list do not all have 3+ items.<br>",
              "points": 0
              }
    find_ice_cream_list = find_list(p_json, 'ice_cream_list', 5, min_items=3)
    if find_ice_cream_list['pass'] is False:
        p_test['fail_message'] += str(find_ice_cream_list['fail_message'])
    find_wet_list = find_list(p_json, 'wet_list', 5, min_items=3)
    if find_wet_list['pass'] is False:
        p_test['fail_message'] += str(find_wet_list['fail_message'])
    find_dry_list = find_list(p_json, 'dry_list', 5, min_items=3)
    if find_dry_list['pass'] is False:
        p_test['fail_message'] += str(find_dry_list['fail_message'])
    p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                              'See example in presentation: <a href="https://docs.google.com/presentation/d/' \
                              '1_GvsbbOnGSE6lCdZvMb1Ji7wjfLd5NDSbeYdBVZ9uLQ/edit#slide=id.g4608b21e0f_0_116"' \
                              'target="_blank">' \
                              '<br>Link to page in presentation </a></h5>'
    if find_ice_cream_list['pass'] and find_wet_list['pass'] and find_dry_list['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test
