def docs_feedback_databases_3002(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    print(text)
    test3a = exact_answer('3a. Christmas island',
                          [r'3a\. .+? tabledata \s* update .+? country .+? set .+? name .*?  = '
                           r'\s* .+? holiday \s island .+? '
                           r'where .+? name .*? = .*? christmas \s island .+? 3b\.',
                           r'3a\. .+? tabledata \s* update .+? country .+? set .+? name .*? \s* = \s* .*? holiday \s island .+? where .+? code .*?  = .*? cxr .+? 3b\.',
                           ], text, points=10)
    test3b = exact_answer('3b. population > 5M', [r'3b\. .+? tabledata \s* select \s* .+? \s* from \s* `*world`* \.'
                                                  r'`*country`* \s* where `* \s* `* population`* \s* > \s* 5,*000,*000 '
                                                  r'\s*'
                                                  r'.+? 3c\.',
                                                  r'3b\. .+? tabledata \s* select \s* .+? \s* from \s* `*country`* \s* where \s* `*population`* \s* > \s* 5,*000,*000 \s* .+? 3c\.  '],
                          text, points=10)
    test3c = exact_answer('3c. Beginning w/York', [r'3c\. .+? tabledata \s* select \s* .+? \s* from .+? `* city `* \s* '
                                                   r'where \s* `*name`* \s* like .+? york% .+? 3d\.',], text, points=5)
    test3d = exact_answer('3d. Ending w/York',    [r'3d\. .+? tabledata \s* select \s* .+? \s* from .+? `* city `* \s* '
                                                   r'where \s* `*name`* \s* like .+? %york .+? 3e\.'], text, points=5)
    test3e = exact_answer('3e. Avg. Asia population', [r'3e\. .+? tabledata \s* select  \s* avg  \(population\) \s* '
                                                         r'from \s* `*country`* \s* where .+? continent .+? asia .+? '
                                                         r'3f\.'], text, points=10)
    test3f = exact_answer('3f. unville', [r'3f\. .+? tabledata \s*  insert \s* into .+? city .+? unville .+? $'],
                          text, points=10)

    tests.extend([test3a, test3b, test3c, test3d, test3e, test3f])
    return tests

