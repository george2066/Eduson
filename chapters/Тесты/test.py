import smtplib
from mailbox import Message

import pytest
from more_itertools.more import side_effect
from pytest_mock import MockFixture
from faker.contrib.pytest.plugin import faker
from faker.proxy import Faker

# Mock
class MailClient:
    def send_email(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")

class Art:
    def _calculate_price(self):
        raise NotImplementedError # pragma: no cover

class Book(Art):
    def __init__(self, price):
        if price <= 0:
            raise ValueError("price mast been more zero")
        self._price = price

    @property
    def price(self):
        return self._calculate_price()

    def _calculate_price(self):
        return self._price

# tests/


###############MailClient########################
def test_mail_client_with_mock(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# а сейчас давайте проверим ошибку!
def test_mail_client_returns_error_with_mock(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'
###############MailClient########################


def test_book_creation(faker: Faker):
    faker.seed_instance(1234)
    price = faker.pyint(min_value=0)
    book = Book(price)
    assert book.price == price

@pytest.mark.parametrize(
    'price', [400, 600, 5000]
)
def test_book_creation(price):
    price = 400
    book = Book(price)
    assert book.price == price

@pytest.mark.parametrize(
    'price', [-400, -600, -5000]
)
def test_error_create_book(faker: Faker):
    price = faker.pydecimal(positive=False, max_value=0)
    with pytest.raises(ValueError) as exc_info:
        Book(price)
    assert str(exc_info.value) == "price mast been more zero"




















