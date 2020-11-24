def full_run(p_filename, percent):
    from CRLS_APCSP_autograder.app.python_labs.io_test import io_test
    import re
    percents = {75: '89%', 0: '0%', 100: '100%'}
    percents_run = {75: 1, 0: 3, 100: 2}

    p_test = {"name": "Given a win % of " + str(percent) + " Expect to win  " + str(percents[percent]) +
              " of the time (5 points) <br>",
              "pass": False,
              "pass_message": "<h5 style=\"color:green;\">Pass!</h5>  Given a win % of " + str(percent) +
                              " Won expected percentage of time  " + str(percents[percent]) +
              " of the time (5 points) <br>",
              "fail_message": "<h5 style=\"color:red;\">Fail.</h5> "
                              "Given a win% of " + str(percent) + " Did not win expected percentage.",
              "points": 0,
              }

    test1 = io_test(p_filename, r'NO_MATCH', percents_run[percent])
    match = re.search(r'won \s this \s many \s matches .*? ([.0-9]+)', test1['fail_message'], re.X | re.M | re.S)
    wins = 123456
    if match:
        wins = float(match.group(1))
        print("MATCHES")
        print(match.group(0))
        print(match.group(1))

    if percent == 0:
        if wins == 0:
            p_test['pass'] = True
    elif percent == 100:
        if wins == 1000:
            p_test['pass'] = True
    elif percent == 75:
        if wins > 88000 or wins < 91500:
            p_test['pass'] = True
    if p_test['pass'] is False:
        p_test['fail_message'] += 'Found this many wins:' + str(wins) + ' (if answer is 123456, did not find the string' \
                                                                        '"won this many matches")<br> '
    else:
        p_test['points'] += 5
    return p_test
