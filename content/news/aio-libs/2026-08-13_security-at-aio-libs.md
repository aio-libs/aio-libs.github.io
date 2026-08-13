Title: How we handle security at aio-libs
Tags: aio-libs, aiohttp

[[aiohttp]] and the wider aio-libs family sit underneath a big slice of the Python ecosystem, which means our bugs become everyone else's bugs.
Security has always been part of the job, but the last year has seen a run of dedicated work on it - two external audits, a funded security program, and a lot of new processes.

## The day-to-day process

Everything starts with the reporting pipeline described in our organisation-wide [security policy](https://github.com/aio-libs/.github/blob/master/SECURITY.md).
We typically receive several reports per month and try to act on them promptly.
You can read how we handle these reports in our [incident response plan](https://docs.aiohttp.org/en/stable/contributing-admins.html#incident-response).

We typically issue CVEs for anything that could plausibly affect users, which means we may allocate more CVEs than some similar projects.
Additionally, aiohttp is a complex project and we must consider security relating to networking, HTTP parsing, general web framework and client code.
Most similar projects only deal with one of these areas.

On the supply-chain side, releases are published with PyPI trusted publishing (so there are no long-lived tokens to steal) and signed with [Sigstore](https://www.sigstore.dev/), CodeQL and Dependabot run on the repositories, and aiohttp's parsers have been fuzzed continuously by [OSS-Fuzz](https://github.com/google/oss-fuzz/tree/master/projects/aiohttp) since 2022.

## A security audit, via NLnet

In 2025, [NLnet](https://nlnet.nl/) funded development work on aiohttp - [improving the type annotations](https://nlnet.nl/project/Aiohttp-typecheck/) - through the NGI Zero Commons Fund, backed by the European Commission's Next Generation Internet programme.
NGI Zero grants come with more than money though: projects also get access to [support services](https://nlnet.nl/NGI0/services/), including a professional security audit.

Ours was performed by [Radically Open Security](https://www.radicallyopensecurity.com/) - particular thanks to Thomas Rinsma - and its findings resulted in five CVEs: denial-of-service vectors like resource exhaustion via large payloads and an infinite loop when Python runs with assertions disabled, a brute-forceable path disclosure in static file handling, and parsing discrepancies around Unicode digits.
The fixes shipped in [aiohttp 3.13.3](https://github.com/aio-libs/aiohttp/releases/tag/v3.13.3) in January, [disclosed in a coordinated batch of eight advisories](https://www.openwall.com/lists/oss-security/2026/01/05/14) together with three issues from independent reporters.
Our thanks to NLnet for funding both the audit and the development time spent fixing the findings.

One of those reports is worth calling out explicitly: a high-severity decompression bomb ([CVE-2025-69223](https://github.com/aio-libs/aiohttp/security/advisories/GHSA-6mq8-rvhq-8wgg)), where a tiny compressed message inflates into a huge one when aiohttp decompresses it automatically.
It also wasn't ours to fix alone - the [brotli](https://github.com/google/brotli) library had no way to cap how much data a decompression call could produce - so the issue was disclosed to Google and we waited for them to provide a fix in brotli 1.2 before we could resolve it.
Due to architectural difficulties, the initial fix capped decompressed output at 32 MiB per call, which also blocked some legitimate highly-compressed payloads, so [aiohttp 3.14.0](https://github.com/aio-libs/aiohttp/releases/tag/v3.14.0) followed up with an overhaul of the decompression code that processes payloads incrementally in bounded chunks, safely handling any valid payload.
The final fix also reduced the amount of data in memory from 32 MiB to 256 KiB, matching most memory assumptions in the rest of the aiohttp code.
Coordinated disclosure sometimes has to run up the dependency chain as well as down it.

## The GitHub Secure Open Source Fund

In April we joined Session 4 of the [GitHub Secure Open Source Fund](https://github.com/open-source/github-secure-open-source-fund), alongside 49 other projects (including friends from the Python ecosystem).
The program pairs $10,000 of funding through GitHub Sponsors with a three-week security sprint - threat modeling, secure coding, vulnerability management and AI security, with a curriculum from GitHub Security Lab - and check-ins over the following year.

The funding is welcome, but the bigger value for us was momentum: a structured push, with security experts on hand, to clear a backlog of security process work.
While we found that we were already doing most of the recommendations covered in the program, we still found plenty of things to take our security to the next level.
So far, we have fixed up license files, written an incident response plan and a detailed threat model, plugged a gap in aiohttp's SBOM, and ran an AI-assisted audit over all our codebases.

The [threat model](https://docs.aiohttp.org/en/stable/threat_model.html) is the biggest piece: a STRIDE analysis of aiohttp covering nineteen subsystems, from the HTTP/1 parser through cookies and DNS resolution to the build and release supply chain.
For each one it records what we trust, what can go wrong, and which mitigations exist or are still wanted - including the mitigations that are the responsibility of applications built on aiohttp, which are explicitly marked as such.
We're still reviewing and publishing the remaining chapters, but expect to complete this over the next few months.
It's a living document: our incident-response process now ends with feeding each new advisory back into it.
This is really important in the age of AI-generated security reports; this is a tool that AI agents can use to verify if their report is actually valid and in scope, reducing the number of false positives getting reported to us.

The [incident response plan](https://docs.aiohttp.org/en/stable/contributing-admins.html#incident-response) writes down what used to be tribal knowledge: severity tiers, the advisory-to-release runbook, the disclosure and notification procedures, and - hopefully never needed - playbooks for a compromised release pipeline, maintainer account or CI.

The SBOM work fixes a blind spot: aiohttp vendors the [llhttp](https://github.com/nodejs/llhttp) parser as a git submodule, which GitHub's dependency graph can't see.
A [workflow](https://github.com/aio-libs/aiohttp/blob/master/.github/workflows/dependency-submission.yml) now registers the vendored llhttp version with the dependency graph on every push, so it appears in the exported SBOM and gets Dependabot alerts like any other dependency.

And the AI-assisted audit, run with GitHub Security Lab's [taskflow agent](https://github.com/GitHubSecurityLab/seclab-taskflows), found one more minor vulnerability in aiohttp - and, more usefully, several issues across other aio-libs projects that haven't seen the same level of scrutiny yet.

There's still more planned from the program: achieving [OpenSSF Baseline](https://baseline.openssf.org/) level 3, reviewing several new tools and configuration of existing ones, bringing the OSS-Fuzz integration into our repo, and generating runtime SBOMs to ship in the wheels.

## Patch the Planet

In June, aiohttp was one of the first projects taken through [Patch the Planet](https://openai.com/index/patch-the-planet/), an OpenAI initiative built with [Trail of Bits](https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/) that points AI-assisted vulnerability research - validated by human security engineers - at critical open source projects, at no cost to the maintainers.

Trail of Bits privately reported a cluster of 10 issues (resulting in 8 CVEs) across our client and server code, including cookies that could regain a broader scope after a save and reload, digest credentials that would answer a challenge from the wrong origin, and resource limits that ran only after attacker-controlled buffering.
All fixes were written, reviewed and merged a couple of days later and shipped in [aiohttp 3.14.1](https://github.com/aio-libs/aiohttp/releases/tag/v3.14.1).

## Keeping it going

None of this makes aiohttp bug-free - every audit above found something, which is exactly why we keep inviting them.
Each round of fresh eyes turns into fixes, regression tests and threat model updates, and each program leaves the process a little stronger than it found it.
Our thanks to NLnet, Radically Open Security, GitHub, OpenAI, Trail of Bits, and every reporter credited in our advisories.

If you believe you've found a vulnerability in any aio-libs project, please report it privately by following our [security policy](https://github.com/aio-libs/.github/blob/master/SECURITY.md).
And if your business relies on this work, consider [sponsoring aio-libs](/sponsorship/) - almost everything above was done by volunteers.
