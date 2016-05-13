#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://pythonworld.ru/web/cgi-3.html

import cgi
import html
import http.cookies
import os

from _wall import Wall
wall = Wall()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session = cookie.get("session")
