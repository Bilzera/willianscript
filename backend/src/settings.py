# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import tmpl_middleware
from tekton.gae.middleware import router_middleware, parameter, webapp2_dependencies, email_errors
from usuario import LogInOut_middleware

SENDER_EMAIL = 'willian.augusto.campos@gmail.com'
WEB_BASE_PACKAGE = "web"
MIDDLEWARES = [LogInOut_middleware.execute,
               tmpl_middleware.execute,
               email_errors.execute,
               webapp2_dependencies.execute,
               parameter.execute,
               router_middleware.execute]

