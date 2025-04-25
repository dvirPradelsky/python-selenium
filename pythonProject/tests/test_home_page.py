from assertpy import assert_that, soft_assertions


from Pages.home_page import HomePage


def test_logo_is_displayed(driver):
    home_page = HomePage(driver)
    assert_that(home_page.logo_element.is_displayed(), "Logo should be displayed").is_true()


def test_list_items_texts(driver):
    home_page = HomePage(driver)
    with soft_assertions():
        assert_that(home_page.get_item(index=0).text, "Verify elements item text").is_equal_to(home_page.data.ELEMENTS)
        assert_that(home_page.get_item(index=1).text, "Verify forms item text").is_equal_to(home_page.data.FORMS)
        assert_that(home_page.get_item(index=2).text, "Verify alerts frame windows item text").is_equal_to(home_page.data.ALERTS_FRAME_WINDOWS)
        assert_that(home_page.get_item(index=3).text, "Verify widgets item text").is_equal_to(home_page.data.WIDGETS)
        assert_that(home_page.get_item(index=4).text, "Verify interactions item text").is_equal_to(home_page.data.INTERACTIONS)
        assert_that(home_page.get_item(index=5).text, "Verify book store applications item text").is_equal_to(home_page.data.BOOK_STORE_APPLICATIONS)
# Todo:  HW- all tests should be with description like here !
#first commit test


def test_current_url(driver):
    home_page = HomePage(driver)
    home_page.verify_current_url(expected_url=home_page.data.URL)
