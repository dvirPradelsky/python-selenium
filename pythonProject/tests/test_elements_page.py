import utils
from Pages.elements_page import ElementsPage
from Pages.home_page import HomePage
from assertpy import assert_that, soft_assertions


def test_navigate_to_elements(driver):
    home_page = HomePage(driver)
    home_page.scroll_down()
    home_page.get_item(index=0).click()

    elements_page = ElementsPage(driver, navigate_to_elements=False)
    elements_page.verify_current_url(expected_url=elements_page.data.URL_PAGE)


def test_elements_text_box_happy_flow(driver):
    """
    Text box happy flow, fill form and verify results.
    """
    elements_page = ElementsPage(driver)
    elements_page.go_to_url(elements_page.data.URL_PAGE)
    elements_page.elements_text_box_list_item.click()
    full_name = 'test'
    email = 'test@gmail.com'
    current_address = 'moshe 4 street, Tel Aviv'
    permanent_address = 'toeva 5 street, Petah Tikva'
    elements_page.elements_text_box_fill_form(
        full_name=full_name,
        email=email,
        current_address=current_address,
        permanent_address=permanent_address
    )
    elements_page.scroll_down()
    elements_page.elements_text_box_submit_button.click()

    actual_result_full_name = utils.split_text(text=elements_page.elements_text_box_name_result.text, separator=':')[1]
    actual_result_email = utils.split_text(text=elements_page.elements_text_box_email_result.text, separator=':')[1]
    actual_result_current_address = utils.split_text(text=elements_page.elements_text_box_current_address_result.text, separator=':')[1]
    actual_result_permanent_address = utils.split_text(text=elements_page.elements_text_box_permanent_address_result.text, separator=':')[1]

    with soft_assertions():
        assert_that(actual_result_full_name, 'Verify full name value in confirm area').is_equal_to(full_name)
        assert_that(actual_result_email, 'Verify email value in confirm area').is_equal_to(email)
        assert_that(actual_result_current_address, 'Verify current address value in confirm area').is_equal_to(current_address)
        assert_that(actual_result_permanent_address, 'Verify permanent address value in confirm area').is_equal_to(permanent_address)


def test_elements_text_box_layout(driver):
    """
    Verify text box layout - static texts (titles, labels etc).
    """
    elements_page = ElementsPage(driver)
    elements_page.go_to_url(elements_page.data.URL_PAGE)
    elements_page.elements_text_box_list_item.click()

    with soft_assertions():
        assert_that(elements_page.elements_text_box_header.text, 'Verify text box header').is_equal_to(elements_page.data.TEXT_BOX_HEADER)
        assert_that(elements_page.elements_text_box_full_name_label.text, 'Verify text box full name label').is_equal_to(
            elements_page.data.TEXT_BOX_FULL_NAME_LABEL)
        assert_that(elements_page.elements_text_box_email_label.text, 'Verify text box email label').is_equal_to(
            elements_page.data.TEXT_BOX_EMAIL_LABEL)
        assert_that(elements_page.elements_text_box_current_address_label.text, 'Verify text box current address label').is_equal_to(
            elements_page.data.TEXT_BOX_CURRENT_ADDRESS_LABEL)
        assert_that(elements_page.elements_text_box_permanent_address_label.text, 'Verify text box permanent address label').is_equal_to(
            elements_page.data.TEXT_BOX_PERMANENT_ADDRESS_LABEL)
        assert_that(elements_page.elements_text_box_submit_button.text, 'Verify text box submit button').is_equal_to(
            elements_page.data.TEXT_BOX_SUBMIT_BUTTON_TEXT)

        elements_page.elements_text_box_fill_form(
            full_name='aaa',
            email='aaa@gmail.com',
            current_address='aaa',
            permanent_address='aaa'
        )

        elements_page.elements_text_box_submit_button.click()

        full_name_label = utils.split_text(text=elements_page.elements_text_box_name_result.text, separator='aaa')[0]
        email_label = utils.split_text(text=elements_page.elements_text_box_email_result.text, separator='aaa')[0]
        current_address_label = utils.split_text(text=elements_page.elements_text_box_current_address_result.text, separator='aaa')[0]
        permanent_address_label = utils.split_text(text=elements_page.elements_text_box_permanent_address_result.text, separator='aaa')[0]

        assert_that(full_name_label, 'Verify full name static text in confirm area').is_equal_to(elements_page.data.TEXT_BOX_CONFIRM_DATA_NAME)
        assert_that(email_label, 'Verify email static text in confirm area').is_equal_to(elements_page.data.TEXT_BOX_CONFIRM_DATA_EMAIL)
        assert_that(current_address_label, 'Verify current address static text in confirm area').is_equal_to(elements_page.data.TEXT_BOX_CONFIRM_DATA_CURRENT_ADDRESS)
        assert_that(permanent_address_label, 'Verify permanent address static text in confirm area').is_equal_to(elements_page.data.TEXT_BOX_CONFIRM_DATA_PERMANENT_ADDRESS)


def test_elements_text_box_errors(driver):
    """
    Verify text box errors - empty fields and email
    """
    elements_page = ElementsPage(driver)
    elements_page.go_to_url(elements_page.data.URL_PAGE)
    elements_page.elements_text_box_list_item.click()

    with soft_assertions():
        elements_page.elements_text_box_submit_button.click()

        # elements_page.elements_text_box_fill_form(
        #     full_name='aaa',
        #     email='aaa@gmail.com',
        #     current_address='aaa',
        #     permanent_address='aaa'
        # )
