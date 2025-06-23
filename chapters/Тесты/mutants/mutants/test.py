import smtplib
from mailbox import Message

import pytest
from more_itertools.more import side_effect
from pytest_mock import MockFixture
from faker.contrib.pytest.plugin import faker
from faker.proxy import Faker
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_yield_from_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = yield from mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = yield from mutants[mutant_name](*call_args, **call_kwargs)
    return result

# Mock
class MailClient:
    def xǁMailClientǁsend_email__mutmut_orig(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_1(self, text: str, send_to_person: str):
        text = None
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_2(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = None
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_3(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(None)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_4(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = None
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_5(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host=None, port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_6(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=None, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_7(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname=None, source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_8(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address=None
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_9(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_10(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_11(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_12(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_13(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="XX...XX", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_14(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8071, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_15(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="XX...XX", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_16(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="XX...XX"
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_17(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(None, from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_18(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr=None, to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_19(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs=None)
    def xǁMailClientǁsend_email__mutmut_20(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(from_addr="...", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_21(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_22(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", )
    def xǁMailClientǁsend_email__mutmut_23(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="XX...XX", to_addrs="...")
    def xǁMailClientǁsend_email__mutmut_24(self, text: str, send_to_person: str):
        text = f'{text}\n\n{send_to_person}'
        message = Message(text)
        smtp_client = smtplib.SMTP(
            host="...", port=8070, local_hostname="...", source_address="..."
        )
        smtp_client.send_message(message, from_addr="...", to_addrs="XX...XX")
    
    xǁMailClientǁsend_email__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁMailClientǁsend_email__mutmut_1': xǁMailClientǁsend_email__mutmut_1, 
        'xǁMailClientǁsend_email__mutmut_2': xǁMailClientǁsend_email__mutmut_2, 
        'xǁMailClientǁsend_email__mutmut_3': xǁMailClientǁsend_email__mutmut_3, 
        'xǁMailClientǁsend_email__mutmut_4': xǁMailClientǁsend_email__mutmut_4, 
        'xǁMailClientǁsend_email__mutmut_5': xǁMailClientǁsend_email__mutmut_5, 
        'xǁMailClientǁsend_email__mutmut_6': xǁMailClientǁsend_email__mutmut_6, 
        'xǁMailClientǁsend_email__mutmut_7': xǁMailClientǁsend_email__mutmut_7, 
        'xǁMailClientǁsend_email__mutmut_8': xǁMailClientǁsend_email__mutmut_8, 
        'xǁMailClientǁsend_email__mutmut_9': xǁMailClientǁsend_email__mutmut_9, 
        'xǁMailClientǁsend_email__mutmut_10': xǁMailClientǁsend_email__mutmut_10, 
        'xǁMailClientǁsend_email__mutmut_11': xǁMailClientǁsend_email__mutmut_11, 
        'xǁMailClientǁsend_email__mutmut_12': xǁMailClientǁsend_email__mutmut_12, 
        'xǁMailClientǁsend_email__mutmut_13': xǁMailClientǁsend_email__mutmut_13, 
        'xǁMailClientǁsend_email__mutmut_14': xǁMailClientǁsend_email__mutmut_14, 
        'xǁMailClientǁsend_email__mutmut_15': xǁMailClientǁsend_email__mutmut_15, 
        'xǁMailClientǁsend_email__mutmut_16': xǁMailClientǁsend_email__mutmut_16, 
        'xǁMailClientǁsend_email__mutmut_17': xǁMailClientǁsend_email__mutmut_17, 
        'xǁMailClientǁsend_email__mutmut_18': xǁMailClientǁsend_email__mutmut_18, 
        'xǁMailClientǁsend_email__mutmut_19': xǁMailClientǁsend_email__mutmut_19, 
        'xǁMailClientǁsend_email__mutmut_20': xǁMailClientǁsend_email__mutmut_20, 
        'xǁMailClientǁsend_email__mutmut_21': xǁMailClientǁsend_email__mutmut_21, 
        'xǁMailClientǁsend_email__mutmut_22': xǁMailClientǁsend_email__mutmut_22, 
        'xǁMailClientǁsend_email__mutmut_23': xǁMailClientǁsend_email__mutmut_23, 
        'xǁMailClientǁsend_email__mutmut_24': xǁMailClientǁsend_email__mutmut_24
    }
    
    def send_email(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMailClientǁsend_email__mutmut_orig"), object.__getattribute__(self, "xǁMailClientǁsend_email__mutmut_mutants"), args, kwargs, self)
        return result 
    
    send_email.__signature__ = _mutmut_signature(xǁMailClientǁsend_email__mutmut_orig)
    xǁMailClientǁsend_email__mutmut_orig.__name__ = 'xǁMailClientǁsend_email'

class Art:
    def _calculate_price(self):
        raise NotImplementedError # pragma: no cover

class Book(Art):
    def xǁBookǁ__init____mutmut_orig(self, price):
        if price <= 0:
            raise ValueError("price mast been more zero")
        self._price = price
    def xǁBookǁ__init____mutmut_1(self, price):
        if price < 0:
            raise ValueError("price mast been more zero")
        self._price = price
    def xǁBookǁ__init____mutmut_2(self, price):
        if price <= 1:
            raise ValueError("price mast been more zero")
        self._price = price
    def xǁBookǁ__init____mutmut_3(self, price):
        if price <= 0:
            raise ValueError(None)
        self._price = price
    def xǁBookǁ__init____mutmut_4(self, price):
        if price <= 0:
            raise ValueError("XXprice mast been more zeroXX")
        self._price = price
    def xǁBookǁ__init____mutmut_5(self, price):
        if price <= 0:
            raise ValueError("PRICE MAST BEEN MORE ZERO")
        self._price = price
    def xǁBookǁ__init____mutmut_6(self, price):
        if price <= 0:
            raise ValueError("Price mast been more zero")
        self._price = price
    def xǁBookǁ__init____mutmut_7(self, price):
        if price <= 0:
            raise ValueError("price mast been more zero")
        self._price = None
    
    xǁBookǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBookǁ__init____mutmut_1': xǁBookǁ__init____mutmut_1, 
        'xǁBookǁ__init____mutmut_2': xǁBookǁ__init____mutmut_2, 
        'xǁBookǁ__init____mutmut_3': xǁBookǁ__init____mutmut_3, 
        'xǁBookǁ__init____mutmut_4': xǁBookǁ__init____mutmut_4, 
        'xǁBookǁ__init____mutmut_5': xǁBookǁ__init____mutmut_5, 
        'xǁBookǁ__init____mutmut_6': xǁBookǁ__init____mutmut_6, 
        'xǁBookǁ__init____mutmut_7': xǁBookǁ__init____mutmut_7
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBookǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBookǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBookǁ__init____mutmut_orig)
    xǁBookǁ__init____mutmut_orig.__name__ = 'xǁBookǁ__init__'

    @property
    def price(self):
        return self._calculate_price()

    def _calculate_price(self):
        return self._price

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_orig(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_1(mocker: MockFixture):
    client = None

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_2(mocker: MockFixture):
    client = MailClient()

    send_email_mock = None

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_3(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        None, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_4(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, None, autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_5(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=None, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_6(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_7(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_8(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_9(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_10(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'XXsend_emailXX', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_11(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'SEND_EMAIL', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_12(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'Send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_13(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=False, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_14(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email(None, 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_15(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', None)
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_16(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_17(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', )
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_18(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('XXhelloXX', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_19(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('HELLO', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_20(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('Hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_21(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'XXOlegXX')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_22(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'oleg')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_23(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'OLEG')
    send_email_mock.assert_called_with('hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_24(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with(None, 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_25(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', None)

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_26(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_27(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', )

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_28(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('XXhelloXX', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_29(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('HELLO', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_30(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('Hello', 'Oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_31(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'XXOlegXX')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_32(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'oleg')

# tests/


###############MailClient########################
def x_test_mail_client_with_mock__mutmut_33(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, return_value=None
    )

    client.send_email('hello', 'Oleg')
    send_email_mock.assert_called_with('hello', 'OLEG')

x_test_mail_client_with_mock__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_mail_client_with_mock__mutmut_1': x_test_mail_client_with_mock__mutmut_1, 
    'x_test_mail_client_with_mock__mutmut_2': x_test_mail_client_with_mock__mutmut_2, 
    'x_test_mail_client_with_mock__mutmut_3': x_test_mail_client_with_mock__mutmut_3, 
    'x_test_mail_client_with_mock__mutmut_4': x_test_mail_client_with_mock__mutmut_4, 
    'x_test_mail_client_with_mock__mutmut_5': x_test_mail_client_with_mock__mutmut_5, 
    'x_test_mail_client_with_mock__mutmut_6': x_test_mail_client_with_mock__mutmut_6, 
    'x_test_mail_client_with_mock__mutmut_7': x_test_mail_client_with_mock__mutmut_7, 
    'x_test_mail_client_with_mock__mutmut_8': x_test_mail_client_with_mock__mutmut_8, 
    'x_test_mail_client_with_mock__mutmut_9': x_test_mail_client_with_mock__mutmut_9, 
    'x_test_mail_client_with_mock__mutmut_10': x_test_mail_client_with_mock__mutmut_10, 
    'x_test_mail_client_with_mock__mutmut_11': x_test_mail_client_with_mock__mutmut_11, 
    'x_test_mail_client_with_mock__mutmut_12': x_test_mail_client_with_mock__mutmut_12, 
    'x_test_mail_client_with_mock__mutmut_13': x_test_mail_client_with_mock__mutmut_13, 
    'x_test_mail_client_with_mock__mutmut_14': x_test_mail_client_with_mock__mutmut_14, 
    'x_test_mail_client_with_mock__mutmut_15': x_test_mail_client_with_mock__mutmut_15, 
    'x_test_mail_client_with_mock__mutmut_16': x_test_mail_client_with_mock__mutmut_16, 
    'x_test_mail_client_with_mock__mutmut_17': x_test_mail_client_with_mock__mutmut_17, 
    'x_test_mail_client_with_mock__mutmut_18': x_test_mail_client_with_mock__mutmut_18, 
    'x_test_mail_client_with_mock__mutmut_19': x_test_mail_client_with_mock__mutmut_19, 
    'x_test_mail_client_with_mock__mutmut_20': x_test_mail_client_with_mock__mutmut_20, 
    'x_test_mail_client_with_mock__mutmut_21': x_test_mail_client_with_mock__mutmut_21, 
    'x_test_mail_client_with_mock__mutmut_22': x_test_mail_client_with_mock__mutmut_22, 
    'x_test_mail_client_with_mock__mutmut_23': x_test_mail_client_with_mock__mutmut_23, 
    'x_test_mail_client_with_mock__mutmut_24': x_test_mail_client_with_mock__mutmut_24, 
    'x_test_mail_client_with_mock__mutmut_25': x_test_mail_client_with_mock__mutmut_25, 
    'x_test_mail_client_with_mock__mutmut_26': x_test_mail_client_with_mock__mutmut_26, 
    'x_test_mail_client_with_mock__mutmut_27': x_test_mail_client_with_mock__mutmut_27, 
    'x_test_mail_client_with_mock__mutmut_28': x_test_mail_client_with_mock__mutmut_28, 
    'x_test_mail_client_with_mock__mutmut_29': x_test_mail_client_with_mock__mutmut_29, 
    'x_test_mail_client_with_mock__mutmut_30': x_test_mail_client_with_mock__mutmut_30, 
    'x_test_mail_client_with_mock__mutmut_31': x_test_mail_client_with_mock__mutmut_31, 
    'x_test_mail_client_with_mock__mutmut_32': x_test_mail_client_with_mock__mutmut_32, 
    'x_test_mail_client_with_mock__mutmut_33': x_test_mail_client_with_mock__mutmut_33
}

def test_mail_client_with_mock(*args, **kwargs):
    result = _mutmut_trampoline(x_test_mail_client_with_mock__mutmut_orig, x_test_mail_client_with_mock__mutmut_mutants, args, kwargs)
    return result 

test_mail_client_with_mock.__signature__ = _mutmut_signature(x_test_mail_client_with_mock__mutmut_orig)
x_test_mail_client_with_mock__mutmut_orig.__name__ = 'x_test_mail_client_with_mock'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_orig(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_1(mocker: MockFixture):
    client = None

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_2(mocker: MockFixture):
    client = MailClient()

    send_email_mock = None
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_3(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        None, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_4(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, None, autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_5(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=None, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_6(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=None
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_7(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_8(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_9(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_10(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_11(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'XXsend_emailXX', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_12(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'SEND_EMAIL', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_13(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'Send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_14(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=False, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_15(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception(None)
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_16(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('XXsome errorXX')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_17(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('SOME ERROR')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_18(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('Some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_19(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(None) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_20(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email(None, 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_21(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', None)
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_22(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_23(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', )
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_24(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('XXhelloXX', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_25(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('HELLO', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_26(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('Hello', 'Oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_27(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'XXOlegXX')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_28(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'oleg')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_29(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'OLEG')
    assert str(exc_info.value) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_30(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(None) == 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_31(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) != 'some error'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_32(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'XXsome errorXX'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_33(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'SOME ERROR'

# а сейчас давайте проверим ошибку!
def x_test_mail_client_returns_error_with_mock__mutmut_34(mocker: MockFixture):
    client = MailClient()

    send_email_mock = mocker.patch.object(
        MailClient, 'send_email', autospec=True, side_effect=Exception('some error')
    )
    with pytest.raises(Exception) as exc_info:
        client.send_email('hello', 'Oleg')
    assert str(exc_info.value) == 'Some error'

x_test_mail_client_returns_error_with_mock__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_mail_client_returns_error_with_mock__mutmut_1': x_test_mail_client_returns_error_with_mock__mutmut_1, 
    'x_test_mail_client_returns_error_with_mock__mutmut_2': x_test_mail_client_returns_error_with_mock__mutmut_2, 
    'x_test_mail_client_returns_error_with_mock__mutmut_3': x_test_mail_client_returns_error_with_mock__mutmut_3, 
    'x_test_mail_client_returns_error_with_mock__mutmut_4': x_test_mail_client_returns_error_with_mock__mutmut_4, 
    'x_test_mail_client_returns_error_with_mock__mutmut_5': x_test_mail_client_returns_error_with_mock__mutmut_5, 
    'x_test_mail_client_returns_error_with_mock__mutmut_6': x_test_mail_client_returns_error_with_mock__mutmut_6, 
    'x_test_mail_client_returns_error_with_mock__mutmut_7': x_test_mail_client_returns_error_with_mock__mutmut_7, 
    'x_test_mail_client_returns_error_with_mock__mutmut_8': x_test_mail_client_returns_error_with_mock__mutmut_8, 
    'x_test_mail_client_returns_error_with_mock__mutmut_9': x_test_mail_client_returns_error_with_mock__mutmut_9, 
    'x_test_mail_client_returns_error_with_mock__mutmut_10': x_test_mail_client_returns_error_with_mock__mutmut_10, 
    'x_test_mail_client_returns_error_with_mock__mutmut_11': x_test_mail_client_returns_error_with_mock__mutmut_11, 
    'x_test_mail_client_returns_error_with_mock__mutmut_12': x_test_mail_client_returns_error_with_mock__mutmut_12, 
    'x_test_mail_client_returns_error_with_mock__mutmut_13': x_test_mail_client_returns_error_with_mock__mutmut_13, 
    'x_test_mail_client_returns_error_with_mock__mutmut_14': x_test_mail_client_returns_error_with_mock__mutmut_14, 
    'x_test_mail_client_returns_error_with_mock__mutmut_15': x_test_mail_client_returns_error_with_mock__mutmut_15, 
    'x_test_mail_client_returns_error_with_mock__mutmut_16': x_test_mail_client_returns_error_with_mock__mutmut_16, 
    'x_test_mail_client_returns_error_with_mock__mutmut_17': x_test_mail_client_returns_error_with_mock__mutmut_17, 
    'x_test_mail_client_returns_error_with_mock__mutmut_18': x_test_mail_client_returns_error_with_mock__mutmut_18, 
    'x_test_mail_client_returns_error_with_mock__mutmut_19': x_test_mail_client_returns_error_with_mock__mutmut_19, 
    'x_test_mail_client_returns_error_with_mock__mutmut_20': x_test_mail_client_returns_error_with_mock__mutmut_20, 
    'x_test_mail_client_returns_error_with_mock__mutmut_21': x_test_mail_client_returns_error_with_mock__mutmut_21, 
    'x_test_mail_client_returns_error_with_mock__mutmut_22': x_test_mail_client_returns_error_with_mock__mutmut_22, 
    'x_test_mail_client_returns_error_with_mock__mutmut_23': x_test_mail_client_returns_error_with_mock__mutmut_23, 
    'x_test_mail_client_returns_error_with_mock__mutmut_24': x_test_mail_client_returns_error_with_mock__mutmut_24, 
    'x_test_mail_client_returns_error_with_mock__mutmut_25': x_test_mail_client_returns_error_with_mock__mutmut_25, 
    'x_test_mail_client_returns_error_with_mock__mutmut_26': x_test_mail_client_returns_error_with_mock__mutmut_26, 
    'x_test_mail_client_returns_error_with_mock__mutmut_27': x_test_mail_client_returns_error_with_mock__mutmut_27, 
    'x_test_mail_client_returns_error_with_mock__mutmut_28': x_test_mail_client_returns_error_with_mock__mutmut_28, 
    'x_test_mail_client_returns_error_with_mock__mutmut_29': x_test_mail_client_returns_error_with_mock__mutmut_29, 
    'x_test_mail_client_returns_error_with_mock__mutmut_30': x_test_mail_client_returns_error_with_mock__mutmut_30, 
    'x_test_mail_client_returns_error_with_mock__mutmut_31': x_test_mail_client_returns_error_with_mock__mutmut_31, 
    'x_test_mail_client_returns_error_with_mock__mutmut_32': x_test_mail_client_returns_error_with_mock__mutmut_32, 
    'x_test_mail_client_returns_error_with_mock__mutmut_33': x_test_mail_client_returns_error_with_mock__mutmut_33, 
    'x_test_mail_client_returns_error_with_mock__mutmut_34': x_test_mail_client_returns_error_with_mock__mutmut_34
}

def test_mail_client_returns_error_with_mock(*args, **kwargs):
    result = _mutmut_trampoline(x_test_mail_client_returns_error_with_mock__mutmut_orig, x_test_mail_client_returns_error_with_mock__mutmut_mutants, args, kwargs)
    return result 

test_mail_client_returns_error_with_mock.__signature__ = _mutmut_signature(x_test_mail_client_returns_error_with_mock__mutmut_orig)
x_test_mail_client_returns_error_with_mock__mutmut_orig.__name__ = 'x_test_mail_client_returns_error_with_mock'
###############MailClient########################


def x_test_book_creation__mutmut_orig(faker: Faker):
    faker.seed_instance(1234)
    price = faker.pyint(min_value=0)
    book = Book(price)
    assert book.price == price
###############MailClient########################


def x_test_book_creation__mutmut_1(faker: Faker):
    faker.seed_instance(None)
    price = faker.pyint(min_value=0)
    book = Book(price)
    assert book.price == price
###############MailClient########################


def x_test_book_creation__mutmut_2(faker: Faker):
    faker.seed_instance(1235)
    price = faker.pyint(min_value=0)
    book = Book(price)
    assert book.price == price
###############MailClient########################


def x_test_book_creation__mutmut_3(faker: Faker):
    faker.seed_instance(1234)
    price = None
    book = Book(price)
    assert book.price == price
###############MailClient########################


def x_test_book_creation__mutmut_4(faker: Faker):
    faker.seed_instance(1234)
    price = faker.pyint(min_value=None)
    book = Book(price)
    assert book.price == price
###############MailClient########################


def x_test_book_creation__mutmut_5(faker: Faker):
    faker.seed_instance(1234)
    price = faker.pyint(min_value=1)
    book = Book(price)
    assert book.price == price
###############MailClient########################


def x_test_book_creation__mutmut_6(faker: Faker):
    faker.seed_instance(1234)
    price = faker.pyint(min_value=0)
    book = None
    assert book.price == price
###############MailClient########################


def x_test_book_creation__mutmut_7(faker: Faker):
    faker.seed_instance(1234)
    price = faker.pyint(min_value=0)
    book = Book(None)
    assert book.price == price
###############MailClient########################


def x_test_book_creation__mutmut_8(faker: Faker):
    faker.seed_instance(1234)
    price = faker.pyint(min_value=0)
    book = Book(price)
    assert book.price != price

x_test_book_creation__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_book_creation__mutmut_1': x_test_book_creation__mutmut_1, 
    'x_test_book_creation__mutmut_2': x_test_book_creation__mutmut_2, 
    'x_test_book_creation__mutmut_3': x_test_book_creation__mutmut_3, 
    'x_test_book_creation__mutmut_4': x_test_book_creation__mutmut_4, 
    'x_test_book_creation__mutmut_5': x_test_book_creation__mutmut_5, 
    'x_test_book_creation__mutmut_6': x_test_book_creation__mutmut_6, 
    'x_test_book_creation__mutmut_7': x_test_book_creation__mutmut_7, 
    'x_test_book_creation__mutmut_8': x_test_book_creation__mutmut_8
}

def test_book_creation(*args, **kwargs):
    result = _mutmut_trampoline(x_test_book_creation__mutmut_orig, x_test_book_creation__mutmut_mutants, args, kwargs)
    return result 

test_book_creation.__signature__ = _mutmut_signature(x_test_book_creation__mutmut_orig)
x_test_book_creation__mutmut_orig.__name__ = 'x_test_book_creation'

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




















