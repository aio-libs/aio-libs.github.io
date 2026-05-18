Title: Aiohttp
Links: Documentation=https://docs.aiohttp.org/en/stable/
       Github=https://github.com/aio-libs/aiohttp/
       Sponsorship=https://opencollective.com/aio-libs/projects/aiohttp

An asynchronous HTTP Client/Server for Python's [asyncio](https://docs.python.org/3/library/asyncio.html), built on the [llhttp](https://llhttp.org/) C parser with Cython-accelerated hot paths.
Sharing client and server in a single, well-tested dependency — with [WebSockets](https://docs.aiohttp.org/en/stable/client_quickstart.html#websockets) and [middlewares](https://docs.aiohttp.org/en/stable/web_advanced.html#middlewares) on both sides — keeps things simple when you're building services that both consume and serve HTTP.

aiohttp powers [Home Assistant](https://www.home-assistant.io/), [Pulp](https://pulpproject.org/), [aiogram](https://aiogram.dev/), the [Molotov](https://molotov.readthedocs.io/) load tester, and [many others](https://docs.aiohttp.org/en/stable/built_with.html).

As a [client](https://docs.aiohttp.org/en/stable/client.html), aiohttp provides:

  - Connection pooling and a shared cookie jar across requests.
  - Streaming uploads and downloads.
  - [WebSocket](https://docs.aiohttp.org/en/stable/client_quickstart.html#websockets) support.
  - [Middlewares](https://docs.aiohttp.org/en/stable/client_advanced.html#client-middleware) to customise request/response processing.
  - [Tracing hooks](https://docs.aiohttp.org/en/stable/tracing_reference.html) for observability.

As a [web server/framework](https://docs.aiohttp.org/en/stable/web.html), aiohttp provides:

  - [WebSocket](https://docs.aiohttp.org/en/stable/web_quickstart.html#websockets) support.
  - [Middlewares](https://docs.aiohttp.org/en/stable/web_advanced.html#middlewares) to customise
request/response processing.
  - Optional [handler cancellation](https://docs.aiohttp.org/en/stable/web_advanced.html#web-handler-cancellation) when a client disconnects.
  - First-party [testing utilities](https://docs.aiohttp.org/en/stable/testing.html), including a [pytest-aiohttp](https://github.com/aio-libs/pytest-aiohttp) plugin.
  - An extensive collection of [first and third party libraries](https://docs.aiohttp.org/en/stable/third_party.html) extending the core functionality.
