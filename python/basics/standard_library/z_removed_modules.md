# Removed Python Standard Library Modules

The modules described in this chapter have been removed from the Python standard library. They are documented here to help people find replacements or alternatives.

---

| Module         | Description / Replacement Suggestion |
|----------------|--------------------------------------|
| aifc           | Read/write AIFF/AIFC files. Use `soundfile` or `audioread`. |
| asynchat       | Async socket command/response handler. Use `asyncio`. |
| asyncore       | Async socket handler. Use `asyncio`. |
| audioop        | Manipulate raw audio data. Use `numpy` or `scipy`. |
| cgi            | CGI support. Use `flask`, `django`, or `wsgi`. |
| cgitb          | Traceback manager for CGI scripts. Use standard `traceback` or web frameworks. |
| chunk          | Read IFF chunked data. Use `struct` or third-party libs. |
| crypt          | Check Unix passwords. Use `passlib` or `cryptography`. |
| distutils      | Build/install modules. Use `setuptools` or `pip`. |
| imghdr         | Determine image type. Use `Pillow`. |
| imp            | Import internals. Use `importlib`. |
| mailcap        | Mailcap file handling. Use third-party libraries. |
| msilib         | Microsoft Installer files. Use third-party libraries. |
| nis            | Sun’s NIS interface. Use third-party libraries. |
| nntplib        | NNTP protocol client. Use third-party libraries. |
| ossaudiodev    | OSS audio devices. Use `sounddevice` or `pyaudio`. |
| pipes          | Shell pipelines interface. Use `subprocess`. |
| smtpd          | SMTP server. Use `aiosmtpd` or other SMTP libraries. |
| sndhdr         | Determine sound file type. Use `Pydub` or `soundfile`. |
| spwd           | Shadow password database. Use third-party libraries. |
| sunau          | Read/write Sun AU files. Use `soundfile`. |
| telnetlib      | Telnet client. Use third-party libraries. |
| uu             | Encode/decode uuencode files. Use third-party libraries. |
| xdrlib         | Encode/decode XDR data. Use third-party libraries. |

---
