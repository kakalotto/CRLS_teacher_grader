def songs_list(p_json, p_points):
    """
     verifies the 3 lists are there
     :param p_json: json of scratch file (dict)
     :param p_points: points this is worth (int)
     :return: a test dictionary
     """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_list
    p_test = {"name": "Checking that there is list that exists: songs "
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The list songs exists .<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The list songs does not exist.<br>"
                              "The lists must be named EXACTLY CORRECT with no caps and the 's' at the end.<br>"
                              "An 's' at the end tells you that it is plural (lists are potentially plural) and "
                              "this is a good trick to help you keep track of things.<br>",
              "points": 0
              }
    p_test['fail_message'] += 'See example in presentation: <a href="https://docs.google.com/presentation/d/' \
                              '1_GvsbbOnGSE6lCdZvMb1Ji7wjfLd5NDSbeYdBVZ9uLQ/edit#slide=id.g4608b21e0f_0_116"' \
                              'target="_blank">' \
                              '<br>Link to page in presentation </a></h5>'
    find_names = find_list(p_json, 'songs', 0)
    if find_names['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test


def songs_list_min_items(p_json, p_points):
    """
     verifies min number of items
     :param p_json: json of scratch file (dict)
     :param p_points: points this is worth (int)
     :return: a test dictionary
     """
    from CRLS_APCSP_autograder.app.scratch_labs.scratch import find_list
    p_test = {"name": "Checking that there is list songs with minimum 6 items"
                      " (" + str(p_points) + " points)<br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  "
                              "The list songs exists with minimum 6 items .<br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "The list songs does not have 6 or more items.",
              "points": 0
              }
    p_test['fail_message'] += '<h5 style=\"color:purple;\">' \
                              'See example in presentation: <a href="https://docs.google.com/presentation/d/' \
                              '1_GvsbbOnGSE6lCdZvMb1Ji7wjfLd5NDSbeYdBVZ9uLQ/edit#slide=id.g4608b21e0f_0_116" ' \
                              'target="_blank">' \
                              '<br>Link to page in presentation </a></h5>'
    find_songs_items = find_list(p_json, 'songs', 0,  min_items=6)
    if find_songs_items['pass'] is False:
        p_test['fail_message'] += str(find_songs_items['fail_message'])
    if find_songs_items['pass']:
        p_test['pass'] = True
        p_test['points'] += p_points
    return p_test
