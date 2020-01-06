def docs_feedback_databases_2002(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test3a = exact_answer('3a. screenshot', [r'3a\. .+? tabledata \s* aaa \s* inlineobject .+? create'], text, points=1)
    test4a = exact_answer('4a. screenshot', [r'4a\. .+? tabledata \s* aaa \s* inlineobject .+? 4b\.'], text, points=1)
    test4b = exact_answer('4b. code', [r'4b\. .+? tabledata \s* insert \s* into .+? deleting'], text, points=5)
    test5a = exact_answer('5a. screenshot', [r'5a\. .+? tabledata \s* aaa \s* inlineobject .+? 5b\.'], text, points=1)
    test5b = exact_answer('5b. code', [r'5b\. .+? tabledata \s* delete \s* from .+? updating'], text, points=5)
    test6a = exact_answer('6a. screenshot', [r'6a\. .+? tabledata \s* aaa \s* inlineobject .+? 6b\.'], text, points=1)
    test6b = exact_answer('6b. code', [r'6b\. .+? tabledata \s* update .+? country .+? set .+? running'], text, points=5)
    test7a = exact_answer('7a. sql query select all',
                          [r'7a\. .+? tabledata \s* select \s* \* \s* from \s* country .+? 7b\.'],
                          text, points=10)
    test7b = exact_answer('7b. sql query select city, M names',
                          [r'7b\. .+? tabledata \s* select .+?  from .+? city .+? where .+? name .+? like \s*'
                           r' .+? m%  .+? 7c\.'],
                          text, points=10)
    test7c = exact_answer('7c. sql query surface area',
                          [r'7c\. .+? tabledata \s* select .+? from .+? country .+? where .+? surfacearea .+? > '
                           r'\s* 50 ,* 000 \s*'
                           r' .+?  7d\.'],
                          text, points=10)
    test7d = exact_answer('7d. life expectancy > 70',
                          [r'7d\. .+? tabledata \s* select \s* count .+? from .+? country .+? where \s* '
                           r'lifeexpectancy \s* > '
                           r'\s* 70 \s*'
                           r' .+?  $'],
                          text, points=10)


    tests.extend([test3a, test4a, test4b, test5a, test5b, test6a, test6b, test7a, test7b, test7c, test7d])
    return tests

