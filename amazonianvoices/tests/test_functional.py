import pytest


@pytest.mark.parametrize(
    "method,path",
    [
        ('get_html', '/'),
        ('get_html', '/languages'),
        ('get_html', '/languages/ashaninka'),
        ('get_html', '/languages/ashaninka#ipa'),
        ('get_html', '/languages/ashaninka?__locale__=es'),
        ('get_dt', '/languages?iSortingCols=1&iSortCol_0=1'),
        ('get_html', '/parameters'),
        ('get_html', '/parameters/18_foot'),
        ('get_html', '/values'),
        ('get_html', '/valuesets'),
        ('get_html', '/values/ashaninka-163_amazonriverdolphin-1'),
        ('get_dt', '/parameters?sSearch_2=drink'),
        ('get_dt', '/values?sSearch_2=drink'),
    ])
def test_pages(app, method, path):
    getattr(app, method)(path)

