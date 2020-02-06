from page_loader.scripts import page_loader


def test_result():
    assert 'Hello world!' == page_loader.main()
