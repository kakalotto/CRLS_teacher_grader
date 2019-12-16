def docs_feedback_databases_3002(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test3a = exact_answer('3a. Christmas island',
                          [r'3a\. .+? tabledata \s* update .+? country \s set \s `*name`* \s* = '
                           r'\s* .+? holiday \s island .+? '
                           r'where \s `*name`* \s* = \s* .+? christmas \s island .+? 3b\.',
                           r'3a\. .+? tabledata \s* update .+? country \s set \s `*name`* \s* = '
                           r'\s* .+? holiday \s island .+? '
                           r'where \s `*code`* \s* = \s* .+? cxr .+? 3b\.'
                           ], text, points=10)
    test3b = exact_answer('3b. population > 5M', [r'3b\. .+? tabledata \s* select \s* .+? \s* from \s* `*world`* \.'
                                                  r'`*country`* \s* where `* \s* `* population`* \s* > \s* 5,*000,*000 '
                                                  r'\s*'
                                                  r'.+? 3c\.'],
                          text, points=10)
    test3c = exact_answer('3c. Beginning w/York', [r'3c\. .+? tabledata \s* select \s* .+? \s* from .+? `* city `* \s* '
                                                   r'where \s* `*name`* \s* like .+? %york .+? 3d\.'], text, points=5)
    test3d = exact_answer('3d. Ending w/York',  [r'3d\. .+? tabledata \s* select \s* .+? \s* from .+? `* city `* \s* '
                                                 r'where \s* `*name`* \s* like .+? york% .+? 3e\.'], text, points=5)
    test3e = exact_answer('3e. Avg. Africa population', [r'3e\. .+? tabledata \s* select  \s* avg  \(population\) \s* '
                                                         r'from \s `*country`* \s* where \s* continent .+? asia .+? '
                                                         r'3f\.'], text, points=10)
    test3f = exact_answer('3f. unville', [r'3f\. .+? tabledata \s*  insert \s* into \s* country .+? unville .+? $'],
                          text, points=10)

    tests.extend([test3a, test3b, test3c, test3d, test3e, test3f])
    return tests

