from thesmuggler import smuggle


def test_smuggle_from_relative_path():
    contraband = smuggle('./fixtures/fake_drugs.py')
    assert contraband.ECSTACY == 'candy hearts'


def test_smuggle_from_bare_path():
    contraband = smuggle('fixtures/fake_drugs.py')
    assert contraband.COCAINE == 'baking soda'


def test_smuggle_from_parent_path():
    contraband = smuggle('../fixtures/contraband.py')
    assert contraband.CUBAN_CIGARS == 'cohiba'


def test_smuggle_nested():
    doll = smuggle('fixtures/outer_russian_doll.py')
    assert doll.DRUGS.MARIJUANA == 'oregano'


def test_smuggle_specific():
    marijuana, whippets = smuggle('MARIJUANA', 'WHIPPETS',
                                  source='fixtures/fake_drugs.py')
    assert marijuana == 'oregano'
    assert whippets == 'bottled farts'
