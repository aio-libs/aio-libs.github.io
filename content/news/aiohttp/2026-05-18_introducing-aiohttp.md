Title: Introducing aiohttp
Tags: aio-libs, aiohttp

Most of you reading this already know [[aiohttp]] as the longest-running asynchronous HTTP client for Python's [asyncio](https://docs.python.org/3/library/asyncio.html).
What is less widely known is that the same package also ships a full-featured web server and framework, available under `aiohttp.web`.

As a [client](https://docs.aiohttp.org/en/stable/client.html), aiohttp offers an ergonomic API for concurrent HTTP and WebSocket traffic, with [middlewares](https://docs.aiohttp.org/en/stable/client_advanced.html#client-middleware) to customise request and response processing and [tracing hooks](https://docs.aiohttp.org/en/stable/tracing_reference.html) for observability.

As a [web server and framework](https://docs.aiohttp.org/en/stable/web.html), `aiohttp.web` covers what you'd expect from a modern framework - WebSockets, middlewares, and an extensive ecosystem of [first and third party libraries](https://docs.aiohttp.org/en/stable/third_party.html) extending the core functionality.
Rarer is its optional [handler cancellation](https://docs.aiohttp.org/en/stable/web_advanced.html#web-handler-cancellation) when a client disconnects, sparing long-running handlers from finishing work no one is waiting for.
It has been quietly powering production services for years and is the backbone of Home Assistant.

Sharing client and server in a single, well-tested dependency keeps things simple when you're building services that both consume and serve HTTP, and aiohttp's focus on performance means you rarely have to reach for something else as traffic grows.

We'll be posting more about aiohttp here over time - new releases, deep dives, and behind-the-scenes notes from the maintainers.
If you'd like to follow along, subscribe to the [aiohttp tag feed](https://aio-libs.org/feeds/aiohttp.atom.xml).
