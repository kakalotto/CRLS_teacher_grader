def docs_feedback_scratch_12(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1b2 = exact_answer('question 1 b2', [r'b\.aaa \s inlineobject\ntabledata?\s*looks?'], text, points=1)
    test1b3 = keyword_and_length('question 1 b3', ['say', 'seconds', 'time', 'text', 'bubble', 'speak',], text,
                                 search_string=r'b\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1c2 = exact_answer('question 1 c2', [r'c\.aaa \s inlineobject\ntabledata?\s*sound?'], text, points=1)
    test1c3 = keyword_and_length('question 1 c3', ['play', 'sound', 'meow', 'noise'], text,
                                 search_string=r'c\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1d2 = exact_answer('question 1 d2', [r'd\.aaa \s inlineobject\ntabledata?\s*looks?'], text, points=1)
    test1d3 = keyword_and_length('question 1 d3', ['costume', 'switch', 'look', 'appear'], text,
                                 search_string=r'd\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1e2 = exact_answer('question 1 e2', [r'e\.aaa \s inlineobject\ntabledata?\s*motion?'], text, points=1)
    test1e3 = keyword_and_length('question 1 e3', ['move', 'glide', 'location', 'smooth', 'slow', 'position', 'slide'], text,
                                 search_string=r'e\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata',  points=1)
    test1f2 = exact_answer('question 1 f2', [r'f\.aaa \s inlineobject\ntabledata?\s*looks?'], text, points=1)
    test1f3 = keyword_and_length('question 1 f3', ['size', 'change', 'size',], text,
                                 search_string=r'f\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1g2 = exact_answer('question 1 g2', [r'g\.aaa \s inlineobject\ntabledata?\s*control?'], text, points=1)
    test1g3 = keyword_and_length('question 1 g3', ['repeat', 'control', ], text,
                                 search_string=r'g\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1h2 = exact_answer('question 1 h2', [r'h\.aaa \s inlineobject\ntabledata?\s*looks?'], text, points=1)
    test1h3 = keyword_and_length('question 1 h3', ['color', 'sprite', 'change', ], text,
                                 search_string=r'h\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1i2 = exact_answer('question 1 i2', [r'i\.aaa \s inlineobject\ntabledata?\s*motion?'], text, points=1)
    test1i3 = keyword_and_length('question 1 i3', ['move', 'go', 'location', 'position' , 'appear'],   text,
                                 search_string=r'i\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata', points=1)
    test1j2 = exact_answer('question 1 j2', [r'j\.aaa \s inlineobject\n.+?tabledata?\s*pen?'], text, points=1)
    test1j3 = keyword_and_length('question 1 j3', ['pen', 'change', 'size', ], text,
                                 search_string=r'j\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata\sk', points=1)
    test1k2 = exact_answer('question 1 k2', [r'k\.aaa \s inlineobject\ntabledata?\s*pen?'], text, points=1)
    test1k3 = keyword_and_length('question 1 k3', ['pen', 'change', 'color', 'set'], text,
                                 search_string=r'k\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)tabledata\sl', points=1)
    test1l2 = exact_answer('question 1 l2', [r'l\.aaa \s inlineobject\ntabledata?\s*motion?'], text, points=1)
    test1l3 = keyword_and_length('question 1 l3', ['point', 'sprite', 'mouse'], text,
                                 search_string=r'l\.aaa \s inlineobject\n .+? tabledata?\s* (.+?)2', points=1)
    test2a = keyword_and_length('question 2a', ['motion', 'move', 'moving', 'category', 'speed', 'way', 'blocks',
                                                'glide', 'turn', 'go', 'set', 'sprite', 'left', 'right'], text,
                                search_string=r'tabledata\sa\.\swhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'motion\scategory\sdo\?\s+you\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+?) tabledata',
                                points=4, min_matches=1)
    test2b = keyword_and_length('question 2b', ['look', 'appear', 'effect', 'talk', 'say', 'disappear',
                                                'category', 'blocks', 'costume',
                                                'set', 'sprite'], text,
                                search_string=r'tabledata\sb\.\swhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'looks\scategory\sdo\?\s+you\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+?) tabledata',
                                points=4, min_matches=1)
    test2c = keyword_and_length('question 2c', ['noise', 'sound', 'music', 'effect', 'cat', 'meow',
                                                'category', 'blocks',
                                                'set', 'sprite'], text,
                                search_string=r'tabledata\sc\.\swhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'sound\scategory\sdo\?\s+you\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+?) tabledata',
                                points=4, min_matches=1)
    test2d = keyword_and_length('question 2d', ['tools', 'pen', 'thickness', 'color', 'size', 'erase', 'clear', 'draw'
                                                'sprite'], text,
                                search_string=r'tabledata\sd\.\swhat\sdo\sthe\sblocks\sin\sthe\s'
                                              r'pen\scategory\sdo\?\s+you\smay\swant\sto\sgive\ssome\sexamples\sof\s'
                                              r'what\syou\scan\sdo\.\ntabledata (.+)',
                                points=4, min_matches=1)

    tests.extend([test1b2, test1b3, test1c2, test1c3, test1d2, test1d3, test1e2, test1e3, test1f2, test1f3, test1g2,
                  test1g3, test1h2, test1h3, test1i2, test1i3, test1j2, test1j3, test1k2, test1k3, test1l2, test1l3,
                  test2a, test2b, test2c, test2d])
    return tests 

