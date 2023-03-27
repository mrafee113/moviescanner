~ via system_venv …
➜ workon moviescanner

~ via moviescanner …
➜ ipy
Python 3.10.7 (main, Mar 10 2023, 10:47:39) [GCC 12.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.13.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import requests

In [2]: from bs4 import BeautifulSoup

In [3]: def get_watched_movies(username):
   ...:     base_url = f"https://letterboxd.com/{username}/films/"

In [4]: def get_watched_movies(username):
   ...:     base_url = f"https://letterboxd.com/{username}/films/"
   ...:     movies = []
   ...: 

In [5]: def get_watched_movies(username):
   ...:     base_url = f"https://letterboxd.com/{username}/films/"
   ...:     movies = []
   ...: 

In [6]: def get_watched_movies(username):
   ...:     base_url = f"https://letterboxd.com/{username}/films/"
   ...:     movies = []
   ...: 

In [7]: def get_watched_movies(username):
   ...:     base_url = f"https://letterboxd.com/{username}/films/"
   ...:     movies = []
   ...: 

In [8]: def get_watched_movies(username):
   ...:     base_url = f"https://letterboxd.com/{username}/films/"
   ...:     movies = []
   ...:     page = 1
   ...:     while True:
   ...:         url = f"{base_url}page/{page}/"

In [9]: def get_watched_movies(username):
   ...:     base_url = f"https://letterboxd.com/{username}/films/"
   ...:     movies = []
   ...:     page = 1
   ...:     while True:
   ...:         url = f"{base_url}page/{page}/"
   ...:         response = requests.get(url)
   ...:         soup = BeautifulSoup(response.content, 'html.parser')
   ...:         movie_elements = soup.find_all('li', class_='poster-container')
   ...:         if not movie_elements:
   ...:             break
   ...:         for movie_element in movie_elements:
   ...:             title_element = movie_element.find('img', class_='frame')
   ...:             title = title_element['alt'] if title_element else ''
   ...:             movies.append(title)
   ...:         page += 1
   ...:     return movies
   ...: 

In [10]: username = 'mrafee113'

In [11]: watched_movies = get_watched_movies(username)
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
Cell In[11], line 1
----> 1 watched_movies = get_watched_movies(username)

Cell In[9], line 7, in get_watched_movies(username)
      5 while True:
      6     url = f"{base_url}page/{page}/"
----> 7     response = requests.get(url)
      8     soup = BeautifulSoup(response.content, 'html.parser')
      9     movie_elements = soup.find_all('li', class_='poster-container')

File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/api.py:73, in get(url, params, **kwargs)
     62 def get(url, params=None, **kwargs):
     63     r"""Sends a GET request.
     64 
     65     :param url: URL for the new :class:`Request` object.
   (...)
     70     :rtype: requests.Response
     71     """
---> 73     return request("get", url, params=params, **kwargs)

File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/api.py:59, in request(method, url, **kwargs)
     55 # By using the 'with' statement we are sure the session is closed, thus we
     56 # avoid leaving sockets open which can trigger a ResourceWarning in some
     57 # cases, and look like a memory leak in others.
     58 with sessions.Session() as session:
---> 59     return session.request(method=method, url=url, **kwargs)

File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/sessions.py:587, in Session.request(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
    582 send_kwargs = {
    583     "timeout": timeout,
    584     "allow_redirects": allow_redirects,
    585 }
    586 send_kwargs.update(settings)
--> 587 resp = self.send(prep, **send_kwargs)
    589 return resp

File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/sessions.py:701, in Session.send(self, request, **kwargs)
    698 start = preferred_clock()
    700 # Send the request
--> 701 r = adapter.send(request, **kwargs)
    703 # Total elapsed time of the request (approximately)
    704 elapsed = preferred_clock() - start

File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/adapters.py:487, in HTTPAdapter.send(self, request, stream, timeout, verify, cert, proxies)
    484     timeout = TimeoutSauce(connect=timeout, read=timeout)
    486 try:
--> 487     resp = conn.urlopen(
    488         method=request.method,
    489         url=url,
    490         body=request.body,
    491         headers=request.headers,
    492         redirect=False,
    493         assert_same_host=False,
    494         preload_content=False,
    495         decode_content=False,
    496         retries=self.max_retries,
    497         timeout=timeout,
    498         chunked=chunked,
    499     )
    501 except (ProtocolError, OSError) as err:
    502     raise ConnectionError(err, request=request)

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/connectionpool.py:703, in HTTPConnectionPool.urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
    700     self._prepare_proxy(conn)
    702 # Make the request on the httplib connection object.
--> 703 httplib_response = self._make_request(
    704     conn,
    705     method,
    706     url,
    707     timeout=timeout_obj,
    708     body=body,
    709     headers=headers,
    710     chunked=chunked,
    711 )
    713 # If we're going to release the connection in ``finally:``, then
    714 # the response doesn't need to know about the connection. Otherwise
    715 # it will also try to release it and we'll have a double-release
    716 # mess.
    717 response_conn = conn if not release_conn else None

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/connectionpool.py:386, in HTTPConnectionPool._make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
    384 # Trigger any extra validation we need to do.
    385 try:
--> 386     self._validate_conn(conn)
    387 except (SocketTimeout, BaseSSLError) as e:
    388     # Py2 raises this as a BaseSSLError, Py3 raises it as socket timeout.
    389     self._raise_timeout(err=e, url=url, timeout_value=conn.timeout)

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/connectionpool.py:1042, in HTTPSConnectionPool._validate_conn(self, conn)
   1040 # Force connect early to allow us to validate the connection.
   1041 if not getattr(conn, "sock", None):  # AppEngine might not have  `.sock`
-> 1042     conn.connect()
   1044 if not conn.is_verified:
   1045     warnings.warn(
   1046         (
   1047             "Unverified HTTPS request is being made to host '%s'. "
   (...)
   1052         InsecureRequestWarning,
   1053     )

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/connection.py:363, in HTTPSConnection.connect(self)
    361 def connect(self):
    362     # Add certificate verification
--> 363     self.sock = conn = self._new_conn()
    364     hostname = self.host
    365     tls_in_tls = False

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/connection.py:174, in HTTPConnection._new_conn(self)
    171     extra_kw["socket_options"] = self.socket_options
    173 try:
--> 174     conn = connection.create_connection(
    175         (self._dns_host, self.port), self.timeout, **extra_kw
    176     )
    178 except SocketTimeout:
    179     raise ConnectTimeoutError(
    180         self,
    181         "Connection to %s timed out. (connect timeout=%s)"
    182         % (self.host, self.timeout),
    183     )

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/util/connection.py:85, in create_connection(address, timeout, source_address, socket_options)
     83     if source_address:
     84         sock.bind(source_address)
---> 85     sock.connect(sa)
     86     return sock
     88 except socket.error as e:

KeyboardInterrupt: 

In [12]: base_url = f'https://letterboxd.com/{username}/films/'

In [13]: movies = []

In [14]: page = 1

In [15]: url = f'{base_url}page/{page}/'

In [16]: proxies = {'http': 'http://localhost:10806', 'https': 'https://localhos
    ...: t:10806'}

In [17]: base_url = f'http://letterboxd.com/{username}/films/'

In [18]: response = requests.get(url, 'html.parser', proxies=proxies)
---------------------------------------------------------------------------
SSLZeroReturnError                        Traceback (most recent call last)
File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/connectionpool.py:700, in HTTPConnectionPool.urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
    699 if is_new_proxy_conn and http_tunnel_required:
--> 700     self._prepare_proxy(conn)
    702 # Make the request on the httplib connection object.

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/connectionpool.py:996, in HTTPSConnectionPool._prepare_proxy(self, conn)
    994     conn.tls_in_tls_required = True
--> 996 conn.connect()

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/connection.py:369, in HTTPSConnection.connect(self)
    368 if self.tls_in_tls_required:
--> 369     self.sock = conn = self._connect_tls_proxy(hostname, conn)
    370     tls_in_tls = True

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/connection.py:504, in HTTPSConnection._connect_tls_proxy(self, hostname, conn)
    502 # If no cert was provided, use only the default options for server
    503 # certificate validation
--> 504 socket = ssl_wrap_socket(
    505     sock=conn,
    506     ca_certs=self.ca_certs,
    507     ca_cert_dir=self.ca_cert_dir,
    508     ca_cert_data=self.ca_cert_data,
    509     server_hostname=hostname,
    510     ssl_context=ssl_context,
    511 )
    513 if ssl_context.verify_mode != ssl.CERT_NONE and not getattr(
    514     ssl_context, "check_hostname", False
    515 ):
    516     # While urllib3 attempts to always turn off hostname matching from
    517     # the TLS library, this cannot always be done. So we check whether
    518     # the TLS Library still thinks it's matching hostnames.

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/util/ssl_.py:449, in ssl_wrap_socket(sock, keyfile, certfile, cert_reqs, ca_certs, server_hostname, ssl_version, ciphers, ssl_context, ca_cert_dir, key_password, ca_cert_data, tls_in_tls)
    448 if send_sni:
--> 449     ssl_sock = _ssl_wrap_socket_impl(
    450         sock, context, tls_in_tls, server_hostname=server_hostname
    451     )
    452 else:

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/util/ssl_.py:493, in _ssl_wrap_socket_impl(sock, ssl_context, tls_in_tls, server_hostname)
    492 if server_hostname:
--> 493     return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
    494 else:

File /usr/lib/python3.10/ssl.py:513, in SSLContext.wrap_socket(self, sock, server_side, do_handshake_on_connect, suppress_ragged_eofs, server_hostname, session)
    507 def wrap_socket(self, sock, server_side=False,
    508                 do_handshake_on_connect=True,
    509                 suppress_ragged_eofs=True,
    510                 server_hostname=None, session=None):
    511     # SSLSocket class handles server_hostname encoding before it calls
    512     # ctx._wrap_socket()
--> 513     return self.sslsocket_class._create(
    514         sock=sock,
    515         server_side=server_side,
    516         do_handshake_on_connect=do_handshake_on_connect,
    517         suppress_ragged_eofs=suppress_ragged_eofs,
    518         server_hostname=server_hostname,
    519         context=self,
    520         session=session
    521     )

File /usr/lib/python3.10/ssl.py:1071, in SSLSocket._create(cls, sock, server_side, do_handshake_on_connect, suppress_ragged_eofs, server_hostname, context, session)
   1070             raise ValueError("do_handshake_on_connect should not be specified for non-blocking sockets")
-> 1071         self.do_handshake()
   1072 except (OSError, ValueError):

File /usr/lib/python3.10/ssl.py:1342, in SSLSocket.do_handshake(self, block)
   1341         self.settimeout(None)
-> 1342     self._sslobj.do_handshake()
   1343 finally:

SSLZeroReturnError: TLS/SSL connection has been closed (EOF) (_ssl.c:997)

During handling of the above exception, another exception occurred:

MaxRetryError                             Traceback (most recent call last)
File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/adapters.py:487, in HTTPAdapter.send(self, request, stream, timeout, verify, cert, proxies)
    486 try:
--> 487     resp = conn.urlopen(
    488         method=request.method,
    489         url=url,
    490         body=request.body,
    491         headers=request.headers,
    492         redirect=False,
    493         assert_same_host=False,
    494         preload_content=False,
    495         decode_content=False,
    496         retries=self.max_retries,
    497         timeout=timeout,
    498         chunked=chunked,
    499     )
    501 except (ProtocolError, OSError) as err:

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/connectionpool.py:787, in HTTPConnectionPool.urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
    785     e = ProtocolError("Connection aborted.", e)
--> 787 retries = retries.increment(
    788     method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
    789 )
    790 retries.sleep()

File ~/.venvs/moviescanner/lib/python3.10/site-packages/urllib3/util/retry.py:592, in Retry.increment(self, method, url, response, error, _pool, _stacktrace)
    591 if new_retry.is_exhausted():
--> 592     raise MaxRetryError(_pool, url, error or ResponseError(cause))
    594 log.debug("Incremented Retry for (url='%s'): %r", url, new_retry)

MaxRetryError: HTTPSConnectionPool(host='letterboxd.com', port=443): Max retries exceeded with url: /mrafee113/films/page/1/?html.parser (Caused by SSLError(SSLZeroReturnError(6, 'TLS/SSL connection has been closed (EOF) (_ssl.c:997)')))

During handling of the above exception, another exception occurred:

SSLError                                  Traceback (most recent call last)
Cell In[18], line 1
----> 1 response = requests.get(url, 'html.parser', proxies=proxies)

File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/api.py:73, in get(url, params, **kwargs)
     62 def get(url, params=None, **kwargs):
     63     r"""Sends a GET request.
     64 
     65     :param url: URL for the new :class:`Request` object.
   (...)
     70     :rtype: requests.Response
     71     """
---> 73     return request("get", url, params=params, **kwargs)

File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/api.py:59, in request(method, url, **kwargs)
     55 # By using the 'with' statement we are sure the session is closed, thus we
     56 # avoid leaving sockets open which can trigger a ResourceWarning in some
     57 # cases, and look like a memory leak in others.
     58 with sessions.Session() as session:
---> 59     return session.request(method=method, url=url, **kwargs)

File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/sessions.py:587, in Session.request(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
    582 send_kwargs = {
    583     "timeout": timeout,
    584     "allow_redirects": allow_redirects,
    585 }
    586 send_kwargs.update(settings)
--> 587 resp = self.send(prep, **send_kwargs)
    589 return resp

File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/sessions.py:701, in Session.send(self, request, **kwargs)
    698 start = preferred_clock()
    700 # Send the request
--> 701 r = adapter.send(request, **kwargs)
    703 # Total elapsed time of the request (approximately)
    704 elapsed = preferred_clock() - start

File ~/.venvs/moviescanner/lib/python3.10/site-packages/requests/adapters.py:518, in HTTPAdapter.send(self, request, stream, timeout, verify, cert, proxies)
    514         raise ProxyError(e, request=request)
    516     if isinstance(e.reason, _SSLError):
    517         # This branch is for urllib3 v1.22 and later.
--> 518         raise SSLError(e, request=request)
    520     raise ConnectionError(e, request=request)
    522 except ClosedPoolError as e:

SSLError: HTTPSConnectionPool(host='letterboxd.com', port=443): Max retries exceeded with url: /mrafee113/films/page/1/?html.parser (Caused by SSLError(SSLZeroReturnError(6, 'TLS/SSL connection has been closed (EOF) (_ssl.c:997)')))

In [19]: proxies
Out[19]: {'http': 'http://localhost:10806', 'https': 'https://localhost:10806'}

In [20]: proxies = {'http': 'socks5://localhost:10806', 'https': 'socks5://local
    ...: host:10806'}

In [21]: response = requests.get(url, 'html.parser', proxies=proxies)

In [22]: response.status_code
Out[22]: 200

In [23]: soup = BeautifulSoup(response.content, 'html.parser')

In [24]: movie_elements = soup.find_all('li', class_='poster-container')

In [25]: for movie_element in movie_elements:
    ...:     title_element = movie_element.find('img', class_='frame')
    ...:     title = title_element['alt'] if title_element else ''
    ...:     movies.append(title)
    ...: 

In [26]: movies
Out[26]: 
['',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '']

In [27]: movies.clear()

In [28]: for movie_element in movie_elements:
    ...:     title_element = movie_element.find('img', class_='frame')
    ...:     print(title_element)
    ...: 
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None

In [29]: movie_elements = soup.find_all('li', class_='poster-container fil
    ...: m-watched')

In [30]: for movie_element in movie_elements:
    ...:     title_element = movie_element.find('img', class_='frame')
    ...:     print(title_element)
    ...: 

In [31]: len(movie_elements)
Out[31]: 0

In [32]: from lxml import html
--------------------------------------------------------------------------
ModuleNotFoundError                      Traceback (most recent call last)
Cell In[32], line 1
----> 1 from lxml import html

ModuleNotFoundError: No module named 'lxml'

In [33]:                                                                  
Do you really want to exit ([y]/n)? y
pi%                                                                       
~ via moviescanner took 12m 36.4s …
➜ pip install lxml     
Collecting lxml
  Using cached lxml-4.9.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (7.1 MB)
Installing collected packages: lxml
Successfully installed lxml-4.9.2

~ via moviescanner took 4.3s …
➜ ipy
Python 3.10.7 (main, Mar 10 2023, 10:47:39) [GCC 12.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.13.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from lxml import html

In [2]: import requests

In [3]: base_url = f'http://letterboxd.com/{username}/films/'
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[3], line 1
----> 1 base_url = f'http://letterboxd.com/{username}/films/'

NameError: name 'username' is not defined

In [4]: username = 'mrafee113'

In [5]: base_url = f'http://letterboxd.com/{username}/films/'

In [6]: movies = []

In [7]: page = 1

In [8]: url = f'{base_url}page/{page}/'

In [9]: proxies = {'http': 'socks5://localhost:10806', 'https': 'socks5://localh
   ...: ost:10806'}

In [10]: response = requests.get(url, 'html.parser', proxies=proxies)

In [11]: inner_html = response.text

In [12]: inner_html
Out[12]: '\n\n<!DOCTYPE html>\n\n<!--[if lt IE 7 ]> <html lang="en" class="ie6 lte9 lte8 lte7 lte6 no-js"> <![endif]-->\n<!--[if IE 7 ]>    <html lang="en" class="ie7 lte9 lte8 lte7 no-js"> <![endif]-->\n<!--[if IE 8 ]>    <html lang="en" class="ie8 lte9 lte8 no-js"> <![endif]-->\n<!--[if IE 9 ]>    <html lang="en" class="ie9 lte9 no-js"> <![endif]-->\n<!--[if (gt IE 9)|!(IE)]><!--> <html id="html" lang="en" class="no-mobile no-js"> <!--<![endif]-->\n<head>\n\t<meta charset="UTF-8" />\n\t<meta name="viewport" content="width=1024" />\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />\n\t<meta name="description" content="Mehdi Rafee’s films" />\n\t\n\t\n\t<meta property="og:url" content="https://letterboxd.com/mrafee113/films/?html.parser" />\n\t<meta property="og:title" content="Mehdi Rafee’s films" />\n\t<meta property="og:description" content="Mehdi Rafee’s films" />\n\t<meta property="og:image" content="https://s.ltrbxd.com/static/img/default-share.e38c5d62.png" />\n\t\n\t<meta name="application-name" content="Letterboxd" />\n\t<meta name="theme-color" content="#445566" />\n\t<meta name="msapplication-TileColor" content="#445566" />\n\t<meta name="apple-itunes-app" content="app-id=1054271011, affiliate-data=11l5KW, app-argument=https://letterboxd.com/mrafee113/films/?html.parser" />\n\t<meta name="mobile-web-app-capable" content="yes" />\n\n\t<title>&lrm;Mehdi Rafee’s films &bull; Letterboxd</title>\n\t\n\t<script>\n\t\twindow.dataLayer = window.dataLayer || [];\n\t\twindow.gtag = window.gtag || function () {\n\t\t\tdataLayer.push(arguments);\n\t\t};\n\t\tfunction ga() {}\n\t</script>\n\n\t<script async src="https://www.googletagmanager.com/gtag/js?id=G-D3ECBB4D7L"></script>\n\n\t<script>\n\t\twindow.dataLayer = window.dataLayer || [];\n\t\twindow.gtag = window.gtag || function () {\n\t\t\tdataLayer.push(arguments);\n\t\t};\n\t\tgtag(\'js\', new Date());\n\t\n\t\tvar analytic_params = {};\n\t\t\n\t\t\n\t\tanalytic_params[\'user_type\'] = \'Visitor\';\n\t\tanalytic_params[\'template\'] = \'/object/person/films-watched\';\n\t\t\n\t\t\n\n\t\tif (analytic_params.member_type) {\n\t\t\tgtag(\'set\', \'user_properties\', { \n\t\t\t\tmember_type: analytic_params.member_type,\n\t\t\t});\n\t\t\tdelete analytic_params.member_type;\n\t\t}\n\t\tvar config = {\n\t\t\t...analytic_params,\n\t\t\t\'cookie_domain\': \'letterboxd.com\', \n\t\t\t\'optimize_id\': \'GTM-TB8HSDN\', \n\t\t};\n\t\tgtag(\'config\', \'G-D3ECBB4D7L\', config);\n\t</script>\n\n\n\t<script>\n\t\tvar isMobile = false,\n\t\t\tisMobileOptimised = true,\n\t\t\trenderMobile = false,\n\t\t\tuseStaticFonts = false,\n\t\t\tdisableFrameProtection = false,\n\t\t\tbaseURL = "",\n\t\t\tsuccessMessages = [],\n\t\t\terrorMessages = [],\n\t\t\tstickyMessages = [],\n\t\t\tglobals = {\n\t\t\tautoAddFilm: false\t\t\t\n\t\t\t\t, spinners: {\n\t\t\t\t\tajax_242d35: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_12_2C3641: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_14_20272f: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_16_161B21: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\'\n\t\t\t\t}\n\t\t\t},\n\t\t\tsupermodelCSRF = "",\n\t\t\tgRecaptchaKey = \'6Le3mMIUAAAAAEXbwZ7M1R5jEv0V5xbvj7bgXq2g\',\n\t\t\tperson = {\n\t\t\t\tusername: ""\n\t\t\t\t, loggedIn: false\n\t\t\t\t\n\t\t\t\t, showAds: true\n\t\t\t\t, role: "guest"\n\t\t\t\t, hasExtendedServiceFilters: false\n\t\t\t\t, canBulkAddToLists: false\n\t\t\t\t, canFilterOwned: false\n\t\t\t\t, hasHqRole: false\n\t\t\t\t, canHaveHqDashboard: false\n\t\t\t\t, hasMemberStatistics: false\n\t\t\t\t, blockedMembers: []\n\t\t\t\t, showAdultContent: false\n\t\t\t\t, validated: null\n\t\t\t\t, trusted: false\n\t\t\t\t, hasBlocked : function(member) { for (var i = 0; i !== person.blockedMembers.length; i++) {if (person.blockedMembers[i] === member) return true;} return false; }\n\t\t\t\t, viewingTags: []\n\t\t\t\t, hasMoreTags: true\n\t\t\t\t, getCustomPoster : function(filmId) { return null; }\n\t\t\t},\n\t\t\tdisableAds = true;\n\t\t\n\t\t\n\t\t\nsupermodelCSRF = "9749e0a0bd2da01647eb";\n\n\t\t\n\n\t\t\n\n\t\t\n\n\t\t\n\t\t\tif ( screen.width < 768 ) {\n\t\t\t\tvar date = new Date();\n\t\t\t\tvar maxAge = 365 * 24 * 60 * 60;\n\t\t\t\tdate.setTime(date.getTime() + maxAge * 1000);\n\t\t\t\tvar expires = \'; expires=\' + date.toUTCString();\n\t\t\t\tdocument.cookie = "useMobileSite=yes" + expires + "; path=/; maxAge=" + maxAge;\n\t\t\t\tif ( document.cookie && document.cookie.indexOf("useMobileSite=yes") >= 0 ) {\n\t\t\t\t\twindow.location.reload(true);\n\t\t\t\t} else {\n\t\t\t\t\t// No cookies.  No Mobile version.\n\t\t\t\t}\n\t\t\t}\n\t\t\n\n\t\tvar isWindows = navigator.platform.toUpperCase().indexOf(\'WIN\') >= 0; // Detect windows platform\n\t\tif (isWindows) { document.documentElement.classList.add(\'is-windows\'); }\n\t\t\n\t\t\n\t</script>\n\n\t<link rel="manifest" href="/manifest.json" />\n\t<link rel="author" type="text/plain" href="/humans.txt" />\n\t<link rel="mask-icon" href="https://s.ltrbxd.com/static/img/icons/letterboxd-decal-l-16px.5fe24c7d.svg" color="#445566" />\n\t<link rel="shortcut icon" sizes="196x196" href="https://s.ltrbxd.com/static/img/icons/touch-icon-192x192.257b84e7.png" />\n\t<link rel="shortcut icon" href="/favicon.ico" />\n\t<link rel="search" type="application/opensearchdescription+xml" title="Letterboxd" href="/static/opensearch.xml" />\n\t\n\t\n\t<!--[if lte IE 9 ]>\n\t\t<link href="https://s.ltrbxd.com/static/css/ie9-1.min.066b855d.css" rel="stylesheet" media="screen, projection"/>\n\t\t<link href="https://s.ltrbxd.com/static/css/ie9-2.min.13b2f50c.css" rel="stylesheet" media="screen, projection"/>\n\t<![endif]-->\n\t<!--[if (gt IE 9)|!(IE)]><!-->\n\t\t<link href="https://s.ltrbxd.com/static/css/main.min.97414920.css" rel="stylesheet" media="screen, projection"/>\n\t<!--<![endif]-->\n\t<!--[if lte IE 6]><script>location.replace("/errors/ie6");</script><![endif]-->\n\t<!--[if IE 7]><script>location.replace("/errors/ie7");</script><![endif]-->\n\t<!--[if IE 8]><script>location.replace("/errors/ie8");</script><![endif]-->\n\t<!--[if IE 9]><script>location.replace("/errors/ie9");</script><![endif]-->\n\t\n\t\n\t\n\t<link href="https://s.ltrbxd.com/static/css/desktop.min.e1d8f367.css" rel="stylesheet" media="screen, projection"/>\n\n\t<script src="https://s.ltrbxd.com/static/js/main.min.a7e00d04.js"></script>\n\t\n\n\n\n\n\n\t<script>\n\t\tif ( $.cookie("letterboxd.admin.signed.in") === person.username ) {\n\t\t\tsuccessMessages.push("You are signed in as " + person.username);\n\t\t\t$(function(){$("#header, #content, body").css("background","#543");});\n\t\t}\n\t</script>\n\t\n</head>\n\n<body class="films-watched wide small-poster-grid" data-owner="mrafee113">\n\t\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<script>\nvar mainMenu = [];\n\n\t\n\tmainMenu.push({\n\t\t"id": 1,\n\t\t"url": "/sign-in/", \n\t\t"name": "Sign In",\n\t\t"cssClassCode": "sign-in-menu",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": true,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 2,\n\t\t"url": "/create-account/", \n\t\t"name": "Create Account",\n\t\t"cssClassCode": "create-account-menu",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 3,\n\t\t"url": "/", \n\t\t"name": "Home",\n\t\t"cssClassCode": "person-home",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 4,\n\t\t"url": "/activity/", \n\t\t"name": "Activity",\n\t\t"cssClassCode": "main-nav-activity",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "Activity",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 5,\n\t\t"url": "/films/", \n\t\t"name": "Films",\n\t\t"cssClassCode": "films-page main-nav-films",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 6,\n\t\t"url": "/lists/", \n\t\t"name": "Lists",\n\t\t"cssClassCode": "lists-page main-nav-lists",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 7,\n\t\t"url": "/members/", \n\t\t"name": "Members",\n\t\t"cssClassCode": "main-nav-people",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 8,\n\t\t"url": "/journal/", \n\t\t"name": "Journal",\n\t\t"cssClassCode": "main-nav-journal",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 9,\n\t\t"url": "/search/", \n\t\t"name": "Search results",\n\t\t"cssClassCode": "",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n</script>\n\n<header class="site-header js-hide-in-app" id="header" data-allow-user-to-add-all-films-to-a-list="true">\n\t<div class="site-header-bg"></div>\n\t<section>\n\t\t<h1 class="site-logo"><a href="/" class="logo replace">Letterboxd &mdash; Your life in film</a></h1>\n\n\t\t<div class="react-component" data-component-class="globals.comps.NavComponent"></div>\n\n\t\t\n\t\t\t\n\t\t\t\n\n\n\t\n\n\n\n\n\n<form method="post" action="#" id="signin" class="signin signin-form js-header-signin-form js-signin" data-url="/user/login.do" data-recaptcha-action="signin" novalidate=\'novalidate\' autocorrect=\'off\' autocapitalize=\'off\'>\n\t<input type="hidden" name="__csrf" value="placeholder" />\n\t<fieldset class="fieldset">\n\t\t<div class="fields">\n\t\t\t<div class="col">\n\t\t\t\t<label for="username">Username or Email</label>\n\t\t\t\t<input type="email" name="username" id="username" class="field signin-field" tabindex="1" data-focus-control="signingIn" autocomplete=\'email\' inputmode=\'email\' value="" />\n\t\t\t</div>\n\t\t\t<div class="col">\n\t\t\t\t<label for="password">Password</label>\n\t\t\t\t<input type="password" name="password" id="password" class="field signin-field" tabindex="2" autocomplete=\'current-password\' value="" />\n\t\t\t</div>\n\t\t\t<div class="signin-actions">\n\t\t\t\t<label for="remember" class="option-label -checkbox -small">\n\t\t\t\t\t<input type="checkbox" name="remember" id="remember" class="checkbox" tabindex="3" value="true" /><i class="substitute"></i>\n\t\t\t\t\t<span class="focus">Remember<span class="mob-hide"> me</span></span>\n\t\t\t\t</label>\n\t\t\t\t<p class="reset" tabindex="5"><a class="reset-password-link" href="/user/request-password-reset" target="_top">Forgotten<span class="elongated"> password</span>?</a></p>\n\t\t\t</div>\n\t\t\t<div class="col buttons">\n\t\t\t\t<div class="button-container"><input type="submit" value="Sign in" class="button -action button-green" tabindex="4" /><i></i></div>\n\t\t\t\t<div class="close js-close-signin">&times;</div>\n\t\t\t</div>\n\t\t</div>\n\t</fieldset>\n\t<div id="signin-message" class="errormessage"></div>\n</form>\n\n\n\t\t\n\t\t\n\t\t\n\t\t\t\n\t\t\t\n\n\n\n\t\t\n\t\t\n\t\t\n\t\t<form id="search" class="js-search-form search-form" action="/search/" method="get" autocorrect="off">\n\t\t\t<input autocomplete="false" name="hidden" type="text" style="display:none;" />\n\t\t\t<fieldset>\n\t\t\t\t<label for="search-q" class="hidden">Search:</label>\n\t\t\t\t<input type="text" name="q" id="search-q" class="field -borderless" data-lpignore=\'true\' inputmode=\'search\' value="" />\n\t\t\t\t<input type="submit" value="Search" class="action" />\n\t\t\t</fieldset>\n\t\t</form>\n\t\t\n\t</section>\n</header>\n\n\n\n\n\n\n<div id="content" class="site-body">\n\t\n\t<div class="content-wrap">\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<section id="profile-header" class="js-profile-header -is-mini-nav" data-person="mrafee113">\n\t\n\n\t<nav class="profile-navigation">\n\t\t\n\t\t\t<div class="profile-mini-person">\n\t\t\t\t<a class="avatar -a24" href="/mrafee113/" > <img src="https://a.ltrbxd.com/resized/avatar/upload/1/4/4/4/1/0/3/shard/avtr-0-48-0-48-crop.jpg?v=484d4bfb0a" alt="Mehdi Rafee" width="24" height="24" /> </a>\n\t\t\t\t<h1 class="title-3"><a href="/mrafee113/">Mehdi Rafee</a></h1>\n\t\t\t\t\n\t\t\t</div>\n\t\t\n\t\t\n\t\t\t<ul class="navlist">\n\t\t\t\t\n\n\t\t\t\t\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem hide-for-owner"><a class="navlink" href="/mrafee113/activity/">Activity</a></li>\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/activity/">Activity</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem -active"><a class="navlink" href="/mrafee113/films/">Films</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/films/diary/">Diary</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/films/reviews/">Reviews</a></li>\n\n\t\t\t\t<li class="navitem" data-owner="mrafee113"><a class="navlink" href="/mrafee113/watchlist/" >Watchlist</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/mrafee113/lists/">Lists</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/likes/">Likes</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/mrafee113/tags/">Tags</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/following/">Network</a></li>\n\n\t\t\t\t\n\n\t\t\t\t\n\n\t\t\t\t\n\n\n\n\t<li data-owner="mrafee113" class="navitem show-when-logged-in hide-for-owner"><a class="navlink" href="/pro/gift/mrafee113/">Gift Pro</a></li>\n\n\n\t\t\t\t<li class="navitem -rss">\n\t\t\t\t\t<a href="/mrafee113/rss/" class="has-icon icon-16 icon-rss tooltip" title="RSS feed">\n\t\t\t\t\t\t<span class="_sr-only">RSS feed for Mehdi</span>\n\t\t\t\t\t</a>\n\t\t\t\t</li>\n\t\t\t</ul>\n\t\t\n    </nav>\n</section>\n\n\n \n\n\n\n<div class="cols-2 overflow">\n\t<section class="section col-main overflow">\n\t\n \t\t\n\n<div id="content-nav" class="tabbed"> <section class="sub-nav-wrapper"><ul class="sub-nav"> <li class=" selected"><a href="/mrafee113/films/" class="tooltip" title="690&nbsp;films">Watched</a></li> <li class=""><a href="/mrafee113/films/diary/" class="tooltip" title="254&nbsp;films">Diary</a></li> <li class=""><a href="/mrafee113/films/reviews/" class="tooltip" title="45&nbsp;films">Reviews</a></li> </ul></section> <div class="sorting-selects has-hide-toggle"> <section class="grid-toggle-menu mob-hide"> <ul> <li class="selected"><a href="/mrafee113/films/" class="grid-toggle ir s grid-toggle-small" data-toggle="large">Small</a></li> <li><a href="/mrafee113/films/size/large/" class="grid-toggle ir s grid-toggle-large" data-toggle="small">Large</a></li> </ul> </section> <section class="smenu-wrapper hide-toggle-menu"> <div class="smenu"> <label><span class="ir s hide-toggle-icon">Visibility Filters</span><i class="ir s icon"></i></label> <ul class="smenu-menu" id="hide-toggle-menu"> <li class="divider-line-below"><a href="#" class="item js-film-filter-remover">Remove filters</a></li> <li class="js-account-filters"> <label class="option-label -toggle -small switch-control js-fade-toggle"> <span class="label">Fade watched films</span> <input class="checkbox" type="checkbox" checked="checked" role="switch" /><span class="state"><span class="track"><span class="handle"></span></span></span> </label> </li> <li class="js-account-filters"> <label class="option-label -toggle -small switch-control js-custom-poster-toggle" data-action="/ajax/poster-mode/"> <span class="label">Show custom posters</span> <input class="checkbox" type="checkbox" checked="checked" role="switch" /><span class="state"><span class="track"><span class="handle"></span></span></span> </label> </li> <li class="divider-line js-account-filters"> <span class="smenu-sublabel -uppercase">Custom posters</span> <div class="segmented-control -small custom-poster-control js-custom-poster-control" role="group" aria-label="Change custom poster visibility" data-action="/ajax/poster-mode/"> <div class="options"> <button type="button" class="option" data-js-trigger="option" data-value="All">Any</button> <button type="button" class="option" data-js-trigger="option" data-value="Theirs">Theirs</button> <button type="button" class="option" data-js-trigger="option" data-value="Yours">Yours</button> <button type="button" class="option" data-js-trigger="option" data-value="None">None</button> </div> </div> </li> <li class="divider-line js-account-filters"> <span class="smenu-sublabel -uppercase">Account Filters</span> <ul> <li class="js-film-filter" data-category="watched" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show watched films</a></li> <li class="js-film-filter" data-category="watched" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide watched films</a></li> <li class="js-film-filter divider-line -inset" data-category="liked" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show liked films</a></li> <li class="js-film-filter" data-category="liked" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide liked films</a></li> <li class="js-film-filter divider-line -inset" data-category="rated" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show rated films</a></li> <li class="js-film-filter" data-category="rated" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide rated films</a></li> <li class="js-film-filter divider-line -inset" data-category="logged" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show logged films</a></li> <li class="js-film-filter" data-category="logged" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide logged films</a></li> <li class="js-film-filter divider-line -inset" data-category="rewatched" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show rewatched films</a></li> <li class="js-film-filter" data-category="rewatched" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide rewatched films</a></li> <li class="js-film-filter divider-line -inset" data-category="reviewed" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show reviewed films</a></li> <li class="js-film-filter" data-category="reviewed" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide reviewed films</a></li> <li class="js-film-filter divider-line -inset" data-category="watchlisted" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films in watchlist</a></li> <li class="js-film-filter" data-category="watchlisted" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films in watchlist</a></li> <li class="js-film-filter divider-line -inset" data-category="owned" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films you own</a></li> <li class="js-film-filter" data-category="owned" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films you own</a></li> <li class="js-film-filter divider-line -inset" data-category="customised" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films you’ve customized</a></li> <li class="js-film-filter" data-category="customised" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films you’ve customized</a></li> </ul> </li> <li class="divider-line js-film-filters"> <span class="smenu-sublabel -uppercase">Content Filters</span> <ul> <li class="js-film-filter" data-category="shorts" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show short films</a></li> <li class="js-film-filter" data-category="shorts" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide short films</a></li> <li class="js-film-filter divider-line -inset" data-category="tv" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show TV shows</a></li> <li class="js-film-filter" data-category="tv" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide TV shows</a></li> <li class="js-film-filter divider-line -inset" data-category="docs" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide documentaries</a></li> <li class="js-film-filter divider-line -inset" data-category="unreleased" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide unreleased titles</a></li> <li class="js-film-filter divider-line -inset" data-category="obscure" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show obscure films</a></li> <li class="js-film-filter" data-category="obscure" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide obscure films</a></li> <li class="js-film-filter divider-line -inset" data-category="backdropped" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films with backdrop</a></li> <li class="js-film-filter" data-category="backdropped" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films with backdrop</a></li> <li class="js-film-filter divider-line -inset" data-category="nanocrowd" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show Nanocrowd films</a></li> <li class="js-film-filter" data-category="nanocrowd" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide Nanocrowd films</a></li> </ul> </li> </ul> </div> </section> <section class="smenu-wrapper"> <strong class="smenu-label">Sort by</strong> <div class="smenu"> <label>Release Date<i class="ir s icon"></i></label> <ul class="smenu-menu"> <li class=""><a class="item" href="/mrafee113/films/by/name/">Film Name</a></li> <li class=""><a class="item" href="/mrafee113/films/by/popular/">Film Popularity</a></li> <li class=""><a class="item" href="/mrafee113/films/by/shuffle/">Shuffle</a></li> <li class=""><span class="smenu-sublabel">When Added</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/date/">Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/date-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">When Rated</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/rated-date/">Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/rated-date-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Release Date</span> <ul> <li class=" smenu-subselected"><a class="item" href="/mrafee113/films/"><i class="ir s icon"></i>Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/release-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Average Rating</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/rating/">Highest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/rating-lowest/">Lowest First</a></li> </ul></li> <li class="" data-owner="mrafee113"><span class="smenu-sublabel" data-owner="mrafee113" data-owner-label="Your Rating">Mehdi’s Rating</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/entry-rating/">Highest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/entry-rating-lowest/">Lowest First</a></li> </ul></li> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><span class="smenu-sublabel">Your Rating</span> <ul> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><a class="item" href="/mrafee113/films/by/your-rating/">Highest First</a></li> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><a class="item" href="/mrafee113/films/by/your-rating-lowest/">Lowest First</a></li> </ul></li> <li class=" show-when-logged-in"><span class="smenu-sublabel">Your Interests</span> <ul> <li class=" show-when-logged-in"><a class="item" href="/mrafee113/films/by/your-interest-liked/">Based on films you liked</a></li> <li class=" show-when-logged-in"><a class="item" href="/mrafee113/films/by/your-interest-related/">Related to films you liked</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Film Length</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/shortest/">Shortest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/longest/">Longest First</a></li> </ul></li> </ul> </div> </section> \n<section class="smenu-wrapper"> <div class="smenu"> <label>Service<i class="ir s icon"></i></label> <ul id="services-menu" class="smenu-menu" data-upgrade-url="/pro/"> <li class="availability- smenu-subselected"> <span class="selected"> All films </span> </li> <li class="divider-line availability-amazon"> <a class="item" href="/mrafee113/films/on/amazon-deu/"> Amazon DE </a> </li> <li class="availability-amazon-video"> <a class="item" href="/mrafee113/films/on/amazon-video-de/"> Amazon Video DE </a> </li> <li class="availability-apple-tv-plus"> <a class="item" href="/mrafee113/films/on/apple-tv-plus-de/"> Apple TV Plus DE </a> </li> <li class="availability-apple-itunes"> <a class="item" href="/mrafee113/films/on/apple-itunes-de/"> iTunes DE </a> </li> <li class="note divider-line -upgrade"> <p>Upgrade to a <a href="/pro/">Letterboxd <span class="badge -pro -small">Pro</span></a> account to add your favorite services to this list—including any service and country pair listed on JustWatch—and to enable one-click filtering by all your favorites.</p></li> <li><a class="item item-small" href="https://www.justwatch.com" target="_blank" rel="noopener noreferrer"><small>Powered by JustWatch</small></a></li> </ul> </div> </section>\n <section class="smenu-wrapper"> <div class="smenu"> <label> Genre<i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><span class="selected">Any genre</span></li> <li class="divider-line"> <ul> <li class=""><a class="item" href="/mrafee113/films/genre/action/"><i class="ir s icon"></i>Action</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/adventure/"><i class="ir s icon"></i>Adventure</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/animation/"><i class="ir s icon"></i>Animation</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/comedy/"><i class="ir s icon"></i>Comedy</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/crime/"><i class="ir s icon"></i>Crime</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/documentary/"><i class="ir s icon"></i>Documentary</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/drama/"><i class="ir s icon"></i>Drama</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/family/"><i class="ir s icon"></i>Family</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/fantasy/"><i class="ir s icon"></i>Fantasy</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/history/"><i class="ir s icon"></i>History</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/horror/"><i class="ir s icon"></i>Horror</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/music/"><i class="ir s icon"></i>Music</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/mystery/"><i class="ir s icon"></i>Mystery</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/romance/"><i class="ir s icon"></i>Romance</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/science-fiction/"><i class="ir s icon"></i>Science Fiction</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/thriller/"><i class="ir s icon"></i>Thriller</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/tv-movie/"><i class="ir s icon"></i>TV Movie</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/war/"><i class="ir s icon"></i>War</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/western/"><i class="ir s icon"></i>Western</a></li> </ul> </li> </ul> </div> </section> <section class="smenu-wrapper"> <div class="smenu"> <label class="x"> Decade<i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><span class="selected">Any decade</span></li> <li class="divider-line "><a class="item" href="/mrafee113/films/decade/2020s/">2020s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/2010s/">2010s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/2000s/">2000s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1990s/">1990s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1980s/">1980s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1970s/">1970s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1960s/">1960s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1950s/">1950s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1940s/">1940s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1930s/">1930s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1920s/">1920s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1910s/">1910s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1900s/">1900s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1890s/">1890s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1880s/">1880s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1870s/">1870s</a></li> </ul> </div> </section> <section class="smenu-wrapper"> <div class="smenu"> <label> Rating <i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><a class="item" href="/mrafee113/films/">Any rating</a></li> <li><a class="item" href="/mrafee113/films/rated/none/">No rating</a></li> <li class="divider-line"> <span class="smenu-sublabel -uppercase">Rating (or range)</span> <div class="menu-rating-filter js-rating-filter" data-rateit-starwidth="10" data-rateit-starheight="19" data-action="/mrafee113/films/rated/%7B%7Bvalue%7D%7D/"> <div class="rateit-range"> <div class="rateit-selected"></div> <div class="rateit-hover"></div> </div> </div> <small class="note">Drag to define range</small> </li> </ul> </div> </section> </div> <div class="clear"></div> </div>\n\t\n\t\t\n\n\t\n\t\t\n\t\t\t\t\n\n\t\t\t\t<ul class="poster-list -p70 -grid film-list clear">\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-726680 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="726680" data-film-slug="/film/mafia-mamma/" data-poster-url="/film/mafia-mamma/image-150/" data-linked="linked" data-target-link="/film/mafia-mamma/" data-target-link-target="" data-cache-busting-key="20289f53" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Mafia Mamma"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-998520 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="998520" data-film-slug="/film/louis-ck-at-the-dolby/" data-poster-url="/film/louis-ck-at-the-dolby/image-150/" data-linked="linked" data-target-link="/film/louis-ck-at-the-dolby/" data-target-link-target="" data-cache-busting-key="93b11804" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Louis C.K. at The Dolby"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-6">★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-575258 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="575258" data-film-slug="/film/renfield/" data-poster-url="/film/renfield/image-150/" data-linked="linked" data-target-link="/film/renfield/" data-target-link-target="" data-cache-busting-key="d129ad49" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Renfield"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-522405 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="522405" data-film-slug="/film/shazam-fury-of-the-gods/" data-poster-url="/film/shazam-fury-of-the-gods/image-150/" data-linked="linked" data-target-link="/film/shazam-fury-of-the-gods/" data-target-link-target="" data-cache-busting-key="1e7571ce" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Shazam! Fury of the Gods"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-424003 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="424003" data-film-slug="/film/dungeons-dragons-honor-among-thieves/" data-poster-url="/film/dungeons-dragons-honor-among-thieves/image-150/" data-linked="linked" data-target-link="/film/dungeons-dragons-honor-among-thieves/" data-target-link-target="" data-cache-busting-key="5c7797c4" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Dungeons & Dragons: Honor Among Thieves"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-838520 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="838520" data-film-slug="/film/champions-2023/" data-poster-url="/film/champions-2023/image-150/" data-linked="linked" data-target-link="/film/champions-2023/" data-target-link-target="" data-cache-busting-key="d119d8a2" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Champions"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-764596 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="764596" data-film-slug="/film/kill-boksoon/" data-poster-url="/film/kill-boksoon/image-150/" data-linked="linked" data-target-link="/film/kill-boksoon/" data-target-link-target="" data-cache-busting-key="280be804" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Kill Boksoon"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-566237 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="566237" data-film-slug="/film/ant-man-and-the-wasp-quantumania/" data-poster-url="/film/ant-man-and-the-wasp-quantumania/image-150/" data-linked="linked" data-target-link="/film/ant-man-and-the-wasp-quantumania/" data-target-link-target="" data-cache-busting-key="df5c617e" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ant-Man and the Wasp: Quantumania"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-558056 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="558056" data-film-slug="/film/knock-at-the-cabin/" data-poster-url="/film/knock-at-the-cabin/image-150/" data-linked="linked" data-target-link="/film/knock-at-the-cabin/" data-target-link-target="" data-cache-busting-key="2e6ced50" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Knock at the Cabin"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-733385 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="733385" data-film-slug="/film/mummies-2023/" data-poster-url="/film/mummies-2023/image-150/" data-linked="linked" data-target-link="/film/mummies-2023/" data-target-link-target="" data-cache-busting-key="fb56ca62" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Mummies"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-661153 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="661153" data-film-slug="/film/operation-fortune-ruse-de-guerre/" data-poster-url="/film/operation-fortune-ruse-de-guerre/image-150/" data-linked="linked" data-target-link="/film/operation-fortune-ruse-de-guerre/" data-target-link-target="" data-cache-busting-key="8d72bd57" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Operation Fortune: Ruse de Guerre"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-242285 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="242285" data-film-slug="/film/puss-in-boots-the-last-wish/" data-poster-url="/film/puss-in-boots-the-last-wish/image-150/" data-linked="linked" data-target-link="/film/puss-in-boots-the-last-wish/" data-target-link-target="" data-cache-busting-key="d60f4abc" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Puss in Boots: The Last Wish"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-789082 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="789082" data-film-slug="/film/strange-world-2022/" data-poster-url="/film/strange-world-2022/image-150/" data-linked="linked" data-target-link="/film/strange-world-2022/" data-target-link-target="" data-cache-busting-key="8df8311d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Strange World"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-744826 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="744826" data-film-slug="/film/enola-holmes-2/" data-poster-url="/film/enola-holmes-2/image-150/" data-linked="linked" data-target-link="/film/enola-holmes-2/" data-target-link-target="" data-cache-busting-key="0b05f98f" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Enola Holmes 2"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-435460 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="435460" data-film-slug="/film/black-panther-wakanda-forever/" data-poster-url="/film/black-panther-wakanda-forever/image-150/" data-linked="linked" data-target-link="/film/black-panther-wakanda-forever/" data-target-link-target="" data-cache-busting-key="87412ddf" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Black Panther: Wakanda Forever"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-589317 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="589317" data-film-slug="/film/amsterdam-2022/" data-poster-url="/film/amsterdam-2022/image-150/" data-linked="linked" data-target-link="/film/amsterdam-2022/" data-target-link-target="" data-cache-busting-key="85997eb0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Amsterdam"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-647390 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="647390" data-film-slug="/film/confess-fletch/" data-poster-url="/film/confess-fletch/image-150/" data-linked="linked" data-target-link="/film/confess-fletch/" data-target-link-target="" data-cache-busting-key="88144a94" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Confess, Fletch"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-441474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="441474" data-film-slug="/film/wendell-wild/" data-poster-url="/film/wendell-wild/image-150/" data-linked="linked" data-target-link="/film/wendell-wild/" data-target-link-target="" data-cache-busting-key="8e24544c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Wendell & Wild"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-523109 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="523109" data-film-slug="/film/causeway/" data-poster-url="/film/causeway/image-150/" data-linked="linked" data-target-link="/film/causeway/" data-target-link-target="" data-cache-busting-key="870478ea" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Causeway"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-721288 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="721288" data-film-slug="/film/the-fabelmans/" data-poster-url="/film/the-fabelmans/image-150/" data-linked="linked" data-target-link="/film/the-fabelmans/" data-target-link-target="" data-cache-busting-key="0dba11a7" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Fabelmans"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-521323 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="521323" data-film-slug="/film/the-menu-2022/" data-poster-url="/film/the-menu-2022/image-150/" data-linked="linked" data-target-link="/film/the-menu-2022/" data-target-link-target="" data-cache-busting-key="8e7be729" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Menu"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-9">★★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-586723 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="586723" data-film-slug="/film/glass-onion/" data-poster-url="/film/glass-onion/image-150/" data-linked="linked" data-target-link="/film/glass-onion/" data-target-link-target="" data-cache-busting-key="304e3660" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Glass Onion"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-820461 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="820461" data-film-slug="/film/the-lost-king/" data-poster-url="/film/the-lost-king/image-150/" data-linked="linked" data-target-link="/film/the-lost-king/" data-target-link-target="" data-cache-busting-key="864fbd75" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Lost King"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-686510 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="686510" data-film-slug="/film/see-how-they-run-2022/" data-poster-url="/film/see-how-they-run-2022/image-150/" data-linked="linked" data-target-link="/film/see-how-they-run-2022/" data-target-link-target="" data-cache-busting-key="8a569c44" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="See How They Run"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-462030 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="462030" data-film-slug="/film/pinocchio-2022/" data-poster-url="/film/pinocchio-2022/image-150/" data-linked="linked" data-target-link="/film/pinocchio-2022/" data-target-link-target="" data-cache-busting-key="beb0d10e" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Pinocchio"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-598882 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="598882" data-film-slug="/film/the-banshees-of-inisherin/" data-poster-url="/film/the-banshees-of-inisherin/image-150/" data-linked="linked" data-target-link="/film/the-banshees-of-inisherin/" data-target-link-target="" data-cache-busting-key="03be9e08" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Banshees of Inisherin"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-734096 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="734096" data-film-slug="/film/tar-2022/" data-poster-url="/film/tar-2022/image-150/" data-linked="linked" data-target-link="/film/tar-2022/" data-target-link-target="" data-cache-busting-key="8caea6a3" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="TÁR"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-666269 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="666269" data-film-slug="/film/white-noise-2022/" data-poster-url="/film/white-noise-2022/image-150/" data-linked="linked" data-target-link="/film/white-noise-2022/" data-target-link-target="" data-cache-busting-key="093db78d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="White Noise"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-676215 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="676215" data-film-slug="/film/day-shift-2022/" data-poster-url="/film/day-shift-2022/image-150/" data-linked="linked" data-target-link="/film/day-shift-2022/" data-target-link-target="" data-cache-busting-key="8097de58" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Day Shift"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-811153 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="811153" data-film-slug="/film/one-piece-film-red/" data-poster-url="/film/one-piece-film-red/image-150/" data-linked="linked" data-target-link="/film/one-piece-film-red/" data-target-link-target="" data-cache-busting-key="093156e5" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="One Piece Film Red"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-647760 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="647760" data-film-slug="/film/the-gray-man-2022/" data-poster-url="/film/the-gray-man-2022/image-150/" data-linked="linked" data-target-link="/film/the-gray-man-2022/" data-target-link-target="" data-cache-busting-key="81ba2f7b" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Gray Man"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-641961 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="641961" data-film-slug="/film/bullet-train/" data-poster-url="/film/bullet-train/image-150/" data-linked="linked" data-target-link="/film/bullet-train/" data-target-link-target="" data-cache-busting-key="0a859e26" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Bullet Train"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-7">★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-371005 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="371005" data-film-slug="/film/minions-the-rise-of-gru/" data-poster-url="/film/minions-the-rise-of-gru/image-150/" data-linked="linked" data-target-link="/film/minions-the-rise-of-gru/" data-target-link-target="" data-cache-busting-key="8a9ee32a" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Minions: The Rise of Gru"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-592465 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="592465" data-film-slug="/film/the-man-from-toronto-2022/" data-poster-url="/film/the-man-from-toronto-2022/image-150/" data-linked="linked" data-target-link="/film/the-man-from-toronto-2022/" data-target-link-target="" data-cache-busting-key="0477e5e9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Man from Toronto"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-543002 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="543002" data-film-slug="/film/thor-love-and-thunder/" data-poster-url="/film/thor-love-and-thunder/image-150/" data-linked="linked" data-target-link="/film/thor-love-and-thunder/" data-target-link-target="" data-cache-busting-key="84638312" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Thor: Love and Thunder"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-878873 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="878873" data-film-slug="/film/vesper-2022/" data-poster-url="/film/vesper-2022/image-150/" data-linked="linked" data-target-link="/film/vesper-2022/" data-target-link-target="" data-cache-busting-key="0317ad27" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Vesper"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-488592 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="488592" data-film-slug="/film/the-sea-beast-2022/" data-poster-url="/film/the-sea-beast-2022/image-150/" data-linked="linked" data-target-link="/film/the-sea-beast-2022/" data-target-link-target="" data-cache-busting-key="8dce9a04" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Sea Beast"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-607401 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="607401" data-film-slug="/film/vengeance-2022/" data-poster-url="/film/vengeance-2022/image-150/" data-linked="linked" data-target-link="/film/vengeance-2022/" data-target-link-target="" data-cache-busting-key="04dc3f16" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Vengeance"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-641574 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="641574" data-film-slug="/film/lightyear-2022/" data-poster-url="/film/lightyear-2022/image-150/" data-linked="linked" data-target-link="/film/lightyear-2022/" data-target-link-target="" data-cache-busting-key="0d45b6f6" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Lightyear"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-812015 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="812015" data-film-slug="/film/close-2022/" data-poster-url="/film/close-2022/image-150/" data-linked="linked" data-target-link="/film/close-2022/" data-target-link-target="" data-cache-busting-key="8ac6ce80" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Close"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-8">★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-875860 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="875860" data-film-slug="/film/ricky-gervais-supernature/" data-poster-url="/film/ricky-gervais-supernature/image-150/" data-linked="linked" data-target-link="/film/ricky-gervais-supernature/" data-target-link-target="" data-cache-busting-key="8c13daef" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ricky Gervais: SuperNature"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-736318 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="736318" data-film-slug="/film/crimes-of-the-future-2022/" data-poster-url="/film/crimes-of-the-future-2022/image-150/" data-linked="linked" data-target-link="/film/crimes-of-the-future-2022/" data-target-link-target="" data-cache-busting-key="8331ef2f" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Crimes of the Future"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-427970 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="427970" data-film-slug="/film/triangle-of-sadness/" data-poster-url="/film/triangle-of-sadness/image-150/" data-linked="linked" data-target-link="/film/triangle-of-sadness/" data-target-link-target="" data-cache-busting-key="8e1eb744" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Triangle of Sadness"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-669198 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="669198" data-film-slug="/film/one-fine-morning-2022/" data-poster-url="/film/one-fine-morning-2022/image-150/" data-linked="linked" data-target-link="/film/one-fine-morning-2022/" data-target-link-target="" data-cache-busting-key="0280d483" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="One Fine Morning"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-485265 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="485265" data-film-slug="/film/three-thousand-years-of-longing/" data-poster-url="/film/three-thousand-years-of-longing/image-150/" data-linked="linked" data-target-link="/film/three-thousand-years-of-longing/" data-target-link-target="" data-cache-busting-key="0c21e1b7" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Three Thousand Years of Longing"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-385511 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="385511" data-film-slug="/film/doctor-strange-in-the-multiverse-of-madness/" data-poster-url="/film/doctor-strange-in-the-multiverse-of-madness/image-150/" data-linked="linked" data-target-link="/film/doctor-strange-in-the-multiverse-of-madness/" data-target-link-target="" data-cache-busting-key="81a4fea9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Doctor Strange in the Multiverse of Madness"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-565852 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="565852" data-film-slug="/film/the-northman/" data-poster-url="/film/the-northman/image-150/" data-linked="linked" data-target-link="/film/the-northman/" data-target-link-target="" data-cache-busting-key="08820bd4" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Northman"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-456327 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="456327" data-film-slug="/film/morbius/" data-poster-url="/film/morbius/image-150/" data-linked="linked" data-target-link="/film/morbius/" data-target-link-target="" data-cache-busting-key="084000b9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Morbius"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-683285 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="683285" data-film-slug="/film/ambulance-2022/" data-poster-url="/film/ambulance-2022/image-150/" data-linked="linked" data-target-link="/film/ambulance-2022/" data-target-link-target="" data-cache-busting-key="02c94c2c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ambulance"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-574385 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="574385" data-film-slug="/film/the-unbearable-weight-of-massive-talent/" data-poster-url="/film/the-unbearable-weight-of-massive-talent/image-150/" data-linked="linked" data-target-link="/film/the-unbearable-weight-of-massive-talent/" data-target-link-target="" data-cache-busting-key="8992593c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Unbearable Weight of Massive Talent"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-673474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="673474" data-film-slug="/film/the-lost-city-2022/" data-poster-url="/film/the-lost-city-2022/image-150/" data-linked="linked" data-target-link="/film/the-lost-city-2022/" data-target-link-target="" data-cache-busting-key="87db30cd" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Lost City"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-474474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="474474" data-film-slug="/film/everything-everywhere-all-at-once/" data-poster-url="/film/everything-everywhere-all-at-once/image-150/" data-linked="linked" data-target-link="/film/everything-everywhere-all-at-once/" data-target-link-target="" data-cache-busting-key="80fbb370" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Everything Everywhere All at Once"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-438727 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="438727" data-film-slug="/film/turning-red/" data-poster-url="/film/turning-red/image-150/" data-linked="linked" data-target-link="/film/turning-red/" data-target-link-target="" data-cache-busting-key="0d037915" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Turning Red"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-620665 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="620665" data-film-slug="/film/the-adam-project/" data-poster-url="/film/the-adam-project/image-150/" data-linked="linked" data-target-link="/film/the-adam-project/" data-target-link-target="" data-cache-busting-key="8f04f942" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Adam Project"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-348914 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="348914" data-film-slug="/film/the-batman/" data-poster-url="/film/the-batman/image-150/" data-linked="linked" data-target-link="/film/the-batman/" data-target-link-target="" data-cache-busting-key="0438ab74" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Batman"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-264328 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="264328" data-film-slug="/film/uncharted-2022/" data-poster-url="/film/uncharted-2022/image-150/" data-linked="linked" data-target-link="/film/uncharted-2022/" data-target-link-target="" data-cache-busting-key="8c645cbf" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Uncharted"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-434913 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="434913" data-film-slug="/film/death-on-the-nile-2022/" data-poster-url="/film/death-on-the-nile-2022/image-150/" data-linked="linked" data-target-link="/film/death-on-the-nile-2022/" data-target-link-target="" data-cache-busting-key="8228a9e0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Death on the Nile"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-777185 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="777185" data-film-slug="/film/emily-the-criminal/" data-poster-url="/film/emily-the-criminal/image-150/" data-linked="linked" data-target-link="/film/emily-the-criminal/" data-target-link-target="" data-cache-busting-key="03df984d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Emily the Criminal"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-680635 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="680635" data-film-slug="/film/living-2022/" data-poster-url="/film/living-2022/image-150/" data-linked="linked" data-target-link="/film/living-2022/" data-target-link-target="" data-cache-busting-key="8db883ac" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Living"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-719315 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="719315" data-film-slug="/film/breaking-2022/" data-poster-url="/film/breaking-2022/image-150/" data-linked="linked" data-target-link="/film/breaking-2022/" data-target-link-target="" data-cache-busting-key="829c2ff0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Breaking"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-735545 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="735545" data-film-slug="/film/emergency-2022/" data-poster-url="/film/emergency-2022/image-150/" data-linked="linked" data-target-link="/film/emergency-2022/" data-target-link-target="" data-cache-busting-key="0a2a26ab" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Emergency"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-823432 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="823432" data-film-slug="/film/louis-ck-sorry-2021/" data-poster-url="/film/louis-ck-sorry-2021/image-150/" data-linked="linked" data-target-link="/film/louis-ck-sorry-2021/" data-target-link-target="" data-cache-busting-key="04941a73" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Louis C.K.: Sorry"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-6">★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-551275 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="551275" data-film-slug="/film/the-matrix-resurrections/" data-poster-url="/film/the-matrix-resurrections/image-150/" data-linked="linked" data-target-link="/film/the-matrix-resurrections/" data-target-link-target="" data-cache-busting-key="0d576ce2" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Matrix Resurrections"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-572255 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="572255" data-film-slug="/film/dont-look-up-2021/" data-poster-url="/film/dont-look-up-2021/image-150/" data-linked="linked" data-target-link="/film/dont-look-up-2021/" data-target-link-target="" data-cache-busting-key="8a7a1c92" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Don\'t Look Up"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-571629 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="571629" data-film-slug="/film/the-unforgivable/" data-poster-url="/film/the-unforgivable/image-150/" data-linked="linked" data-target-link="/film/the-unforgivable/" data-target-link-target="" data-cache-busting-key="8fd1eb25" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Unforgivable"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-9">★★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-466291 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="466291" data-film-slug="/film/tick-tick-boom-2021/" data-poster-url="/film/tick-tick-boom-2021/image-150/" data-linked="linked" data-target-link="/film/tick-tick-boom-2021/" data-target-link-target="" data-cache-busting-key="071f7a54" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="tick, tick...BOOM!"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-441858 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="441858" data-film-slug="/film/red-notice/" data-poster-url="/film/red-notice/image-150/" data-linked="linked" data-target-link="/film/red-notice/" data-target-link-target="" data-cache-busting-key="0ef37870" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Red Notice"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-714279 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="714279" data-film-slug="/film/army-of-thieves/" data-poster-url="/film/army-of-thieves/image-150/" data-linked="linked" data-target-link="/film/army-of-thieves/" data-target-link-target="" data-cache-busting-key="0deeede3" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Army of Thieves"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-454016 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="454016" data-film-slug="/film/eternals/" data-poster-url="/film/eternals/image-150/" data-linked="linked" data-target-link="/film/eternals/" data-target-link-target="" data-cache-busting-key="0a67ea1a" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Eternals"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-496592 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="496592" data-film-slug="/film/encanto/" data-poster-url="/film/encanto/image-150/" data-linked="linked" data-target-link="/film/encanto/" data-target-link-target="" data-cache-busting-key="8d86b9e5" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Encanto"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-544936 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="544936" data-film-slug="/film/the-harder-they-fall-2021/" data-poster-url="/film/the-harder-they-fall-2021/image-150/" data-linked="linked" data-target-link="/film/the-harder-they-fall-2021/" data-target-link-target="" data-cache-busting-key="863a9c16" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Harder They Fall"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-790798 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="790798" data-film-slug="/film/dave-chappelle-the-closer/" data-poster-url="/film/dave-chappelle-the-closer/image-150/" data-linked="linked" data-target-link="/film/dave-chappelle-the-closer/" data-target-link-target="" data-cache-busting-key="04f75162" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Dave Chappelle: The Closer"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t</ul>\n\t\t\t\t<div class="pagination"> <div class="paginate-nextprev paginate-disabled"><span class="previous">Newer</span></div> <div class="paginate-nextprev"><a class="next" href="/mrafee113/films/page/2/">Older</a></div> <div class="paginate-pages"> <ul> <li class="paginate-page paginate-current"><span>1</span></li> <li class="paginate-page"><a href="/mrafee113/films/page/2/">2</a></li> <li class="paginate-page"><a href="/mrafee113/films/page/3/">3</a></li> <li class="paginate-page unseen-pages">&hellip;</li> <li class="paginate-page"><a href="/mrafee113/films/page/10/">10</a></li> </ul> </div> </div>\n\t\t\t\n\t\t<div class="clear"></div>\n\t</section>\n\t\n\t<div class="clear"></div>\n\t\n</div>\n\n\n\n\n\n\n\n\n\n\n\t\t</div> \n\n\t\t\n\n\t</div> \n\n\n\n\t<footer id="page-footer" class="page-footer js-page-footer js-hide-in-app">\n\t\t<div class="content-wrap">\n\t\t\t\n\t\t\t\t<nav class="footer-nav js-footer-nav">\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li><a href="/about/">About</a></li>\n\t\t\t\t\t\t<li><a href="/journal/">News</a></li>\n\t\t\t\t\t\t<li class="js-hide-in-app"><a href="/pro/">Pro</a></li>\n\t\t\t\t\t\t<li><a href="/apps/">Apps</a></li>\n\t\t\t\t\t\t<li><a href="https://apple.co/3TfzHVG" target="_blank" rel="noopener noreferrer">Podcast</a></li>\n\t\t\t\t\t\t<li><a href="/year-in-review/">Year in Review</a></li>\n\t\t\t\t\t\t<li><a href="/gift-guide/">Gift Guide</a></li>\n\t\t\t\t\t\t<li><a href="/welcome/">Help</a></li>\n\t\t\t\t\t\t<li><a href="/legal/terms-of-use/">Terms</a></li>\n\t\t\t\t\t\t<li><a href="/api-beta/">API</a></li>\n\t\t\t\t\t\t<li><a href="/contact/">Contact</a></li>\n\t\t\t\t\t</ul>\n\t\t\t\t</nav>\n\t\n\n\t\t\t<div class="socials">\n\t\t\t\t<nav class="social-service-list -inline">\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://twitter.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Twitter">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="20" height="16" xmlns="http://www.w3.org/2000/svg"><path d="M17.96 4.51V4c.8-.56 1.49-1.28 2.04-2.1-.74.33-1.53.54-2.36.65.85-.5 1.5-1.3 1.8-2.24-.78.46-1.66.8-2.6.98a4.13 4.13 0 0 0-7.1 2.76c0 .31.04.62.1.92A11.72 11.72 0 0 1 1.38.74a3.99 3.99 0 0 0 1.28 5.4A4.2 4.2 0 0 1 .8 5.62v.06c0 1.95 1.42 3.59 3.29 3.96a4.06 4.06 0 0 1-1.85.07 4.1 4.1 0 0 0 3.83 2.8A8.32 8.32 0 0 1 0 14.2C1.8 15.33 3.97 16 6.28 16A11.5 11.5 0 0 0 17.96 4.51Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Twitter</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.facebook.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Facebook">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="19" height="19" xmlns="http://www.w3.org/2000/svg"><path d="M9.5 0a9.5 9.5 0 0 0-1.48 18.89V12H5.6V9.25h2.42V7.41c0-2.38 1.41-3.7 3.58-3.7 1.04 0 2.13.19 2.13.19v2.33h-1.2c-1.18 0-1.54.74-1.54 1.49v1.53h2.63L13.2 12h-2.21v6.89A9.5 9.5 0 0 0 9.5 0Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Facebook</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.instagram.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Instagram">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="20" height="20" xmlns="http://www.w3.org/2000/svg"><path d="M14.12.06c1.07.05 1.8.22 2.43.46.66.26 1.21.6 1.77 1.16.56.55.9 1.11 1.15 1.77.25.63.42 1.36.47 2.43.04.94.06 1.32.06 3.3v1.37c0 1.54 0 2.19-.03 2.77v.22l-.03.58a7.34 7.34 0 0 1-.47 2.43 4.9 4.9 0 0 1-1.15 1.77 4.9 4.9 0 0 1-1.77 1.16c-.64.24-1.36.41-2.43.46l-.61.03h-.23c-.5.02-1.06.03-2.21.03H9.2c-2 0-2.37-.02-3.32-.06a7.34 7.34 0 0 1-2.43-.46 4.9 4.9 0 0 1-1.77-1.16 4.9 4.9 0 0 1-1.16-1.77 7.34 7.34 0 0 1-.46-2.43l-.03-.61v-.2A60.9 60.9 0 0 1 0 11.5V8.75C0 7.7.01 7.17.03 6.7v-.2l.03-.61C.1 4.8.28 4.08.52 3.45a4.9 4.9 0 0 1 1.16-1.77A4.9 4.9 0 0 1 3.45.52 7.34 7.34 0 0 1 5.88.06l.61-.03h.2C7.12 0 7.6 0 8.5 0h2.74c1.62 0 2 .02 2.88.06ZM11.02 2H8.97c-1.7 0-2.05.02-2.92.06a5.4 5.4 0 0 0-1.82.33c-.45.18-.78.39-1.12.73-.34.34-.55.67-.73 1.12-.13.35-.3.86-.33 1.82C2.02 6.93 2 7.29 2 8.98v2.04c0 1.7.02 2.05.06 2.92.04.95.2 1.47.33 1.81.18.46.39.78.73 1.13.34.34.67.55 1.12.73.35.13.86.29 1.82.33.83.04 1.2.05 2.7.06h2.47c1.51 0 1.87-.02 2.71-.06a5.4 5.4 0 0 0 1.81-.33c.46-.18.78-.4 1.12-.73.35-.35.56-.67.73-1.13.14-.34.3-.86.34-1.8a49 49 0 0 0 .06-2.72V8.77a49 49 0 0 0-.06-2.71 5.4 5.4 0 0 0-.34-1.82 3.02 3.02 0 0 0-.73-1.12 3.02 3.02 0 0 0-1.12-.73 5.4 5.4 0 0 0-1.81-.33c-.88-.04-1.23-.06-2.93-.06ZM10 4.86a5.14 5.14 0 1 1 0 10.28 5.14 5.14 0 0 1 0-10.28ZM10 7a3 3 0 1 0 0 6 3 3 0 0 0 0-6Zm5.25-3.5a1.25 1.25 0 1 1 0 2.5 1.25 1.25 0 0 1 0-2.5Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Instagram</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.tiktok.com/@letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on TikTok">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="17" height="18" xmlns="http://www.w3.org/2000/svg"><path d="M16.48 4.32a4.62 4.62 0 0 1-3.92-2.66A4.04 4.04 0 0 1 12.23 0H9.07v11.85c0 1.93-1.19 3.07-2.65 3.07a2.71 2.71 0 0 1-2.04-.9 2.57 2.57 0 0 1-.6-2.1 2.55 2.55 0 0 1 1.26-1.81 2.7 2.7 0 0 1 2.24-.21V6.77a5.92 5.92 0 0 0-4.08.86 5.7 5.7 0 0 0-2.15 2.55 5.53 5.53 0 0 0 1.26 6.16 5.86 5.86 0 0 0 6.33 1.23 5.78 5.78 0 0 0 2.6-2.08c.64-.94.98-2.03.98-3.15V5.96a7.74 7.74 0 0 0 4.25 1.25V4.32Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">TikTok</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.youtube.com/letterboxdhq" target="_blank" rel="noopener noreferrer" title="Letterboxd on YouTube">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="23" height="16" xmlns="http://www.w3.org/2000/svg"><path d="M11.74 0c.61 0 2.33.02 4.11.08l.54.02c1.7.06 3.35.18 4.1.38a2.87 2.87 0 0 1 2.03 2.02c.45 1.67.48 5.04.48 5.46v.08c0 .42-.03 3.8-.48 5.46a2.87 2.87 0 0 1-2.03 2.02c-.75.2-2.4.32-4.1.38l-.54.02c-1.78.07-3.5.08-4.11.08H11.26c-.62 0-2.33-.01-4.11-.08l-.54-.02c-1.7-.06-3.36-.18-4.1-.38A2.87 2.87 0 0 1 .48 13.5C.04 11.9 0 8.68 0 8.1v-.2c0-.58.04-3.79.48-5.4A2.87 2.87 0 0 1 2.5.48c.74-.2 2.4-.32 4.1-.38l.54-.02C8.93.02 10.65 0 11.26 0ZM9 4.57v6.86L15 8 9 4.57Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">YouTube</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\t\t\t\t</nav>\n\t\t\t</div>\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t<p class="copyright">\n\t\t\t\t&copy; Letterboxd Limited. Made by <a href="/crew/" class="mute">fans</a> in Aotearoa New Zealand.\n\t\t\t\t<span class="nobr"><a href="https://letterboxd.com/about/film-data/" class="mute">Film data</a> from <a href="https://www.themoviedb.org" class="mute">TMDb</a>. \n\t\t\t\t\n\t\t\t\t\t\t<a href="#" class="mute mobile-site-switch" data-use-mobile-site="yes">Mobile&nbsp;site</a>.\n\t\t\t\t\t\n\t</span>\n\t\t\t\t<span class="recap" style="display:none"><br/>This site is protected by reCAPTCHA and the Google <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer" class="mute">privacy policy</a> and <a href="https://policies.google.com/terms" target="_blank" rel="noopener noreferrer" class="mute">terms of service</a>&nbsp;apply.</span>\n\t\t\t</p>\n\t\t</div>\n\t</footer>\n\n\t<div id="remove-ads-modal" class="modal-neue fade" tabindex="-1" aria-labelledby="remove-ads-modal-title" aria-hidden="true">\n    <div class="modal-dialog -sm modal-dialog-centered">\n        <div class="modal-content">\n            <div class="modal-header">\n                <h5 class="modal-title" id="remove-ads-modal-title">Upgrade to remove&nbsp;ads</h5>\n                <button type="button" class="close" data-bs-dismiss="modal-neue" aria-label="Close">\n                    <svg class="glyph" width="16" height="16" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd" stroke-linecap="round" stroke="#000" stroke-width="2"><path d="m1 1 14 14M1 15 15 1"/></g></svg>\n                </button>\n            </div>\n            <div class="modal-body">\n                <div class="body-text -hero">\n                    <p>Letterboxd is an independent service created by a small team, and we rely mostly on the support of our members to maintain our site and apps. Please consider upgrading to a <a href="/pro/">Pro account</a>—for less than a couple bucks a month, you’ll get cool additional features like all-time and annual stats pages (<a href="https://letterboxd.com/jack/stats/">example</a>), the ability to select (and filter by) your favorite streaming services, and no ads!</p>\n                </div>\n            </div>\n            <div class="modal-footer">\n                <a href="/pro/" class="button -action button-action">Learn more about Pro</a>\n            </div>\n        </div>\n    </div>\n</div>\n\t\n\n\n\n\n\n\n<form id="poster-picker-modal" class="modal-neue fade poster-picker-modal" method="post" action="" novalidate="novalidate" tabindex="-1" role="dialog" aria-labelledby="poster-picker-modal-title" aria-hidden="true" data-bs-backdrop="static">\n    <div class="modal-dialog -lg modal-dialog-centered modal-dialog-scrollable">\n        <div class="modal-content">\n            <div class="modal-header">\n                <h5 class="modal-title" id="poster-picker-modal-title">Select your preferred poster</h5>\n                <button type="button" class="close" data-bs-dismiss="modal-neue" aria-label="Close">\n                    <svg class="glyph" width="16" height="16" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd" stroke-linecap="round" stroke="#000" stroke-width="2"><path d="m1 1 14 14M1 15 15 1"></path></g></svg>\n                </button>\n            </div>\n            <div class="modal-body">\n                <div id="poster-picker-b427140c-d820-493e-a8cf-bb50fce997b3" data-poster-picker-options=\'{"id": "b427140c-d820-493e-a8cf-bb50fce997b3"}\' data-js-target="poster-picker"></div>\n            </div>\n            <div class="modal-footer">\n                <div class="poster-picker-note">\n                    <div class="body-text -small">\n                        \n<p>Posters are sourced from <a href="https://www.themoviedb.org" target="_blank">TMDb</a> and <a href="https://posteritati.com" target="_blank">Posteritati</a>, and appear for you and visitors to your profile and content, depending on settings. <a href="https://letterboxd.com/journal/posterity-custom-posters/" target="_blank">Learn more.</a></p>\n\n                    </div>\n                </div>\n\n                <div class="poster-picker-controls" data-poster-picker-controls-for="b427140c-d820-493e-a8cf-bb50fce997b3">\n                    <div class="modal-action-group -center">\n                        <button class="button -destructive" type="button" data-js-trigger="reset" disabled><span class="label">Reset poster</span></button>\n                        <button class="button -action" type="submit" data-js-trigger="submit" disabled><span class="label">Save<span class="mob-hide"> changes</span></span></button>\n                    </div>\n                    \n                </div>\n            </div>\n        </div>\n    </div>\n</form>\n\t\n\t\n</body>\n</html>'

In [13]: doc = html.document_fromstring(inner_html)

In [14]: movies_xpath = '/body/div[@id="content"]/div[@class="content-wrap"]/div
    ...: [1]/section[1]/ul[1]/li'

In [15]: movie_elements = doc.xpath(movies_xpath)

In [16]: len(movie_elements)
Out[16]: 0

In [17]: movie_elements
Out[17]: []

In [18]: movies_xpath = '/body/div[@id="content"]/div[@class="content-wrap"]/div
    ...: [1]/section[1]/ul[1]/li'

In [19]: xpath = '/body/div[@id="content"]/div[@class="content-wrap"]'

In [20]: doc.xpath(xpath)
Out[20]: []

In [21]: 'content-wrap' in inner_html
Out[21]: True

In [22]: doc.xpath('/body')
Out[22]: []

In [23]: doc.xpath('/html/body')
Out[23]: [<Element body at 0x7f0924c89df0>]

In [24]: movies_xpath = '/html/body/div[@id="content"]/div[@class="content-wrap"
    ...: ]/div[1]/section[1]/ul[1]/li'

In [25]: doc.xpath(movies_xpath)
Out[25]: 
[<Element li at 0x7f0924c905e0>,
 <Element li at 0x7f0924c918a0>,
 <Element li at 0x7f0924c6e570>,
 <Element li at 0x7f09257b0860>,
 <Element li at 0x7f09257b19e0>,
 <Element li at 0x7f0924c8b380>,
 <Element li at 0x7f0924c8a3e0>,
 <Element li at 0x7f0924c8b5b0>,
 <Element li at 0x7f0924c88590>,
 <Element li at 0x7f0924c8bba0>,
 <Element li at 0x7f0924c8a7a0>,
 <Element li at 0x7f0924c8bce0>,
 <Element li at 0x7f0924c88d60>,
 <Element li at 0x7f0924c885e0>,
 <Element li at 0x7f0924c89990>,
 <Element li at 0x7f0924c8bd80>,
 <Element li at 0x7f0924c8ae30>,
 <Element li at 0x7f0925bd8c20>,
 <Element li at 0x7f0925bd8950>,
 <Element li at 0x7f0925bd8ae0>,
 <Element li at 0x7f0925bd8bd0>,
 <Element li at 0x7f0925bd8a40>,
 <Element li at 0x7f0925bd89f0>,
 <Element li at 0x7f0925bd8b80>,
 <Element li at 0x7f0925bd8860>,
 <Element li at 0x7f0925bd8900>,
 <Element li at 0x7f0925bd87c0>,
 <Element li at 0x7f0925bd8770>,
 <Element li at 0x7f0925bd8720>,
 <Element li at 0x7f0925bd86d0>,
 <Element li at 0x7f0925bd8680>,
 <Element li at 0x7f0925bd8630>,
 <Element li at 0x7f0925bd85e0>,
 <Element li at 0x7f0925bd8590>,
 <Element li at 0x7f0925bd8540>,
 <Element li at 0x7f0925bd84f0>,
 <Element li at 0x7f0925bd84a0>,
 <Element li at 0x7f0925bd8450>,
 <Element li at 0x7f0925bd8400>,
 <Element li at 0x7f0925bd83b0>,
 <Element li at 0x7f0925bd8360>,
 <Element li at 0x7f0925bd8310>,
 <Element li at 0x7f0925bd82c0>,
 <Element li at 0x7f0925bd8270>,
 <Element li at 0x7f0925bd8220>,
 <Element li at 0x7f0925bd81d0>,
 <Element li at 0x7f0925bd8180>,
 <Element li at 0x7f0925bd8130>,
 <Element li at 0x7f0925bd80e0>,
 <Element li at 0x7f0925bd8090>,
 <Element li at 0x7f0925bd8040>,
 <Element li at 0x7f0925bcc590>,
 <Element li at 0x7f0925bcc310>,
 <Element li at 0x7f0925bcdc60>,
 <Element li at 0x7f0925bcc270>,
 <Element li at 0x7f0925bcc1d0>,
 <Element li at 0x7f0925bcc0e0>,
 <Element li at 0x7f0925bcc810>,
 <Element li at 0x7f0925bcc180>,
 <Element li at 0x7f0925bcc220>,
 <Element li at 0x7f0925bcc2c0>,
 <Element li at 0x7f0925bcffb0>,
 <Element li at 0x7f0925bcff60>,
 <Element li at 0x7f0925bcff10>,
 <Element li at 0x7f0925bcfec0>,
 <Element li at 0x7f0925bcfe70>,
 <Element li at 0x7f0925bcfe20>,
 <Element li at 0x7f0925bcfdd0>,
 <Element li at 0x7f0925bcfd80>,
 <Element li at 0x7f0925bcfd30>,
 <Element li at 0x7f0925bcfce0>,
 <Element li at 0x7f0925bcfc90>]

In [26]: movie_elements = doc.xpath(movies_xpath)

In [27]: for movie_element in movie_elements:
    ...:     title_element = movie_element.find('img', class_='frame')
    ...:     print(title_element)
    ...: 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[27], line 2
      1 for movie_element in movie_elements:
----> 2     title_element = movie_element.find('img', class_='frame')
      3     print(title_element)

File src/lxml/etree.pyx:1539, in lxml.etree._Element.find()

TypeError: find() got an unexpected keyword argument 'class_'

In [28]: for movie_element in movie_elements:
    ...:     title_element = movie_element.xpath('./div[1]/div[1]/a')
    ...:     print(title_element)
    ...: 
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]

In [29]: for movie_element in movie_elements:
    ...:     title_element = movie_element.xpath('//div[1]/div[1]/a')
    ...:     print(title_element)
    ...: 
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]

In [30]: for movie_element in movie_elements:
    ...:     title_element = movie_element.xpath('//div/div/a')
    ...:     print(title_element)
    ...: 
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]
[<Element a at 0x7f0925580f40>, <Element a at 0x7f09255804a0>]

In [31]: for movie_element in movie_elements:
    ...:     title_element = movie_element.xpath('./div/div/a')
    ...:     print(title_element)
    ...: 
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]

In [32]: for movie_element in movie_elements:
    ...:     title_element = movie_element.xpath('//div/div/a/span[1]')
    ...:     print(title_element.text_content())
    ...: 
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[32], line 3
      1 for movie_element in movie_elements:
      2     title_element = movie_element.xpath('//div/div/a/span[1]')
----> 3     print(title_element.text_content())

AttributeError: 'list' object has no attribute 'text_content'

In [33]: for movie_element in movie_elements:
    ...:     title_element = movie_element.xpath('//div/div/a/span[1]')
    ...:     print(title_element[0].text_content())
    ...: 
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[33], line 3
      1 for movie_element in movie_elements:
      2     title_element = movie_element.xpath('//div/div/a/span[1]')
----> 3     print(title_element[0].text_content())

IndexError: list index out of range

In [34]: for movie_element in movie_elements:
    ...:     title_element = movie_element.xpath('//div/div/a/span[1]')
    ...:     print(title_element)
    ...: 
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]

In [35]: for movie_element in movie_elements:
    ...:     title_element = movie_element.xpath('//div/div/a/span[1]')
    ...:     print(title_element)
    ...: 
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]

In [36]: for movie_element in movie_elements:
    ...:     title_element = movie_element.xpath('//div/div/a')
    ...:     print(title_element)
    ...: 
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]
[<Element a at 0x7f092573a250>, <Element a at 0x7f09255ea9d0>]

In [37]: movie_elements
Out[37]: 
[<Element li at 0x7f0924c905e0>,
 <Element li at 0x7f0924c918a0>,
 <Element li at 0x7f0924c6e570>,
 <Element li at 0x7f09257b0860>,
 <Element li at 0x7f09257b19e0>,
 <Element li at 0x7f0924c8b380>,
 <Element li at 0x7f0924c8a3e0>,
 <Element li at 0x7f0924c8b5b0>,
 <Element li at 0x7f0924c88590>,
 <Element li at 0x7f0924c8bba0>,
 <Element li at 0x7f0924c8a7a0>,
 <Element li at 0x7f0924c8bce0>,
 <Element li at 0x7f0924c88d60>,
 <Element li at 0x7f0924c885e0>,
 <Element li at 0x7f0924c89990>,
 <Element li at 0x7f0924c8bd80>,
 <Element li at 0x7f0924c8ae30>,
 <Element li at 0x7f0925bd8c20>,
 <Element li at 0x7f0925bd8950>,
 <Element li at 0x7f0925bd8ae0>,
 <Element li at 0x7f0925bd8bd0>,
 <Element li at 0x7f0925bd8a40>,
 <Element li at 0x7f0925bd89f0>,
 <Element li at 0x7f0925bd8b80>,
 <Element li at 0x7f0925bd8860>,
 <Element li at 0x7f0925bd8900>,
 <Element li at 0x7f0925bd87c0>,
 <Element li at 0x7f0925bd8770>,
 <Element li at 0x7f0925bd8720>,
 <Element li at 0x7f0925bd86d0>,
 <Element li at 0x7f0925bd8680>,
 <Element li at 0x7f0925bd8630>,
 <Element li at 0x7f0925bd85e0>,
 <Element li at 0x7f0925bd8590>,
 <Element li at 0x7f0925bd8540>,
 <Element li at 0x7f0925bd84f0>,
 <Element li at 0x7f0925bd84a0>,
 <Element li at 0x7f0925bd8450>,
 <Element li at 0x7f0925bd8400>,
 <Element li at 0x7f0925bd83b0>,
 <Element li at 0x7f0925bd8360>,
 <Element li at 0x7f0925bd8310>,
 <Element li at 0x7f0925bd82c0>,
 <Element li at 0x7f0925bd8270>,
 <Element li at 0x7f0925bd8220>,
 <Element li at 0x7f0925bd81d0>,
 <Element li at 0x7f0925bd8180>,
 <Element li at 0x7f0925bd8130>,
 <Element li at 0x7f0925bd80e0>,
 <Element li at 0x7f0925bd8090>,
 <Element li at 0x7f0925bd8040>,
 <Element li at 0x7f0925bcc590>,
 <Element li at 0x7f0925bcc310>,
 <Element li at 0x7f0925bcdc60>,
 <Element li at 0x7f0925bcc270>,
 <Element li at 0x7f0925bcc1d0>,
 <Element li at 0x7f0925bcc0e0>,
 <Element li at 0x7f0925bcc810>,
 <Element li at 0x7f0925bcc180>,
 <Element li at 0x7f0925bcc220>,
 <Element li at 0x7f0925bcc2c0>,
 <Element li at 0x7f0925bcffb0>,
 <Element li at 0x7f0925bcff60>,
 <Element li at 0x7f0925bcff10>,
 <Element li at 0x7f0925bcfec0>,
 <Element li at 0x7f0925bcfe70>,
 <Element li at 0x7f0925bcfe20>,
 <Element li at 0x7f0925bcfdd0>,
 <Element li at 0x7f0925bcfd80>,
 <Element li at 0x7f0925bcfd30>,
 <Element li at 0x7f0925bcfce0>,
 <Element li at 0x7f0925bcfc90>]

In [38]: for movie_element in movie_elements:
    ...:     title_element = movie_element.xpath('./div/div/a')
    ...:     print(title_element)
    ...: 
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]

In [39]: movie_titles = doc.xpath(f'{movies_xpath}/div[1]/div[1]/a/span[1]')

In [40]: for el in movie_titles:
    ...:     print(el.text.content())
    ...: 

In [41]: 

In [41]: movie_titles
Out[41]: []

In [42]: movie_titles = doc.xpath(f'{movies_xpath}/div/div/a/span')

In [43]: movie_titles
Out[43]: []

In [44]: movie_titles = doc.xpath(f'{movies_xpath}')

In [45]: doc.xpath(f'{movies_xpath}/div/div/a/span')
Out[45]: []

In [46]: doc.xpath(f'{movies_xpath}')
Out[46]: 
[<Element li at 0x7f0924c905e0>,
 <Element li at 0x7f0924c918a0>,
 <Element li at 0x7f0924c6e570>,
 <Element li at 0x7f09257b0860>,
 <Element li at 0x7f09257b19e0>,
 <Element li at 0x7f0924c8b380>,
 <Element li at 0x7f0924c8a3e0>,
 <Element li at 0x7f0924c8b5b0>,
 <Element li at 0x7f0924c88590>,
 <Element li at 0x7f0924c8bba0>,
 <Element li at 0x7f0924c8a7a0>,
 <Element li at 0x7f0924c8bce0>,
 <Element li at 0x7f0924c88d60>,
 <Element li at 0x7f0924c885e0>,
 <Element li at 0x7f0924c89990>,
 <Element li at 0x7f0924c8bd80>,
 <Element li at 0x7f0924c8ae30>,
 <Element li at 0x7f0925bd8c20>,
 <Element li at 0x7f0925bd8950>,
 <Element li at 0x7f0925bd8ae0>,
 <Element li at 0x7f0925bd8bd0>,
 <Element li at 0x7f0925bd8a40>,
 <Element li at 0x7f0925bd89f0>,
 <Element li at 0x7f0925bd8b80>,
 <Element li at 0x7f0925bd8860>,
 <Element li at 0x7f0925bd8900>,
 <Element li at 0x7f0925bd87c0>,
 <Element li at 0x7f0925bd8770>,
 <Element li at 0x7f0925bd8720>,
 <Element li at 0x7f0925bd86d0>,
 <Element li at 0x7f0925bd8680>,
 <Element li at 0x7f0925bd8630>,
 <Element li at 0x7f0925bd85e0>,
 <Element li at 0x7f0925bd8590>,
 <Element li at 0x7f0925bd8540>,
 <Element li at 0x7f0925bd84f0>,
 <Element li at 0x7f0925bd84a0>,
 <Element li at 0x7f0925bd8450>,
 <Element li at 0x7f0925bd8400>,
 <Element li at 0x7f0925bd83b0>,
 <Element li at 0x7f0925bd8360>,
 <Element li at 0x7f0925bd8310>,
 <Element li at 0x7f0925bd82c0>,
 <Element li at 0x7f0925bd8270>,
 <Element li at 0x7f0925bd8220>,
 <Element li at 0x7f0925bd81d0>,
 <Element li at 0x7f0925bd8180>,
 <Element li at 0x7f0925bd8130>,
 <Element li at 0x7f0925bd80e0>,
 <Element li at 0x7f0925bd8090>,
 <Element li at 0x7f0925bd8040>,
 <Element li at 0x7f0925bcc590>,
 <Element li at 0x7f0925bcc310>,
 <Element li at 0x7f0925bcdc60>,
 <Element li at 0x7f0925bcc270>,
 <Element li at 0x7f0925bcc1d0>,
 <Element li at 0x7f0925bcc0e0>,
 <Element li at 0x7f0925bcc810>,
 <Element li at 0x7f0925bcc180>,
 <Element li at 0x7f0925bcc220>,
 <Element li at 0x7f0925bcc2c0>,
 <Element li at 0x7f0925bcffb0>,
 <Element li at 0x7f0925bcff60>,
 <Element li at 0x7f0925bcff10>,
 <Element li at 0x7f0925bcfec0>,
 <Element li at 0x7f0925bcfe70>,
 <Element li at 0x7f0925bcfe20>,
 <Element li at 0x7f0925bcfdd0>,
 <Element li at 0x7f0925bcfd80>,
 <Element li at 0x7f0925bcfd30>,
 <Element li at 0x7f0925bcfce0>,
 <Element li at 0x7f0925bcfc90>]

In [47]: doc.xpath(f'{movies_xpath}/div')
Out[47]: 
[<Element div at 0x7f0925738720>,
 <Element div at 0x7f092573ba60>,
 <Element div at 0x7f0924c6e340>,
 <Element div at 0x7f0924c6e250>,
 <Element div at 0x7f0924c6c4a0>,
 <Element div at 0x7f0924c6fb50>,
 <Element div at 0x7f0924c6fec0>,
 <Element div at 0x7f0924c6d170>,
 <Element div at 0x7f0924c6f240>,
 <Element div at 0x7f0924c6d120>,
 <Element div at 0x7f0924c6d8a0>,
 <Element div at 0x7f0924c6fce0>,
 <Element div at 0x7f092559fe70>,
 <Element div at 0x7f092559f1f0>,
 <Element div at 0x7f092518be70>,
 <Element div at 0x7f0925189350>,
 <Element div at 0x7f092518aa20>,
 <Element div at 0x7f0925188d10>,
 <Element div at 0x7f092518a7a0>,
 <Element div at 0x7f0925188cc0>,
 <Element div at 0x7f092518a2a0>,
 <Element div at 0x7f092518b560>,
 <Element div at 0x7f09251892b0>,
 <Element div at 0x7f09251efb50>,
 <Element div at 0x7f09251ee5c0>,
 <Element div at 0x7f09251ecc20>,
 <Element div at 0x7f09251ed3f0>,
 <Element div at 0x7f09255ea2f0>,
 <Element div at 0x7f09255eb6a0>,
 <Element div at 0x7f09255e9e40>,
 <Element div at 0x7f09255eb8d0>,
 <Element div at 0x7f09255ea0c0>,
 <Element div at 0x7f09255e8e00>,
 <Element div at 0x7f09255eacf0>,
 <Element div at 0x7f09255eb510>,
 <Element div at 0x7f09255eaa70>,
 <Element div at 0x7f09255e8cc0>,
 <Element div at 0x7f09255eb330>,
 <Element div at 0x7f09255eb240>,
 <Element div at 0x7f09255e9c60>,
 <Element div at 0x7f09255eab60>,
 <Element div at 0x7f09255e9a30>,
 <Element div at 0x7f09255eafc0>,
 <Element div at 0x7f09255e9850>,
 <Element div at 0x7f09255e9a80>,
 <Element div at 0x7f09255e9440>,
 <Element div at 0x7f09255ea930>,
 <Element div at 0x7f09255ea020>,
 <Element div at 0x7f09255eb7e0>,
 <Element div at 0x7f09255e8c70>,
 <Element div at 0x7f09255e9b70>,
 <Element div at 0x7f09255eb1f0>,
 <Element div at 0x7f09255e9800>,
 <Element div at 0x7f09255e9030>,
 <Element div at 0x7f09255ebe20>,
 <Element div at 0x7f09255e8f90>,
 <Element div at 0x7f09255eb6f0>,
 <Element div at 0x7f09255e93f0>,
 <Element div at 0x7f09255ebe70>,
 <Element div at 0x7f09255eb970>,
 <Element div at 0x7f09255e98a0>,
 <Element div at 0x7f09255eb5b0>,
 <Element div at 0x7f09255e9c10>,
 <Element div at 0x7f09255eb3d0>,
 <Element div at 0x7f09255ea700>,
 <Element div at 0x7f09255ebb50>,
 <Element div at 0x7f09255e9ad0>,
 <Element div at 0x7f09255e9d50>,
 <Element div at 0x7f09255e9580>,
 <Element div at 0x7f09255eac50>,
 <Element div at 0x7f09255e99e0>,
 <Element div at 0x7f09255ea8e0>]

In [48]: doc.xpath(f'{movies_xpath}/div[1]')
Out[48]: 
[<Element div at 0x7f0925738720>,
 <Element div at 0x7f092573ba60>,
 <Element div at 0x7f0924c6e340>,
 <Element div at 0x7f0924c6e250>,
 <Element div at 0x7f0924c6c4a0>,
 <Element div at 0x7f0924c6fb50>,
 <Element div at 0x7f0924c6fec0>,
 <Element div at 0x7f0924c6d170>,
 <Element div at 0x7f0924c6f240>,
 <Element div at 0x7f0924c6d120>,
 <Element div at 0x7f0924c6d8a0>,
 <Element div at 0x7f0924c6fce0>,
 <Element div at 0x7f092559fe70>,
 <Element div at 0x7f092559f1f0>,
 <Element div at 0x7f092518be70>,
 <Element div at 0x7f0925189350>,
 <Element div at 0x7f092518aa20>,
 <Element div at 0x7f0925188d10>,
 <Element div at 0x7f092518a7a0>,
 <Element div at 0x7f0925188cc0>,
 <Element div at 0x7f092518a2a0>,
 <Element div at 0x7f092518b560>,
 <Element div at 0x7f09251892b0>,
 <Element div at 0x7f09251efb50>,
 <Element div at 0x7f09251ee5c0>,
 <Element div at 0x7f09251ecc20>,
 <Element div at 0x7f09251ed3f0>,
 <Element div at 0x7f09255ea2f0>,
 <Element div at 0x7f09255eb6a0>,
 <Element div at 0x7f09255e9e40>,
 <Element div at 0x7f09255eb8d0>,
 <Element div at 0x7f09255ea0c0>,
 <Element div at 0x7f09255e8e00>,
 <Element div at 0x7f09255eacf0>,
 <Element div at 0x7f09255eb510>,
 <Element div at 0x7f09255eaa70>,
 <Element div at 0x7f09255e8cc0>,
 <Element div at 0x7f09255eb330>,
 <Element div at 0x7f09255eb240>,
 <Element div at 0x7f09255e9c60>,
 <Element div at 0x7f09255eab60>,
 <Element div at 0x7f09255e9a30>,
 <Element div at 0x7f09255eafc0>,
 <Element div at 0x7f09255e9850>,
 <Element div at 0x7f09255e9a80>,
 <Element div at 0x7f09255e9440>,
 <Element div at 0x7f09255ea930>,
 <Element div at 0x7f09255ea020>,
 <Element div at 0x7f09255eb7e0>,
 <Element div at 0x7f09255e8c70>,
 <Element div at 0x7f09255e9b70>,
 <Element div at 0x7f09255eb1f0>,
 <Element div at 0x7f09255e9800>,
 <Element div at 0x7f09255e9030>,
 <Element div at 0x7f09255ebe20>,
 <Element div at 0x7f09255e8f90>,
 <Element div at 0x7f09255eb6f0>,
 <Element div at 0x7f09255e93f0>,
 <Element div at 0x7f09255ebe70>,
 <Element div at 0x7f09255eb970>,
 <Element div at 0x7f09255e98a0>,
 <Element div at 0x7f09255eb5b0>,
 <Element div at 0x7f09255e9c10>,
 <Element div at 0x7f09255eb3d0>,
 <Element div at 0x7f09255ea700>,
 <Element div at 0x7f09255ebb50>,
 <Element div at 0x7f09255e9ad0>,
 <Element div at 0x7f09255e9d50>,
 <Element div at 0x7f09255e9580>,
 <Element div at 0x7f09255eac50>,
 <Element div at 0x7f09255e99e0>,
 <Element div at 0x7f09255ea8e0>]

In [49]: doc.xpath(f'{movies_xpath}/div[1]/div[1]')
Out[49]: []

In [50]: doc.xpath(f'{movies_xpath}/div[1]//span[@class="frame-title"]')
Out[50]: 
[<Element span at 0x7f09251ec770>,
 <Element span at 0x7f09251ec810>,
 <Element span at 0x7f09251ec090>,
 <Element span at 0x7f09251ed850>,
 <Element span at 0x7f09251ef2e0>,
 <Element span at 0x7f09251ee1b0>,
 <Element span at 0x7f09251ee570>,
 <Element span at 0x7f09251ed6c0>,
 <Element span at 0x7f09251ee4d0>,
 <Element span at 0x7f09251ed670>,
 <Element span at 0x7f09251ee200>,
 <Element span at 0x7f09251ed800>,
 <Element span at 0x7f09251ee750>,
 <Element span at 0x7f09251ed080>,
 <Element span at 0x7f09251ed620>,
 <Element span at 0x7f09251ed4e0>,
 <Element span at 0x7f0924c89f80>,
 <Element span at 0x7f0924c88d10>,
 <Element span at 0x7f0924c8be70>,
 <Element span at 0x7f0924c8a520>,
 <Element span at 0x7f0924c88450>,
 <Element span at 0x7f0924c8bec0>,
 <Element span at 0x7f0924c8b8d0>,
 <Element span at 0x7f0924c8aca0>,
 <Element span at 0x7f0924c8ba10>,
 <Element span at 0x7f0924c8a930>,
 <Element span at 0x7f0924c88c70>,
 <Element span at 0x7f0924c8ab10>,
 <Element span at 0x7f0924c8bf60>,
 <Element span at 0x7f0924c8a2f0>,
 <Element span at 0x7f0924c8bdd0>,
 <Element span at 0x7f0924c8ac50>,
 <Element span at 0x7f0924c8a250>,
 <Element span at 0x7f0924c8a480>,
 <Element span at 0x7f0924c8af20>,
 <Element span at 0x7f0924c8bd30>,
 <Element span at 0x7f09251df880>,
 <Element span at 0x7f09251dda30>,
 <Element span at 0x7f09251ddcb0>,
 <Element span at 0x7f09251ddb20>,
 <Element span at 0x7f09251df3d0>,
 <Element span at 0x7f09251dfb50>,
 <Element span at 0x7f09251dd210>,
 <Element span at 0x7f09251dd300>,
 <Element span at 0x7f09251de930>,
 <Element span at 0x7f09251deb60>,
 <Element span at 0x7f09251dfb00>,
 <Element span at 0x7f09251dd710>,
 <Element span at 0x7f09251de2a0>,
 <Element span at 0x7f09251de700>,
 <Element span at 0x7f09251dfec0>,
 <Element span at 0x7f09251dea20>,
 <Element span at 0x7f09251de7f0>,
 <Element span at 0x7f09251df6a0>,
 <Element span at 0x7f09251de200>,
 <Element span at 0x7f09251de9d0>,
 <Element span at 0x7f0925189760>,
 <Element span at 0x7f0925189800>,
 <Element span at 0x7f0925188d60>,
 <Element span at 0x7f09251893f0>,
 <Element span at 0x7f092518a6b0>,
 <Element span at 0x7f0925189210>,
 <Element span at 0x7f092518a070>,
 <Element span at 0x7f092518a890>,
 <Element span at 0x7f092518b8d0>,
 <Element span at 0x7f0925189940>,
 <Element span at 0x7f092518b880>,
 <Element span at 0x7f0925188a40>,
 <Element span at 0x7f0925189da0>,
 <Element span at 0x7f0925189d00>,
 <Element span at 0x7f09251883b0>,
 <Element span at 0x7f0925188e00>]

In [51]: for el in doc.xpath(f'{movies_xpath}/div[1]//span[@class="frame-title"]
    ...: '):
    ...:     print(el.text_content)
    ...: 
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ec770>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ec810>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ec090>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ed850>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ef2e0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ee1b0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ee570>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ed6c0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ee4d0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ed670>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ee200>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ed800>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ee750>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ed080>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ed620>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ed4e0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c89f80>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c88d10>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8be70>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8a520>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c88450>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8bec0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8b8d0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8aca0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8ba10>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8a930>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c88c70>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8ab10>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8bf60>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8a2f0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8bdd0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8ac50>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8a250>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8a480>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8af20>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924c8bd30>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251df880>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251dda30>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ddcb0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251ddb20>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251df3d0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251dfb50>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251dd210>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251dd300>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251de930>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251deb60>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251dfb00>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251dd710>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251de2a0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251de700>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251dfec0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251dea20>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251de7f0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251df6a0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251de200>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251de9d0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925189760>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925189800>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925188d60>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251893f0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092518a6b0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925189210>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092518a070>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092518a890>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092518b8d0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925189940>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092518b880>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925188a40>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925189da0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925189d00>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251883b0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925188e00>>

In [52]: for el in doc.xpath(f'{movies_xpath}/div[1]//span[@class="frame-title"]
    ...: '):
    ...:     print(el.text_content())
    ...: 









































































In [53]: for el in doc.xpath(f'{movies_xpath}/div[1]/span[@class="frame-title"]'):
    ...:     print(el.text_content())
    ...: 

In [54]: doc.xpath(f'/html/body/span[@class="frame-title"]')
Out[54]: []

In [55]: doc.xpath(f'/html/body//span[@class="frame-title"]')
Out[55]: 
[<Element span at 0x7f09251ec770>,
 <Element span at 0x7f09251ec810>,
 <Element span at 0x7f09251ec090>,
 <Element span at 0x7f09251ed850>,
 <Element span at 0x7f09251ef2e0>,
 <Element span at 0x7f09251ee1b0>,
 <Element span at 0x7f09251ee570>,
 <Element span at 0x7f09251ed6c0>,
 <Element span at 0x7f09251ee4d0>,
 <Element span at 0x7f09251ed670>,
 <Element span at 0x7f09251ee200>,
 <Element span at 0x7f09251ed800>,
 <Element span at 0x7f09251ee750>,
 <Element span at 0x7f09251ed080>,
 <Element span at 0x7f09251ed620>,
 <Element span at 0x7f09251ed4e0>,
 <Element span at 0x7f0924c89f80>,
 <Element span at 0x7f0924c88d10>,
 <Element span at 0x7f0924c8be70>,
 <Element span at 0x7f0924c8a520>,
 <Element span at 0x7f0924c88450>,
 <Element span at 0x7f0924c8bec0>,
 <Element span at 0x7f0924c8b8d0>,
 <Element span at 0x7f0924c8aca0>,
 <Element span at 0x7f0924c8ba10>,
 <Element span at 0x7f0924c8a930>,
 <Element span at 0x7f0924c88c70>,
 <Element span at 0x7f0924c8ab10>,
 <Element span at 0x7f0924c8bf60>,
 <Element span at 0x7f0924c8a2f0>,
 <Element span at 0x7f0924c8bdd0>,
 <Element span at 0x7f0924c8ac50>,
 <Element span at 0x7f0924c8a250>,
 <Element span at 0x7f0924c8a480>,
 <Element span at 0x7f0924c8af20>,
 <Element span at 0x7f0924c8bd30>,
 <Element span at 0x7f09251df880>,
 <Element span at 0x7f09251dda30>,
 <Element span at 0x7f09251ddcb0>,
 <Element span at 0x7f09251ddb20>,
 <Element span at 0x7f09251df3d0>,
 <Element span at 0x7f09251dfb50>,
 <Element span at 0x7f09251dd210>,
 <Element span at 0x7f09251dd300>,
 <Element span at 0x7f09251de930>,
 <Element span at 0x7f09251deb60>,
 <Element span at 0x7f09251dfb00>,
 <Element span at 0x7f09251dd710>,
 <Element span at 0x7f09251de2a0>,
 <Element span at 0x7f09251de700>,
 <Element span at 0x7f09251dfec0>,
 <Element span at 0x7f09251dea20>,
 <Element span at 0x7f09251de7f0>,
 <Element span at 0x7f09251df6a0>,
 <Element span at 0x7f09251de200>,
 <Element span at 0x7f09251de9d0>,
 <Element span at 0x7f0925189760>,
 <Element span at 0x7f0925189800>,
 <Element span at 0x7f0925188d60>,
 <Element span at 0x7f09251893f0>,
 <Element span at 0x7f092518a6b0>,
 <Element span at 0x7f0925189210>,
 <Element span at 0x7f092518a070>,
 <Element span at 0x7f092518a890>,
 <Element span at 0x7f092518b8d0>,
 <Element span at 0x7f0925189940>,
 <Element span at 0x7f092518b880>,
 <Element span at 0x7f0925188a40>,
 <Element span at 0x7f0925189da0>,
 <Element span at 0x7f0925189d00>,
 <Element span at 0x7f09251883b0>,
 <Element span at 0x7f0925188e00>]

In [56]: for el in doc.xpath(f'/html/body//span[@class="frame-title"]'):
    ...:     print(el.text_content())
    ...: 









































































In [57]: elements = doc.xpath(f'/html/body//span[@class="frame-title"]')

In [58]: elements
Out[58]: 
[<Element span at 0x7f09251ec770>,
 <Element span at 0x7f09251ec810>,
 <Element span at 0x7f09251ec090>,
 <Element span at 0x7f09251ed850>,
 <Element span at 0x7f09251ef2e0>,
 <Element span at 0x7f09251ee1b0>,
 <Element span at 0x7f09251ee570>,
 <Element span at 0x7f09251ed6c0>,
 <Element span at 0x7f09251ee4d0>,
 <Element span at 0x7f09251ed670>,
 <Element span at 0x7f09251ee200>,
 <Element span at 0x7f09251ed800>,
 <Element span at 0x7f09251ee750>,
 <Element span at 0x7f09251ed080>,
 <Element span at 0x7f09251ed620>,
 <Element span at 0x7f09251ed4e0>,
 <Element span at 0x7f0924c89f80>,
 <Element span at 0x7f0924c88d10>,
 <Element span at 0x7f0924c8be70>,
 <Element span at 0x7f0924c8a520>,
 <Element span at 0x7f0924c88450>,
 <Element span at 0x7f0924c8bec0>,
 <Element span at 0x7f0924c8b8d0>,
 <Element span at 0x7f0924c8aca0>,
 <Element span at 0x7f0924c8ba10>,
 <Element span at 0x7f0924c8a930>,
 <Element span at 0x7f0924c88c70>,
 <Element span at 0x7f0924c8ab10>,
 <Element span at 0x7f0924c8bf60>,
 <Element span at 0x7f0924c8a2f0>,
 <Element span at 0x7f0924c8bdd0>,
 <Element span at 0x7f0924c8ac50>,
 <Element span at 0x7f0924c8a250>,
 <Element span at 0x7f0924c8a480>,
 <Element span at 0x7f0924c8af20>,
 <Element span at 0x7f0924c8bd30>,
 <Element span at 0x7f09251df880>,
 <Element span at 0x7f09251dda30>,
 <Element span at 0x7f09251ddcb0>,
 <Element span at 0x7f09251ddb20>,
 <Element span at 0x7f09251df3d0>,
 <Element span at 0x7f09251dfb50>,
 <Element span at 0x7f09251dd210>,
 <Element span at 0x7f09251dd300>,
 <Element span at 0x7f09251de930>,
 <Element span at 0x7f09251deb60>,
 <Element span at 0x7f09251dfb00>,
 <Element span at 0x7f09251dd710>,
 <Element span at 0x7f09251de2a0>,
 <Element span at 0x7f09251de700>,
 <Element span at 0x7f09251dfec0>,
 <Element span at 0x7f09251dea20>,
 <Element span at 0x7f09251de7f0>,
 <Element span at 0x7f09251df6a0>,
 <Element span at 0x7f09251de200>,
 <Element span at 0x7f09251de9d0>,
 <Element span at 0x7f0925189760>,
 <Element span at 0x7f0925189800>,
 <Element span at 0x7f0925188d60>,
 <Element span at 0x7f09251893f0>,
 <Element span at 0x7f092518a6b0>,
 <Element span at 0x7f0925189210>,
 <Element span at 0x7f092518a070>,
 <Element span at 0x7f092518a890>,
 <Element span at 0x7f092518b8d0>,
 <Element span at 0x7f0925189940>,
 <Element span at 0x7f092518b880>,
 <Element span at 0x7f0925188a40>,
 <Element span at 0x7f0925189da0>,
 <Element span at 0x7f0925189d00>,
 <Element span at 0x7f09251883b0>,
 <Element span at 0x7f0925188e00>]

In [59]: elements
Out[59]: 
[<Element span at 0x7f09251ec770>,
 <Element span at 0x7f09251ec810>,
 <Element span at 0x7f09251ec090>,
 <Element span at 0x7f09251ed850>,
 <Element span at 0x7f09251ef2e0>,
 <Element span at 0x7f09251ee1b0>,
 <Element span at 0x7f09251ee570>,
 <Element span at 0x7f09251ed6c0>,
 <Element span at 0x7f09251ee4d0>,
 <Element span at 0x7f09251ed670>,
 <Element span at 0x7f09251ee200>,
 <Element span at 0x7f09251ed800>,
 <Element span at 0x7f09251ee750>,
 <Element span at 0x7f09251ed080>,
 <Element span at 0x7f09251ed620>,
 <Element span at 0x7f09251ed4e0>,
 <Element span at 0x7f0924c89f80>,
 <Element span at 0x7f0924c88d10>,
 <Element span at 0x7f0924c8be70>,
 <Element span at 0x7f0924c8a520>,
 <Element span at 0x7f0924c88450>,
 <Element span at 0x7f0924c8bec0>,
 <Element span at 0x7f0924c8b8d0>,
 <Element span at 0x7f0924c8aca0>,
 <Element span at 0x7f0924c8ba10>,
 <Element span at 0x7f0924c8a930>,
 <Element span at 0x7f0924c88c70>,
 <Element span at 0x7f0924c8ab10>,
 <Element span at 0x7f0924c8bf60>,
 <Element span at 0x7f0924c8a2f0>,
 <Element span at 0x7f0924c8bdd0>,
 <Element span at 0x7f0924c8ac50>,
 <Element span at 0x7f0924c8a250>,
 <Element span at 0x7f0924c8a480>,
 <Element span at 0x7f0924c8af20>,
 <Element span at 0x7f0924c8bd30>,
 <Element span at 0x7f09251df880>,
 <Element span at 0x7f09251dda30>,
 <Element span at 0x7f09251ddcb0>,
 <Element span at 0x7f09251ddb20>,
 <Element span at 0x7f09251df3d0>,
 <Element span at 0x7f09251dfb50>,
 <Element span at 0x7f09251dd210>,
 <Element span at 0x7f09251dd300>,
 <Element span at 0x7f09251de930>,
 <Element span at 0x7f09251deb60>,
 <Element span at 0x7f09251dfb00>,
 <Element span at 0x7f09251dd710>,
 <Element span at 0x7f09251de2a0>,
 <Element span at 0x7f09251de700>,
 <Element span at 0x7f09251dfec0>,
 <Element span at 0x7f09251dea20>,
 <Element span at 0x7f09251de7f0>,
 <Element span at 0x7f09251df6a0>,
 <Element span at 0x7f09251de200>,
 <Element span at 0x7f09251de9d0>,
 <Element span at 0x7f0925189760>,
 <Element span at 0x7f0925189800>,
 <Element span at 0x7f0925188d60>,
 <Element span at 0x7f09251893f0>,
 <Element span at 0x7f092518a6b0>,
 <Element span at 0x7f0925189210>,
 <Element span at 0x7f092518a070>,
 <Element span at 0x7f092518a890>,
 <Element span at 0x7f092518b8d0>,
 <Element span at 0x7f0925189940>,
 <Element span at 0x7f092518b880>,
 <Element span at 0x7f0925188a40>,
 <Element span at 0x7f0925189da0>,
 <Element span at 0x7f0925189d00>,
 <Element span at 0x7f09251883b0>,
 <Element span at 0x7f0925188e00>]

In [60]: elements[0]
Out[60]: <Element span at 0x7f09251ec770>

In [61]: elements[0].text_content
Out[61]: <bound method HtmlMixin.text_content of <Element span at 0x7f09251ec770>>

In [62]: elements[0].text_content()
Out[62]: ''

In [63]: elements[0].text

In [64]: elements[0].text()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[64], line 1
----> 1 elements[0].text()

TypeError: 'NoneType' object is not callable

In [65]: elements[0].text_content()
Out[65]: ''

In [66]: help(elements[0].text_content)


In [67]: doc.xpath(f'/html/body//li[@class="poster-container film-watched"]')
Out[67]: []

In [68]: doc.xpath(f'/html/body//li')
Out[68]: 
[<Element li at 0x7f0924c93bf0>,
 <Element li at 0x7f09251eef70>,
 <Element li at 0x7f092a390cc0>,
 <Element li at 0x7f092a390b80>,
 <Element li at 0x7f0924ee6c00>,
 <Element li at 0x7f0924ee45e0>,
 <Element li at 0x7f0924ee5d50>,
 <Element li at 0x7f0925bcefc0>,
 <Element li at 0x7f0925bce980>,
 <Element li at 0x7f0925bcf510>,
 <Element li at 0x7f0925bce5c0>,
 <Element li at 0x7f0925bcea20>,
 <Element li at 0x7f0927b68a40>,
 <Element li at 0x7f0927b6bd30>,
 <Element li at 0x7f0927b69bc0>,
 <Element li at 0x7f0927b682c0>,
 <Element li at 0x7f0927b68270>,
 <Element li at 0x7f0927b69120>,
 <Element li at 0x7f0925164130>,
 <Element li at 0x7f0925166c50>,
 <Element li at 0x7f0925167b50>,
 <Element li at 0x7f09251642c0>,
 <Element li at 0x7f0925164310>,
 <Element li at 0x7f09251667a0>,
 <Element li at 0x7f09251667f0>,
 <Element li at 0x7f0925164db0>,
 <Element li at 0x7f0925167c40>,
 <Element li at 0x7f0925166020>,
 <Element li at 0x7f0925165260>,
 <Element li at 0x7f0925165b20>,
 <Element li at 0x7f09251652b0>,
 <Element li at 0x7f09251662f0>,
 <Element li at 0x7f0925166340>,
 <Element li at 0x7f0925166250>,
 <Element li at 0x7f0925165b70>,
 <Element li at 0x7f0925165d00>,
 <Element li at 0x7f09251659e0>,
 <Element li at 0x7f09251658a0>,
 <Element li at 0x7f0925165440>,
 <Element li at 0x7f0925164400>,
 <Element li at 0x7f0925165170>,
 <Element li at 0x7f0925166160>,
 <Element li at 0x7f09251660c0>,
 <Element li at 0x7f0925165df0>,
 <Element li at 0x7f0925166520>,
 <Element li at 0x7f0925165210>,
 <Element li at 0x7f0925165c10>,
 <Element li at 0x7f0925166930>,
 <Element li at 0x7f0925166200>,
 <Element li at 0x7f09251655d0>,
 <Element li at 0x7f0925167c90>,
 <Element li at 0x7f09251668e0>,
 <Element li at 0x7f09251663e0>,
 <Element li at 0x7f0925165760>,
 <Element li at 0x7f0925164270>,
 <Element li at 0x7f09251671a0>,
 <Element li at 0x7f0925166d40>,
 <Element li at 0x7f0925165da0>,
 <Element li at 0x7f09251651c0>,
 <Element li at 0x7f0925164090>,
 <Element li at 0x7f0925165ee0>,
 <Element li at 0x7f0925165620>,
 <Element li at 0x7f0925165bc0>,
 <Element li at 0x7f0925166cf0>,
 <Element li at 0x7f09251656c0>,
 <Element li at 0x7f09251653a0>,
 <Element li at 0x7f0925166a70>,
 <Element li at 0x7f09251665c0>,
 <Element li at 0x7f09251653f0>,
 <Element li at 0x7f0925164180>,
 <Element li at 0x7f0925165fd0>,
 <Element li at 0x7f0925166b60>,
 <Element li at 0x7f0925166b10>,
 <Element li at 0x7f09251641d0>,
 <Element li at 0x7f0925166890>,
 <Element li at 0x7f0925167790>,
 <Element li at 0x7f0925de8db0>,
 <Element li at 0x7f0925de8ea0>,
 <Element li at 0x7f0925de9760>,
 <Element li at 0x7f0925100bd0>,
 <Element li at 0x7f0925100b80>,
 <Element li at 0x7f0925100c70>,
 <Element li at 0x7f0925100c20>,
 <Element li at 0x7f0925100cc0>,
 <Element li at 0x7f0925100d10>,
 <Element li at 0x7f0925100d60>,
 <Element li at 0x7f0925100db0>,
 <Element li at 0x7f0925100e00>,
 <Element li at 0x7f0925100e50>,
 <Element li at 0x7f0925100ea0>,
 <Element li at 0x7f0925100ef0>,
 <Element li at 0x7f0925100f40>,
 <Element li at 0x7f0925100f90>,
 <Element li at 0x7f0925100fe0>,
 <Element li at 0x7f0925101030>,
 <Element li at 0x7f0925101080>,
 <Element li at 0x7f09251010d0>,
 <Element li at 0x7f0925101120>,
 <Element li at 0x7f0925101170>,
 <Element li at 0x7f09251011c0>,
 <Element li at 0x7f0925101210>,
 <Element li at 0x7f0925101260>,
 <Element li at 0x7f09251012b0>,
 <Element li at 0x7f0925101350>,
 <Element li at 0x7f0925103330>,
 <Element li at 0x7f0925103560>,
 <Element li at 0x7f09251034c0>,
 <Element li at 0x7f09251013a0>,
 <Element li at 0x7f0925101440>,
 <Element li at 0x7f09251013f0>,
 <Element li at 0x7f0925101490>,
 <Element li at 0x7f09251014e0>,
 <Element li at 0x7f0925101530>,
 <Element li at 0x7f0925101580>,
 <Element li at 0x7f09251015d0>,
 <Element li at 0x7f0925101620>,
 <Element li at 0x7f0925101670>,
 <Element li at 0x7f09251016c0>,
 <Element li at 0x7f0925101710>,
 <Element li at 0x7f0925101760>,
 <Element li at 0x7f09251017b0>,
 <Element li at 0x7f0925101800>,
 <Element li at 0x7f0925101850>,
 <Element li at 0x7f09251018a0>,
 <Element li at 0x7f09251018f0>,
 <Element li at 0x7f0925101940>,
 <Element li at 0x7f0925101990>,
 <Element li at 0x7f09251019e0>,
 <Element li at 0x7f0924c905e0>,
 <Element li at 0x7f0924c918a0>,
 <Element li at 0x7f0924c6e570>,
 <Element li at 0x7f09257b0860>,
 <Element li at 0x7f09257b19e0>,
 <Element li at 0x7f0924c8b380>,
 <Element li at 0x7f0924c8a3e0>,
 <Element li at 0x7f0924c8b5b0>,
 <Element li at 0x7f0924c88590>,
 <Element li at 0x7f0924c8bba0>,
 <Element li at 0x7f0924c8a7a0>,
 <Element li at 0x7f0924c8bce0>,
 <Element li at 0x7f0924c88d60>,
 <Element li at 0x7f0924c885e0>,
 <Element li at 0x7f0924c89990>,
 <Element li at 0x7f0924c8bd80>,
 <Element li at 0x7f0924c8ae30>,
 <Element li at 0x7f0925bd8c20>,
 <Element li at 0x7f0925bd8950>,
 <Element li at 0x7f0925bd8ae0>,
 <Element li at 0x7f0925bd8bd0>,
 <Element li at 0x7f0925bd8a40>,
 <Element li at 0x7f0925bd89f0>,
 <Element li at 0x7f0925bd8b80>,
 <Element li at 0x7f0925bd8860>,
 <Element li at 0x7f0925bd8900>,
 <Element li at 0x7f0925bd87c0>,
 <Element li at 0x7f0925bd8770>,
 <Element li at 0x7f0925bd8720>,
 <Element li at 0x7f0925bd86d0>,
 <Element li at 0x7f0925bd8680>,
 <Element li at 0x7f0925bd8630>,
 <Element li at 0x7f0925bd85e0>,
 <Element li at 0x7f0925bd8590>,
 <Element li at 0x7f0925bd8540>,
 <Element li at 0x7f0925bd84f0>,
 <Element li at 0x7f0925bd84a0>,
 <Element li at 0x7f0925bd8450>,
 <Element li at 0x7f0925bd8400>,
 <Element li at 0x7f0925bd83b0>,
 <Element li at 0x7f0925bd8360>,
 <Element li at 0x7f0925bd8310>,
 <Element li at 0x7f0925bd82c0>,
 <Element li at 0x7f0925bd8270>,
 <Element li at 0x7f0925bd8220>,
 <Element li at 0x7f0925bd81d0>,
 <Element li at 0x7f0925bd8180>,
 <Element li at 0x7f0925bd8130>,
 <Element li at 0x7f0925bd80e0>,
 <Element li at 0x7f0925bd8090>,
 <Element li at 0x7f0925bd8040>,
 <Element li at 0x7f0925bcc590>,
 <Element li at 0x7f0925bcc310>,
 <Element li at 0x7f0925bcdc60>,
 <Element li at 0x7f0925bcc270>,
 <Element li at 0x7f0925bcc1d0>,
 <Element li at 0x7f0925bcc0e0>,
 <Element li at 0x7f0925bcc810>,
 <Element li at 0x7f0925bcc180>,
 <Element li at 0x7f0925bcc220>,
 <Element li at 0x7f0925bcc2c0>,
 <Element li at 0x7f0925bcffb0>,
 <Element li at 0x7f0925bcff60>,
 <Element li at 0x7f0925bcff10>,
 <Element li at 0x7f0925bcfec0>,
 <Element li at 0x7f0925bcfe70>,
 <Element li at 0x7f0925bcfe20>,
 <Element li at 0x7f0925bcfdd0>,
 <Element li at 0x7f0925bcfd80>,
 <Element li at 0x7f0925bcfd30>,
 <Element li at 0x7f0925bcfce0>,
 <Element li at 0x7f0925bcfc90>,
 <Element li at 0x7f0925101a30>,
 <Element li at 0x7f0925101a80>,
 <Element li at 0x7f0925101ad0>,
 <Element li at 0x7f0925101b20>,
 <Element li at 0x7f0925101b70>,
 <Element li at 0x7f0925101bc0>,
 <Element li at 0x7f0925101c10>,
 <Element li at 0x7f0925101c60>,
 <Element li at 0x7f0925101cb0>,
 <Element li at 0x7f0925101d00>,
 <Element li at 0x7f0925101d50>,
 <Element li at 0x7f0925101da0>,
 <Element li at 0x7f0925101df0>,
 <Element li at 0x7f0925101e40>,
 <Element li at 0x7f0925101e90>,
 <Element li at 0x7f0925101ee0>]

In [69]: len(elements)
Out[69]: 72

In [70]: len(doc.xpath(f'/html/body//li'))
Out[70]: 216

In [71]: for i in doc.xpath(f'/html/body//li'):
    ...:     print(i.text_content())
    ...: 
Activity
Activity
Films
Diary
Reviews
Watchlist
Lists
Likes
Tags
Network
Gift Pro

					
						RSS feed for Mehdi
					
				
Watched
Diary
Reviews
Small
Large
Remove filters
  Fade watched films   
  Show custom posters   
 Custom posters   Any Theirs Yours None   
 Account Filters  Show watched films Hide watched films Show liked films Hide liked films Show rated films Hide rated films Show logged films Hide logged films Show rewatched films Hide rewatched films Show reviewed films Hide reviewed films Show films in watchlist Hide films in watchlist Show films you own Hide films you own Show films you’ve customized Hide films you’ve customized  
Show watched films
Hide watched films
Show liked films
Hide liked films
Show rated films
Hide rated films
Show logged films
Hide logged films
Show rewatched films
Hide rewatched films
Show reviewed films
Hide reviewed films
Show films in watchlist
Hide films in watchlist
Show films you own
Hide films you own
Show films you’ve customized
Hide films you’ve customized
 Content Filters  Show short films Hide short films Show TV shows Hide TV shows Hide documentaries Hide unreleased titles Show obscure films Hide obscure films Show films with backdrop Hide films with backdrop Show Nanocrowd films Hide Nanocrowd films  
Show short films
Hide short films
Show TV shows
Hide TV shows
Hide documentaries
Hide unreleased titles
Show obscure films
Hide obscure films
Show films with backdrop
Hide films with backdrop
Show Nanocrowd films
Hide Nanocrowd films
Film Name
Film Popularity
Shuffle
When Added  Newest First Earliest First 
Newest First
Earliest First
When Rated  Newest First Earliest First 
Newest First
Earliest First
Release Date  Newest First Earliest First 
Newest First
Earliest First
Average Rating  Highest First Lowest First 
Highest First
Lowest First
Mehdi’s Rating  Highest First Lowest First 
Highest First
Lowest First
Your Rating  Highest First Lowest First 
Highest First
Lowest First
Your Interests  Based on films you liked Related to films you liked 
Based on films you liked
Related to films you liked
Film Length  Shortest First Longest First 
Shortest First
Longest First
  All films  
  Amazon DE  
  Amazon Video DE  
  Apple TV Plus DE  
  iTunes DE  
 Upgrade to a Letterboxd Pro account to add your favorite services to this list—including any service and country pair listed on JustWatch—and to enable one-click filtering by all your favorites.
Powered by JustWatch
Any genre
  Action Adventure Animation Comedy Crime Documentary Drama Family Fantasy History Horror Music Mystery Romance Science Fiction Thriller TV Movie War Western  
Action
Adventure
Animation
Comedy
Crime
Documentary
Drama
Family
Fantasy
History
Horror
Music
Mystery
Romance
Science Fiction
Thriller
TV Movie
War
Western
Any decade
2020s
2010s
2000s
1990s
1980s
1970s
1960s
1950s
1940s
1930s
1920s
1910s
1900s
1890s
1880s
1870s
Any rating
No rating
 Rating (or range)       Drag to define range 

							     

						

							     ★★★  

						

							     

						

							     

						

							     

						

							     

						

							     ★★★★ 

						

							     

						

							     

						

							     

						

							     

						

							     ★★★ 

						

							     

						

							     

						

							     

						

							     ★★★★ 

						

							     ★★★★ 

						

							     

						

							     ★★★★★  

						

							     ★★★ 

						

							     ★★★★½  

						

							     ★★★★ 

						

							     

						

							     

						

							     

						

							     

						

							     

						

							     

						

							     

						

							     ★★★ 

						

							     

						

							     ★★★½  

						

							     

						

							     

						

							     

						

							     

						

							     

						

							     ★★★★ 

						

							     

						

							     ★★★★  

						

							     

						

							     

						

							     ★★★★★  

						

							     

						

							     ★★★★ 

						

							     

						

							     ★★★½ 

						

							     

						

							     

						

							     ★★★½ 

						

							     

						

							     ★★★★★  

						

							     

						

							     

						

							     ★★★½ 

						

							     

						

							     ★★★★ 

						

							     

						

							     

						

							     

						

							     

						

							     ★★★  

						

							     

						

							     ★★★ 

						

							     ★★★★½  

						

							     ★★★ 

						

							     

						

							     

						

							     

						

							     ★★★½ 

						

							     ★★★ 

						

							     

						
1
2
3
…
10
About
News
Pro
Apps
Podcast
Year in Review
Gift Guide
Help
Terms
API
Contact

In [72]: response.raw
Out[72]: <urllib3.response.HTTPResponse at 0x7f0925aac8e0>

In [73]: response.raw()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[73], line 1
----> 1 response.raw()

TypeError: 'HTTPResponse' object is not callable

In [74]: response.raw.decode_content()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[74], line 1
----> 1 response.raw.decode_content()

TypeError: 'bool' object is not callable

In [75]: response.raw.decode_content
Out[75]: False

In [76]: response.raw.decode_content = True

In [77]: response.text
Out[77]: '\n\n<!DOCTYPE html>\n\n<!--[if lt IE 7 ]> <html lang="en" class="ie6 lte9 lte8 lte7 lte6 no-js"> <![endif]-->\n<!--[if IE 7 ]>    <html lang="en" class="ie7 lte9 lte8 lte7 no-js"> <![endif]-->\n<!--[if IE 8 ]>    <html lang="en" class="ie8 lte9 lte8 no-js"> <![endif]-->\n<!--[if IE 9 ]>    <html lang="en" class="ie9 lte9 no-js"> <![endif]-->\n<!--[if (gt IE 9)|!(IE)]><!--> <html id="html" lang="en" class="no-mobile no-js"> <!--<![endif]-->\n<head>\n\t<meta charset="UTF-8" />\n\t<meta name="viewport" content="width=1024" />\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />\n\t<meta name="description" content="Mehdi Rafee’s films" />\n\t\n\t\n\t<meta property="og:url" content="https://letterboxd.com/mrafee113/films/?html.parser" />\n\t<meta property="og:title" content="Mehdi Rafee’s films" />\n\t<meta property="og:description" content="Mehdi Rafee’s films" />\n\t<meta property="og:image" content="https://s.ltrbxd.com/static/img/default-share.e38c5d62.png" />\n\t\n\t<meta name="application-name" content="Letterboxd" />\n\t<meta name="theme-color" content="#445566" />\n\t<meta name="msapplication-TileColor" content="#445566" />\n\t<meta name="apple-itunes-app" content="app-id=1054271011, affiliate-data=11l5KW, app-argument=https://letterboxd.com/mrafee113/films/?html.parser" />\n\t<meta name="mobile-web-app-capable" content="yes" />\n\n\t<title>&lrm;Mehdi Rafee’s films &bull; Letterboxd</title>\n\t\n\t<script>\n\t\twindow.dataLayer = window.dataLayer || [];\n\t\twindow.gtag = window.gtag || function () {\n\t\t\tdataLayer.push(arguments);\n\t\t};\n\t\tfunction ga() {}\n\t</script>\n\n\t<script async src="https://www.googletagmanager.com/gtag/js?id=G-D3ECBB4D7L"></script>\n\n\t<script>\n\t\twindow.dataLayer = window.dataLayer || [];\n\t\twindow.gtag = window.gtag || function () {\n\t\t\tdataLayer.push(arguments);\n\t\t};\n\t\tgtag(\'js\', new Date());\n\t\n\t\tvar analytic_params = {};\n\t\t\n\t\t\n\t\tanalytic_params[\'user_type\'] = \'Visitor\';\n\t\tanalytic_params[\'template\'] = \'/object/person/films-watched\';\n\t\t\n\t\t\n\n\t\tif (analytic_params.member_type) {\n\t\t\tgtag(\'set\', \'user_properties\', { \n\t\t\t\tmember_type: analytic_params.member_type,\n\t\t\t});\n\t\t\tdelete analytic_params.member_type;\n\t\t}\n\t\tvar config = {\n\t\t\t...analytic_params,\n\t\t\t\'cookie_domain\': \'letterboxd.com\', \n\t\t\t\'optimize_id\': \'GTM-TB8HSDN\', \n\t\t};\n\t\tgtag(\'config\', \'G-D3ECBB4D7L\', config);\n\t</script>\n\n\n\t<script>\n\t\tvar isMobile = false,\n\t\t\tisMobileOptimised = true,\n\t\t\trenderMobile = false,\n\t\t\tuseStaticFonts = false,\n\t\t\tdisableFrameProtection = false,\n\t\t\tbaseURL = "",\n\t\t\tsuccessMessages = [],\n\t\t\terrorMessages = [],\n\t\t\tstickyMessages = [],\n\t\t\tglobals = {\n\t\t\tautoAddFilm: false\t\t\t\n\t\t\t\t, spinners: {\n\t\t\t\t\tajax_242d35: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_12_2C3641: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_14_20272f: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_16_161B21: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\'\n\t\t\t\t}\n\t\t\t},\n\t\t\tsupermodelCSRF = "",\n\t\t\tgRecaptchaKey = \'6Le3mMIUAAAAAEXbwZ7M1R5jEv0V5xbvj7bgXq2g\',\n\t\t\tperson = {\n\t\t\t\tusername: ""\n\t\t\t\t, loggedIn: false\n\t\t\t\t\n\t\t\t\t, showAds: true\n\t\t\t\t, role: "guest"\n\t\t\t\t, hasExtendedServiceFilters: false\n\t\t\t\t, canBulkAddToLists: false\n\t\t\t\t, canFilterOwned: false\n\t\t\t\t, hasHqRole: false\n\t\t\t\t, canHaveHqDashboard: false\n\t\t\t\t, hasMemberStatistics: false\n\t\t\t\t, blockedMembers: []\n\t\t\t\t, showAdultContent: false\n\t\t\t\t, validated: null\n\t\t\t\t, trusted: false\n\t\t\t\t, hasBlocked : function(member) { for (var i = 0; i !== person.blockedMembers.length; i++) {if (person.blockedMembers[i] === member) return true;} return false; }\n\t\t\t\t, viewingTags: []\n\t\t\t\t, hasMoreTags: true\n\t\t\t\t, getCustomPoster : function(filmId) { return null; }\n\t\t\t},\n\t\t\tdisableAds = true;\n\t\t\n\t\t\n\t\t\nsupermodelCSRF = "9749e0a0bd2da01647eb";\n\n\t\t\n\n\t\t\n\n\t\t\n\n\t\t\n\t\t\tif ( screen.width < 768 ) {\n\t\t\t\tvar date = new Date();\n\t\t\t\tvar maxAge = 365 * 24 * 60 * 60;\n\t\t\t\tdate.setTime(date.getTime() + maxAge * 1000);\n\t\t\t\tvar expires = \'; expires=\' + date.toUTCString();\n\t\t\t\tdocument.cookie = "useMobileSite=yes" + expires + "; path=/; maxAge=" + maxAge;\n\t\t\t\tif ( document.cookie && document.cookie.indexOf("useMobileSite=yes") >= 0 ) {\n\t\t\t\t\twindow.location.reload(true);\n\t\t\t\t} else {\n\t\t\t\t\t// No cookies.  No Mobile version.\n\t\t\t\t}\n\t\t\t}\n\t\t\n\n\t\tvar isWindows = navigator.platform.toUpperCase().indexOf(\'WIN\') >= 0; // Detect windows platform\n\t\tif (isWindows) { document.documentElement.classList.add(\'is-windows\'); }\n\t\t\n\t\t\n\t</script>\n\n\t<link rel="manifest" href="/manifest.json" />\n\t<link rel="author" type="text/plain" href="/humans.txt" />\n\t<link rel="mask-icon" href="https://s.ltrbxd.com/static/img/icons/letterboxd-decal-l-16px.5fe24c7d.svg" color="#445566" />\n\t<link rel="shortcut icon" sizes="196x196" href="https://s.ltrbxd.com/static/img/icons/touch-icon-192x192.257b84e7.png" />\n\t<link rel="shortcut icon" href="/favicon.ico" />\n\t<link rel="search" type="application/opensearchdescription+xml" title="Letterboxd" href="/static/opensearch.xml" />\n\t\n\t\n\t<!--[if lte IE 9 ]>\n\t\t<link href="https://s.ltrbxd.com/static/css/ie9-1.min.066b855d.css" rel="stylesheet" media="screen, projection"/>\n\t\t<link href="https://s.ltrbxd.com/static/css/ie9-2.min.13b2f50c.css" rel="stylesheet" media="screen, projection"/>\n\t<![endif]-->\n\t<!--[if (gt IE 9)|!(IE)]><!-->\n\t\t<link href="https://s.ltrbxd.com/static/css/main.min.97414920.css" rel="stylesheet" media="screen, projection"/>\n\t<!--<![endif]-->\n\t<!--[if lte IE 6]><script>location.replace("/errors/ie6");</script><![endif]-->\n\t<!--[if IE 7]><script>location.replace("/errors/ie7");</script><![endif]-->\n\t<!--[if IE 8]><script>location.replace("/errors/ie8");</script><![endif]-->\n\t<!--[if IE 9]><script>location.replace("/errors/ie9");</script><![endif]-->\n\t\n\t\n\t\n\t<link href="https://s.ltrbxd.com/static/css/desktop.min.e1d8f367.css" rel="stylesheet" media="screen, projection"/>\n\n\t<script src="https://s.ltrbxd.com/static/js/main.min.a7e00d04.js"></script>\n\t\n\n\n\n\n\n\t<script>\n\t\tif ( $.cookie("letterboxd.admin.signed.in") === person.username ) {\n\t\t\tsuccessMessages.push("You are signed in as " + person.username);\n\t\t\t$(function(){$("#header, #content, body").css("background","#543");});\n\t\t}\n\t</script>\n\t\n</head>\n\n<body class="films-watched wide small-poster-grid" data-owner="mrafee113">\n\t\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<script>\nvar mainMenu = [];\n\n\t\n\tmainMenu.push({\n\t\t"id": 1,\n\t\t"url": "/sign-in/", \n\t\t"name": "Sign In",\n\t\t"cssClassCode": "sign-in-menu",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": true,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 2,\n\t\t"url": "/create-account/", \n\t\t"name": "Create Account",\n\t\t"cssClassCode": "create-account-menu",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 3,\n\t\t"url": "/", \n\t\t"name": "Home",\n\t\t"cssClassCode": "person-home",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 4,\n\t\t"url": "/activity/", \n\t\t"name": "Activity",\n\t\t"cssClassCode": "main-nav-activity",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "Activity",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 5,\n\t\t"url": "/films/", \n\t\t"name": "Films",\n\t\t"cssClassCode": "films-page main-nav-films",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 6,\n\t\t"url": "/lists/", \n\t\t"name": "Lists",\n\t\t"cssClassCode": "lists-page main-nav-lists",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 7,\n\t\t"url": "/members/", \n\t\t"name": "Members",\n\t\t"cssClassCode": "main-nav-people",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 8,\n\t\t"url": "/journal/", \n\t\t"name": "Journal",\n\t\t"cssClassCode": "main-nav-journal",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 9,\n\t\t"url": "/search/", \n\t\t"name": "Search results",\n\t\t"cssClassCode": "",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n</script>\n\n<header class="site-header js-hide-in-app" id="header" data-allow-user-to-add-all-films-to-a-list="true">\n\t<div class="site-header-bg"></div>\n\t<section>\n\t\t<h1 class="site-logo"><a href="/" class="logo replace">Letterboxd &mdash; Your life in film</a></h1>\n\n\t\t<div class="react-component" data-component-class="globals.comps.NavComponent"></div>\n\n\t\t\n\t\t\t\n\t\t\t\n\n\n\t\n\n\n\n\n\n<form method="post" action="#" id="signin" class="signin signin-form js-header-signin-form js-signin" data-url="/user/login.do" data-recaptcha-action="signin" novalidate=\'novalidate\' autocorrect=\'off\' autocapitalize=\'off\'>\n\t<input type="hidden" name="__csrf" value="placeholder" />\n\t<fieldset class="fieldset">\n\t\t<div class="fields">\n\t\t\t<div class="col">\n\t\t\t\t<label for="username">Username or Email</label>\n\t\t\t\t<input type="email" name="username" id="username" class="field signin-field" tabindex="1" data-focus-control="signingIn" autocomplete=\'email\' inputmode=\'email\' value="" />\n\t\t\t</div>\n\t\t\t<div class="col">\n\t\t\t\t<label for="password">Password</label>\n\t\t\t\t<input type="password" name="password" id="password" class="field signin-field" tabindex="2" autocomplete=\'current-password\' value="" />\n\t\t\t</div>\n\t\t\t<div class="signin-actions">\n\t\t\t\t<label for="remember" class="option-label -checkbox -small">\n\t\t\t\t\t<input type="checkbox" name="remember" id="remember" class="checkbox" tabindex="3" value="true" /><i class="substitute"></i>\n\t\t\t\t\t<span class="focus">Remember<span class="mob-hide"> me</span></span>\n\t\t\t\t</label>\n\t\t\t\t<p class="reset" tabindex="5"><a class="reset-password-link" href="/user/request-password-reset" target="_top">Forgotten<span class="elongated"> password</span>?</a></p>\n\t\t\t</div>\n\t\t\t<div class="col buttons">\n\t\t\t\t<div class="button-container"><input type="submit" value="Sign in" class="button -action button-green" tabindex="4" /><i></i></div>\n\t\t\t\t<div class="close js-close-signin">&times;</div>\n\t\t\t</div>\n\t\t</div>\n\t</fieldset>\n\t<div id="signin-message" class="errormessage"></div>\n</form>\n\n\n\t\t\n\t\t\n\t\t\n\t\t\t\n\t\t\t\n\n\n\n\t\t\n\t\t\n\t\t\n\t\t<form id="search" class="js-search-form search-form" action="/search/" method="get" autocorrect="off">\n\t\t\t<input autocomplete="false" name="hidden" type="text" style="display:none;" />\n\t\t\t<fieldset>\n\t\t\t\t<label for="search-q" class="hidden">Search:</label>\n\t\t\t\t<input type="text" name="q" id="search-q" class="field -borderless" data-lpignore=\'true\' inputmode=\'search\' value="" />\n\t\t\t\t<input type="submit" value="Search" class="action" />\n\t\t\t</fieldset>\n\t\t</form>\n\t\t\n\t</section>\n</header>\n\n\n\n\n\n\n<div id="content" class="site-body">\n\t\n\t<div class="content-wrap">\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<section id="profile-header" class="js-profile-header -is-mini-nav" data-person="mrafee113">\n\t\n\n\t<nav class="profile-navigation">\n\t\t\n\t\t\t<div class="profile-mini-person">\n\t\t\t\t<a class="avatar -a24" href="/mrafee113/" > <img src="https://a.ltrbxd.com/resized/avatar/upload/1/4/4/4/1/0/3/shard/avtr-0-48-0-48-crop.jpg?v=484d4bfb0a" alt="Mehdi Rafee" width="24" height="24" /> </a>\n\t\t\t\t<h1 class="title-3"><a href="/mrafee113/">Mehdi Rafee</a></h1>\n\t\t\t\t\n\t\t\t</div>\n\t\t\n\t\t\n\t\t\t<ul class="navlist">\n\t\t\t\t\n\n\t\t\t\t\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem hide-for-owner"><a class="navlink" href="/mrafee113/activity/">Activity</a></li>\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/activity/">Activity</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem -active"><a class="navlink" href="/mrafee113/films/">Films</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/films/diary/">Diary</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/films/reviews/">Reviews</a></li>\n\n\t\t\t\t<li class="navitem" data-owner="mrafee113"><a class="navlink" href="/mrafee113/watchlist/" >Watchlist</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/mrafee113/lists/">Lists</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/likes/">Likes</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/mrafee113/tags/">Tags</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/following/">Network</a></li>\n\n\t\t\t\t\n\n\t\t\t\t\n\n\t\t\t\t\n\n\n\n\t<li data-owner="mrafee113" class="navitem show-when-logged-in hide-for-owner"><a class="navlink" href="/pro/gift/mrafee113/">Gift Pro</a></li>\n\n\n\t\t\t\t<li class="navitem -rss">\n\t\t\t\t\t<a href="/mrafee113/rss/" class="has-icon icon-16 icon-rss tooltip" title="RSS feed">\n\t\t\t\t\t\t<span class="_sr-only">RSS feed for Mehdi</span>\n\t\t\t\t\t</a>\n\t\t\t\t</li>\n\t\t\t</ul>\n\t\t\n    </nav>\n</section>\n\n\n \n\n\n\n<div class="cols-2 overflow">\n\t<section class="section col-main overflow">\n\t\n \t\t\n\n<div id="content-nav" class="tabbed"> <section class="sub-nav-wrapper"><ul class="sub-nav"> <li class=" selected"><a href="/mrafee113/films/" class="tooltip" title="690&nbsp;films">Watched</a></li> <li class=""><a href="/mrafee113/films/diary/" class="tooltip" title="254&nbsp;films">Diary</a></li> <li class=""><a href="/mrafee113/films/reviews/" class="tooltip" title="45&nbsp;films">Reviews</a></li> </ul></section> <div class="sorting-selects has-hide-toggle"> <section class="grid-toggle-menu mob-hide"> <ul> <li class="selected"><a href="/mrafee113/films/" class="grid-toggle ir s grid-toggle-small" data-toggle="large">Small</a></li> <li><a href="/mrafee113/films/size/large/" class="grid-toggle ir s grid-toggle-large" data-toggle="small">Large</a></li> </ul> </section> <section class="smenu-wrapper hide-toggle-menu"> <div class="smenu"> <label><span class="ir s hide-toggle-icon">Visibility Filters</span><i class="ir s icon"></i></label> <ul class="smenu-menu" id="hide-toggle-menu"> <li class="divider-line-below"><a href="#" class="item js-film-filter-remover">Remove filters</a></li> <li class="js-account-filters"> <label class="option-label -toggle -small switch-control js-fade-toggle"> <span class="label">Fade watched films</span> <input class="checkbox" type="checkbox" checked="checked" role="switch" /><span class="state"><span class="track"><span class="handle"></span></span></span> </label> </li> <li class="js-account-filters"> <label class="option-label -toggle -small switch-control js-custom-poster-toggle" data-action="/ajax/poster-mode/"> <span class="label">Show custom posters</span> <input class="checkbox" type="checkbox" checked="checked" role="switch" /><span class="state"><span class="track"><span class="handle"></span></span></span> </label> </li> <li class="divider-line js-account-filters"> <span class="smenu-sublabel -uppercase">Custom posters</span> <div class="segmented-control -small custom-poster-control js-custom-poster-control" role="group" aria-label="Change custom poster visibility" data-action="/ajax/poster-mode/"> <div class="options"> <button type="button" class="option" data-js-trigger="option" data-value="All">Any</button> <button type="button" class="option" data-js-trigger="option" data-value="Theirs">Theirs</button> <button type="button" class="option" data-js-trigger="option" data-value="Yours">Yours</button> <button type="button" class="option" data-js-trigger="option" data-value="None">None</button> </div> </div> </li> <li class="divider-line js-account-filters"> <span class="smenu-sublabel -uppercase">Account Filters</span> <ul> <li class="js-film-filter" data-category="watched" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show watched films</a></li> <li class="js-film-filter" data-category="watched" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide watched films</a></li> <li class="js-film-filter divider-line -inset" data-category="liked" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show liked films</a></li> <li class="js-film-filter" data-category="liked" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide liked films</a></li> <li class="js-film-filter divider-line -inset" data-category="rated" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show rated films</a></li> <li class="js-film-filter" data-category="rated" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide rated films</a></li> <li class="js-film-filter divider-line -inset" data-category="logged" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show logged films</a></li> <li class="js-film-filter" data-category="logged" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide logged films</a></li> <li class="js-film-filter divider-line -inset" data-category="rewatched" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show rewatched films</a></li> <li class="js-film-filter" data-category="rewatched" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide rewatched films</a></li> <li class="js-film-filter divider-line -inset" data-category="reviewed" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show reviewed films</a></li> <li class="js-film-filter" data-category="reviewed" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide reviewed films</a></li> <li class="js-film-filter divider-line -inset" data-category="watchlisted" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films in watchlist</a></li> <li class="js-film-filter" data-category="watchlisted" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films in watchlist</a></li> <li class="js-film-filter divider-line -inset" data-category="owned" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films you own</a></li> <li class="js-film-filter" data-category="owned" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films you own</a></li> <li class="js-film-filter divider-line -inset" data-category="customised" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films you’ve customized</a></li> <li class="js-film-filter" data-category="customised" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films you’ve customized</a></li> </ul> </li> <li class="divider-line js-film-filters"> <span class="smenu-sublabel -uppercase">Content Filters</span> <ul> <li class="js-film-filter" data-category="shorts" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show short films</a></li> <li class="js-film-filter" data-category="shorts" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide short films</a></li> <li class="js-film-filter divider-line -inset" data-category="tv" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show TV shows</a></li> <li class="js-film-filter" data-category="tv" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide TV shows</a></li> <li class="js-film-filter divider-line -inset" data-category="docs" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide documentaries</a></li> <li class="js-film-filter divider-line -inset" data-category="unreleased" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide unreleased titles</a></li> <li class="js-film-filter divider-line -inset" data-category="obscure" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show obscure films</a></li> <li class="js-film-filter" data-category="obscure" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide obscure films</a></li> <li class="js-film-filter divider-line -inset" data-category="backdropped" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films with backdrop</a></li> <li class="js-film-filter" data-category="backdropped" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films with backdrop</a></li> <li class="js-film-filter divider-line -inset" data-category="nanocrowd" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show Nanocrowd films</a></li> <li class="js-film-filter" data-category="nanocrowd" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide Nanocrowd films</a></li> </ul> </li> </ul> </div> </section> <section class="smenu-wrapper"> <strong class="smenu-label">Sort by</strong> <div class="smenu"> <label>Release Date<i class="ir s icon"></i></label> <ul class="smenu-menu"> <li class=""><a class="item" href="/mrafee113/films/by/name/">Film Name</a></li> <li class=""><a class="item" href="/mrafee113/films/by/popular/">Film Popularity</a></li> <li class=""><a class="item" href="/mrafee113/films/by/shuffle/">Shuffle</a></li> <li class=""><span class="smenu-sublabel">When Added</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/date/">Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/date-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">When Rated</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/rated-date/">Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/rated-date-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Release Date</span> <ul> <li class=" smenu-subselected"><a class="item" href="/mrafee113/films/"><i class="ir s icon"></i>Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/release-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Average Rating</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/rating/">Highest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/rating-lowest/">Lowest First</a></li> </ul></li> <li class="" data-owner="mrafee113"><span class="smenu-sublabel" data-owner="mrafee113" data-owner-label="Your Rating">Mehdi’s Rating</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/entry-rating/">Highest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/entry-rating-lowest/">Lowest First</a></li> </ul></li> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><span class="smenu-sublabel">Your Rating</span> <ul> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><a class="item" href="/mrafee113/films/by/your-rating/">Highest First</a></li> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><a class="item" href="/mrafee113/films/by/your-rating-lowest/">Lowest First</a></li> </ul></li> <li class=" show-when-logged-in"><span class="smenu-sublabel">Your Interests</span> <ul> <li class=" show-when-logged-in"><a class="item" href="/mrafee113/films/by/your-interest-liked/">Based on films you liked</a></li> <li class=" show-when-logged-in"><a class="item" href="/mrafee113/films/by/your-interest-related/">Related to films you liked</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Film Length</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/shortest/">Shortest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/longest/">Longest First</a></li> </ul></li> </ul> </div> </section> \n<section class="smenu-wrapper"> <div class="smenu"> <label>Service<i class="ir s icon"></i></label> <ul id="services-menu" class="smenu-menu" data-upgrade-url="/pro/"> <li class="availability- smenu-subselected"> <span class="selected"> All films </span> </li> <li class="divider-line availability-amazon"> <a class="item" href="/mrafee113/films/on/amazon-deu/"> Amazon DE </a> </li> <li class="availability-amazon-video"> <a class="item" href="/mrafee113/films/on/amazon-video-de/"> Amazon Video DE </a> </li> <li class="availability-apple-tv-plus"> <a class="item" href="/mrafee113/films/on/apple-tv-plus-de/"> Apple TV Plus DE </a> </li> <li class="availability-apple-itunes"> <a class="item" href="/mrafee113/films/on/apple-itunes-de/"> iTunes DE </a> </li> <li class="note divider-line -upgrade"> <p>Upgrade to a <a href="/pro/">Letterboxd <span class="badge -pro -small">Pro</span></a> account to add your favorite services to this list—including any service and country pair listed on JustWatch—and to enable one-click filtering by all your favorites.</p></li> <li><a class="item item-small" href="https://www.justwatch.com" target="_blank" rel="noopener noreferrer"><small>Powered by JustWatch</small></a></li> </ul> </div> </section>\n <section class="smenu-wrapper"> <div class="smenu"> <label> Genre<i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><span class="selected">Any genre</span></li> <li class="divider-line"> <ul> <li class=""><a class="item" href="/mrafee113/films/genre/action/"><i class="ir s icon"></i>Action</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/adventure/"><i class="ir s icon"></i>Adventure</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/animation/"><i class="ir s icon"></i>Animation</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/comedy/"><i class="ir s icon"></i>Comedy</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/crime/"><i class="ir s icon"></i>Crime</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/documentary/"><i class="ir s icon"></i>Documentary</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/drama/"><i class="ir s icon"></i>Drama</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/family/"><i class="ir s icon"></i>Family</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/fantasy/"><i class="ir s icon"></i>Fantasy</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/history/"><i class="ir s icon"></i>History</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/horror/"><i class="ir s icon"></i>Horror</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/music/"><i class="ir s icon"></i>Music</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/mystery/"><i class="ir s icon"></i>Mystery</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/romance/"><i class="ir s icon"></i>Romance</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/science-fiction/"><i class="ir s icon"></i>Science Fiction</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/thriller/"><i class="ir s icon"></i>Thriller</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/tv-movie/"><i class="ir s icon"></i>TV Movie</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/war/"><i class="ir s icon"></i>War</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/western/"><i class="ir s icon"></i>Western</a></li> </ul> </li> </ul> </div> </section> <section class="smenu-wrapper"> <div class="smenu"> <label class="x"> Decade<i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><span class="selected">Any decade</span></li> <li class="divider-line "><a class="item" href="/mrafee113/films/decade/2020s/">2020s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/2010s/">2010s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/2000s/">2000s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1990s/">1990s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1980s/">1980s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1970s/">1970s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1960s/">1960s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1950s/">1950s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1940s/">1940s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1930s/">1930s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1920s/">1920s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1910s/">1910s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1900s/">1900s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1890s/">1890s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1880s/">1880s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1870s/">1870s</a></li> </ul> </div> </section> <section class="smenu-wrapper"> <div class="smenu"> <label> Rating <i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><a class="item" href="/mrafee113/films/">Any rating</a></li> <li><a class="item" href="/mrafee113/films/rated/none/">No rating</a></li> <li class="divider-line"> <span class="smenu-sublabel -uppercase">Rating (or range)</span> <div class="menu-rating-filter js-rating-filter" data-rateit-starwidth="10" data-rateit-starheight="19" data-action="/mrafee113/films/rated/%7B%7Bvalue%7D%7D/"> <div class="rateit-range"> <div class="rateit-selected"></div> <div class="rateit-hover"></div> </div> </div> <small class="note">Drag to define range</small> </li> </ul> </div> </section> </div> <div class="clear"></div> </div>\n\t\n\t\t\n\n\t\n\t\t\n\t\t\t\t\n\n\t\t\t\t<ul class="poster-list -p70 -grid film-list clear">\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-726680 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="726680" data-film-slug="/film/mafia-mamma/" data-poster-url="/film/mafia-mamma/image-150/" data-linked="linked" data-target-link="/film/mafia-mamma/" data-target-link-target="" data-cache-busting-key="20289f53" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Mafia Mamma"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-998520 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="998520" data-film-slug="/film/louis-ck-at-the-dolby/" data-poster-url="/film/louis-ck-at-the-dolby/image-150/" data-linked="linked" data-target-link="/film/louis-ck-at-the-dolby/" data-target-link-target="" data-cache-busting-key="93b11804" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Louis C.K. at The Dolby"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-6">★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-575258 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="575258" data-film-slug="/film/renfield/" data-poster-url="/film/renfield/image-150/" data-linked="linked" data-target-link="/film/renfield/" data-target-link-target="" data-cache-busting-key="d129ad49" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Renfield"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-522405 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="522405" data-film-slug="/film/shazam-fury-of-the-gods/" data-poster-url="/film/shazam-fury-of-the-gods/image-150/" data-linked="linked" data-target-link="/film/shazam-fury-of-the-gods/" data-target-link-target="" data-cache-busting-key="1e7571ce" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Shazam! Fury of the Gods"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-424003 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="424003" data-film-slug="/film/dungeons-dragons-honor-among-thieves/" data-poster-url="/film/dungeons-dragons-honor-among-thieves/image-150/" data-linked="linked" data-target-link="/film/dungeons-dragons-honor-among-thieves/" data-target-link-target="" data-cache-busting-key="5c7797c4" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Dungeons & Dragons: Honor Among Thieves"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-838520 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="838520" data-film-slug="/film/champions-2023/" data-poster-url="/film/champions-2023/image-150/" data-linked="linked" data-target-link="/film/champions-2023/" data-target-link-target="" data-cache-busting-key="d119d8a2" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Champions"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-764596 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="764596" data-film-slug="/film/kill-boksoon/" data-poster-url="/film/kill-boksoon/image-150/" data-linked="linked" data-target-link="/film/kill-boksoon/" data-target-link-target="" data-cache-busting-key="280be804" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Kill Boksoon"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-566237 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="566237" data-film-slug="/film/ant-man-and-the-wasp-quantumania/" data-poster-url="/film/ant-man-and-the-wasp-quantumania/image-150/" data-linked="linked" data-target-link="/film/ant-man-and-the-wasp-quantumania/" data-target-link-target="" data-cache-busting-key="df5c617e" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ant-Man and the Wasp: Quantumania"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-558056 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="558056" data-film-slug="/film/knock-at-the-cabin/" data-poster-url="/film/knock-at-the-cabin/image-150/" data-linked="linked" data-target-link="/film/knock-at-the-cabin/" data-target-link-target="" data-cache-busting-key="2e6ced50" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Knock at the Cabin"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-733385 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="733385" data-film-slug="/film/mummies-2023/" data-poster-url="/film/mummies-2023/image-150/" data-linked="linked" data-target-link="/film/mummies-2023/" data-target-link-target="" data-cache-busting-key="fb56ca62" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Mummies"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-661153 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="661153" data-film-slug="/film/operation-fortune-ruse-de-guerre/" data-poster-url="/film/operation-fortune-ruse-de-guerre/image-150/" data-linked="linked" data-target-link="/film/operation-fortune-ruse-de-guerre/" data-target-link-target="" data-cache-busting-key="8d72bd57" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Operation Fortune: Ruse de Guerre"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-242285 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="242285" data-film-slug="/film/puss-in-boots-the-last-wish/" data-poster-url="/film/puss-in-boots-the-last-wish/image-150/" data-linked="linked" data-target-link="/film/puss-in-boots-the-last-wish/" data-target-link-target="" data-cache-busting-key="d60f4abc" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Puss in Boots: The Last Wish"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-789082 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="789082" data-film-slug="/film/strange-world-2022/" data-poster-url="/film/strange-world-2022/image-150/" data-linked="linked" data-target-link="/film/strange-world-2022/" data-target-link-target="" data-cache-busting-key="8df8311d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Strange World"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-744826 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="744826" data-film-slug="/film/enola-holmes-2/" data-poster-url="/film/enola-holmes-2/image-150/" data-linked="linked" data-target-link="/film/enola-holmes-2/" data-target-link-target="" data-cache-busting-key="0b05f98f" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Enola Holmes 2"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-435460 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="435460" data-film-slug="/film/black-panther-wakanda-forever/" data-poster-url="/film/black-panther-wakanda-forever/image-150/" data-linked="linked" data-target-link="/film/black-panther-wakanda-forever/" data-target-link-target="" data-cache-busting-key="87412ddf" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Black Panther: Wakanda Forever"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-589317 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="589317" data-film-slug="/film/amsterdam-2022/" data-poster-url="/film/amsterdam-2022/image-150/" data-linked="linked" data-target-link="/film/amsterdam-2022/" data-target-link-target="" data-cache-busting-key="85997eb0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Amsterdam"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-647390 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="647390" data-film-slug="/film/confess-fletch/" data-poster-url="/film/confess-fletch/image-150/" data-linked="linked" data-target-link="/film/confess-fletch/" data-target-link-target="" data-cache-busting-key="88144a94" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Confess, Fletch"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-441474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="441474" data-film-slug="/film/wendell-wild/" data-poster-url="/film/wendell-wild/image-150/" data-linked="linked" data-target-link="/film/wendell-wild/" data-target-link-target="" data-cache-busting-key="8e24544c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Wendell & Wild"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-523109 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="523109" data-film-slug="/film/causeway/" data-poster-url="/film/causeway/image-150/" data-linked="linked" data-target-link="/film/causeway/" data-target-link-target="" data-cache-busting-key="870478ea" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Causeway"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-721288 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="721288" data-film-slug="/film/the-fabelmans/" data-poster-url="/film/the-fabelmans/image-150/" data-linked="linked" data-target-link="/film/the-fabelmans/" data-target-link-target="" data-cache-busting-key="0dba11a7" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Fabelmans"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-521323 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="521323" data-film-slug="/film/the-menu-2022/" data-poster-url="/film/the-menu-2022/image-150/" data-linked="linked" data-target-link="/film/the-menu-2022/" data-target-link-target="" data-cache-busting-key="8e7be729" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Menu"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-9">★★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-586723 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="586723" data-film-slug="/film/glass-onion/" data-poster-url="/film/glass-onion/image-150/" data-linked="linked" data-target-link="/film/glass-onion/" data-target-link-target="" data-cache-busting-key="304e3660" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Glass Onion"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-820461 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="820461" data-film-slug="/film/the-lost-king/" data-poster-url="/film/the-lost-king/image-150/" data-linked="linked" data-target-link="/film/the-lost-king/" data-target-link-target="" data-cache-busting-key="864fbd75" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Lost King"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-686510 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="686510" data-film-slug="/film/see-how-they-run-2022/" data-poster-url="/film/see-how-they-run-2022/image-150/" data-linked="linked" data-target-link="/film/see-how-they-run-2022/" data-target-link-target="" data-cache-busting-key="8a569c44" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="See How They Run"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-462030 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="462030" data-film-slug="/film/pinocchio-2022/" data-poster-url="/film/pinocchio-2022/image-150/" data-linked="linked" data-target-link="/film/pinocchio-2022/" data-target-link-target="" data-cache-busting-key="beb0d10e" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Pinocchio"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-598882 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="598882" data-film-slug="/film/the-banshees-of-inisherin/" data-poster-url="/film/the-banshees-of-inisherin/image-150/" data-linked="linked" data-target-link="/film/the-banshees-of-inisherin/" data-target-link-target="" data-cache-busting-key="03be9e08" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Banshees of Inisherin"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-734096 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="734096" data-film-slug="/film/tar-2022/" data-poster-url="/film/tar-2022/image-150/" data-linked="linked" data-target-link="/film/tar-2022/" data-target-link-target="" data-cache-busting-key="8caea6a3" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="TÁR"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-666269 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="666269" data-film-slug="/film/white-noise-2022/" data-poster-url="/film/white-noise-2022/image-150/" data-linked="linked" data-target-link="/film/white-noise-2022/" data-target-link-target="" data-cache-busting-key="093db78d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="White Noise"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-676215 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="676215" data-film-slug="/film/day-shift-2022/" data-poster-url="/film/day-shift-2022/image-150/" data-linked="linked" data-target-link="/film/day-shift-2022/" data-target-link-target="" data-cache-busting-key="8097de58" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Day Shift"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-811153 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="811153" data-film-slug="/film/one-piece-film-red/" data-poster-url="/film/one-piece-film-red/image-150/" data-linked="linked" data-target-link="/film/one-piece-film-red/" data-target-link-target="" data-cache-busting-key="093156e5" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="One Piece Film Red"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-647760 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="647760" data-film-slug="/film/the-gray-man-2022/" data-poster-url="/film/the-gray-man-2022/image-150/" data-linked="linked" data-target-link="/film/the-gray-man-2022/" data-target-link-target="" data-cache-busting-key="81ba2f7b" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Gray Man"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-641961 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="641961" data-film-slug="/film/bullet-train/" data-poster-url="/film/bullet-train/image-150/" data-linked="linked" data-target-link="/film/bullet-train/" data-target-link-target="" data-cache-busting-key="0a859e26" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Bullet Train"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-7">★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-371005 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="371005" data-film-slug="/film/minions-the-rise-of-gru/" data-poster-url="/film/minions-the-rise-of-gru/image-150/" data-linked="linked" data-target-link="/film/minions-the-rise-of-gru/" data-target-link-target="" data-cache-busting-key="8a9ee32a" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Minions: The Rise of Gru"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-592465 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="592465" data-film-slug="/film/the-man-from-toronto-2022/" data-poster-url="/film/the-man-from-toronto-2022/image-150/" data-linked="linked" data-target-link="/film/the-man-from-toronto-2022/" data-target-link-target="" data-cache-busting-key="0477e5e9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Man from Toronto"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-543002 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="543002" data-film-slug="/film/thor-love-and-thunder/" data-poster-url="/film/thor-love-and-thunder/image-150/" data-linked="linked" data-target-link="/film/thor-love-and-thunder/" data-target-link-target="" data-cache-busting-key="84638312" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Thor: Love and Thunder"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-878873 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="878873" data-film-slug="/film/vesper-2022/" data-poster-url="/film/vesper-2022/image-150/" data-linked="linked" data-target-link="/film/vesper-2022/" data-target-link-target="" data-cache-busting-key="0317ad27" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Vesper"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-488592 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="488592" data-film-slug="/film/the-sea-beast-2022/" data-poster-url="/film/the-sea-beast-2022/image-150/" data-linked="linked" data-target-link="/film/the-sea-beast-2022/" data-target-link-target="" data-cache-busting-key="8dce9a04" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Sea Beast"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-607401 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="607401" data-film-slug="/film/vengeance-2022/" data-poster-url="/film/vengeance-2022/image-150/" data-linked="linked" data-target-link="/film/vengeance-2022/" data-target-link-target="" data-cache-busting-key="04dc3f16" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Vengeance"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-641574 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="641574" data-film-slug="/film/lightyear-2022/" data-poster-url="/film/lightyear-2022/image-150/" data-linked="linked" data-target-link="/film/lightyear-2022/" data-target-link-target="" data-cache-busting-key="0d45b6f6" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Lightyear"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-812015 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="812015" data-film-slug="/film/close-2022/" data-poster-url="/film/close-2022/image-150/" data-linked="linked" data-target-link="/film/close-2022/" data-target-link-target="" data-cache-busting-key="8ac6ce80" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Close"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-8">★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-875860 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="875860" data-film-slug="/film/ricky-gervais-supernature/" data-poster-url="/film/ricky-gervais-supernature/image-150/" data-linked="linked" data-target-link="/film/ricky-gervais-supernature/" data-target-link-target="" data-cache-busting-key="8c13daef" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ricky Gervais: SuperNature"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-736318 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="736318" data-film-slug="/film/crimes-of-the-future-2022/" data-poster-url="/film/crimes-of-the-future-2022/image-150/" data-linked="linked" data-target-link="/film/crimes-of-the-future-2022/" data-target-link-target="" data-cache-busting-key="8331ef2f" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Crimes of the Future"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-427970 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="427970" data-film-slug="/film/triangle-of-sadness/" data-poster-url="/film/triangle-of-sadness/image-150/" data-linked="linked" data-target-link="/film/triangle-of-sadness/" data-target-link-target="" data-cache-busting-key="8e1eb744" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Triangle of Sadness"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-669198 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="669198" data-film-slug="/film/one-fine-morning-2022/" data-poster-url="/film/one-fine-morning-2022/image-150/" data-linked="linked" data-target-link="/film/one-fine-morning-2022/" data-target-link-target="" data-cache-busting-key="0280d483" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="One Fine Morning"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-485265 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="485265" data-film-slug="/film/three-thousand-years-of-longing/" data-poster-url="/film/three-thousand-years-of-longing/image-150/" data-linked="linked" data-target-link="/film/three-thousand-years-of-longing/" data-target-link-target="" data-cache-busting-key="0c21e1b7" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Three Thousand Years of Longing"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-385511 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="385511" data-film-slug="/film/doctor-strange-in-the-multiverse-of-madness/" data-poster-url="/film/doctor-strange-in-the-multiverse-of-madness/image-150/" data-linked="linked" data-target-link="/film/doctor-strange-in-the-multiverse-of-madness/" data-target-link-target="" data-cache-busting-key="81a4fea9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Doctor Strange in the Multiverse of Madness"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-565852 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="565852" data-film-slug="/film/the-northman/" data-poster-url="/film/the-northman/image-150/" data-linked="linked" data-target-link="/film/the-northman/" data-target-link-target="" data-cache-busting-key="08820bd4" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Northman"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-456327 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="456327" data-film-slug="/film/morbius/" data-poster-url="/film/morbius/image-150/" data-linked="linked" data-target-link="/film/morbius/" data-target-link-target="" data-cache-busting-key="084000b9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Morbius"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-683285 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="683285" data-film-slug="/film/ambulance-2022/" data-poster-url="/film/ambulance-2022/image-150/" data-linked="linked" data-target-link="/film/ambulance-2022/" data-target-link-target="" data-cache-busting-key="02c94c2c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ambulance"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-574385 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="574385" data-film-slug="/film/the-unbearable-weight-of-massive-talent/" data-poster-url="/film/the-unbearable-weight-of-massive-talent/image-150/" data-linked="linked" data-target-link="/film/the-unbearable-weight-of-massive-talent/" data-target-link-target="" data-cache-busting-key="8992593c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Unbearable Weight of Massive Talent"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-673474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="673474" data-film-slug="/film/the-lost-city-2022/" data-poster-url="/film/the-lost-city-2022/image-150/" data-linked="linked" data-target-link="/film/the-lost-city-2022/" data-target-link-target="" data-cache-busting-key="87db30cd" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Lost City"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-474474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="474474" data-film-slug="/film/everything-everywhere-all-at-once/" data-poster-url="/film/everything-everywhere-all-at-once/image-150/" data-linked="linked" data-target-link="/film/everything-everywhere-all-at-once/" data-target-link-target="" data-cache-busting-key="80fbb370" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Everything Everywhere All at Once"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-438727 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="438727" data-film-slug="/film/turning-red/" data-poster-url="/film/turning-red/image-150/" data-linked="linked" data-target-link="/film/turning-red/" data-target-link-target="" data-cache-busting-key="0d037915" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Turning Red"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-620665 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="620665" data-film-slug="/film/the-adam-project/" data-poster-url="/film/the-adam-project/image-150/" data-linked="linked" data-target-link="/film/the-adam-project/" data-target-link-target="" data-cache-busting-key="8f04f942" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Adam Project"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-348914 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="348914" data-film-slug="/film/the-batman/" data-poster-url="/film/the-batman/image-150/" data-linked="linked" data-target-link="/film/the-batman/" data-target-link-target="" data-cache-busting-key="0438ab74" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Batman"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-264328 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="264328" data-film-slug="/film/uncharted-2022/" data-poster-url="/film/uncharted-2022/image-150/" data-linked="linked" data-target-link="/film/uncharted-2022/" data-target-link-target="" data-cache-busting-key="8c645cbf" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Uncharted"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-434913 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="434913" data-film-slug="/film/death-on-the-nile-2022/" data-poster-url="/film/death-on-the-nile-2022/image-150/" data-linked="linked" data-target-link="/film/death-on-the-nile-2022/" data-target-link-target="" data-cache-busting-key="8228a9e0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Death on the Nile"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-777185 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="777185" data-film-slug="/film/emily-the-criminal/" data-poster-url="/film/emily-the-criminal/image-150/" data-linked="linked" data-target-link="/film/emily-the-criminal/" data-target-link-target="" data-cache-busting-key="03df984d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Emily the Criminal"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-680635 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="680635" data-film-slug="/film/living-2022/" data-poster-url="/film/living-2022/image-150/" data-linked="linked" data-target-link="/film/living-2022/" data-target-link-target="" data-cache-busting-key="8db883ac" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Living"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-719315 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="719315" data-film-slug="/film/breaking-2022/" data-poster-url="/film/breaking-2022/image-150/" data-linked="linked" data-target-link="/film/breaking-2022/" data-target-link-target="" data-cache-busting-key="829c2ff0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Breaking"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-735545 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="735545" data-film-slug="/film/emergency-2022/" data-poster-url="/film/emergency-2022/image-150/" data-linked="linked" data-target-link="/film/emergency-2022/" data-target-link-target="" data-cache-busting-key="0a2a26ab" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Emergency"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-823432 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="823432" data-film-slug="/film/louis-ck-sorry-2021/" data-poster-url="/film/louis-ck-sorry-2021/image-150/" data-linked="linked" data-target-link="/film/louis-ck-sorry-2021/" data-target-link-target="" data-cache-busting-key="04941a73" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Louis C.K.: Sorry"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-6">★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-551275 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="551275" data-film-slug="/film/the-matrix-resurrections/" data-poster-url="/film/the-matrix-resurrections/image-150/" data-linked="linked" data-target-link="/film/the-matrix-resurrections/" data-target-link-target="" data-cache-busting-key="0d576ce2" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Matrix Resurrections"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-572255 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="572255" data-film-slug="/film/dont-look-up-2021/" data-poster-url="/film/dont-look-up-2021/image-150/" data-linked="linked" data-target-link="/film/dont-look-up-2021/" data-target-link-target="" data-cache-busting-key="8a7a1c92" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Don\'t Look Up"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-571629 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="571629" data-film-slug="/film/the-unforgivable/" data-poster-url="/film/the-unforgivable/image-150/" data-linked="linked" data-target-link="/film/the-unforgivable/" data-target-link-target="" data-cache-busting-key="8fd1eb25" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Unforgivable"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-9">★★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-466291 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="466291" data-film-slug="/film/tick-tick-boom-2021/" data-poster-url="/film/tick-tick-boom-2021/image-150/" data-linked="linked" data-target-link="/film/tick-tick-boom-2021/" data-target-link-target="" data-cache-busting-key="071f7a54" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="tick, tick...BOOM!"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-441858 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="441858" data-film-slug="/film/red-notice/" data-poster-url="/film/red-notice/image-150/" data-linked="linked" data-target-link="/film/red-notice/" data-target-link-target="" data-cache-busting-key="0ef37870" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Red Notice"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-714279 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="714279" data-film-slug="/film/army-of-thieves/" data-poster-url="/film/army-of-thieves/image-150/" data-linked="linked" data-target-link="/film/army-of-thieves/" data-target-link-target="" data-cache-busting-key="0deeede3" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Army of Thieves"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-454016 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="454016" data-film-slug="/film/eternals/" data-poster-url="/film/eternals/image-150/" data-linked="linked" data-target-link="/film/eternals/" data-target-link-target="" data-cache-busting-key="0a67ea1a" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Eternals"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-496592 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="496592" data-film-slug="/film/encanto/" data-poster-url="/film/encanto/image-150/" data-linked="linked" data-target-link="/film/encanto/" data-target-link-target="" data-cache-busting-key="8d86b9e5" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Encanto"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-544936 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="544936" data-film-slug="/film/the-harder-they-fall-2021/" data-poster-url="/film/the-harder-they-fall-2021/image-150/" data-linked="linked" data-target-link="/film/the-harder-they-fall-2021/" data-target-link-target="" data-cache-busting-key="863a9c16" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Harder They Fall"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-790798 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="790798" data-film-slug="/film/dave-chappelle-the-closer/" data-poster-url="/film/dave-chappelle-the-closer/image-150/" data-linked="linked" data-target-link="/film/dave-chappelle-the-closer/" data-target-link-target="" data-cache-busting-key="04f75162" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Dave Chappelle: The Closer"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t</ul>\n\t\t\t\t<div class="pagination"> <div class="paginate-nextprev paginate-disabled"><span class="previous">Newer</span></div> <div class="paginate-nextprev"><a class="next" href="/mrafee113/films/page/2/">Older</a></div> <div class="paginate-pages"> <ul> <li class="paginate-page paginate-current"><span>1</span></li> <li class="paginate-page"><a href="/mrafee113/films/page/2/">2</a></li> <li class="paginate-page"><a href="/mrafee113/films/page/3/">3</a></li> <li class="paginate-page unseen-pages">&hellip;</li> <li class="paginate-page"><a href="/mrafee113/films/page/10/">10</a></li> </ul> </div> </div>\n\t\t\t\n\t\t<div class="clear"></div>\n\t</section>\n\t\n\t<div class="clear"></div>\n\t\n</div>\n\n\n\n\n\n\n\n\n\n\n\t\t</div> \n\n\t\t\n\n\t</div> \n\n\n\n\t<footer id="page-footer" class="page-footer js-page-footer js-hide-in-app">\n\t\t<div class="content-wrap">\n\t\t\t\n\t\t\t\t<nav class="footer-nav js-footer-nav">\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li><a href="/about/">About</a></li>\n\t\t\t\t\t\t<li><a href="/journal/">News</a></li>\n\t\t\t\t\t\t<li class="js-hide-in-app"><a href="/pro/">Pro</a></li>\n\t\t\t\t\t\t<li><a href="/apps/">Apps</a></li>\n\t\t\t\t\t\t<li><a href="https://apple.co/3TfzHVG" target="_blank" rel="noopener noreferrer">Podcast</a></li>\n\t\t\t\t\t\t<li><a href="/year-in-review/">Year in Review</a></li>\n\t\t\t\t\t\t<li><a href="/gift-guide/">Gift Guide</a></li>\n\t\t\t\t\t\t<li><a href="/welcome/">Help</a></li>\n\t\t\t\t\t\t<li><a href="/legal/terms-of-use/">Terms</a></li>\n\t\t\t\t\t\t<li><a href="/api-beta/">API</a></li>\n\t\t\t\t\t\t<li><a href="/contact/">Contact</a></li>\n\t\t\t\t\t</ul>\n\t\t\t\t</nav>\n\t\n\n\t\t\t<div class="socials">\n\t\t\t\t<nav class="social-service-list -inline">\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://twitter.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Twitter">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="20" height="16" xmlns="http://www.w3.org/2000/svg"><path d="M17.96 4.51V4c.8-.56 1.49-1.28 2.04-2.1-.74.33-1.53.54-2.36.65.85-.5 1.5-1.3 1.8-2.24-.78.46-1.66.8-2.6.98a4.13 4.13 0 0 0-7.1 2.76c0 .31.04.62.1.92A11.72 11.72 0 0 1 1.38.74a3.99 3.99 0 0 0 1.28 5.4A4.2 4.2 0 0 1 .8 5.62v.06c0 1.95 1.42 3.59 3.29 3.96a4.06 4.06 0 0 1-1.85.07 4.1 4.1 0 0 0 3.83 2.8A8.32 8.32 0 0 1 0 14.2C1.8 15.33 3.97 16 6.28 16A11.5 11.5 0 0 0 17.96 4.51Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Twitter</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.facebook.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Facebook">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="19" height="19" xmlns="http://www.w3.org/2000/svg"><path d="M9.5 0a9.5 9.5 0 0 0-1.48 18.89V12H5.6V9.25h2.42V7.41c0-2.38 1.41-3.7 3.58-3.7 1.04 0 2.13.19 2.13.19v2.33h-1.2c-1.18 0-1.54.74-1.54 1.49v1.53h2.63L13.2 12h-2.21v6.89A9.5 9.5 0 0 0 9.5 0Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Facebook</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.instagram.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Instagram">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="20" height="20" xmlns="http://www.w3.org/2000/svg"><path d="M14.12.06c1.07.05 1.8.22 2.43.46.66.26 1.21.6 1.77 1.16.56.55.9 1.11 1.15 1.77.25.63.42 1.36.47 2.43.04.94.06 1.32.06 3.3v1.37c0 1.54 0 2.19-.03 2.77v.22l-.03.58a7.34 7.34 0 0 1-.47 2.43 4.9 4.9 0 0 1-1.15 1.77 4.9 4.9 0 0 1-1.77 1.16c-.64.24-1.36.41-2.43.46l-.61.03h-.23c-.5.02-1.06.03-2.21.03H9.2c-2 0-2.37-.02-3.32-.06a7.34 7.34 0 0 1-2.43-.46 4.9 4.9 0 0 1-1.77-1.16 4.9 4.9 0 0 1-1.16-1.77 7.34 7.34 0 0 1-.46-2.43l-.03-.61v-.2A60.9 60.9 0 0 1 0 11.5V8.75C0 7.7.01 7.17.03 6.7v-.2l.03-.61C.1 4.8.28 4.08.52 3.45a4.9 4.9 0 0 1 1.16-1.77A4.9 4.9 0 0 1 3.45.52 7.34 7.34 0 0 1 5.88.06l.61-.03h.2C7.12 0 7.6 0 8.5 0h2.74c1.62 0 2 .02 2.88.06ZM11.02 2H8.97c-1.7 0-2.05.02-2.92.06a5.4 5.4 0 0 0-1.82.33c-.45.18-.78.39-1.12.73-.34.34-.55.67-.73 1.12-.13.35-.3.86-.33 1.82C2.02 6.93 2 7.29 2 8.98v2.04c0 1.7.02 2.05.06 2.92.04.95.2 1.47.33 1.81.18.46.39.78.73 1.13.34.34.67.55 1.12.73.35.13.86.29 1.82.33.83.04 1.2.05 2.7.06h2.47c1.51 0 1.87-.02 2.71-.06a5.4 5.4 0 0 0 1.81-.33c.46-.18.78-.4 1.12-.73.35-.35.56-.67.73-1.13.14-.34.3-.86.34-1.8a49 49 0 0 0 .06-2.72V8.77a49 49 0 0 0-.06-2.71 5.4 5.4 0 0 0-.34-1.82 3.02 3.02 0 0 0-.73-1.12 3.02 3.02 0 0 0-1.12-.73 5.4 5.4 0 0 0-1.81-.33c-.88-.04-1.23-.06-2.93-.06ZM10 4.86a5.14 5.14 0 1 1 0 10.28 5.14 5.14 0 0 1 0-10.28ZM10 7a3 3 0 1 0 0 6 3 3 0 0 0 0-6Zm5.25-3.5a1.25 1.25 0 1 1 0 2.5 1.25 1.25 0 0 1 0-2.5Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Instagram</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.tiktok.com/@letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on TikTok">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="17" height="18" xmlns="http://www.w3.org/2000/svg"><path d="M16.48 4.32a4.62 4.62 0 0 1-3.92-2.66A4.04 4.04 0 0 1 12.23 0H9.07v11.85c0 1.93-1.19 3.07-2.65 3.07a2.71 2.71 0 0 1-2.04-.9 2.57 2.57 0 0 1-.6-2.1 2.55 2.55 0 0 1 1.26-1.81 2.7 2.7 0 0 1 2.24-.21V6.77a5.92 5.92 0 0 0-4.08.86 5.7 5.7 0 0 0-2.15 2.55 5.53 5.53 0 0 0 1.26 6.16 5.86 5.86 0 0 0 6.33 1.23 5.78 5.78 0 0 0 2.6-2.08c.64-.94.98-2.03.98-3.15V5.96a7.74 7.74 0 0 0 4.25 1.25V4.32Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">TikTok</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.youtube.com/letterboxdhq" target="_blank" rel="noopener noreferrer" title="Letterboxd on YouTube">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="23" height="16" xmlns="http://www.w3.org/2000/svg"><path d="M11.74 0c.61 0 2.33.02 4.11.08l.54.02c1.7.06 3.35.18 4.1.38a2.87 2.87 0 0 1 2.03 2.02c.45 1.67.48 5.04.48 5.46v.08c0 .42-.03 3.8-.48 5.46a2.87 2.87 0 0 1-2.03 2.02c-.75.2-2.4.32-4.1.38l-.54.02c-1.78.07-3.5.08-4.11.08H11.26c-.62 0-2.33-.01-4.11-.08l-.54-.02c-1.7-.06-3.36-.18-4.1-.38A2.87 2.87 0 0 1 .48 13.5C.04 11.9 0 8.68 0 8.1v-.2c0-.58.04-3.79.48-5.4A2.87 2.87 0 0 1 2.5.48c.74-.2 2.4-.32 4.1-.38l.54-.02C8.93.02 10.65 0 11.26 0ZM9 4.57v6.86L15 8 9 4.57Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">YouTube</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\t\t\t\t</nav>\n\t\t\t</div>\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t<p class="copyright">\n\t\t\t\t&copy; Letterboxd Limited. Made by <a href="/crew/" class="mute">fans</a> in Aotearoa New Zealand.\n\t\t\t\t<span class="nobr"><a href="https://letterboxd.com/about/film-data/" class="mute">Film data</a> from <a href="https://www.themoviedb.org" class="mute">TMDb</a>. \n\t\t\t\t\n\t\t\t\t\t\t<a href="#" class="mute mobile-site-switch" data-use-mobile-site="yes">Mobile&nbsp;site</a>.\n\t\t\t\t\t\n\t</span>\n\t\t\t\t<span class="recap" style="display:none"><br/>This site is protected by reCAPTCHA and the Google <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer" class="mute">privacy policy</a> and <a href="https://policies.google.com/terms" target="_blank" rel="noopener noreferrer" class="mute">terms of service</a>&nbsp;apply.</span>\n\t\t\t</p>\n\t\t</div>\n\t</footer>\n\n\t<div id="remove-ads-modal" class="modal-neue fade" tabindex="-1" aria-labelledby="remove-ads-modal-title" aria-hidden="true">\n    <div class="modal-dialog -sm modal-dialog-centered">\n        <div class="modal-content">\n            <div class="modal-header">\n                <h5 class="modal-title" id="remove-ads-modal-title">Upgrade to remove&nbsp;ads</h5>\n                <button type="button" class="close" data-bs-dismiss="modal-neue" aria-label="Close">\n                    <svg class="glyph" width="16" height="16" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd" stroke-linecap="round" stroke="#000" stroke-width="2"><path d="m1 1 14 14M1 15 15 1"/></g></svg>\n                </button>\n            </div>\n            <div class="modal-body">\n                <div class="body-text -hero">\n                    <p>Letterboxd is an independent service created by a small team, and we rely mostly on the support of our members to maintain our site and apps. Please consider upgrading to a <a href="/pro/">Pro account</a>—for less than a couple bucks a month, you’ll get cool additional features like all-time and annual stats pages (<a href="https://letterboxd.com/jack/stats/">example</a>), the ability to select (and filter by) your favorite streaming services, and no ads!</p>\n                </div>\n            </div>\n            <div class="modal-footer">\n                <a href="/pro/" class="button -action button-action">Learn more about Pro</a>\n            </div>\n        </div>\n    </div>\n</div>\n\t\n\n\n\n\n\n\n<form id="poster-picker-modal" class="modal-neue fade poster-picker-modal" method="post" action="" novalidate="novalidate" tabindex="-1" role="dialog" aria-labelledby="poster-picker-modal-title" aria-hidden="true" data-bs-backdrop="static">\n    <div class="modal-dialog -lg modal-dialog-centered modal-dialog-scrollable">\n        <div class="modal-content">\n            <div class="modal-header">\n                <h5 class="modal-title" id="poster-picker-modal-title">Select your preferred poster</h5>\n                <button type="button" class="close" data-bs-dismiss="modal-neue" aria-label="Close">\n                    <svg class="glyph" width="16" height="16" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd" stroke-linecap="round" stroke="#000" stroke-width="2"><path d="m1 1 14 14M1 15 15 1"></path></g></svg>\n                </button>\n            </div>\n            <div class="modal-body">\n                <div id="poster-picker-b427140c-d820-493e-a8cf-bb50fce997b3" data-poster-picker-options=\'{"id": "b427140c-d820-493e-a8cf-bb50fce997b3"}\' data-js-target="poster-picker"></div>\n            </div>\n            <div class="modal-footer">\n                <div class="poster-picker-note">\n                    <div class="body-text -small">\n                        \n<p>Posters are sourced from <a href="https://www.themoviedb.org" target="_blank">TMDb</a> and <a href="https://posteritati.com" target="_blank">Posteritati</a>, and appear for you and visitors to your profile and content, depending on settings. <a href="https://letterboxd.com/journal/posterity-custom-posters/" target="_blank">Learn more.</a></p>\n\n                    </div>\n                </div>\n\n                <div class="poster-picker-controls" data-poster-picker-controls-for="b427140c-d820-493e-a8cf-bb50fce997b3">\n                    <div class="modal-action-group -center">\n                        <button class="button -destructive" type="button" data-js-trigger="reset" disabled><span class="label">Reset poster</span></button>\n                        <button class="button -action" type="submit" data-js-trigger="submit" disabled><span class="label">Save<span class="mob-hide"> changes</span></span></button>\n                    </div>\n                    \n                </div>\n            </div>\n        </div>\n    </div>\n</form>\n\t\n\t\n</body>\n</html>'

In [78]: 'Mafia' in inner_html
Out[78]: True

In [79]: doc = html.document_fromstring(response.content)

In [80]: doc.xpath(f'/html/body//li')
Out[80]: 
[<Element li at 0x7f09251004a0>,
 <Element li at 0x7f0925102ac0>,
 <Element li at 0x7f0925100220>,
 <Element li at 0x7f0925102b60>,
 <Element li at 0x7f092536f1f0>,
 <Element li at 0x7f092536eb10>,
 <Element li at 0x7f092536fb00>,
 <Element li at 0x7f092536d350>,
 <Element li at 0x7f092536cd10>,
 <Element li at 0x7f092536fe70>,
 <Element li at 0x7f092536fc90>,
 <Element li at 0x7f092536de40>,
 <Element li at 0x7f092536f5b0>,
 <Element li at 0x7f092536eb60>,
 <Element li at 0x7f092536fab0>,
 <Element li at 0x7f092536fb50>,
 <Element li at 0x7f092536f3d0>,
 <Element li at 0x7f092536c8b0>,
 <Element li at 0x7f092536f420>,
 <Element li at 0x7f092536e020>,
 <Element li at 0x7f092501e020>,
 <Element li at 0x7f092501e2f0>,
 <Element li at 0x7f092501e160>,
 <Element li at 0x7f092501e110>,
 <Element li at 0x7f092501e200>,
 <Element li at 0x7f092501e2a0>,
 <Element li at 0x7f092501e0c0>,
 <Element li at 0x7f092501e3e0>,
 <Element li at 0x7f092501e340>,
 <Element li at 0x7f092501e480>,
 <Element li at 0x7f092501e4d0>,
 <Element li at 0x7f092501e520>,
 <Element li at 0x7f092501e570>,
 <Element li at 0x7f092501e5c0>,
 <Element li at 0x7f092501e610>,
 <Element li at 0x7f092501e660>,
 <Element li at 0x7f092501e6b0>,
 <Element li at 0x7f092501e700>,
 <Element li at 0x7f092501e750>,
 <Element li at 0x7f092501e7a0>,
 <Element li at 0x7f092501e7f0>,
 <Element li at 0x7f092501e840>,
 <Element li at 0x7f092501e890>,
 <Element li at 0x7f092501e8e0>,
 <Element li at 0x7f092501e930>,
 <Element li at 0x7f092501e980>,
 <Element li at 0x7f092501e9d0>,
 <Element li at 0x7f092501ea20>,
 <Element li at 0x7f092501ea70>,
 <Element li at 0x7f092501eac0>,
 <Element li at 0x7f092501eb10>,
 <Element li at 0x7f092501eb60>,
 <Element li at 0x7f092501ebb0>,
 <Element li at 0x7f092501ec00>,
 <Element li at 0x7f092501ec50>,
 <Element li at 0x7f092501eca0>,
 <Element li at 0x7f092501ecf0>,
 <Element li at 0x7f092501ed40>,
 <Element li at 0x7f092501ed90>,
 <Element li at 0x7f092501ede0>,
 <Element li at 0x7f092501ee30>,
 <Element li at 0x7f092501ee80>,
 <Element li at 0x7f092501eed0>,
 <Element li at 0x7f092501ef20>,
 <Element li at 0x7f092501ef70>,
 <Element li at 0x7f092501efc0>,
 <Element li at 0x7f092501f010>,
 <Element li at 0x7f092501f060>,
 <Element li at 0x7f092501f0b0>,
 <Element li at 0x7f092501f100>,
 <Element li at 0x7f092501f150>,
 <Element li at 0x7f092501f1a0>,
 <Element li at 0x7f092501f1f0>,
 <Element li at 0x7f092501f240>,
 <Element li at 0x7f092501f290>,
 <Element li at 0x7f092501f2e0>,
 <Element li at 0x7f092501f330>,
 <Element li at 0x7f092501f380>,
 <Element li at 0x7f092501f3d0>,
 <Element li at 0x7f092501f420>,
 <Element li at 0x7f092501f470>,
 <Element li at 0x7f092501f4c0>,
 <Element li at 0x7f092501f510>,
 <Element li at 0x7f092501f560>,
 <Element li at 0x7f092501f5b0>,
 <Element li at 0x7f092501f600>,
 <Element li at 0x7f092501f650>,
 <Element li at 0x7f092501f6a0>,
 <Element li at 0x7f092501f6f0>,
 <Element li at 0x7f092501f740>,
 <Element li at 0x7f092501f790>,
 <Element li at 0x7f092501f7e0>,
 <Element li at 0x7f092501f830>,
 <Element li at 0x7f092501f880>,
 <Element li at 0x7f092501f8d0>,
 <Element li at 0x7f092501f920>,
 <Element li at 0x7f092501f970>,
 <Element li at 0x7f092501f9c0>,
 <Element li at 0x7f092501fa10>,
 <Element li at 0x7f092501fa60>,
 <Element li at 0x7f092501fab0>,
 <Element li at 0x7f092501fb00>,
 <Element li at 0x7f092501fb50>,
 <Element li at 0x7f092501fba0>,
 <Element li at 0x7f092501fbf0>,
 <Element li at 0x7f092501fc40>,
 <Element li at 0x7f092501fc90>,
 <Element li at 0x7f092501fce0>,
 <Element li at 0x7f092501fd30>,
 <Element li at 0x7f092501fd80>,
 <Element li at 0x7f092501fdd0>,
 <Element li at 0x7f092501fe20>,
 <Element li at 0x7f092501fe70>,
 <Element li at 0x7f092501fec0>,
 <Element li at 0x7f092501ff10>,
 <Element li at 0x7f092501ff60>,
 <Element li at 0x7f092501ffb0>,
 <Element li at 0x7f092504c040>,
 <Element li at 0x7f092504c090>,
 <Element li at 0x7f092504c0e0>,
 <Element li at 0x7f092504c130>,
 <Element li at 0x7f092504c180>,
 <Element li at 0x7f092504c1d0>,
 <Element li at 0x7f092504c220>,
 <Element li at 0x7f092504c270>,
 <Element li at 0x7f092504c2c0>,
 <Element li at 0x7f092504c310>,
 <Element li at 0x7f092504c360>,
 <Element li at 0x7f092504c3b0>,
 <Element li at 0x7f092504c400>,
 <Element li at 0x7f092504c450>,
 <Element li at 0x7f092504c4a0>,
 <Element li at 0x7f092504c4f0>,
 <Element li at 0x7f092504c540>,
 <Element li at 0x7f092504c590>,
 <Element li at 0x7f092504c5e0>,
 <Element li at 0x7f092504c630>,
 <Element li at 0x7f092504c680>,
 <Element li at 0x7f092504c6d0>,
 <Element li at 0x7f092504c720>,
 <Element li at 0x7f092504c770>,
 <Element li at 0x7f092504c7c0>,
 <Element li at 0x7f092504c810>,
 <Element li at 0x7f092504c860>,
 <Element li at 0x7f092504c8b0>,
 <Element li at 0x7f092504c900>,
 <Element li at 0x7f092504c950>,
 <Element li at 0x7f092504c9a0>,
 <Element li at 0x7f092504c9f0>,
 <Element li at 0x7f092504ca40>,
 <Element li at 0x7f092504ca90>,
 <Element li at 0x7f092504cae0>,
 <Element li at 0x7f092504cb30>,
 <Element li at 0x7f092504cb80>,
 <Element li at 0x7f092504cbd0>,
 <Element li at 0x7f092504cc20>,
 <Element li at 0x7f092504cc70>,
 <Element li at 0x7f092504ccc0>,
 <Element li at 0x7f092504cd10>,
 <Element li at 0x7f092504cd60>,
 <Element li at 0x7f092504cdb0>,
 <Element li at 0x7f092504ce00>,
 <Element li at 0x7f092504ce50>,
 <Element li at 0x7f092504cea0>,
 <Element li at 0x7f092504cef0>,
 <Element li at 0x7f092504cf40>,
 <Element li at 0x7f092504cf90>,
 <Element li at 0x7f092504cfe0>,
 <Element li at 0x7f092504d030>,
 <Element li at 0x7f092504d080>,
 <Element li at 0x7f092504d0d0>,
 <Element li at 0x7f092504d120>,
 <Element li at 0x7f092504d170>,
 <Element li at 0x7f092504d1c0>,
 <Element li at 0x7f092504d210>,
 <Element li at 0x7f092504d260>,
 <Element li at 0x7f092504d2b0>,
 <Element li at 0x7f092504d300>,
 <Element li at 0x7f092504d350>,
 <Element li at 0x7f092504d3a0>,
 <Element li at 0x7f092504d3f0>,
 <Element li at 0x7f092504d440>,
 <Element li at 0x7f092504d490>,
 <Element li at 0x7f092504d4e0>,
 <Element li at 0x7f092504d530>,
 <Element li at 0x7f092504d580>,
 <Element li at 0x7f092504d5d0>,
 <Element li at 0x7f092504d620>,
 <Element li at 0x7f092504d670>,
 <Element li at 0x7f092504d6c0>,
 <Element li at 0x7f092504d710>,
 <Element li at 0x7f092504d760>,
 <Element li at 0x7f092504d7b0>,
 <Element li at 0x7f092504d800>,
 <Element li at 0x7f092504d850>,
 <Element li at 0x7f092504d8a0>,
 <Element li at 0x7f092504d8f0>,
 <Element li at 0x7f092504d940>,
 <Element li at 0x7f092504d990>,
 <Element li at 0x7f092504d9e0>,
 <Element li at 0x7f092504da30>,
 <Element li at 0x7f092504da80>,
 <Element li at 0x7f092504dad0>,
 <Element li at 0x7f092504db20>,
 <Element li at 0x7f092504db70>,
 <Element li at 0x7f092504dbc0>,
 <Element li at 0x7f092504dc10>,
 <Element li at 0x7f092504dc60>,
 <Element li at 0x7f092504dcb0>,
 <Element li at 0x7f092504dd00>,
 <Element li at 0x7f092504dd50>,
 <Element li at 0x7f092504dda0>,
 <Element li at 0x7f092504ddf0>,
 <Element li at 0x7f092504de40>,
 <Element li at 0x7f092504de90>,
 <Element li at 0x7f092504dee0>]

In [81]: doc.xpath(f'/html/body//li[@class="poster-container film-watched"]')
Out[81]: []

In [82]: for el in doc.xpath(f'{movies_xpath}/div[1]//span[@class="frame-title"]'):
    ...:     print(el.text_content)
    ...: 
<bound method HtmlMixin.text_content of <Element span at 0x7f0924edcd60>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924edf8d0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924edd9e0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924edfab0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0924edf920>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092536f510>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092536ebb0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092536dd50>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092536e7a0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092536fce0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092536fa10>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925057880>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925057d80>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925057100>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09250574c0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925055ad0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925054900>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925057dd0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09250571f0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925054450>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925055120>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925055170>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09250555d0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09250545e0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f09251026b0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504eed0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e840>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e340>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504ede0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504ebb0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e020>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e480>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e7f0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e9d0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e660>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504df30>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e750>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e8e0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504ea20>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e6b0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504ecf0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e700>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504ed40>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504ec50>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504ea70>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504eca0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504ee30>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504eac0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504ec00>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e7a0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e430>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e2a0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e250>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e160>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e200>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e390>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e520>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e2f0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e070>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e570>>
<bound method HtmlMixin.text_content of <Element span at 0x7f092504e0c0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925167d80>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925165350>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925165a80>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925167b00>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925164860>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925167ec0>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925167150>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925166750>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925167510>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925164d60>>
<bound method HtmlMixin.text_content of <Element span at 0x7f0925164f90>>

In [83]: for el in doc.xpath(f'{movies_xpath}/div[1]//span[@class="frame-title"]'):
    ...:     print(el.text_content())
    ...: 









































































In [84]: content = response.content.decode(response.encoding)

In [85]: doc = html.document_fromstring(response.content)

In [86]: doc = html.document_fromstring(content)

In [87]: for el in doc.xpath(f'{movies_xpath}/div[1]//span[@class="frame-title"]'):
    ...:     print(el.text_content())
    ...: 









































































In [88]: for el in doc.xpath(f'{movies_xpath}/div[1]//span[@class="frame-title"]'):
    ...:     print(el.text)
    ...: 
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None

In [89]: doc.xpath(f'/html/body//span[@class="frame-title"]')
Out[89]: 
[<Element span at 0x7f09249142c0>,
 <Element span at 0x7f0924914720>,
 <Element span at 0x7f0924915850>,
 <Element span at 0x7f0924916660>,
 <Element span at 0x7f0924914590>,
 <Element span at 0x7f09249173d0>,
 <Element span at 0x7f0924917290>,
 <Element span at 0x7f0924917880>,
 <Element span at 0x7f0924914f90>,
 <Element span at 0x7f0924915b20>,
 <Element span at 0x7f0924914db0>,
 <Element span at 0x7f0924916160>,
 <Element span at 0x7f0924916570>,
 <Element span at 0x7f0924915ad0>,
 <Element span at 0x7f092504e340>,
 <Element span at 0x7f092504eca0>,
 <Element span at 0x7f092504e8e0>,
 <Element span at 0x7f092504fc90>,
 <Element span at 0x7f092504f4c0>,
 <Element span at 0x7f092504ef20>,
 <Element span at 0x7f092504f3d0>,
 <Element span at 0x7f092504f0b0>,
 <Element span at 0x7f092504e840>,
 <Element span at 0x7f092504e930>,
 <Element span at 0x7f092504ebb0>,
 <Element span at 0x7f092504f920>,
 <Element span at 0x7f092504eac0>,
 <Element span at 0x7f092504e480>,
 <Element span at 0x7f092504e430>,
 <Element span at 0x7f092504e750>,
 <Element span at 0x7f092504e660>,
 <Element span at 0x7f092504ede0>,
 <Element span at 0x7f092504ea70>,
 <Element span at 0x7f092504df30>,
 <Element span at 0x7f092504ed40>,
 <Element span at 0x7f092504f830>,
 <Element span at 0x7f092504fb00>,
 <Element span at 0x7f092504fba0>,
 <Element span at 0x7f092504ffb0>,
 <Element span at 0x7f092504ff60>,
 <Element span at 0x7f092536f510>,
 <Element span at 0x7f092536cc20>,
 <Element span at 0x7f092536c1d0>,
 <Element span at 0x7f092536c360>,
 <Element span at 0x7f092536c040>,
 <Element span at 0x7f092536c450>,
 <Element span at 0x7f092536c130>,
 <Element span at 0x7f092536d080>,
 <Element span at 0x7f092536c310>,
 <Element span at 0x7f092536cef0>,
 <Element span at 0x7f092536d0d0>,
 <Element span at 0x7f092536ce50>,
 <Element span at 0x7f092536d120>,
 <Element span at 0x7f092536ce00>,
 <Element span at 0x7f092536d850>,
 <Element span at 0x7f092536d2b0>,
 <Element span at 0x7f092536d800>,
 <Element span at 0x7f092536d580>,
 <Element span at 0x7f092536d3a0>,
 <Element span at 0x7f092536df80>,
 <Element span at 0x7f092536d4e0>,
 <Element span at 0x7f092536cae0>,
 <Element span at 0x7f092536d710>,
 <Element span at 0x7f092536d6c0>,
 <Element span at 0x7f092536d760>,
 <Element span at 0x7f092536d8a0>,
 <Element span at 0x7f092536de90>,
 <Element span at 0x7f092536e070>,
 <Element span at 0x7f092536e0c0>,
 <Element span at 0x7f092536e340>,
 <Element span at 0x7f092536cfe0>,
 <Element span at 0x7f09244af880>]

In [90]: len(doc.xpath(f'/html/body//span[@class="frame-title"]'))
Out[90]: 72

In [91]: doc.xpath(f'/html/body//span[@class="frame-title"]')[0]
Out[91]: <Element span at 0x7f09249142c0>

In [92]: doc.xpath(f'/html/body//span[@class="frame-title"]')[0].text

In [93]: doc.xpath(f'/html/body//span[@class="frame-title"]')[0].text_content()
Out[93]: ''

In [94]: print(doc)
<Element html at 0x7f09250564d0>

In [95]: content
Out[95]: '\n\n<!DOCTYPE html>\n\n<!--[if lt IE 7 ]> <html lang="en" class="ie6 lte9 lte8 lte7 lte6 no-js"> <![endif]-->\n<!--[if IE 7 ]>    <html lang="en" class="ie7 lte9 lte8 lte7 no-js"> <![endif]-->\n<!--[if IE 8 ]>    <html lang="en" class="ie8 lte9 lte8 no-js"> <![endif]-->\n<!--[if IE 9 ]>    <html lang="en" class="ie9 lte9 no-js"> <![endif]-->\n<!--[if (gt IE 9)|!(IE)]><!--> <html id="html" lang="en" class="no-mobile no-js"> <!--<![endif]-->\n<head>\n\t<meta charset="UTF-8" />\n\t<meta name="viewport" content="width=1024" />\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />\n\t<meta name="description" content="Mehdi Rafee’s films" />\n\t\n\t\n\t<meta property="og:url" content="https://letterboxd.com/mrafee113/films/?html.parser" />\n\t<meta property="og:title" content="Mehdi Rafee’s films" />\n\t<meta property="og:description" content="Mehdi Rafee’s films" />\n\t<meta property="og:image" content="https://s.ltrbxd.com/static/img/default-share.e38c5d62.png" />\n\t\n\t<meta name="application-name" content="Letterboxd" />\n\t<meta name="theme-color" content="#445566" />\n\t<meta name="msapplication-TileColor" content="#445566" />\n\t<meta name="apple-itunes-app" content="app-id=1054271011, affiliate-data=11l5KW, app-argument=https://letterboxd.com/mrafee113/films/?html.parser" />\n\t<meta name="mobile-web-app-capable" content="yes" />\n\n\t<title>&lrm;Mehdi Rafee’s films &bull; Letterboxd</title>\n\t\n\t<script>\n\t\twindow.dataLayer = window.dataLayer || [];\n\t\twindow.gtag = window.gtag || function () {\n\t\t\tdataLayer.push(arguments);\n\t\t};\n\t\tfunction ga() {}\n\t</script>\n\n\t<script async src="https://www.googletagmanager.com/gtag/js?id=G-D3ECBB4D7L"></script>\n\n\t<script>\n\t\twindow.dataLayer = window.dataLayer || [];\n\t\twindow.gtag = window.gtag || function () {\n\t\t\tdataLayer.push(arguments);\n\t\t};\n\t\tgtag(\'js\', new Date());\n\t\n\t\tvar analytic_params = {};\n\t\t\n\t\t\n\t\tanalytic_params[\'user_type\'] = \'Visitor\';\n\t\tanalytic_params[\'template\'] = \'/object/person/films-watched\';\n\t\t\n\t\t\n\n\t\tif (analytic_params.member_type) {\n\t\t\tgtag(\'set\', \'user_properties\', { \n\t\t\t\tmember_type: analytic_params.member_type,\n\t\t\t});\n\t\t\tdelete analytic_params.member_type;\n\t\t}\n\t\tvar config = {\n\t\t\t...analytic_params,\n\t\t\t\'cookie_domain\': \'letterboxd.com\', \n\t\t\t\'optimize_id\': \'GTM-TB8HSDN\', \n\t\t};\n\t\tgtag(\'config\', \'G-D3ECBB4D7L\', config);\n\t</script>\n\n\n\t<script>\n\t\tvar isMobile = false,\n\t\t\tisMobileOptimised = true,\n\t\t\trenderMobile = false,\n\t\t\tuseStaticFonts = false,\n\t\t\tdisableFrameProtection = false,\n\t\t\tbaseURL = "",\n\t\t\tsuccessMessages = [],\n\t\t\terrorMessages = [],\n\t\t\tstickyMessages = [],\n\t\t\tglobals = {\n\t\t\tautoAddFilm: false\t\t\t\n\t\t\t\t, spinners: {\n\t\t\t\t\tajax_242d35: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_12_2C3641: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_14_20272f: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_16_161B21: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\'\n\t\t\t\t}\n\t\t\t},\n\t\t\tsupermodelCSRF = "",\n\t\t\tgRecaptchaKey = \'6Le3mMIUAAAAAEXbwZ7M1R5jEv0V5xbvj7bgXq2g\',\n\t\t\tperson = {\n\t\t\t\tusername: ""\n\t\t\t\t, loggedIn: false\n\t\t\t\t\n\t\t\t\t, showAds: true\n\t\t\t\t, role: "guest"\n\t\t\t\t, hasExtendedServiceFilters: false\n\t\t\t\t, canBulkAddToLists: false\n\t\t\t\t, canFilterOwned: false\n\t\t\t\t, hasHqRole: false\n\t\t\t\t, canHaveHqDashboard: false\n\t\t\t\t, hasMemberStatistics: false\n\t\t\t\t, blockedMembers: []\n\t\t\t\t, showAdultContent: false\n\t\t\t\t, validated: null\n\t\t\t\t, trusted: false\n\t\t\t\t, hasBlocked : function(member) { for (var i = 0; i !== person.blockedMembers.length; i++) {if (person.blockedMembers[i] === member) return true;} return false; }\n\t\t\t\t, viewingTags: []\n\t\t\t\t, hasMoreTags: true\n\t\t\t\t, getCustomPoster : function(filmId) { return null; }\n\t\t\t},\n\t\t\tdisableAds = true;\n\t\t\n\t\t\n\t\t\nsupermodelCSRF = "9749e0a0bd2da01647eb";\n\n\t\t\n\n\t\t\n\n\t\t\n\n\t\t\n\t\t\tif ( screen.width < 768 ) {\n\t\t\t\tvar date = new Date();\n\t\t\t\tvar maxAge = 365 * 24 * 60 * 60;\n\t\t\t\tdate.setTime(date.getTime() + maxAge * 1000);\n\t\t\t\tvar expires = \'; expires=\' + date.toUTCString();\n\t\t\t\tdocument.cookie = "useMobileSite=yes" + expires + "; path=/; maxAge=" + maxAge;\n\t\t\t\tif ( document.cookie && document.cookie.indexOf("useMobileSite=yes") >= 0 ) {\n\t\t\t\t\twindow.location.reload(true);\n\t\t\t\t} else {\n\t\t\t\t\t// No cookies.  No Mobile version.\n\t\t\t\t}\n\t\t\t}\n\t\t\n\n\t\tvar isWindows = navigator.platform.toUpperCase().indexOf(\'WIN\') >= 0; // Detect windows platform\n\t\tif (isWindows) { document.documentElement.classList.add(\'is-windows\'); }\n\t\t\n\t\t\n\t</script>\n\n\t<link rel="manifest" href="/manifest.json" />\n\t<link rel="author" type="text/plain" href="/humans.txt" />\n\t<link rel="mask-icon" href="https://s.ltrbxd.com/static/img/icons/letterboxd-decal-l-16px.5fe24c7d.svg" color="#445566" />\n\t<link rel="shortcut icon" sizes="196x196" href="https://s.ltrbxd.com/static/img/icons/touch-icon-192x192.257b84e7.png" />\n\t<link rel="shortcut icon" href="/favicon.ico" />\n\t<link rel="search" type="application/opensearchdescription+xml" title="Letterboxd" href="/static/opensearch.xml" />\n\t\n\t\n\t<!--[if lte IE 9 ]>\n\t\t<link href="https://s.ltrbxd.com/static/css/ie9-1.min.066b855d.css" rel="stylesheet" media="screen, projection"/>\n\t\t<link href="https://s.ltrbxd.com/static/css/ie9-2.min.13b2f50c.css" rel="stylesheet" media="screen, projection"/>\n\t<![endif]-->\n\t<!--[if (gt IE 9)|!(IE)]><!-->\n\t\t<link href="https://s.ltrbxd.com/static/css/main.min.97414920.css" rel="stylesheet" media="screen, projection"/>\n\t<!--<![endif]-->\n\t<!--[if lte IE 6]><script>location.replace("/errors/ie6");</script><![endif]-->\n\t<!--[if IE 7]><script>location.replace("/errors/ie7");</script><![endif]-->\n\t<!--[if IE 8]><script>location.replace("/errors/ie8");</script><![endif]-->\n\t<!--[if IE 9]><script>location.replace("/errors/ie9");</script><![endif]-->\n\t\n\t\n\t\n\t<link href="https://s.ltrbxd.com/static/css/desktop.min.e1d8f367.css" rel="stylesheet" media="screen, projection"/>\n\n\t<script src="https://s.ltrbxd.com/static/js/main.min.a7e00d04.js"></script>\n\t\n\n\n\n\n\n\t<script>\n\t\tif ( $.cookie("letterboxd.admin.signed.in") === person.username ) {\n\t\t\tsuccessMessages.push("You are signed in as " + person.username);\n\t\t\t$(function(){$("#header, #content, body").css("background","#543");});\n\t\t}\n\t</script>\n\t\n</head>\n\n<body class="films-watched wide small-poster-grid" data-owner="mrafee113">\n\t\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<script>\nvar mainMenu = [];\n\n\t\n\tmainMenu.push({\n\t\t"id": 1,\n\t\t"url": "/sign-in/", \n\t\t"name": "Sign In",\n\t\t"cssClassCode": "sign-in-menu",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": true,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 2,\n\t\t"url": "/create-account/", \n\t\t"name": "Create Account",\n\t\t"cssClassCode": "create-account-menu",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 3,\n\t\t"url": "/", \n\t\t"name": "Home",\n\t\t"cssClassCode": "person-home",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 4,\n\t\t"url": "/activity/", \n\t\t"name": "Activity",\n\t\t"cssClassCode": "main-nav-activity",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "Activity",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 5,\n\t\t"url": "/films/", \n\t\t"name": "Films",\n\t\t"cssClassCode": "films-page main-nav-films",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 6,\n\t\t"url": "/lists/", \n\t\t"name": "Lists",\n\t\t"cssClassCode": "lists-page main-nav-lists",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 7,\n\t\t"url": "/members/", \n\t\t"name": "Members",\n\t\t"cssClassCode": "main-nav-people",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 8,\n\t\t"url": "/journal/", \n\t\t"name": "Journal",\n\t\t"cssClassCode": "main-nav-journal",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 9,\n\t\t"url": "/search/", \n\t\t"name": "Search results",\n\t\t"cssClassCode": "",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n</script>\n\n<header class="site-header js-hide-in-app" id="header" data-allow-user-to-add-all-films-to-a-list="true">\n\t<div class="site-header-bg"></div>\n\t<section>\n\t\t<h1 class="site-logo"><a href="/" class="logo replace">Letterboxd &mdash; Your life in film</a></h1>\n\n\t\t<div class="react-component" data-component-class="globals.comps.NavComponent"></div>\n\n\t\t\n\t\t\t\n\t\t\t\n\n\n\t\n\n\n\n\n\n<form method="post" action="#" id="signin" class="signin signin-form js-header-signin-form js-signin" data-url="/user/login.do" data-recaptcha-action="signin" novalidate=\'novalidate\' autocorrect=\'off\' autocapitalize=\'off\'>\n\t<input type="hidden" name="__csrf" value="placeholder" />\n\t<fieldset class="fieldset">\n\t\t<div class="fields">\n\t\t\t<div class="col">\n\t\t\t\t<label for="username">Username or Email</label>\n\t\t\t\t<input type="email" name="username" id="username" class="field signin-field" tabindex="1" data-focus-control="signingIn" autocomplete=\'email\' inputmode=\'email\' value="" />\n\t\t\t</div>\n\t\t\t<div class="col">\n\t\t\t\t<label for="password">Password</label>\n\t\t\t\t<input type="password" name="password" id="password" class="field signin-field" tabindex="2" autocomplete=\'current-password\' value="" />\n\t\t\t</div>\n\t\t\t<div class="signin-actions">\n\t\t\t\t<label for="remember" class="option-label -checkbox -small">\n\t\t\t\t\t<input type="checkbox" name="remember" id="remember" class="checkbox" tabindex="3" value="true" /><i class="substitute"></i>\n\t\t\t\t\t<span class="focus">Remember<span class="mob-hide"> me</span></span>\n\t\t\t\t</label>\n\t\t\t\t<p class="reset" tabindex="5"><a class="reset-password-link" href="/user/request-password-reset" target="_top">Forgotten<span class="elongated"> password</span>?</a></p>\n\t\t\t</div>\n\t\t\t<div class="col buttons">\n\t\t\t\t<div class="button-container"><input type="submit" value="Sign in" class="button -action button-green" tabindex="4" /><i></i></div>\n\t\t\t\t<div class="close js-close-signin">&times;</div>\n\t\t\t</div>\n\t\t</div>\n\t</fieldset>\n\t<div id="signin-message" class="errormessage"></div>\n</form>\n\n\n\t\t\n\t\t\n\t\t\n\t\t\t\n\t\t\t\n\n\n\n\t\t\n\t\t\n\t\t\n\t\t<form id="search" class="js-search-form search-form" action="/search/" method="get" autocorrect="off">\n\t\t\t<input autocomplete="false" name="hidden" type="text" style="display:none;" />\n\t\t\t<fieldset>\n\t\t\t\t<label for="search-q" class="hidden">Search:</label>\n\t\t\t\t<input type="text" name="q" id="search-q" class="field -borderless" data-lpignore=\'true\' inputmode=\'search\' value="" />\n\t\t\t\t<input type="submit" value="Search" class="action" />\n\t\t\t</fieldset>\n\t\t</form>\n\t\t\n\t</section>\n</header>\n\n\n\n\n\n\n<div id="content" class="site-body">\n\t\n\t<div class="content-wrap">\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<section id="profile-header" class="js-profile-header -is-mini-nav" data-person="mrafee113">\n\t\n\n\t<nav class="profile-navigation">\n\t\t\n\t\t\t<div class="profile-mini-person">\n\t\t\t\t<a class="avatar -a24" href="/mrafee113/" > <img src="https://a.ltrbxd.com/resized/avatar/upload/1/4/4/4/1/0/3/shard/avtr-0-48-0-48-crop.jpg?v=484d4bfb0a" alt="Mehdi Rafee" width="24" height="24" /> </a>\n\t\t\t\t<h1 class="title-3"><a href="/mrafee113/">Mehdi Rafee</a></h1>\n\t\t\t\t\n\t\t\t</div>\n\t\t\n\t\t\n\t\t\t<ul class="navlist">\n\t\t\t\t\n\n\t\t\t\t\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem hide-for-owner"><a class="navlink" href="/mrafee113/activity/">Activity</a></li>\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/activity/">Activity</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem -active"><a class="navlink" href="/mrafee113/films/">Films</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/films/diary/">Diary</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/films/reviews/">Reviews</a></li>\n\n\t\t\t\t<li class="navitem" data-owner="mrafee113"><a class="navlink" href="/mrafee113/watchlist/" >Watchlist</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/mrafee113/lists/">Lists</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/likes/">Likes</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/mrafee113/tags/">Tags</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/following/">Network</a></li>\n\n\t\t\t\t\n\n\t\t\t\t\n\n\t\t\t\t\n\n\n\n\t<li data-owner="mrafee113" class="navitem show-when-logged-in hide-for-owner"><a class="navlink" href="/pro/gift/mrafee113/">Gift Pro</a></li>\n\n\n\t\t\t\t<li class="navitem -rss">\n\t\t\t\t\t<a href="/mrafee113/rss/" class="has-icon icon-16 icon-rss tooltip" title="RSS feed">\n\t\t\t\t\t\t<span class="_sr-only">RSS feed for Mehdi</span>\n\t\t\t\t\t</a>\n\t\t\t\t</li>\n\t\t\t</ul>\n\t\t\n    </nav>\n</section>\n\n\n \n\n\n\n<div class="cols-2 overflow">\n\t<section class="section col-main overflow">\n\t\n \t\t\n\n<div id="content-nav" class="tabbed"> <section class="sub-nav-wrapper"><ul class="sub-nav"> <li class=" selected"><a href="/mrafee113/films/" class="tooltip" title="690&nbsp;films">Watched</a></li> <li class=""><a href="/mrafee113/films/diary/" class="tooltip" title="254&nbsp;films">Diary</a></li> <li class=""><a href="/mrafee113/films/reviews/" class="tooltip" title="45&nbsp;films">Reviews</a></li> </ul></section> <div class="sorting-selects has-hide-toggle"> <section class="grid-toggle-menu mob-hide"> <ul> <li class="selected"><a href="/mrafee113/films/" class="grid-toggle ir s grid-toggle-small" data-toggle="large">Small</a></li> <li><a href="/mrafee113/films/size/large/" class="grid-toggle ir s grid-toggle-large" data-toggle="small">Large</a></li> </ul> </section> <section class="smenu-wrapper hide-toggle-menu"> <div class="smenu"> <label><span class="ir s hide-toggle-icon">Visibility Filters</span><i class="ir s icon"></i></label> <ul class="smenu-menu" id="hide-toggle-menu"> <li class="divider-line-below"><a href="#" class="item js-film-filter-remover">Remove filters</a></li> <li class="js-account-filters"> <label class="option-label -toggle -small switch-control js-fade-toggle"> <span class="label">Fade watched films</span> <input class="checkbox" type="checkbox" checked="checked" role="switch" /><span class="state"><span class="track"><span class="handle"></span></span></span> </label> </li> <li class="js-account-filters"> <label class="option-label -toggle -small switch-control js-custom-poster-toggle" data-action="/ajax/poster-mode/"> <span class="label">Show custom posters</span> <input class="checkbox" type="checkbox" checked="checked" role="switch" /><span class="state"><span class="track"><span class="handle"></span></span></span> </label> </li> <li class="divider-line js-account-filters"> <span class="smenu-sublabel -uppercase">Custom posters</span> <div class="segmented-control -small custom-poster-control js-custom-poster-control" role="group" aria-label="Change custom poster visibility" data-action="/ajax/poster-mode/"> <div class="options"> <button type="button" class="option" data-js-trigger="option" data-value="All">Any</button> <button type="button" class="option" data-js-trigger="option" data-value="Theirs">Theirs</button> <button type="button" class="option" data-js-trigger="option" data-value="Yours">Yours</button> <button type="button" class="option" data-js-trigger="option" data-value="None">None</button> </div> </div> </li> <li class="divider-line js-account-filters"> <span class="smenu-sublabel -uppercase">Account Filters</span> <ul> <li class="js-film-filter" data-category="watched" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show watched films</a></li> <li class="js-film-filter" data-category="watched" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide watched films</a></li> <li class="js-film-filter divider-line -inset" data-category="liked" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show liked films</a></li> <li class="js-film-filter" data-category="liked" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide liked films</a></li> <li class="js-film-filter divider-line -inset" data-category="rated" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show rated films</a></li> <li class="js-film-filter" data-category="rated" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide rated films</a></li> <li class="js-film-filter divider-line -inset" data-category="logged" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show logged films</a></li> <li class="js-film-filter" data-category="logged" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide logged films</a></li> <li class="js-film-filter divider-line -inset" data-category="rewatched" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show rewatched films</a></li> <li class="js-film-filter" data-category="rewatched" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide rewatched films</a></li> <li class="js-film-filter divider-line -inset" data-category="reviewed" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show reviewed films</a></li> <li class="js-film-filter" data-category="reviewed" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide reviewed films</a></li> <li class="js-film-filter divider-line -inset" data-category="watchlisted" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films in watchlist</a></li> <li class="js-film-filter" data-category="watchlisted" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films in watchlist</a></li> <li class="js-film-filter divider-line -inset" data-category="owned" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films you own</a></li> <li class="js-film-filter" data-category="owned" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films you own</a></li> <li class="js-film-filter divider-line -inset" data-category="customised" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films you’ve customized</a></li> <li class="js-film-filter" data-category="customised" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films you’ve customized</a></li> </ul> </li> <li class="divider-line js-film-filters"> <span class="smenu-sublabel -uppercase">Content Filters</span> <ul> <li class="js-film-filter" data-category="shorts" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show short films</a></li> <li class="js-film-filter" data-category="shorts" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide short films</a></li> <li class="js-film-filter divider-line -inset" data-category="tv" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show TV shows</a></li> <li class="js-film-filter" data-category="tv" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide TV shows</a></li> <li class="js-film-filter divider-line -inset" data-category="docs" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide documentaries</a></li> <li class="js-film-filter divider-line -inset" data-category="unreleased" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide unreleased titles</a></li> <li class="js-film-filter divider-line -inset" data-category="obscure" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show obscure films</a></li> <li class="js-film-filter" data-category="obscure" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide obscure films</a></li> <li class="js-film-filter divider-line -inset" data-category="backdropped" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films with backdrop</a></li> <li class="js-film-filter" data-category="backdropped" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films with backdrop</a></li> <li class="js-film-filter divider-line -inset" data-category="nanocrowd" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show Nanocrowd films</a></li> <li class="js-film-filter" data-category="nanocrowd" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide Nanocrowd films</a></li> </ul> </li> </ul> </div> </section> <section class="smenu-wrapper"> <strong class="smenu-label">Sort by</strong> <div class="smenu"> <label>Release Date<i class="ir s icon"></i></label> <ul class="smenu-menu"> <li class=""><a class="item" href="/mrafee113/films/by/name/">Film Name</a></li> <li class=""><a class="item" href="/mrafee113/films/by/popular/">Film Popularity</a></li> <li class=""><a class="item" href="/mrafee113/films/by/shuffle/">Shuffle</a></li> <li class=""><span class="smenu-sublabel">When Added</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/date/">Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/date-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">When Rated</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/rated-date/">Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/rated-date-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Release Date</span> <ul> <li class=" smenu-subselected"><a class="item" href="/mrafee113/films/"><i class="ir s icon"></i>Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/release-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Average Rating</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/rating/">Highest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/rating-lowest/">Lowest First</a></li> </ul></li> <li class="" data-owner="mrafee113"><span class="smenu-sublabel" data-owner="mrafee113" data-owner-label="Your Rating">Mehdi’s Rating</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/entry-rating/">Highest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/entry-rating-lowest/">Lowest First</a></li> </ul></li> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><span class="smenu-sublabel">Your Rating</span> <ul> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><a class="item" href="/mrafee113/films/by/your-rating/">Highest First</a></li> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><a class="item" href="/mrafee113/films/by/your-rating-lowest/">Lowest First</a></li> </ul></li> <li class=" show-when-logged-in"><span class="smenu-sublabel">Your Interests</span> <ul> <li class=" show-when-logged-in"><a class="item" href="/mrafee113/films/by/your-interest-liked/">Based on films you liked</a></li> <li class=" show-when-logged-in"><a class="item" href="/mrafee113/films/by/your-interest-related/">Related to films you liked</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Film Length</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/shortest/">Shortest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/longest/">Longest First</a></li> </ul></li> </ul> </div> </section> \n<section class="smenu-wrapper"> <div class="smenu"> <label>Service<i class="ir s icon"></i></label> <ul id="services-menu" class="smenu-menu" data-upgrade-url="/pro/"> <li class="availability- smenu-subselected"> <span class="selected"> All films </span> </li> <li class="divider-line availability-amazon"> <a class="item" href="/mrafee113/films/on/amazon-deu/"> Amazon DE </a> </li> <li class="availability-amazon-video"> <a class="item" href="/mrafee113/films/on/amazon-video-de/"> Amazon Video DE </a> </li> <li class="availability-apple-tv-plus"> <a class="item" href="/mrafee113/films/on/apple-tv-plus-de/"> Apple TV Plus DE </a> </li> <li class="availability-apple-itunes"> <a class="item" href="/mrafee113/films/on/apple-itunes-de/"> iTunes DE </a> </li> <li class="note divider-line -upgrade"> <p>Upgrade to a <a href="/pro/">Letterboxd <span class="badge -pro -small">Pro</span></a> account to add your favorite services to this list—including any service and country pair listed on JustWatch—and to enable one-click filtering by all your favorites.</p></li> <li><a class="item item-small" href="https://www.justwatch.com" target="_blank" rel="noopener noreferrer"><small>Powered by JustWatch</small></a></li> </ul> </div> </section>\n <section class="smenu-wrapper"> <div class="smenu"> <label> Genre<i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><span class="selected">Any genre</span></li> <li class="divider-line"> <ul> <li class=""><a class="item" href="/mrafee113/films/genre/action/"><i class="ir s icon"></i>Action</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/adventure/"><i class="ir s icon"></i>Adventure</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/animation/"><i class="ir s icon"></i>Animation</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/comedy/"><i class="ir s icon"></i>Comedy</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/crime/"><i class="ir s icon"></i>Crime</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/documentary/"><i class="ir s icon"></i>Documentary</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/drama/"><i class="ir s icon"></i>Drama</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/family/"><i class="ir s icon"></i>Family</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/fantasy/"><i class="ir s icon"></i>Fantasy</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/history/"><i class="ir s icon"></i>History</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/horror/"><i class="ir s icon"></i>Horror</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/music/"><i class="ir s icon"></i>Music</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/mystery/"><i class="ir s icon"></i>Mystery</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/romance/"><i class="ir s icon"></i>Romance</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/science-fiction/"><i class="ir s icon"></i>Science Fiction</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/thriller/"><i class="ir s icon"></i>Thriller</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/tv-movie/"><i class="ir s icon"></i>TV Movie</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/war/"><i class="ir s icon"></i>War</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/western/"><i class="ir s icon"></i>Western</a></li> </ul> </li> </ul> </div> </section> <section class="smenu-wrapper"> <div class="smenu"> <label class="x"> Decade<i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><span class="selected">Any decade</span></li> <li class="divider-line "><a class="item" href="/mrafee113/films/decade/2020s/">2020s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/2010s/">2010s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/2000s/">2000s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1990s/">1990s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1980s/">1980s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1970s/">1970s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1960s/">1960s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1950s/">1950s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1940s/">1940s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1930s/">1930s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1920s/">1920s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1910s/">1910s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1900s/">1900s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1890s/">1890s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1880s/">1880s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1870s/">1870s</a></li> </ul> </div> </section> <section class="smenu-wrapper"> <div class="smenu"> <label> Rating <i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><a class="item" href="/mrafee113/films/">Any rating</a></li> <li><a class="item" href="/mrafee113/films/rated/none/">No rating</a></li> <li class="divider-line"> <span class="smenu-sublabel -uppercase">Rating (or range)</span> <div class="menu-rating-filter js-rating-filter" data-rateit-starwidth="10" data-rateit-starheight="19" data-action="/mrafee113/films/rated/%7B%7Bvalue%7D%7D/"> <div class="rateit-range"> <div class="rateit-selected"></div> <div class="rateit-hover"></div> </div> </div> <small class="note">Drag to define range</small> </li> </ul> </div> </section> </div> <div class="clear"></div> </div>\n\t\n\t\t\n\n\t\n\t\t\n\t\t\t\t\n\n\t\t\t\t<ul class="poster-list -p70 -grid film-list clear">\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-726680 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="726680" data-film-slug="/film/mafia-mamma/" data-poster-url="/film/mafia-mamma/image-150/" data-linked="linked" data-target-link="/film/mafia-mamma/" data-target-link-target="" data-cache-busting-key="20289f53" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Mafia Mamma"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-998520 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="998520" data-film-slug="/film/louis-ck-at-the-dolby/" data-poster-url="/film/louis-ck-at-the-dolby/image-150/" data-linked="linked" data-target-link="/film/louis-ck-at-the-dolby/" data-target-link-target="" data-cache-busting-key="93b11804" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Louis C.K. at The Dolby"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-6">★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-575258 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="575258" data-film-slug="/film/renfield/" data-poster-url="/film/renfield/image-150/" data-linked="linked" data-target-link="/film/renfield/" data-target-link-target="" data-cache-busting-key="d129ad49" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Renfield"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-522405 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="522405" data-film-slug="/film/shazam-fury-of-the-gods/" data-poster-url="/film/shazam-fury-of-the-gods/image-150/" data-linked="linked" data-target-link="/film/shazam-fury-of-the-gods/" data-target-link-target="" data-cache-busting-key="1e7571ce" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Shazam! Fury of the Gods"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-424003 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="424003" data-film-slug="/film/dungeons-dragons-honor-among-thieves/" data-poster-url="/film/dungeons-dragons-honor-among-thieves/image-150/" data-linked="linked" data-target-link="/film/dungeons-dragons-honor-among-thieves/" data-target-link-target="" data-cache-busting-key="5c7797c4" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Dungeons & Dragons: Honor Among Thieves"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-838520 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="838520" data-film-slug="/film/champions-2023/" data-poster-url="/film/champions-2023/image-150/" data-linked="linked" data-target-link="/film/champions-2023/" data-target-link-target="" data-cache-busting-key="d119d8a2" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Champions"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-764596 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="764596" data-film-slug="/film/kill-boksoon/" data-poster-url="/film/kill-boksoon/image-150/" data-linked="linked" data-target-link="/film/kill-boksoon/" data-target-link-target="" data-cache-busting-key="280be804" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Kill Boksoon"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-566237 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="566237" data-film-slug="/film/ant-man-and-the-wasp-quantumania/" data-poster-url="/film/ant-man-and-the-wasp-quantumania/image-150/" data-linked="linked" data-target-link="/film/ant-man-and-the-wasp-quantumania/" data-target-link-target="" data-cache-busting-key="df5c617e" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ant-Man and the Wasp: Quantumania"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-558056 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="558056" data-film-slug="/film/knock-at-the-cabin/" data-poster-url="/film/knock-at-the-cabin/image-150/" data-linked="linked" data-target-link="/film/knock-at-the-cabin/" data-target-link-target="" data-cache-busting-key="2e6ced50" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Knock at the Cabin"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-733385 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="733385" data-film-slug="/film/mummies-2023/" data-poster-url="/film/mummies-2023/image-150/" data-linked="linked" data-target-link="/film/mummies-2023/" data-target-link-target="" data-cache-busting-key="fb56ca62" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Mummies"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-661153 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="661153" data-film-slug="/film/operation-fortune-ruse-de-guerre/" data-poster-url="/film/operation-fortune-ruse-de-guerre/image-150/" data-linked="linked" data-target-link="/film/operation-fortune-ruse-de-guerre/" data-target-link-target="" data-cache-busting-key="8d72bd57" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Operation Fortune: Ruse de Guerre"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-242285 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="242285" data-film-slug="/film/puss-in-boots-the-last-wish/" data-poster-url="/film/puss-in-boots-the-last-wish/image-150/" data-linked="linked" data-target-link="/film/puss-in-boots-the-last-wish/" data-target-link-target="" data-cache-busting-key="d60f4abc" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Puss in Boots: The Last Wish"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-789082 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="789082" data-film-slug="/film/strange-world-2022/" data-poster-url="/film/strange-world-2022/image-150/" data-linked="linked" data-target-link="/film/strange-world-2022/" data-target-link-target="" data-cache-busting-key="8df8311d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Strange World"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-744826 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="744826" data-film-slug="/film/enola-holmes-2/" data-poster-url="/film/enola-holmes-2/image-150/" data-linked="linked" data-target-link="/film/enola-holmes-2/" data-target-link-target="" data-cache-busting-key="0b05f98f" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Enola Holmes 2"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-435460 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="435460" data-film-slug="/film/black-panther-wakanda-forever/" data-poster-url="/film/black-panther-wakanda-forever/image-150/" data-linked="linked" data-target-link="/film/black-panther-wakanda-forever/" data-target-link-target="" data-cache-busting-key="87412ddf" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Black Panther: Wakanda Forever"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-589317 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="589317" data-film-slug="/film/amsterdam-2022/" data-poster-url="/film/amsterdam-2022/image-150/" data-linked="linked" data-target-link="/film/amsterdam-2022/" data-target-link-target="" data-cache-busting-key="85997eb0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Amsterdam"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-647390 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="647390" data-film-slug="/film/confess-fletch/" data-poster-url="/film/confess-fletch/image-150/" data-linked="linked" data-target-link="/film/confess-fletch/" data-target-link-target="" data-cache-busting-key="88144a94" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Confess, Fletch"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-441474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="441474" data-film-slug="/film/wendell-wild/" data-poster-url="/film/wendell-wild/image-150/" data-linked="linked" data-target-link="/film/wendell-wild/" data-target-link-target="" data-cache-busting-key="8e24544c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Wendell & Wild"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-523109 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="523109" data-film-slug="/film/causeway/" data-poster-url="/film/causeway/image-150/" data-linked="linked" data-target-link="/film/causeway/" data-target-link-target="" data-cache-busting-key="870478ea" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Causeway"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-721288 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="721288" data-film-slug="/film/the-fabelmans/" data-poster-url="/film/the-fabelmans/image-150/" data-linked="linked" data-target-link="/film/the-fabelmans/" data-target-link-target="" data-cache-busting-key="0dba11a7" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Fabelmans"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-521323 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="521323" data-film-slug="/film/the-menu-2022/" data-poster-url="/film/the-menu-2022/image-150/" data-linked="linked" data-target-link="/film/the-menu-2022/" data-target-link-target="" data-cache-busting-key="8e7be729" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Menu"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-9">★★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-586723 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="586723" data-film-slug="/film/glass-onion/" data-poster-url="/film/glass-onion/image-150/" data-linked="linked" data-target-link="/film/glass-onion/" data-target-link-target="" data-cache-busting-key="304e3660" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Glass Onion"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-820461 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="820461" data-film-slug="/film/the-lost-king/" data-poster-url="/film/the-lost-king/image-150/" data-linked="linked" data-target-link="/film/the-lost-king/" data-target-link-target="" data-cache-busting-key="864fbd75" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Lost King"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-686510 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="686510" data-film-slug="/film/see-how-they-run-2022/" data-poster-url="/film/see-how-they-run-2022/image-150/" data-linked="linked" data-target-link="/film/see-how-they-run-2022/" data-target-link-target="" data-cache-busting-key="8a569c44" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="See How They Run"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-462030 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="462030" data-film-slug="/film/pinocchio-2022/" data-poster-url="/film/pinocchio-2022/image-150/" data-linked="linked" data-target-link="/film/pinocchio-2022/" data-target-link-target="" data-cache-busting-key="beb0d10e" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Pinocchio"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-598882 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="598882" data-film-slug="/film/the-banshees-of-inisherin/" data-poster-url="/film/the-banshees-of-inisherin/image-150/" data-linked="linked" data-target-link="/film/the-banshees-of-inisherin/" data-target-link-target="" data-cache-busting-key="03be9e08" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Banshees of Inisherin"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-734096 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="734096" data-film-slug="/film/tar-2022/" data-poster-url="/film/tar-2022/image-150/" data-linked="linked" data-target-link="/film/tar-2022/" data-target-link-target="" data-cache-busting-key="8caea6a3" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="TÁR"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-666269 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="666269" data-film-slug="/film/white-noise-2022/" data-poster-url="/film/white-noise-2022/image-150/" data-linked="linked" data-target-link="/film/white-noise-2022/" data-target-link-target="" data-cache-busting-key="093db78d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="White Noise"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-676215 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="676215" data-film-slug="/film/day-shift-2022/" data-poster-url="/film/day-shift-2022/image-150/" data-linked="linked" data-target-link="/film/day-shift-2022/" data-target-link-target="" data-cache-busting-key="8097de58" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Day Shift"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-811153 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="811153" data-film-slug="/film/one-piece-film-red/" data-poster-url="/film/one-piece-film-red/image-150/" data-linked="linked" data-target-link="/film/one-piece-film-red/" data-target-link-target="" data-cache-busting-key="093156e5" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="One Piece Film Red"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-647760 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="647760" data-film-slug="/film/the-gray-man-2022/" data-poster-url="/film/the-gray-man-2022/image-150/" data-linked="linked" data-target-link="/film/the-gray-man-2022/" data-target-link-target="" data-cache-busting-key="81ba2f7b" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Gray Man"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-641961 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="641961" data-film-slug="/film/bullet-train/" data-poster-url="/film/bullet-train/image-150/" data-linked="linked" data-target-link="/film/bullet-train/" data-target-link-target="" data-cache-busting-key="0a859e26" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Bullet Train"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-7">★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-371005 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="371005" data-film-slug="/film/minions-the-rise-of-gru/" data-poster-url="/film/minions-the-rise-of-gru/image-150/" data-linked="linked" data-target-link="/film/minions-the-rise-of-gru/" data-target-link-target="" data-cache-busting-key="8a9ee32a" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Minions: The Rise of Gru"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-592465 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="592465" data-film-slug="/film/the-man-from-toronto-2022/" data-poster-url="/film/the-man-from-toronto-2022/image-150/" data-linked="linked" data-target-link="/film/the-man-from-toronto-2022/" data-target-link-target="" data-cache-busting-key="0477e5e9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Man from Toronto"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-543002 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="543002" data-film-slug="/film/thor-love-and-thunder/" data-poster-url="/film/thor-love-and-thunder/image-150/" data-linked="linked" data-target-link="/film/thor-love-and-thunder/" data-target-link-target="" data-cache-busting-key="84638312" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Thor: Love and Thunder"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-878873 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="878873" data-film-slug="/film/vesper-2022/" data-poster-url="/film/vesper-2022/image-150/" data-linked="linked" data-target-link="/film/vesper-2022/" data-target-link-target="" data-cache-busting-key="0317ad27" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Vesper"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-488592 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="488592" data-film-slug="/film/the-sea-beast-2022/" data-poster-url="/film/the-sea-beast-2022/image-150/" data-linked="linked" data-target-link="/film/the-sea-beast-2022/" data-target-link-target="" data-cache-busting-key="8dce9a04" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Sea Beast"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-607401 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="607401" data-film-slug="/film/vengeance-2022/" data-poster-url="/film/vengeance-2022/image-150/" data-linked="linked" data-target-link="/film/vengeance-2022/" data-target-link-target="" data-cache-busting-key="04dc3f16" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Vengeance"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-641574 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="641574" data-film-slug="/film/lightyear-2022/" data-poster-url="/film/lightyear-2022/image-150/" data-linked="linked" data-target-link="/film/lightyear-2022/" data-target-link-target="" data-cache-busting-key="0d45b6f6" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Lightyear"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-812015 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="812015" data-film-slug="/film/close-2022/" data-poster-url="/film/close-2022/image-150/" data-linked="linked" data-target-link="/film/close-2022/" data-target-link-target="" data-cache-busting-key="8ac6ce80" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Close"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-8">★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-875860 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="875860" data-film-slug="/film/ricky-gervais-supernature/" data-poster-url="/film/ricky-gervais-supernature/image-150/" data-linked="linked" data-target-link="/film/ricky-gervais-supernature/" data-target-link-target="" data-cache-busting-key="8c13daef" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ricky Gervais: SuperNature"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-736318 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="736318" data-film-slug="/film/crimes-of-the-future-2022/" data-poster-url="/film/crimes-of-the-future-2022/image-150/" data-linked="linked" data-target-link="/film/crimes-of-the-future-2022/" data-target-link-target="" data-cache-busting-key="8331ef2f" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Crimes of the Future"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-427970 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="427970" data-film-slug="/film/triangle-of-sadness/" data-poster-url="/film/triangle-of-sadness/image-150/" data-linked="linked" data-target-link="/film/triangle-of-sadness/" data-target-link-target="" data-cache-busting-key="8e1eb744" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Triangle of Sadness"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-669198 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="669198" data-film-slug="/film/one-fine-morning-2022/" data-poster-url="/film/one-fine-morning-2022/image-150/" data-linked="linked" data-target-link="/film/one-fine-morning-2022/" data-target-link-target="" data-cache-busting-key="0280d483" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="One Fine Morning"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-485265 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="485265" data-film-slug="/film/three-thousand-years-of-longing/" data-poster-url="/film/three-thousand-years-of-longing/image-150/" data-linked="linked" data-target-link="/film/three-thousand-years-of-longing/" data-target-link-target="" data-cache-busting-key="0c21e1b7" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Three Thousand Years of Longing"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-385511 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="385511" data-film-slug="/film/doctor-strange-in-the-multiverse-of-madness/" data-poster-url="/film/doctor-strange-in-the-multiverse-of-madness/image-150/" data-linked="linked" data-target-link="/film/doctor-strange-in-the-multiverse-of-madness/" data-target-link-target="" data-cache-busting-key="81a4fea9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Doctor Strange in the Multiverse of Madness"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-565852 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="565852" data-film-slug="/film/the-northman/" data-poster-url="/film/the-northman/image-150/" data-linked="linked" data-target-link="/film/the-northman/" data-target-link-target="" data-cache-busting-key="08820bd4" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Northman"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-456327 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="456327" data-film-slug="/film/morbius/" data-poster-url="/film/morbius/image-150/" data-linked="linked" data-target-link="/film/morbius/" data-target-link-target="" data-cache-busting-key="084000b9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Morbius"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-683285 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="683285" data-film-slug="/film/ambulance-2022/" data-poster-url="/film/ambulance-2022/image-150/" data-linked="linked" data-target-link="/film/ambulance-2022/" data-target-link-target="" data-cache-busting-key="02c94c2c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ambulance"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-574385 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="574385" data-film-slug="/film/the-unbearable-weight-of-massive-talent/" data-poster-url="/film/the-unbearable-weight-of-massive-talent/image-150/" data-linked="linked" data-target-link="/film/the-unbearable-weight-of-massive-talent/" data-target-link-target="" data-cache-busting-key="8992593c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Unbearable Weight of Massive Talent"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-673474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="673474" data-film-slug="/film/the-lost-city-2022/" data-poster-url="/film/the-lost-city-2022/image-150/" data-linked="linked" data-target-link="/film/the-lost-city-2022/" data-target-link-target="" data-cache-busting-key="87db30cd" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Lost City"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-474474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="474474" data-film-slug="/film/everything-everywhere-all-at-once/" data-poster-url="/film/everything-everywhere-all-at-once/image-150/" data-linked="linked" data-target-link="/film/everything-everywhere-all-at-once/" data-target-link-target="" data-cache-busting-key="80fbb370" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Everything Everywhere All at Once"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-438727 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="438727" data-film-slug="/film/turning-red/" data-poster-url="/film/turning-red/image-150/" data-linked="linked" data-target-link="/film/turning-red/" data-target-link-target="" data-cache-busting-key="0d037915" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Turning Red"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-620665 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="620665" data-film-slug="/film/the-adam-project/" data-poster-url="/film/the-adam-project/image-150/" data-linked="linked" data-target-link="/film/the-adam-project/" data-target-link-target="" data-cache-busting-key="8f04f942" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Adam Project"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-348914 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="348914" data-film-slug="/film/the-batman/" data-poster-url="/film/the-batman/image-150/" data-linked="linked" data-target-link="/film/the-batman/" data-target-link-target="" data-cache-busting-key="0438ab74" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Batman"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-264328 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="264328" data-film-slug="/film/uncharted-2022/" data-poster-url="/film/uncharted-2022/image-150/" data-linked="linked" data-target-link="/film/uncharted-2022/" data-target-link-target="" data-cache-busting-key="8c645cbf" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Uncharted"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-434913 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="434913" data-film-slug="/film/death-on-the-nile-2022/" data-poster-url="/film/death-on-the-nile-2022/image-150/" data-linked="linked" data-target-link="/film/death-on-the-nile-2022/" data-target-link-target="" data-cache-busting-key="8228a9e0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Death on the Nile"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-777185 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="777185" data-film-slug="/film/emily-the-criminal/" data-poster-url="/film/emily-the-criminal/image-150/" data-linked="linked" data-target-link="/film/emily-the-criminal/" data-target-link-target="" data-cache-busting-key="03df984d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Emily the Criminal"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-680635 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="680635" data-film-slug="/film/living-2022/" data-poster-url="/film/living-2022/image-150/" data-linked="linked" data-target-link="/film/living-2022/" data-target-link-target="" data-cache-busting-key="8db883ac" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Living"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-719315 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="719315" data-film-slug="/film/breaking-2022/" data-poster-url="/film/breaking-2022/image-150/" data-linked="linked" data-target-link="/film/breaking-2022/" data-target-link-target="" data-cache-busting-key="829c2ff0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Breaking"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-735545 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="735545" data-film-slug="/film/emergency-2022/" data-poster-url="/film/emergency-2022/image-150/" data-linked="linked" data-target-link="/film/emergency-2022/" data-target-link-target="" data-cache-busting-key="0a2a26ab" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Emergency"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-823432 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="823432" data-film-slug="/film/louis-ck-sorry-2021/" data-poster-url="/film/louis-ck-sorry-2021/image-150/" data-linked="linked" data-target-link="/film/louis-ck-sorry-2021/" data-target-link-target="" data-cache-busting-key="04941a73" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Louis C.K.: Sorry"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-6">★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-551275 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="551275" data-film-slug="/film/the-matrix-resurrections/" data-poster-url="/film/the-matrix-resurrections/image-150/" data-linked="linked" data-target-link="/film/the-matrix-resurrections/" data-target-link-target="" data-cache-busting-key="0d576ce2" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Matrix Resurrections"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-572255 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="572255" data-film-slug="/film/dont-look-up-2021/" data-poster-url="/film/dont-look-up-2021/image-150/" data-linked="linked" data-target-link="/film/dont-look-up-2021/" data-target-link-target="" data-cache-busting-key="8a7a1c92" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Don\'t Look Up"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-571629 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="571629" data-film-slug="/film/the-unforgivable/" data-poster-url="/film/the-unforgivable/image-150/" data-linked="linked" data-target-link="/film/the-unforgivable/" data-target-link-target="" data-cache-busting-key="8fd1eb25" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Unforgivable"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-9">★★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-466291 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="466291" data-film-slug="/film/tick-tick-boom-2021/" data-poster-url="/film/tick-tick-boom-2021/image-150/" data-linked="linked" data-target-link="/film/tick-tick-boom-2021/" data-target-link-target="" data-cache-busting-key="071f7a54" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="tick, tick...BOOM!"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-441858 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="441858" data-film-slug="/film/red-notice/" data-poster-url="/film/red-notice/image-150/" data-linked="linked" data-target-link="/film/red-notice/" data-target-link-target="" data-cache-busting-key="0ef37870" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Red Notice"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-714279 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="714279" data-film-slug="/film/army-of-thieves/" data-poster-url="/film/army-of-thieves/image-150/" data-linked="linked" data-target-link="/film/army-of-thieves/" data-target-link-target="" data-cache-busting-key="0deeede3" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Army of Thieves"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-454016 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="454016" data-film-slug="/film/eternals/" data-poster-url="/film/eternals/image-150/" data-linked="linked" data-target-link="/film/eternals/" data-target-link-target="" data-cache-busting-key="0a67ea1a" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Eternals"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-496592 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="496592" data-film-slug="/film/encanto/" data-poster-url="/film/encanto/image-150/" data-linked="linked" data-target-link="/film/encanto/" data-target-link-target="" data-cache-busting-key="8d86b9e5" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Encanto"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-544936 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="544936" data-film-slug="/film/the-harder-they-fall-2021/" data-poster-url="/film/the-harder-they-fall-2021/image-150/" data-linked="linked" data-target-link="/film/the-harder-they-fall-2021/" data-target-link-target="" data-cache-busting-key="863a9c16" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Harder They Fall"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-790798 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="790798" data-film-slug="/film/dave-chappelle-the-closer/" data-poster-url="/film/dave-chappelle-the-closer/image-150/" data-linked="linked" data-target-link="/film/dave-chappelle-the-closer/" data-target-link-target="" data-cache-busting-key="04f75162" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Dave Chappelle: The Closer"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t</ul>\n\t\t\t\t<div class="pagination"> <div class="paginate-nextprev paginate-disabled"><span class="previous">Newer</span></div> <div class="paginate-nextprev"><a class="next" href="/mrafee113/films/page/2/">Older</a></div> <div class="paginate-pages"> <ul> <li class="paginate-page paginate-current"><span>1</span></li> <li class="paginate-page"><a href="/mrafee113/films/page/2/">2</a></li> <li class="paginate-page"><a href="/mrafee113/films/page/3/">3</a></li> <li class="paginate-page unseen-pages">&hellip;</li> <li class="paginate-page"><a href="/mrafee113/films/page/10/">10</a></li> </ul> </div> </div>\n\t\t\t\n\t\t<div class="clear"></div>\n\t</section>\n\t\n\t<div class="clear"></div>\n\t\n</div>\n\n\n\n\n\n\n\n\n\n\n\t\t</div> \n\n\t\t\n\n\t</div> \n\n\n\n\t<footer id="page-footer" class="page-footer js-page-footer js-hide-in-app">\n\t\t<div class="content-wrap">\n\t\t\t\n\t\t\t\t<nav class="footer-nav js-footer-nav">\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li><a href="/about/">About</a></li>\n\t\t\t\t\t\t<li><a href="/journal/">News</a></li>\n\t\t\t\t\t\t<li class="js-hide-in-app"><a href="/pro/">Pro</a></li>\n\t\t\t\t\t\t<li><a href="/apps/">Apps</a></li>\n\t\t\t\t\t\t<li><a href="https://apple.co/3TfzHVG" target="_blank" rel="noopener noreferrer">Podcast</a></li>\n\t\t\t\t\t\t<li><a href="/year-in-review/">Year in Review</a></li>\n\t\t\t\t\t\t<li><a href="/gift-guide/">Gift Guide</a></li>\n\t\t\t\t\t\t<li><a href="/welcome/">Help</a></li>\n\t\t\t\t\t\t<li><a href="/legal/terms-of-use/">Terms</a></li>\n\t\t\t\t\t\t<li><a href="/api-beta/">API</a></li>\n\t\t\t\t\t\t<li><a href="/contact/">Contact</a></li>\n\t\t\t\t\t</ul>\n\t\t\t\t</nav>\n\t\n\n\t\t\t<div class="socials">\n\t\t\t\t<nav class="social-service-list -inline">\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://twitter.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Twitter">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="20" height="16" xmlns="http://www.w3.org/2000/svg"><path d="M17.96 4.51V4c.8-.56 1.49-1.28 2.04-2.1-.74.33-1.53.54-2.36.65.85-.5 1.5-1.3 1.8-2.24-.78.46-1.66.8-2.6.98a4.13 4.13 0 0 0-7.1 2.76c0 .31.04.62.1.92A11.72 11.72 0 0 1 1.38.74a3.99 3.99 0 0 0 1.28 5.4A4.2 4.2 0 0 1 .8 5.62v.06c0 1.95 1.42 3.59 3.29 3.96a4.06 4.06 0 0 1-1.85.07 4.1 4.1 0 0 0 3.83 2.8A8.32 8.32 0 0 1 0 14.2C1.8 15.33 3.97 16 6.28 16A11.5 11.5 0 0 0 17.96 4.51Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Twitter</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.facebook.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Facebook">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="19" height="19" xmlns="http://www.w3.org/2000/svg"><path d="M9.5 0a9.5 9.5 0 0 0-1.48 18.89V12H5.6V9.25h2.42V7.41c0-2.38 1.41-3.7 3.58-3.7 1.04 0 2.13.19 2.13.19v2.33h-1.2c-1.18 0-1.54.74-1.54 1.49v1.53h2.63L13.2 12h-2.21v6.89A9.5 9.5 0 0 0 9.5 0Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Facebook</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.instagram.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Instagram">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="20" height="20" xmlns="http://www.w3.org/2000/svg"><path d="M14.12.06c1.07.05 1.8.22 2.43.46.66.26 1.21.6 1.77 1.16.56.55.9 1.11 1.15 1.77.25.63.42 1.36.47 2.43.04.94.06 1.32.06 3.3v1.37c0 1.54 0 2.19-.03 2.77v.22l-.03.58a7.34 7.34 0 0 1-.47 2.43 4.9 4.9 0 0 1-1.15 1.77 4.9 4.9 0 0 1-1.77 1.16c-.64.24-1.36.41-2.43.46l-.61.03h-.23c-.5.02-1.06.03-2.21.03H9.2c-2 0-2.37-.02-3.32-.06a7.34 7.34 0 0 1-2.43-.46 4.9 4.9 0 0 1-1.77-1.16 4.9 4.9 0 0 1-1.16-1.77 7.34 7.34 0 0 1-.46-2.43l-.03-.61v-.2A60.9 60.9 0 0 1 0 11.5V8.75C0 7.7.01 7.17.03 6.7v-.2l.03-.61C.1 4.8.28 4.08.52 3.45a4.9 4.9 0 0 1 1.16-1.77A4.9 4.9 0 0 1 3.45.52 7.34 7.34 0 0 1 5.88.06l.61-.03h.2C7.12 0 7.6 0 8.5 0h2.74c1.62 0 2 .02 2.88.06ZM11.02 2H8.97c-1.7 0-2.05.02-2.92.06a5.4 5.4 0 0 0-1.82.33c-.45.18-.78.39-1.12.73-.34.34-.55.67-.73 1.12-.13.35-.3.86-.33 1.82C2.02 6.93 2 7.29 2 8.98v2.04c0 1.7.02 2.05.06 2.92.04.95.2 1.47.33 1.81.18.46.39.78.73 1.13.34.34.67.55 1.12.73.35.13.86.29 1.82.33.83.04 1.2.05 2.7.06h2.47c1.51 0 1.87-.02 2.71-.06a5.4 5.4 0 0 0 1.81-.33c.46-.18.78-.4 1.12-.73.35-.35.56-.67.73-1.13.14-.34.3-.86.34-1.8a49 49 0 0 0 .06-2.72V8.77a49 49 0 0 0-.06-2.71 5.4 5.4 0 0 0-.34-1.82 3.02 3.02 0 0 0-.73-1.12 3.02 3.02 0 0 0-1.12-.73 5.4 5.4 0 0 0-1.81-.33c-.88-.04-1.23-.06-2.93-.06ZM10 4.86a5.14 5.14 0 1 1 0 10.28 5.14 5.14 0 0 1 0-10.28ZM10 7a3 3 0 1 0 0 6 3 3 0 0 0 0-6Zm5.25-3.5a1.25 1.25 0 1 1 0 2.5 1.25 1.25 0 0 1 0-2.5Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Instagram</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.tiktok.com/@letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on TikTok">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="17" height="18" xmlns="http://www.w3.org/2000/svg"><path d="M16.48 4.32a4.62 4.62 0 0 1-3.92-2.66A4.04 4.04 0 0 1 12.23 0H9.07v11.85c0 1.93-1.19 3.07-2.65 3.07a2.71 2.71 0 0 1-2.04-.9 2.57 2.57 0 0 1-.6-2.1 2.55 2.55 0 0 1 1.26-1.81 2.7 2.7 0 0 1 2.24-.21V6.77a5.92 5.92 0 0 0-4.08.86 5.7 5.7 0 0 0-2.15 2.55 5.53 5.53 0 0 0 1.26 6.16 5.86 5.86 0 0 0 6.33 1.23 5.78 5.78 0 0 0 2.6-2.08c.64-.94.98-2.03.98-3.15V5.96a7.74 7.74 0 0 0 4.25 1.25V4.32Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">TikTok</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.youtube.com/letterboxdhq" target="_blank" rel="noopener noreferrer" title="Letterboxd on YouTube">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="23" height="16" xmlns="http://www.w3.org/2000/svg"><path d="M11.74 0c.61 0 2.33.02 4.11.08l.54.02c1.7.06 3.35.18 4.1.38a2.87 2.87 0 0 1 2.03 2.02c.45 1.67.48 5.04.48 5.46v.08c0 .42-.03 3.8-.48 5.46a2.87 2.87 0 0 1-2.03 2.02c-.75.2-2.4.32-4.1.38l-.54.02c-1.78.07-3.5.08-4.11.08H11.26c-.62 0-2.33-.01-4.11-.08l-.54-.02c-1.7-.06-3.36-.18-4.1-.38A2.87 2.87 0 0 1 .48 13.5C.04 11.9 0 8.68 0 8.1v-.2c0-.58.04-3.79.48-5.4A2.87 2.87 0 0 1 2.5.48c.74-.2 2.4-.32 4.1-.38l.54-.02C8.93.02 10.65 0 11.26 0ZM9 4.57v6.86L15 8 9 4.57Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">YouTube</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\t\t\t\t</nav>\n\t\t\t</div>\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t<p class="copyright">\n\t\t\t\t&copy; Letterboxd Limited. Made by <a href="/crew/" class="mute">fans</a> in Aotearoa New Zealand.\n\t\t\t\t<span class="nobr"><a href="https://letterboxd.com/about/film-data/" class="mute">Film data</a> from <a href="https://www.themoviedb.org" class="mute">TMDb</a>. \n\t\t\t\t\n\t\t\t\t\t\t<a href="#" class="mute mobile-site-switch" data-use-mobile-site="yes">Mobile&nbsp;site</a>.\n\t\t\t\t\t\n\t</span>\n\t\t\t\t<span class="recap" style="display:none"><br/>This site is protected by reCAPTCHA and the Google <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer" class="mute">privacy policy</a> and <a href="https://policies.google.com/terms" target="_blank" rel="noopener noreferrer" class="mute">terms of service</a>&nbsp;apply.</span>\n\t\t\t</p>\n\t\t</div>\n\t</footer>\n\n\t<div id="remove-ads-modal" class="modal-neue fade" tabindex="-1" aria-labelledby="remove-ads-modal-title" aria-hidden="true">\n    <div class="modal-dialog -sm modal-dialog-centered">\n        <div class="modal-content">\n            <div class="modal-header">\n                <h5 class="modal-title" id="remove-ads-modal-title">Upgrade to remove&nbsp;ads</h5>\n                <button type="button" class="close" data-bs-dismiss="modal-neue" aria-label="Close">\n                    <svg class="glyph" width="16" height="16" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd" stroke-linecap="round" stroke="#000" stroke-width="2"><path d="m1 1 14 14M1 15 15 1"/></g></svg>\n                </button>\n            </div>\n            <div class="modal-body">\n                <div class="body-text -hero">\n                    <p>Letterboxd is an independent service created by a small team, and we rely mostly on the support of our members to maintain our site and apps. Please consider upgrading to a <a href="/pro/">Pro account</a>—for less than a couple bucks a month, you’ll get cool additional features like all-time and annual stats pages (<a href="https://letterboxd.com/jack/stats/">example</a>), the ability to select (and filter by) your favorite streaming services, and no ads!</p>\n                </div>\n            </div>\n            <div class="modal-footer">\n                <a href="/pro/" class="button -action button-action">Learn more about Pro</a>\n            </div>\n        </div>\n    </div>\n</div>\n\t\n\n\n\n\n\n\n<form id="poster-picker-modal" class="modal-neue fade poster-picker-modal" method="post" action="" novalidate="novalidate" tabindex="-1" role="dialog" aria-labelledby="poster-picker-modal-title" aria-hidden="true" data-bs-backdrop="static">\n    <div class="modal-dialog -lg modal-dialog-centered modal-dialog-scrollable">\n        <div class="modal-content">\n            <div class="modal-header">\n                <h5 class="modal-title" id="poster-picker-modal-title">Select your preferred poster</h5>\n                <button type="button" class="close" data-bs-dismiss="modal-neue" aria-label="Close">\n                    <svg class="glyph" width="16" height="16" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd" stroke-linecap="round" stroke="#000" stroke-width="2"><path d="m1 1 14 14M1 15 15 1"></path></g></svg>\n                </button>\n            </div>\n            <div class="modal-body">\n                <div id="poster-picker-b427140c-d820-493e-a8cf-bb50fce997b3" data-poster-picker-options=\'{"id": "b427140c-d820-493e-a8cf-bb50fce997b3"}\' data-js-target="poster-picker"></div>\n            </div>\n            <div class="modal-footer">\n                <div class="poster-picker-note">\n                    <div class="body-text -small">\n                        \n<p>Posters are sourced from <a href="https://www.themoviedb.org" target="_blank">TMDb</a> and <a href="https://posteritati.com" target="_blank">Posteritati</a>, and appear for you and visitors to your profile and content, depending on settings. <a href="https://letterboxd.com/journal/posterity-custom-posters/" target="_blank">Learn more.</a></p>\n\n                    </div>\n                </div>\n\n                <div class="poster-picker-controls" data-poster-picker-controls-for="b427140c-d820-493e-a8cf-bb50fce997b3">\n                    <div class="modal-action-group -center">\n                        <button class="button -destructive" type="button" data-js-trigger="reset" disabled><span class="label">Reset poster</span></button>\n                        <button class="button -action" type="submit" data-js-trigger="submit" disabled><span class="label">Save<span class="mob-hide"> changes</span></span></button>\n                    </div>\n                    \n                </div>\n            </div>\n        </div>\n    </div>\n</form>\n\t\n\t\n</body>\n</html>'

In [96]: len(doc.xpath(f'/html/body//img[@class="img"]'))
Out[96]: 0

In [97]: len(doc.xpath(f'/html/body//img[@class="imgage"]'))
Out[97]: 0

In [98]: len(doc.xpath(f'/html/body//img[@class="image"]'))
Out[98]: 72

In [99]: for i in doc.xpath(f'/html/body//img[@class="image"]'):
    ...:     print(i.text_content())
    ...: 









































































In [100]: for i in doc.xpath(f'/html/body//img[@class="image"]'):
     ...:     print(i.attrib['alt'])
     ...: 
Mafia Mamma
Louis C.K. at The Dolby
Renfield
Shazam! Fury of the Gods
Dungeons & Dragons: Honor Among Thieves
Champions
Kill Boksoon
Ant-Man and the Wasp: Quantumania
Knock at the Cabin
Mummies
Operation Fortune: Ruse de Guerre
Puss in Boots: The Last Wish
Strange World
Enola Holmes 2
Black Panther: Wakanda Forever
Amsterdam
Confess, Fletch
Wendell & Wild
Causeway
The Fabelmans
The Menu
Glass Onion
The Lost King
See How They Run
Pinocchio
The Banshees of Inisherin
TÁR
White Noise
Day Shift
One Piece Film Red
The Gray Man
Bullet Train
Minions: The Rise of Gru
The Man from Toronto
Thor: Love and Thunder
Vesper
The Sea Beast
Vengeance
Lightyear
Close
Ricky Gervais: SuperNature
Crimes of the Future
Triangle of Sadness
One Fine Morning
Three Thousand Years of Longing
Doctor Strange in the Multiverse of Madness
The Northman
Morbius
Ambulance
The Unbearable Weight of Massive Talent
The Lost City
Everything Everywhere All at Once
Turning Red
The Adam Project
The Batman
Uncharted
Death on the Nile
Emily the Criminal
Living
Breaking
Emergency
Louis C.K.: Sorry
The Matrix Resurrections
Don't Look Up
The Unforgivable
tick, tick...BOOM!
Red Notice
Army of Thieves
Eternals
Encanto
The Harder They Fall
Dave Chappelle: The Closer

In [101]: content
Out[101]: '\n\n<!DOCTYPE html>\n\n<!--[if lt IE 7 ]> <html lang="en" class="ie6 lte9 lte8 lte7 lte6 no-js"> <![endif]-->\n<!--[if IE 7 ]>    <html lang="en" class="ie7 lte9 lte8 lte7 no-js"> <![endif]-->\n<!--[if IE 8 ]>    <html lang="en" class="ie8 lte9 lte8 no-js"> <![endif]-->\n<!--[if IE 9 ]>    <html lang="en" class="ie9 lte9 no-js"> <![endif]-->\n<!--[if (gt IE 9)|!(IE)]><!--> <html id="html" lang="en" class="no-mobile no-js"> <!--<![endif]-->\n<head>\n\t<meta charset="UTF-8" />\n\t<meta name="viewport" content="width=1024" />\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />\n\t<meta name="description" content="Mehdi Rafee’s films" />\n\t\n\t\n\t<meta property="og:url" content="https://letterboxd.com/mrafee113/films/?html.parser" />\n\t<meta property="og:title" content="Mehdi Rafee’s films" />\n\t<meta property="og:description" content="Mehdi Rafee’s films" />\n\t<meta property="og:image" content="https://s.ltrbxd.com/static/img/default-share.e38c5d62.png" />\n\t\n\t<meta name="application-name" content="Letterboxd" />\n\t<meta name="theme-color" content="#445566" />\n\t<meta name="msapplication-TileColor" content="#445566" />\n\t<meta name="apple-itunes-app" content="app-id=1054271011, affiliate-data=11l5KW, app-argument=https://letterboxd.com/mrafee113/films/?html.parser" />\n\t<meta name="mobile-web-app-capable" content="yes" />\n\n\t<title>&lrm;Mehdi Rafee’s films &bull; Letterboxd</title>\n\t\n\t<script>\n\t\twindow.dataLayer = window.dataLayer || [];\n\t\twindow.gtag = window.gtag || function () {\n\t\t\tdataLayer.push(arguments);\n\t\t};\n\t\tfunction ga() {}\n\t</script>\n\n\t<script async src="https://www.googletagmanager.com/gtag/js?id=G-D3ECBB4D7L"></script>\n\n\t<script>\n\t\twindow.dataLayer = window.dataLayer || [];\n\t\twindow.gtag = window.gtag || function () {\n\t\t\tdataLayer.push(arguments);\n\t\t};\n\t\tgtag(\'js\', new Date());\n\t\n\t\tvar analytic_params = {};\n\t\t\n\t\t\n\t\tanalytic_params[\'user_type\'] = \'Visitor\';\n\t\tanalytic_params[\'template\'] = \'/object/person/films-watched\';\n\t\t\n\t\t\n\n\t\tif (analytic_params.member_type) {\n\t\t\tgtag(\'set\', \'user_properties\', { \n\t\t\t\tmember_type: analytic_params.member_type,\n\t\t\t});\n\t\t\tdelete analytic_params.member_type;\n\t\t}\n\t\tvar config = {\n\t\t\t...analytic_params,\n\t\t\t\'cookie_domain\': \'letterboxd.com\', \n\t\t\t\'optimize_id\': \'GTM-TB8HSDN\', \n\t\t};\n\t\tgtag(\'config\', \'G-D3ECBB4D7L\', config);\n\t</script>\n\n\n\t<script>\n\t\tvar isMobile = false,\n\t\t\tisMobileOptimised = true,\n\t\t\trenderMobile = false,\n\t\t\tuseStaticFonts = false,\n\t\t\tdisableFrameProtection = false,\n\t\t\tbaseURL = "",\n\t\t\tsuccessMessages = [],\n\t\t\terrorMessages = [],\n\t\t\tstickyMessages = [],\n\t\t\tglobals = {\n\t\t\tautoAddFilm: false\t\t\t\n\t\t\t\t, spinners: {\n\t\t\t\t\tajax_242d35: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_12_2C3641: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_14_20272f: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\',\n\t\t\t\t\tspinner_16_161B21: \'https://s.ltrbxd.com/static/img/spinner-dark-2x.fda24f88.gif\'\n\t\t\t\t}\n\t\t\t},\n\t\t\tsupermodelCSRF = "",\n\t\t\tgRecaptchaKey = \'6Le3mMIUAAAAAEXbwZ7M1R5jEv0V5xbvj7bgXq2g\',\n\t\t\tperson = {\n\t\t\t\tusername: ""\n\t\t\t\t, loggedIn: false\n\t\t\t\t\n\t\t\t\t, showAds: true\n\t\t\t\t, role: "guest"\n\t\t\t\t, hasExtendedServiceFilters: false\n\t\t\t\t, canBulkAddToLists: false\n\t\t\t\t, canFilterOwned: false\n\t\t\t\t, hasHqRole: false\n\t\t\t\t, canHaveHqDashboard: false\n\t\t\t\t, hasMemberStatistics: false\n\t\t\t\t, blockedMembers: []\n\t\t\t\t, showAdultContent: false\n\t\t\t\t, validated: null\n\t\t\t\t, trusted: false\n\t\t\t\t, hasBlocked : function(member) { for (var i = 0; i !== person.blockedMembers.length; i++) {if (person.blockedMembers[i] === member) return true;} return false; }\n\t\t\t\t, viewingTags: []\n\t\t\t\t, hasMoreTags: true\n\t\t\t\t, getCustomPoster : function(filmId) { return null; }\n\t\t\t},\n\t\t\tdisableAds = true;\n\t\t\n\t\t\n\t\t\nsupermodelCSRF = "9749e0a0bd2da01647eb";\n\n\t\t\n\n\t\t\n\n\t\t\n\n\t\t\n\t\t\tif ( screen.width < 768 ) {\n\t\t\t\tvar date = new Date();\n\t\t\t\tvar maxAge = 365 * 24 * 60 * 60;\n\t\t\t\tdate.setTime(date.getTime() + maxAge * 1000);\n\t\t\t\tvar expires = \'; expires=\' + date.toUTCString();\n\t\t\t\tdocument.cookie = "useMobileSite=yes" + expires + "; path=/; maxAge=" + maxAge;\n\t\t\t\tif ( document.cookie && document.cookie.indexOf("useMobileSite=yes") >= 0 ) {\n\t\t\t\t\twindow.location.reload(true);\n\t\t\t\t} else {\n\t\t\t\t\t// No cookies.  No Mobile version.\n\t\t\t\t}\n\t\t\t}\n\t\t\n\n\t\tvar isWindows = navigator.platform.toUpperCase().indexOf(\'WIN\') >= 0; // Detect windows platform\n\t\tif (isWindows) { document.documentElement.classList.add(\'is-windows\'); }\n\t\t\n\t\t\n\t</script>\n\n\t<link rel="manifest" href="/manifest.json" />\n\t<link rel="author" type="text/plain" href="/humans.txt" />\n\t<link rel="mask-icon" href="https://s.ltrbxd.com/static/img/icons/letterboxd-decal-l-16px.5fe24c7d.svg" color="#445566" />\n\t<link rel="shortcut icon" sizes="196x196" href="https://s.ltrbxd.com/static/img/icons/touch-icon-192x192.257b84e7.png" />\n\t<link rel="shortcut icon" href="/favicon.ico" />\n\t<link rel="search" type="application/opensearchdescription+xml" title="Letterboxd" href="/static/opensearch.xml" />\n\t\n\t\n\t<!--[if lte IE 9 ]>\n\t\t<link href="https://s.ltrbxd.com/static/css/ie9-1.min.066b855d.css" rel="stylesheet" media="screen, projection"/>\n\t\t<link href="https://s.ltrbxd.com/static/css/ie9-2.min.13b2f50c.css" rel="stylesheet" media="screen, projection"/>\n\t<![endif]-->\n\t<!--[if (gt IE 9)|!(IE)]><!-->\n\t\t<link href="https://s.ltrbxd.com/static/css/main.min.97414920.css" rel="stylesheet" media="screen, projection"/>\n\t<!--<![endif]-->\n\t<!--[if lte IE 6]><script>location.replace("/errors/ie6");</script><![endif]-->\n\t<!--[if IE 7]><script>location.replace("/errors/ie7");</script><![endif]-->\n\t<!--[if IE 8]><script>location.replace("/errors/ie8");</script><![endif]-->\n\t<!--[if IE 9]><script>location.replace("/errors/ie9");</script><![endif]-->\n\t\n\t\n\t\n\t<link href="https://s.ltrbxd.com/static/css/desktop.min.e1d8f367.css" rel="stylesheet" media="screen, projection"/>\n\n\t<script src="https://s.ltrbxd.com/static/js/main.min.a7e00d04.js"></script>\n\t\n\n\n\n\n\n\t<script>\n\t\tif ( $.cookie("letterboxd.admin.signed.in") === person.username ) {\n\t\t\tsuccessMessages.push("You are signed in as " + person.username);\n\t\t\t$(function(){$("#header, #content, body").css("background","#543");});\n\t\t}\n\t</script>\n\t\n</head>\n\n<body class="films-watched wide small-poster-grid" data-owner="mrafee113">\n\t\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<script>\nvar mainMenu = [];\n\n\t\n\tmainMenu.push({\n\t\t"id": 1,\n\t\t"url": "/sign-in/", \n\t\t"name": "Sign In",\n\t\t"cssClassCode": "sign-in-menu",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": true,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 2,\n\t\t"url": "/create-account/", \n\t\t"name": "Create Account",\n\t\t"cssClassCode": "create-account-menu",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 3,\n\t\t"url": "/", \n\t\t"name": "Home",\n\t\t"cssClassCode": "person-home",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 4,\n\t\t"url": "/activity/", \n\t\t"name": "Activity",\n\t\t"cssClassCode": "main-nav-activity",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "Activity",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 5,\n\t\t"url": "/films/", \n\t\t"name": "Films",\n\t\t"cssClassCode": "films-page main-nav-films",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 6,\n\t\t"url": "/lists/", \n\t\t"name": "Lists",\n\t\t"cssClassCode": "lists-page main-nav-lists",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 7,\n\t\t"url": "/members/", \n\t\t"name": "Members",\n\t\t"cssClassCode": "main-nav-people",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 8,\n\t\t"url": "/journal/", \n\t\t"name": "Journal",\n\t\t"cssClassCode": "main-nav-journal",\n\t\t"hideWhenSignedIn": false,\n\t\t"hideWhenNotSignedIn": false,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n\t\n\tmainMenu.push({\n\t\t"id": 9,\n\t\t"url": "/search/", \n\t\t"name": "Search results",\n\t\t"cssClassCode": "",\n\t\t"hideWhenSignedIn": true,\n\t\t"hideWhenNotSignedIn": true,\n\t\t"showInMainNavForMobile": false,\n\t\t"tooltip": "",\n\t\t"selected": false\n\t});\n\n</script>\n\n<header class="site-header js-hide-in-app" id="header" data-allow-user-to-add-all-films-to-a-list="true">\n\t<div class="site-header-bg"></div>\n\t<section>\n\t\t<h1 class="site-logo"><a href="/" class="logo replace">Letterboxd &mdash; Your life in film</a></h1>\n\n\t\t<div class="react-component" data-component-class="globals.comps.NavComponent"></div>\n\n\t\t\n\t\t\t\n\t\t\t\n\n\n\t\n\n\n\n\n\n<form method="post" action="#" id="signin" class="signin signin-form js-header-signin-form js-signin" data-url="/user/login.do" data-recaptcha-action="signin" novalidate=\'novalidate\' autocorrect=\'off\' autocapitalize=\'off\'>\n\t<input type="hidden" name="__csrf" value="placeholder" />\n\t<fieldset class="fieldset">\n\t\t<div class="fields">\n\t\t\t<div class="col">\n\t\t\t\t<label for="username">Username or Email</label>\n\t\t\t\t<input type="email" name="username" id="username" class="field signin-field" tabindex="1" data-focus-control="signingIn" autocomplete=\'email\' inputmode=\'email\' value="" />\n\t\t\t</div>\n\t\t\t<div class="col">\n\t\t\t\t<label for="password">Password</label>\n\t\t\t\t<input type="password" name="password" id="password" class="field signin-field" tabindex="2" autocomplete=\'current-password\' value="" />\n\t\t\t</div>\n\t\t\t<div class="signin-actions">\n\t\t\t\t<label for="remember" class="option-label -checkbox -small">\n\t\t\t\t\t<input type="checkbox" name="remember" id="remember" class="checkbox" tabindex="3" value="true" /><i class="substitute"></i>\n\t\t\t\t\t<span class="focus">Remember<span class="mob-hide"> me</span></span>\n\t\t\t\t</label>\n\t\t\t\t<p class="reset" tabindex="5"><a class="reset-password-link" href="/user/request-password-reset" target="_top">Forgotten<span class="elongated"> password</span>?</a></p>\n\t\t\t</div>\n\t\t\t<div class="col buttons">\n\t\t\t\t<div class="button-container"><input type="submit" value="Sign in" class="button -action button-green" tabindex="4" /><i></i></div>\n\t\t\t\t<div class="close js-close-signin">&times;</div>\n\t\t\t</div>\n\t\t</div>\n\t</fieldset>\n\t<div id="signin-message" class="errormessage"></div>\n</form>\n\n\n\t\t\n\t\t\n\t\t\n\t\t\t\n\t\t\t\n\n\n\n\t\t\n\t\t\n\t\t\n\t\t<form id="search" class="js-search-form search-form" action="/search/" method="get" autocorrect="off">\n\t\t\t<input autocomplete="false" name="hidden" type="text" style="display:none;" />\n\t\t\t<fieldset>\n\t\t\t\t<label for="search-q" class="hidden">Search:</label>\n\t\t\t\t<input type="text" name="q" id="search-q" class="field -borderless" data-lpignore=\'true\' inputmode=\'search\' value="" />\n\t\t\t\t<input type="submit" value="Search" class="action" />\n\t\t\t</fieldset>\n\t\t</form>\n\t\t\n\t</section>\n</header>\n\n\n\n\n\n\n<div id="content" class="site-body">\n\t\n\t<div class="content-wrap">\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<section id="profile-header" class="js-profile-header -is-mini-nav" data-person="mrafee113">\n\t\n\n\t<nav class="profile-navigation">\n\t\t\n\t\t\t<div class="profile-mini-person">\n\t\t\t\t<a class="avatar -a24" href="/mrafee113/" > <img src="https://a.ltrbxd.com/resized/avatar/upload/1/4/4/4/1/0/3/shard/avtr-0-48-0-48-crop.jpg?v=484d4bfb0a" alt="Mehdi Rafee" width="24" height="24" /> </a>\n\t\t\t\t<h1 class="title-3"><a href="/mrafee113/">Mehdi Rafee</a></h1>\n\t\t\t\t\n\t\t\t</div>\n\t\t\n\t\t\n\t\t\t<ul class="navlist">\n\t\t\t\t\n\n\t\t\t\t\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem hide-for-owner"><a class="navlink" href="/mrafee113/activity/">Activity</a></li>\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/activity/">Activity</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem -active"><a class="navlink" href="/mrafee113/films/">Films</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/films/diary/">Diary</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/films/reviews/">Reviews</a></li>\n\n\t\t\t\t<li class="navitem" data-owner="mrafee113"><a class="navlink" href="/mrafee113/watchlist/" >Watchlist</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/mrafee113/lists/">Lists</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/likes/">Likes</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem show-for-owner"><a class="navlink" href="/mrafee113/tags/">Tags</a></li>\n\n\t\t\t\t<li data-owner="mrafee113" class="navitem"><a class="navlink" href="/mrafee113/following/">Network</a></li>\n\n\t\t\t\t\n\n\t\t\t\t\n\n\t\t\t\t\n\n\n\n\t<li data-owner="mrafee113" class="navitem show-when-logged-in hide-for-owner"><a class="navlink" href="/pro/gift/mrafee113/">Gift Pro</a></li>\n\n\n\t\t\t\t<li class="navitem -rss">\n\t\t\t\t\t<a href="/mrafee113/rss/" class="has-icon icon-16 icon-rss tooltip" title="RSS feed">\n\t\t\t\t\t\t<span class="_sr-only">RSS feed for Mehdi</span>\n\t\t\t\t\t</a>\n\t\t\t\t</li>\n\t\t\t</ul>\n\t\t\n    </nav>\n</section>\n\n\n \n\n\n\n<div class="cols-2 overflow">\n\t<section class="section col-main overflow">\n\t\n \t\t\n\n<div id="content-nav" class="tabbed"> <section class="sub-nav-wrapper"><ul class="sub-nav"> <li class=" selected"><a href="/mrafee113/films/" class="tooltip" title="690&nbsp;films">Watched</a></li> <li class=""><a href="/mrafee113/films/diary/" class="tooltip" title="254&nbsp;films">Diary</a></li> <li class=""><a href="/mrafee113/films/reviews/" class="tooltip" title="45&nbsp;films">Reviews</a></li> </ul></section> <div class="sorting-selects has-hide-toggle"> <section class="grid-toggle-menu mob-hide"> <ul> <li class="selected"><a href="/mrafee113/films/" class="grid-toggle ir s grid-toggle-small" data-toggle="large">Small</a></li> <li><a href="/mrafee113/films/size/large/" class="grid-toggle ir s grid-toggle-large" data-toggle="small">Large</a></li> </ul> </section> <section class="smenu-wrapper hide-toggle-menu"> <div class="smenu"> <label><span class="ir s hide-toggle-icon">Visibility Filters</span><i class="ir s icon"></i></label> <ul class="smenu-menu" id="hide-toggle-menu"> <li class="divider-line-below"><a href="#" class="item js-film-filter-remover">Remove filters</a></li> <li class="js-account-filters"> <label class="option-label -toggle -small switch-control js-fade-toggle"> <span class="label">Fade watched films</span> <input class="checkbox" type="checkbox" checked="checked" role="switch" /><span class="state"><span class="track"><span class="handle"></span></span></span> </label> </li> <li class="js-account-filters"> <label class="option-label -toggle -small switch-control js-custom-poster-toggle" data-action="/ajax/poster-mode/"> <span class="label">Show custom posters</span> <input class="checkbox" type="checkbox" checked="checked" role="switch" /><span class="state"><span class="track"><span class="handle"></span></span></span> </label> </li> <li class="divider-line js-account-filters"> <span class="smenu-sublabel -uppercase">Custom posters</span> <div class="segmented-control -small custom-poster-control js-custom-poster-control" role="group" aria-label="Change custom poster visibility" data-action="/ajax/poster-mode/"> <div class="options"> <button type="button" class="option" data-js-trigger="option" data-value="All">Any</button> <button type="button" class="option" data-js-trigger="option" data-value="Theirs">Theirs</button> <button type="button" class="option" data-js-trigger="option" data-value="Yours">Yours</button> <button type="button" class="option" data-js-trigger="option" data-value="None">None</button> </div> </div> </li> <li class="divider-line js-account-filters"> <span class="smenu-sublabel -uppercase">Account Filters</span> <ul> <li class="js-film-filter" data-category="watched" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show watched films</a></li> <li class="js-film-filter" data-category="watched" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide watched films</a></li> <li class="js-film-filter divider-line -inset" data-category="liked" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show liked films</a></li> <li class="js-film-filter" data-category="liked" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide liked films</a></li> <li class="js-film-filter divider-line -inset" data-category="rated" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show rated films</a></li> <li class="js-film-filter" data-category="rated" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide rated films</a></li> <li class="js-film-filter divider-line -inset" data-category="logged" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show logged films</a></li> <li class="js-film-filter" data-category="logged" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide logged films</a></li> <li class="js-film-filter divider-line -inset" data-category="rewatched" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show rewatched films</a></li> <li class="js-film-filter" data-category="rewatched" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide rewatched films</a></li> <li class="js-film-filter divider-line -inset" data-category="reviewed" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show reviewed films</a></li> <li class="js-film-filter" data-category="reviewed" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide reviewed films</a></li> <li class="js-film-filter divider-line -inset" data-category="watchlisted" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films in watchlist</a></li> <li class="js-film-filter" data-category="watchlisted" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films in watchlist</a></li> <li class="js-film-filter divider-line -inset" data-category="owned" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films you own</a></li> <li class="js-film-filter" data-category="owned" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films you own</a></li> <li class="js-film-filter divider-line -inset" data-category="customised" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films you’ve customized</a></li> <li class="js-film-filter" data-category="customised" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films you’ve customized</a></li> </ul> </li> <li class="divider-line js-film-filters"> <span class="smenu-sublabel -uppercase">Content Filters</span> <ul> <li class="js-film-filter" data-category="shorts" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show short films</a></li> <li class="js-film-filter" data-category="shorts" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide short films</a></li> <li class="js-film-filter divider-line -inset" data-category="tv" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show TV shows</a></li> <li class="js-film-filter" data-category="tv" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide TV shows</a></li> <li class="js-film-filter divider-line -inset" data-category="docs" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide documentaries</a></li> <li class="js-film-filter divider-line -inset" data-category="unreleased" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide unreleased titles</a></li> <li class="js-film-filter divider-line -inset" data-category="obscure" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show obscure films</a></li> <li class="js-film-filter" data-category="obscure" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide obscure films</a></li> <li class="js-film-filter divider-line -inset" data-category="backdropped" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show films with backdrop</a></li> <li class="js-film-filter" data-category="backdropped" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide films with backdrop</a></li> <li class="js-film-filter divider-line -inset" data-category="nanocrowd" data-type="show"><a class="item" href="#"><i class="ir s icon"></i>Show Nanocrowd films</a></li> <li class="js-film-filter" data-category="nanocrowd" data-type="hide"><a class="item" href="#"><i class="ir s icon"></i>Hide Nanocrowd films</a></li> </ul> </li> </ul> </div> </section> <section class="smenu-wrapper"> <strong class="smenu-label">Sort by</strong> <div class="smenu"> <label>Release Date<i class="ir s icon"></i></label> <ul class="smenu-menu"> <li class=""><a class="item" href="/mrafee113/films/by/name/">Film Name</a></li> <li class=""><a class="item" href="/mrafee113/films/by/popular/">Film Popularity</a></li> <li class=""><a class="item" href="/mrafee113/films/by/shuffle/">Shuffle</a></li> <li class=""><span class="smenu-sublabel">When Added</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/date/">Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/date-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">When Rated</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/rated-date/">Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/rated-date-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Release Date</span> <ul> <li class=" smenu-subselected"><a class="item" href="/mrafee113/films/"><i class="ir s icon"></i>Newest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/release-earliest/">Earliest First</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Average Rating</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/rating/">Highest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/rating-lowest/">Lowest First</a></li> </ul></li> <li class="" data-owner="mrafee113"><span class="smenu-sublabel" data-owner="mrafee113" data-owner-label="Your Rating">Mehdi’s Rating</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/entry-rating/">Highest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/entry-rating-lowest/">Lowest First</a></li> </ul></li> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><span class="smenu-sublabel">Your Rating</span> <ul> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><a class="item" href="/mrafee113/films/by/your-rating/">Highest First</a></li> <li class=" show-when-logged-in hide-for-owner" data-owner="mrafee113"><a class="item" href="/mrafee113/films/by/your-rating-lowest/">Lowest First</a></li> </ul></li> <li class=" show-when-logged-in"><span class="smenu-sublabel">Your Interests</span> <ul> <li class=" show-when-logged-in"><a class="item" href="/mrafee113/films/by/your-interest-liked/">Based on films you liked</a></li> <li class=" show-when-logged-in"><a class="item" href="/mrafee113/films/by/your-interest-related/">Related to films you liked</a></li> </ul></li> <li class=""><span class="smenu-sublabel">Film Length</span> <ul> <li class=""><a class="item" href="/mrafee113/films/by/shortest/">Shortest First</a></li> <li class=""><a class="item" href="/mrafee113/films/by/longest/">Longest First</a></li> </ul></li> </ul> </div> </section> \n<section class="smenu-wrapper"> <div class="smenu"> <label>Service<i class="ir s icon"></i></label> <ul id="services-menu" class="smenu-menu" data-upgrade-url="/pro/"> <li class="availability- smenu-subselected"> <span class="selected"> All films </span> </li> <li class="divider-line availability-amazon"> <a class="item" href="/mrafee113/films/on/amazon-deu/"> Amazon DE </a> </li> <li class="availability-amazon-video"> <a class="item" href="/mrafee113/films/on/amazon-video-de/"> Amazon Video DE </a> </li> <li class="availability-apple-tv-plus"> <a class="item" href="/mrafee113/films/on/apple-tv-plus-de/"> Apple TV Plus DE </a> </li> <li class="availability-apple-itunes"> <a class="item" href="/mrafee113/films/on/apple-itunes-de/"> iTunes DE </a> </li> <li class="note divider-line -upgrade"> <p>Upgrade to a <a href="/pro/">Letterboxd <span class="badge -pro -small">Pro</span></a> account to add your favorite services to this list—including any service and country pair listed on JustWatch—and to enable one-click filtering by all your favorites.</p></li> <li><a class="item item-small" href="https://www.justwatch.com" target="_blank" rel="noopener noreferrer"><small>Powered by JustWatch</small></a></li> </ul> </div> </section>\n <section class="smenu-wrapper"> <div class="smenu"> <label> Genre<i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><span class="selected">Any genre</span></li> <li class="divider-line"> <ul> <li class=""><a class="item" href="/mrafee113/films/genre/action/"><i class="ir s icon"></i>Action</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/adventure/"><i class="ir s icon"></i>Adventure</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/animation/"><i class="ir s icon"></i>Animation</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/comedy/"><i class="ir s icon"></i>Comedy</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/crime/"><i class="ir s icon"></i>Crime</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/documentary/"><i class="ir s icon"></i>Documentary</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/drama/"><i class="ir s icon"></i>Drama</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/family/"><i class="ir s icon"></i>Family</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/fantasy/"><i class="ir s icon"></i>Fantasy</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/history/"><i class="ir s icon"></i>History</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/horror/"><i class="ir s icon"></i>Horror</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/music/"><i class="ir s icon"></i>Music</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/mystery/"><i class="ir s icon"></i>Mystery</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/romance/"><i class="ir s icon"></i>Romance</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/science-fiction/"><i class="ir s icon"></i>Science Fiction</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/thriller/"><i class="ir s icon"></i>Thriller</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/tv-movie/"><i class="ir s icon"></i>TV Movie</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/war/"><i class="ir s icon"></i>War</a></li> <li class=""><a class="item" href="/mrafee113/films/genre/western/"><i class="ir s icon"></i>Western</a></li> </ul> </li> </ul> </div> </section> <section class="smenu-wrapper"> <div class="smenu"> <label class="x"> Decade<i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><span class="selected">Any decade</span></li> <li class="divider-line "><a class="item" href="/mrafee113/films/decade/2020s/">2020s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/2010s/">2010s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/2000s/">2000s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1990s/">1990s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1980s/">1980s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1970s/">1970s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1960s/">1960s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1950s/">1950s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1940s/">1940s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1930s/">1930s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1920s/">1920s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1910s/">1910s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1900s/">1900s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1890s/">1890s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1880s/">1880s</a></li> <li class=""><a class="item" href="/mrafee113/films/decade/1870s/">1870s</a></li> </ul> </div> </section> <section class="smenu-wrapper"> <div class="smenu"> <label> Rating <i class="ir s icon"></i> </label> <ul class="smenu-menu"> <li class="smenu-subselected"><a class="item" href="/mrafee113/films/">Any rating</a></li> <li><a class="item" href="/mrafee113/films/rated/none/">No rating</a></li> <li class="divider-line"> <span class="smenu-sublabel -uppercase">Rating (or range)</span> <div class="menu-rating-filter js-rating-filter" data-rateit-starwidth="10" data-rateit-starheight="19" data-action="/mrafee113/films/rated/%7B%7Bvalue%7D%7D/"> <div class="rateit-range"> <div class="rateit-selected"></div> <div class="rateit-hover"></div> </div> </div> <small class="note">Drag to define range</small> </li> </ul> </div> </section> </div> <div class="clear"></div> </div>\n\t\n\t\t\n\n\t\n\t\t\n\t\t\t\t\n\n\t\t\t\t<ul class="poster-list -p70 -grid film-list clear">\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-726680 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="726680" data-film-slug="/film/mafia-mamma/" data-poster-url="/film/mafia-mamma/image-150/" data-linked="linked" data-target-link="/film/mafia-mamma/" data-target-link-target="" data-cache-busting-key="20289f53" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Mafia Mamma"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-998520 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="998520" data-film-slug="/film/louis-ck-at-the-dolby/" data-poster-url="/film/louis-ck-at-the-dolby/image-150/" data-linked="linked" data-target-link="/film/louis-ck-at-the-dolby/" data-target-link-target="" data-cache-busting-key="93b11804" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Louis C.K. at The Dolby"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-6">★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-575258 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="575258" data-film-slug="/film/renfield/" data-poster-url="/film/renfield/image-150/" data-linked="linked" data-target-link="/film/renfield/" data-target-link-target="" data-cache-busting-key="d129ad49" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Renfield"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-522405 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="522405" data-film-slug="/film/shazam-fury-of-the-gods/" data-poster-url="/film/shazam-fury-of-the-gods/image-150/" data-linked="linked" data-target-link="/film/shazam-fury-of-the-gods/" data-target-link-target="" data-cache-busting-key="1e7571ce" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Shazam! Fury of the Gods"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-424003 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="424003" data-film-slug="/film/dungeons-dragons-honor-among-thieves/" data-poster-url="/film/dungeons-dragons-honor-among-thieves/image-150/" data-linked="linked" data-target-link="/film/dungeons-dragons-honor-among-thieves/" data-target-link-target="" data-cache-busting-key="5c7797c4" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Dungeons & Dragons: Honor Among Thieves"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-838520 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="838520" data-film-slug="/film/champions-2023/" data-poster-url="/film/champions-2023/image-150/" data-linked="linked" data-target-link="/film/champions-2023/" data-target-link-target="" data-cache-busting-key="d119d8a2" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Champions"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-764596 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="764596" data-film-slug="/film/kill-boksoon/" data-poster-url="/film/kill-boksoon/image-150/" data-linked="linked" data-target-link="/film/kill-boksoon/" data-target-link-target="" data-cache-busting-key="280be804" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Kill Boksoon"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-566237 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="566237" data-film-slug="/film/ant-man-and-the-wasp-quantumania/" data-poster-url="/film/ant-man-and-the-wasp-quantumania/image-150/" data-linked="linked" data-target-link="/film/ant-man-and-the-wasp-quantumania/" data-target-link-target="" data-cache-busting-key="df5c617e" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ant-Man and the Wasp: Quantumania"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-558056 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="558056" data-film-slug="/film/knock-at-the-cabin/" data-poster-url="/film/knock-at-the-cabin/image-150/" data-linked="linked" data-target-link="/film/knock-at-the-cabin/" data-target-link-target="" data-cache-busting-key="2e6ced50" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Knock at the Cabin"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-733385 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="733385" data-film-slug="/film/mummies-2023/" data-poster-url="/film/mummies-2023/image-150/" data-linked="linked" data-target-link="/film/mummies-2023/" data-target-link-target="" data-cache-busting-key="fb56ca62" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Mummies"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-661153 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="661153" data-film-slug="/film/operation-fortune-ruse-de-guerre/" data-poster-url="/film/operation-fortune-ruse-de-guerre/image-150/" data-linked="linked" data-target-link="/film/operation-fortune-ruse-de-guerre/" data-target-link-target="" data-cache-busting-key="8d72bd57" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Operation Fortune: Ruse de Guerre"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-242285 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="242285" data-film-slug="/film/puss-in-boots-the-last-wish/" data-poster-url="/film/puss-in-boots-the-last-wish/image-150/" data-linked="linked" data-target-link="/film/puss-in-boots-the-last-wish/" data-target-link-target="" data-cache-busting-key="d60f4abc" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Puss in Boots: The Last Wish"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-789082 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="789082" data-film-slug="/film/strange-world-2022/" data-poster-url="/film/strange-world-2022/image-150/" data-linked="linked" data-target-link="/film/strange-world-2022/" data-target-link-target="" data-cache-busting-key="8df8311d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Strange World"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-744826 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="744826" data-film-slug="/film/enola-holmes-2/" data-poster-url="/film/enola-holmes-2/image-150/" data-linked="linked" data-target-link="/film/enola-holmes-2/" data-target-link-target="" data-cache-busting-key="0b05f98f" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Enola Holmes 2"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-435460 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="435460" data-film-slug="/film/black-panther-wakanda-forever/" data-poster-url="/film/black-panther-wakanda-forever/image-150/" data-linked="linked" data-target-link="/film/black-panther-wakanda-forever/" data-target-link-target="" data-cache-busting-key="87412ddf" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Black Panther: Wakanda Forever"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-589317 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="589317" data-film-slug="/film/amsterdam-2022/" data-poster-url="/film/amsterdam-2022/image-150/" data-linked="linked" data-target-link="/film/amsterdam-2022/" data-target-link-target="" data-cache-busting-key="85997eb0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Amsterdam"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-647390 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="647390" data-film-slug="/film/confess-fletch/" data-poster-url="/film/confess-fletch/image-150/" data-linked="linked" data-target-link="/film/confess-fletch/" data-target-link-target="" data-cache-busting-key="88144a94" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Confess, Fletch"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-441474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="441474" data-film-slug="/film/wendell-wild/" data-poster-url="/film/wendell-wild/image-150/" data-linked="linked" data-target-link="/film/wendell-wild/" data-target-link-target="" data-cache-busting-key="8e24544c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Wendell & Wild"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-523109 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="523109" data-film-slug="/film/causeway/" data-poster-url="/film/causeway/image-150/" data-linked="linked" data-target-link="/film/causeway/" data-target-link-target="" data-cache-busting-key="870478ea" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Causeway"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-721288 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="721288" data-film-slug="/film/the-fabelmans/" data-poster-url="/film/the-fabelmans/image-150/" data-linked="linked" data-target-link="/film/the-fabelmans/" data-target-link-target="" data-cache-busting-key="0dba11a7" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Fabelmans"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-521323 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="521323" data-film-slug="/film/the-menu-2022/" data-poster-url="/film/the-menu-2022/image-150/" data-linked="linked" data-target-link="/film/the-menu-2022/" data-target-link-target="" data-cache-busting-key="8e7be729" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Menu"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-9">★★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-586723 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="586723" data-film-slug="/film/glass-onion/" data-poster-url="/film/glass-onion/image-150/" data-linked="linked" data-target-link="/film/glass-onion/" data-target-link-target="" data-cache-busting-key="304e3660" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Glass Onion"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-820461 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="820461" data-film-slug="/film/the-lost-king/" data-poster-url="/film/the-lost-king/image-150/" data-linked="linked" data-target-link="/film/the-lost-king/" data-target-link-target="" data-cache-busting-key="864fbd75" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Lost King"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-686510 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="686510" data-film-slug="/film/see-how-they-run-2022/" data-poster-url="/film/see-how-they-run-2022/image-150/" data-linked="linked" data-target-link="/film/see-how-they-run-2022/" data-target-link-target="" data-cache-busting-key="8a569c44" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="See How They Run"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-462030 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="462030" data-film-slug="/film/pinocchio-2022/" data-poster-url="/film/pinocchio-2022/image-150/" data-linked="linked" data-target-link="/film/pinocchio-2022/" data-target-link-target="" data-cache-busting-key="beb0d10e" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Pinocchio"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-598882 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="598882" data-film-slug="/film/the-banshees-of-inisherin/" data-poster-url="/film/the-banshees-of-inisherin/image-150/" data-linked="linked" data-target-link="/film/the-banshees-of-inisherin/" data-target-link-target="" data-cache-busting-key="03be9e08" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Banshees of Inisherin"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-734096 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="734096" data-film-slug="/film/tar-2022/" data-poster-url="/film/tar-2022/image-150/" data-linked="linked" data-target-link="/film/tar-2022/" data-target-link-target="" data-cache-busting-key="8caea6a3" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="TÁR"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-666269 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="666269" data-film-slug="/film/white-noise-2022/" data-poster-url="/film/white-noise-2022/image-150/" data-linked="linked" data-target-link="/film/white-noise-2022/" data-target-link-target="" data-cache-busting-key="093db78d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="White Noise"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-676215 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="676215" data-film-slug="/film/day-shift-2022/" data-poster-url="/film/day-shift-2022/image-150/" data-linked="linked" data-target-link="/film/day-shift-2022/" data-target-link-target="" data-cache-busting-key="8097de58" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Day Shift"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-811153 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="811153" data-film-slug="/film/one-piece-film-red/" data-poster-url="/film/one-piece-film-red/image-150/" data-linked="linked" data-target-link="/film/one-piece-film-red/" data-target-link-target="" data-cache-busting-key="093156e5" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="One Piece Film Red"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-647760 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="647760" data-film-slug="/film/the-gray-man-2022/" data-poster-url="/film/the-gray-man-2022/image-150/" data-linked="linked" data-target-link="/film/the-gray-man-2022/" data-target-link-target="" data-cache-busting-key="81ba2f7b" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Gray Man"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-641961 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="641961" data-film-slug="/film/bullet-train/" data-poster-url="/film/bullet-train/image-150/" data-linked="linked" data-target-link="/film/bullet-train/" data-target-link-target="" data-cache-busting-key="0a859e26" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Bullet Train"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-7">★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-371005 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="371005" data-film-slug="/film/minions-the-rise-of-gru/" data-poster-url="/film/minions-the-rise-of-gru/image-150/" data-linked="linked" data-target-link="/film/minions-the-rise-of-gru/" data-target-link-target="" data-cache-busting-key="8a9ee32a" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Minions: The Rise of Gru"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-592465 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="592465" data-film-slug="/film/the-man-from-toronto-2022/" data-poster-url="/film/the-man-from-toronto-2022/image-150/" data-linked="linked" data-target-link="/film/the-man-from-toronto-2022/" data-target-link-target="" data-cache-busting-key="0477e5e9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Man from Toronto"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-543002 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="543002" data-film-slug="/film/thor-love-and-thunder/" data-poster-url="/film/thor-love-and-thunder/image-150/" data-linked="linked" data-target-link="/film/thor-love-and-thunder/" data-target-link-target="" data-cache-busting-key="84638312" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Thor: Love and Thunder"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-878873 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="878873" data-film-slug="/film/vesper-2022/" data-poster-url="/film/vesper-2022/image-150/" data-linked="linked" data-target-link="/film/vesper-2022/" data-target-link-target="" data-cache-busting-key="0317ad27" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Vesper"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-488592 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="488592" data-film-slug="/film/the-sea-beast-2022/" data-poster-url="/film/the-sea-beast-2022/image-150/" data-linked="linked" data-target-link="/film/the-sea-beast-2022/" data-target-link-target="" data-cache-busting-key="8dce9a04" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Sea Beast"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-607401 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="607401" data-film-slug="/film/vengeance-2022/" data-poster-url="/film/vengeance-2022/image-150/" data-linked="linked" data-target-link="/film/vengeance-2022/" data-target-link-target="" data-cache-busting-key="04dc3f16" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Vengeance"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-641574 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="641574" data-film-slug="/film/lightyear-2022/" data-poster-url="/film/lightyear-2022/image-150/" data-linked="linked" data-target-link="/film/lightyear-2022/" data-target-link-target="" data-cache-busting-key="0d45b6f6" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Lightyear"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-812015 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="812015" data-film-slug="/film/close-2022/" data-poster-url="/film/close-2022/image-150/" data-linked="linked" data-target-link="/film/close-2022/" data-target-link-target="" data-cache-busting-key="8ac6ce80" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Close"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-8">★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-875860 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="875860" data-film-slug="/film/ricky-gervais-supernature/" data-poster-url="/film/ricky-gervais-supernature/image-150/" data-linked="linked" data-target-link="/film/ricky-gervais-supernature/" data-target-link-target="" data-cache-busting-key="8c13daef" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ricky Gervais: SuperNature"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-736318 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="736318" data-film-slug="/film/crimes-of-the-future-2022/" data-poster-url="/film/crimes-of-the-future-2022/image-150/" data-linked="linked" data-target-link="/film/crimes-of-the-future-2022/" data-target-link-target="" data-cache-busting-key="8331ef2f" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Crimes of the Future"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-427970 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="427970" data-film-slug="/film/triangle-of-sadness/" data-poster-url="/film/triangle-of-sadness/image-150/" data-linked="linked" data-target-link="/film/triangle-of-sadness/" data-target-link-target="" data-cache-busting-key="8e1eb744" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Triangle of Sadness"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-669198 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="669198" data-film-slug="/film/one-fine-morning-2022/" data-poster-url="/film/one-fine-morning-2022/image-150/" data-linked="linked" data-target-link="/film/one-fine-morning-2022/" data-target-link-target="" data-cache-busting-key="0280d483" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="One Fine Morning"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-485265 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="485265" data-film-slug="/film/three-thousand-years-of-longing/" data-poster-url="/film/three-thousand-years-of-longing/image-150/" data-linked="linked" data-target-link="/film/three-thousand-years-of-longing/" data-target-link-target="" data-cache-busting-key="0c21e1b7" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Three Thousand Years of Longing"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-385511 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="385511" data-film-slug="/film/doctor-strange-in-the-multiverse-of-madness/" data-poster-url="/film/doctor-strange-in-the-multiverse-of-madness/image-150/" data-linked="linked" data-target-link="/film/doctor-strange-in-the-multiverse-of-madness/" data-target-link-target="" data-cache-busting-key="81a4fea9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Doctor Strange in the Multiverse of Madness"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-565852 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="565852" data-film-slug="/film/the-northman/" data-poster-url="/film/the-northman/image-150/" data-linked="linked" data-target-link="/film/the-northman/" data-target-link-target="" data-cache-busting-key="08820bd4" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Northman"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-456327 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="456327" data-film-slug="/film/morbius/" data-poster-url="/film/morbius/image-150/" data-linked="linked" data-target-link="/film/morbius/" data-target-link-target="" data-cache-busting-key="084000b9" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Morbius"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-683285 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="683285" data-film-slug="/film/ambulance-2022/" data-poster-url="/film/ambulance-2022/image-150/" data-linked="linked" data-target-link="/film/ambulance-2022/" data-target-link-target="" data-cache-busting-key="02c94c2c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Ambulance"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-574385 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="574385" data-film-slug="/film/the-unbearable-weight-of-massive-talent/" data-poster-url="/film/the-unbearable-weight-of-massive-talent/image-150/" data-linked="linked" data-target-link="/film/the-unbearable-weight-of-massive-talent/" data-target-link-target="" data-cache-busting-key="8992593c" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Unbearable Weight of Massive Talent"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-673474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="673474" data-film-slug="/film/the-lost-city-2022/" data-poster-url="/film/the-lost-city-2022/image-150/" data-linked="linked" data-target-link="/film/the-lost-city-2022/" data-target-link-target="" data-cache-busting-key="87db30cd" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Lost City"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-474474 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="474474" data-film-slug="/film/everything-everywhere-all-at-once/" data-poster-url="/film/everything-everywhere-all-at-once/image-150/" data-linked="linked" data-target-link="/film/everything-everywhere-all-at-once/" data-target-link-target="" data-cache-busting-key="80fbb370" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Everything Everywhere All at Once"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-10">★★★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-438727 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="438727" data-film-slug="/film/turning-red/" data-poster-url="/film/turning-red/image-150/" data-linked="linked" data-target-link="/film/turning-red/" data-target-link-target="" data-cache-busting-key="0d037915" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Turning Red"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-620665 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="620665" data-film-slug="/film/the-adam-project/" data-poster-url="/film/the-adam-project/image-150/" data-linked="linked" data-target-link="/film/the-adam-project/" data-target-link-target="" data-cache-busting-key="8f04f942" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Adam Project"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-348914 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="348914" data-film-slug="/film/the-batman/" data-poster-url="/film/the-batman/image-150/" data-linked="linked" data-target-link="/film/the-batman/" data-target-link-target="" data-cache-busting-key="0438ab74" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Batman"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-264328 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="264328" data-film-slug="/film/uncharted-2022/" data-poster-url="/film/uncharted-2022/image-150/" data-linked="linked" data-target-link="/film/uncharted-2022/" data-target-link-target="" data-cache-busting-key="8c645cbf" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Uncharted"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-434913 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="434913" data-film-slug="/film/death-on-the-nile-2022/" data-poster-url="/film/death-on-the-nile-2022/image-150/" data-linked="linked" data-target-link="/film/death-on-the-nile-2022/" data-target-link-target="" data-cache-busting-key="8228a9e0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Death on the Nile"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-8">★★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-777185 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="777185" data-film-slug="/film/emily-the-criminal/" data-poster-url="/film/emily-the-criminal/image-150/" data-linked="linked" data-target-link="/film/emily-the-criminal/" data-target-link-target="" data-cache-busting-key="03df984d" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Emily the Criminal"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-680635 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="680635" data-film-slug="/film/living-2022/" data-poster-url="/film/living-2022/image-150/" data-linked="linked" data-target-link="/film/living-2022/" data-target-link-target="" data-cache-busting-key="8db883ac" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Living"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-719315 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="719315" data-film-slug="/film/breaking-2022/" data-poster-url="/film/breaking-2022/image-150/" data-linked="linked" data-target-link="/film/breaking-2022/" data-target-link-target="" data-cache-busting-key="829c2ff0" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Breaking"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-735545 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="735545" data-film-slug="/film/emergency-2022/" data-poster-url="/film/emergency-2022/image-150/" data-linked="linked" data-target-link="/film/emergency-2022/" data-target-link-target="" data-cache-busting-key="0a2a26ab" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Emergency"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-823432 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="823432" data-film-slug="/film/louis-ck-sorry-2021/" data-poster-url="/film/louis-ck-sorry-2021/image-150/" data-linked="linked" data-target-link="/film/louis-ck-sorry-2021/" data-target-link-target="" data-cache-busting-key="04941a73" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Louis C.K.: Sorry"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-6">★★★</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-551275 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="551275" data-film-slug="/film/the-matrix-resurrections/" data-poster-url="/film/the-matrix-resurrections/image-150/" data-linked="linked" data-target-link="/film/the-matrix-resurrections/" data-target-link-target="" data-cache-busting-key="0d576ce2" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Matrix Resurrections"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-572255 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="572255" data-film-slug="/film/dont-look-up-2021/" data-poster-url="/film/dont-look-up-2021/image-150/" data-linked="linked" data-target-link="/film/dont-look-up-2021/" data-target-link-target="" data-cache-busting-key="8a7a1c92" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Don\'t Look Up"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-571629 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="571629" data-film-slug="/film/the-unforgivable/" data-poster-url="/film/the-unforgivable/image-150/" data-linked="linked" data-target-link="/film/the-unforgivable/" data-target-link-target="" data-cache-busting-key="8fd1eb25" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Unforgivable"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata -rated-and-liked"> <span class="rating -tiny -darker rated-9">★★★★½</span> <span class="like has-icon icon-liked icon-16"><span class="icon"></span></span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-466291 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="466291" data-film-slug="/film/tick-tick-boom-2021/" data-poster-url="/film/tick-tick-boom-2021/image-150/" data-linked="linked" data-target-link="/film/tick-tick-boom-2021/" data-target-link-target="" data-cache-busting-key="071f7a54" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="tick, tick...BOOM!"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-441858 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="441858" data-film-slug="/film/red-notice/" data-poster-url="/film/red-notice/image-150/" data-linked="linked" data-target-link="/film/red-notice/" data-target-link-target="" data-cache-busting-key="0ef37870" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Red Notice"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-714279 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="714279" data-film-slug="/film/army-of-thieves/" data-poster-url="/film/army-of-thieves/image-150/" data-linked="linked" data-target-link="/film/army-of-thieves/" data-target-link-target="" data-cache-busting-key="0deeede3" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Army of Thieves"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-454016 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="454016" data-film-slug="/film/eternals/" data-poster-url="/film/eternals/image-150/" data-linked="linked" data-target-link="/film/eternals/" data-target-link-target="" data-cache-busting-key="0a67ea1a" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Eternals"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-496592 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="496592" data-film-slug="/film/encanto/" data-poster-url="/film/encanto/image-150/" data-linked="linked" data-target-link="/film/encanto/" data-target-link-target="" data-cache-busting-key="8d86b9e5" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Encanto"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-7">★★★½</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-544936 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="544936" data-film-slug="/film/the-harder-they-fall-2021/" data-poster-url="/film/the-harder-they-fall-2021/image-150/" data-linked="linked" data-target-link="/film/the-harder-they-fall-2021/" data-target-link-target="" data-cache-busting-key="863a9c16" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="The Harder They Fall"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> <span class="rating -tiny -darker rated-6">★★★</span> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t\t\t<li class="poster-container">\n\t\t\t\t\t\t\t<div class="really-lazy-load poster film-poster film-poster-790798 linked-film-poster" data-image-width="70" data-image-height="105" data-film-id="790798" data-film-slug="/film/dave-chappelle-the-closer/" data-poster-url="/film/dave-chappelle-the-closer/image-150/" data-linked="linked" data-target-link="/film/dave-chappelle-the-closer/" data-target-link-target="" data-cache-busting-key="04f75162" data-show-menu="true" > <img src="https://s.ltrbxd.com/static/img/empty-poster-70.8112b435.png" class="image" width="70" height="105" alt="Dave Chappelle: The Closer"/> <span class="frame"><span class="frame-title"></span></span> </div> <p class="poster-viewingdata"> </p>\n\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\n\t\t\t\t</ul>\n\t\t\t\t<div class="pagination"> <div class="paginate-nextprev paginate-disabled"><span class="previous">Newer</span></div> <div class="paginate-nextprev"><a class="next" href="/mrafee113/films/page/2/">Older</a></div> <div class="paginate-pages"> <ul> <li class="paginate-page paginate-current"><span>1</span></li> <li class="paginate-page"><a href="/mrafee113/films/page/2/">2</a></li> <li class="paginate-page"><a href="/mrafee113/films/page/3/">3</a></li> <li class="paginate-page unseen-pages">&hellip;</li> <li class="paginate-page"><a href="/mrafee113/films/page/10/">10</a></li> </ul> </div> </div>\n\t\t\t\n\t\t<div class="clear"></div>\n\t</section>\n\t\n\t<div class="clear"></div>\n\t\n</div>\n\n\n\n\n\n\n\n\n\n\n\t\t</div> \n\n\t\t\n\n\t</div> \n\n\n\n\t<footer id="page-footer" class="page-footer js-page-footer js-hide-in-app">\n\t\t<div class="content-wrap">\n\t\t\t\n\t\t\t\t<nav class="footer-nav js-footer-nav">\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li><a href="/about/">About</a></li>\n\t\t\t\t\t\t<li><a href="/journal/">News</a></li>\n\t\t\t\t\t\t<li class="js-hide-in-app"><a href="/pro/">Pro</a></li>\n\t\t\t\t\t\t<li><a href="/apps/">Apps</a></li>\n\t\t\t\t\t\t<li><a href="https://apple.co/3TfzHVG" target="_blank" rel="noopener noreferrer">Podcast</a></li>\n\t\t\t\t\t\t<li><a href="/year-in-review/">Year in Review</a></li>\n\t\t\t\t\t\t<li><a href="/gift-guide/">Gift Guide</a></li>\n\t\t\t\t\t\t<li><a href="/welcome/">Help</a></li>\n\t\t\t\t\t\t<li><a href="/legal/terms-of-use/">Terms</a></li>\n\t\t\t\t\t\t<li><a href="/api-beta/">API</a></li>\n\t\t\t\t\t\t<li><a href="/contact/">Contact</a></li>\n\t\t\t\t\t</ul>\n\t\t\t\t</nav>\n\t\n\n\t\t\t<div class="socials">\n\t\t\t\t<nav class="social-service-list -inline">\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://twitter.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Twitter">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="20" height="16" xmlns="http://www.w3.org/2000/svg"><path d="M17.96 4.51V4c.8-.56 1.49-1.28 2.04-2.1-.74.33-1.53.54-2.36.65.85-.5 1.5-1.3 1.8-2.24-.78.46-1.66.8-2.6.98a4.13 4.13 0 0 0-7.1 2.76c0 .31.04.62.1.92A11.72 11.72 0 0 1 1.38.74a3.99 3.99 0 0 0 1.28 5.4A4.2 4.2 0 0 1 .8 5.62v.06c0 1.95 1.42 3.59 3.29 3.96a4.06 4.06 0 0 1-1.85.07 4.1 4.1 0 0 0 3.83 2.8A8.32 8.32 0 0 1 0 14.2C1.8 15.33 3.97 16 6.28 16A11.5 11.5 0 0 0 17.96 4.51Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Twitter</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.facebook.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Facebook">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="19" height="19" xmlns="http://www.w3.org/2000/svg"><path d="M9.5 0a9.5 9.5 0 0 0-1.48 18.89V12H5.6V9.25h2.42V7.41c0-2.38 1.41-3.7 3.58-3.7 1.04 0 2.13.19 2.13.19v2.33h-1.2c-1.18 0-1.54.74-1.54 1.49v1.53h2.63L13.2 12h-2.21v6.89A9.5 9.5 0 0 0 9.5 0Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Facebook</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.instagram.com/letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on Instagram">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="20" height="20" xmlns="http://www.w3.org/2000/svg"><path d="M14.12.06c1.07.05 1.8.22 2.43.46.66.26 1.21.6 1.77 1.16.56.55.9 1.11 1.15 1.77.25.63.42 1.36.47 2.43.04.94.06 1.32.06 3.3v1.37c0 1.54 0 2.19-.03 2.77v.22l-.03.58a7.34 7.34 0 0 1-.47 2.43 4.9 4.9 0 0 1-1.15 1.77 4.9 4.9 0 0 1-1.77 1.16c-.64.24-1.36.41-2.43.46l-.61.03h-.23c-.5.02-1.06.03-2.21.03H9.2c-2 0-2.37-.02-3.32-.06a7.34 7.34 0 0 1-2.43-.46 4.9 4.9 0 0 1-1.77-1.16 4.9 4.9 0 0 1-1.16-1.77 7.34 7.34 0 0 1-.46-2.43l-.03-.61v-.2A60.9 60.9 0 0 1 0 11.5V8.75C0 7.7.01 7.17.03 6.7v-.2l.03-.61C.1 4.8.28 4.08.52 3.45a4.9 4.9 0 0 1 1.16-1.77A4.9 4.9 0 0 1 3.45.52 7.34 7.34 0 0 1 5.88.06l.61-.03h.2C7.12 0 7.6 0 8.5 0h2.74c1.62 0 2 .02 2.88.06ZM11.02 2H8.97c-1.7 0-2.05.02-2.92.06a5.4 5.4 0 0 0-1.82.33c-.45.18-.78.39-1.12.73-.34.34-.55.67-.73 1.12-.13.35-.3.86-.33 1.82C2.02 6.93 2 7.29 2 8.98v2.04c0 1.7.02 2.05.06 2.92.04.95.2 1.47.33 1.81.18.46.39.78.73 1.13.34.34.67.55 1.12.73.35.13.86.29 1.82.33.83.04 1.2.05 2.7.06h2.47c1.51 0 1.87-.02 2.71-.06a5.4 5.4 0 0 0 1.81-.33c.46-.18.78-.4 1.12-.73.35-.35.56-.67.73-1.13.14-.34.3-.86.34-1.8a49 49 0 0 0 .06-2.72V8.77a49 49 0 0 0-.06-2.71 5.4 5.4 0 0 0-.34-1.82 3.02 3.02 0 0 0-.73-1.12 3.02 3.02 0 0 0-1.12-.73 5.4 5.4 0 0 0-1.81-.33c-.88-.04-1.23-.06-2.93-.06ZM10 4.86a5.14 5.14 0 1 1 0 10.28 5.14 5.14 0 0 1 0-10.28ZM10 7a3 3 0 1 0 0 6 3 3 0 0 0 0-6Zm5.25-3.5a1.25 1.25 0 1 1 0 2.5 1.25 1.25 0 0 1 0-2.5Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">Instagram</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.tiktok.com/@letterboxd" target="_blank" rel="noopener noreferrer" title="Letterboxd on TikTok">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="17" height="18" xmlns="http://www.w3.org/2000/svg"><path d="M16.48 4.32a4.62 4.62 0 0 1-3.92-2.66A4.04 4.04 0 0 1 12.23 0H9.07v11.85c0 1.93-1.19 3.07-2.65 3.07a2.71 2.71 0 0 1-2.04-.9 2.57 2.57 0 0 1-.6-2.1 2.55 2.55 0 0 1 1.26-1.81 2.7 2.7 0 0 1 2.24-.21V6.77a5.92 5.92 0 0 0-4.08.86 5.7 5.7 0 0 0-2.15 2.55 5.53 5.53 0 0 0 1.26 6.16 5.86 5.86 0 0 0 6.33 1.23 5.78 5.78 0 0 0 2.6-2.08c.64-.94.98-2.03.98-3.15V5.96a7.74 7.74 0 0 0 4.25 1.25V4.32Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">TikTok</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="listitem -icononly">\n\t\t\t\t\t\t<a class="trigger tooltip" href="https://www.youtube.com/letterboxdhq" target="_blank" rel="noopener noreferrer" title="Letterboxd on YouTube">\n\t\t\t\t\t\t\t<svg class="glyph" aria-hidden="true" role="presentation" width="23" height="16" xmlns="http://www.w3.org/2000/svg"><path d="M11.74 0c.61 0 2.33.02 4.11.08l.54.02c1.7.06 3.35.18 4.1.38a2.87 2.87 0 0 1 2.03 2.02c.45 1.67.48 5.04.48 5.46v.08c0 .42-.03 3.8-.48 5.46a2.87 2.87 0 0 1-2.03 2.02c-.75.2-2.4.32-4.1.38l-.54.02c-1.78.07-3.5.08-4.11.08H11.26c-.62 0-2.33-.01-4.11-.08l-.54-.02c-1.7-.06-3.36-.18-4.1-.38A2.87 2.87 0 0 1 .48 13.5C.04 11.9 0 8.68 0 8.1v-.2c0-.58.04-3.79.48-5.4A2.87 2.87 0 0 1 2.5.48c.74-.2 2.4-.32 4.1-.38l.54-.02C8.93.02 10.65 0 11.26 0ZM9 4.57v6.86L15 8 9 4.57Z"/></svg>\n\t\t\t\t\t\t\t<span class="label">YouTube</span>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</div>\n\t\t\t\t</nav>\n\t\t\t</div>\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t<p class="copyright">\n\t\t\t\t&copy; Letterboxd Limited. Made by <a href="/crew/" class="mute">fans</a> in Aotearoa New Zealand.\n\t\t\t\t<span class="nobr"><a href="https://letterboxd.com/about/film-data/" class="mute">Film data</a> from <a href="https://www.themoviedb.org" class="mute">TMDb</a>. \n\t\t\t\t\n\t\t\t\t\t\t<a href="#" class="mute mobile-site-switch" data-use-mobile-site="yes">Mobile&nbsp;site</a>.\n\t\t\t\t\t\n\t</span>\n\t\t\t\t<span class="recap" style="display:none"><br/>This site is protected by reCAPTCHA and the Google <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer" class="mute">privacy policy</a> and <a href="https://policies.google.com/terms" target="_blank" rel="noopener noreferrer" class="mute">terms of service</a>&nbsp;apply.</span>\n\t\t\t</p>\n\t\t</div>\n\t</footer>\n\n\t<div id="remove-ads-modal" class="modal-neue fade" tabindex="-1" aria-labelledby="remove-ads-modal-title" aria-hidden="true">\n    <div class="modal-dialog -sm modal-dialog-centered">\n        <div class="modal-content">\n            <div class="modal-header">\n                <h5 class="modal-title" id="remove-ads-modal-title">Upgrade to remove&nbsp;ads</h5>\n                <button type="button" class="close" data-bs-dismiss="modal-neue" aria-label="Close">\n                    <svg class="glyph" width="16" height="16" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd" stroke-linecap="round" stroke="#000" stroke-width="2"><path d="m1 1 14 14M1 15 15 1"/></g></svg>\n                </button>\n            </div>\n            <div class="modal-body">\n                <div class="body-text -hero">\n                    <p>Letterboxd is an independent service created by a small team, and we rely mostly on the support of our members to maintain our site and apps. Please consider upgrading to a <a href="/pro/">Pro account</a>—for less than a couple bucks a month, you’ll get cool additional features like all-time and annual stats pages (<a href="https://letterboxd.com/jack/stats/">example</a>), the ability to select (and filter by) your favorite streaming services, and no ads!</p>\n                </div>\n            </div>\n            <div class="modal-footer">\n                <a href="/pro/" class="button -action button-action">Learn more about Pro</a>\n            </div>\n        </div>\n    </div>\n</div>\n\t\n\n\n\n\n\n\n<form id="poster-picker-modal" class="modal-neue fade poster-picker-modal" method="post" action="" novalidate="novalidate" tabindex="-1" role="dialog" aria-labelledby="poster-picker-modal-title" aria-hidden="true" data-bs-backdrop="static">\n    <div class="modal-dialog -lg modal-dialog-centered modal-dialog-scrollable">\n        <div class="modal-content">\n            <div class="modal-header">\n                <h5 class="modal-title" id="poster-picker-modal-title">Select your preferred poster</h5>\n                <button type="button" class="close" data-bs-dismiss="modal-neue" aria-label="Close">\n                    <svg class="glyph" width="16" height="16" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd" stroke-linecap="round" stroke="#000" stroke-width="2"><path d="m1 1 14 14M1 15 15 1"></path></g></svg>\n                </button>\n            </div>\n            <div class="modal-body">\n                <div id="poster-picker-b427140c-d820-493e-a8cf-bb50fce997b3" data-poster-picker-options=\'{"id": "b427140c-d820-493e-a8cf-bb50fce997b3"}\' data-js-target="poster-picker"></div>\n            </div>\n            <div class="modal-footer">\n                <div class="poster-picker-note">\n                    <div class="body-text -small">\n                        \n<p>Posters are sourced from <a href="https://www.themoviedb.org" target="_blank">TMDb</a> and <a href="https://posteritati.com" target="_blank">Posteritati</a>, and appear for you and visitors to your profile and content, depending on settings. <a href="https://letterboxd.com/journal/posterity-custom-posters/" target="_blank">Learn more.</a></p>\n\n                    </div>\n                </div>\n\n                <div class="poster-picker-controls" data-poster-picker-controls-for="b427140c-d820-493e-a8cf-bb50fce997b3">\n                    <div class="modal-action-group -center">\n                        <button class="button -destructive" type="button" data-js-trigger="reset" disabled><span class="label">Reset poster</span></button>\n                        <button class="button -action" type="submit" data-js-trigger="submit" disabled><span class="label">Save<span class="mob-hide"> changes</span></span></button>\n                    </div>\n                    \n                </div>\n            </div>\n        </div>\n    </div>\n</form>\n\t\n\t\n</body>\n</html>'

In [102]: for i in doc.xpath(f'/html/body//img[@class="image"]'):
     ...:     print(i.attrib['alt'])
     ...: 
Mafia Mamma
Louis C.K. at The Dolby
Renfield
Shazam! Fury of the Gods
Dungeons & Dragons: Honor Among Thieves
Champions
Kill Boksoon
Ant-Man and the Wasp: Quantumania
Knock at the Cabin
Mummies
Operation Fortune: Ruse de Guerre
Puss in Boots: The Last Wish
Strange World
Enola Holmes 2
Black Panther: Wakanda Forever
Amsterdam
Confess, Fletch
Wendell & Wild
Causeway
The Fabelmans
The Menu
Glass Onion
The Lost King
See How They Run
Pinocchio
The Banshees of Inisherin
TÁR
White Noise
Day Shift
One Piece Film Red
The Gray Man
Bullet Train
Minions: The Rise of Gru
The Man from Toronto
Thor: Love and Thunder
Vesper
The Sea Beast
Vengeance
Lightyear
Close
Ricky Gervais: SuperNature
Crimes of the Future
Triangle of Sadness
One Fine Morning
Three Thousand Years of Longing
Doctor Strange in the Multiverse of Madness
The Northman
Morbius
Ambulance
The Unbearable Weight of Massive Talent
The Lost City
Everything Everywhere All at Once
Turning Red
The Adam Project
The Batman
Uncharted
Death on the Nile
Emily the Criminal
Living
Breaking
Emergency
Louis C.K.: Sorry
The Matrix Resurrections
Don't Look Up
The Unforgivable
tick, tick...BOOM!
Red Notice
Army of Thieves
Eternals
Encanto
The Harder They Fall
Dave Chappelle: The Closer

In [103]: for i in doc.xpath(f'/html/body//img[@class="image"]'):
     ...:     print(i.attrib['alt'])

