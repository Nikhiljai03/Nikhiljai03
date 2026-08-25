<div align="center">
  <img src="assets/banner.svg" alt="Nikhil Jai — AI Systems · Backend · Cloud Architecture" width="100%">
</div>

<p align="center">
  <a href="https://kolanikhiljai.vercel.app/"><img alt="Portfolio" src="https://img.shields.io/badge/portfolio-kolanikhiljai.vercel.app-0B0E14?style=flat-square&labelColor=0B0E14&color=22D3EE"></a>
  <a href="https://linkedin.com/in/nikhil-jai"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-nikhil--jai-0B0E14?style=flat-square&labelColor=0B0E14&color=A78BFA"></a>
  <a href="mailto:nikhilraina95@gmail.com"><img alt="Email" src="https://img.shields.io/badge/email-nikhilraina95@gmail.com-0B0E14?style=flat-square&labelColor=0B0E14&color=38BDF8"></a>
  <img alt="Location" src="https://img.shields.io/badge/base-Hyderabad,%20IN-0B0E14?style=flat-square&labelColor=0B0E14&color=64748B">
</p>

---

### `~/ whoami`

```txt
Kola Nikhil Jai
B.Tech Information Technology — Vignan Institute of Technology & Science, Hyderabad
SWE Intern @ CDPL · Feb 2026 → present

I build the unglamorous middle of AI products: the gateway that picks the
right model, the worker that reproduces a bug inside a sandbox before it
touches a PR, and the cache that makes the second call cost nothing.
```

---

### `~/ how I route a problem`

<div align="center">

```mermaid
flowchart LR
    Q(["incoming problem"]) --> R{{"classify"}}
    R -->|"cost & latency"| A["<b>AI Systems</b><br/>LLM gateways · RAG · agents<br/>eval loops · guardrails"]
    R -->|"correctness"| B["<b>Backend</b><br/>FastAPI · Postgres · Redis<br/>Kafka · Docker"]
    R -->|"has to be used"| C["<b>Product</b><br/>Next.js · TypeScript<br/>Tailwind · Vercel"]
    A --> S(["shipped, measured, iterated"])
    B --> S
    C --> S

    classDef node fill:#0F172A,stroke:#22D3EE,stroke-width:1px,color:#E2E8F0
    classDef hub fill:#1E1B4B,stroke:#A78BFA,stroke-width:1.5px,color:#EDE9FE
    classDef cap fill:#0B1120,stroke:#334155,stroke-width:1px,color:#94A3B8
    class A,B,C node
    class R hub
    class Q,S cap
```

</div>

---

### `~/ featured builds`

| Project | What it actually does | Stack |
|:--|:--|:--|
| **[Triage Agent](https://github.com/Nikhiljai03/Triage-Agent)** | Autonomous GitHub issue triage — RAG-based duplicate detection, reproduces bugs in a sandboxed Docker container, classifies severity, drafts fix PRs. Dry-run by default, behind guardrails. | `FastAPI` `Qdrant` `Redis` `Docker` |
| **[Multi-LLM Query Router](https://github.com/Nikhiljai03/Multi-LLM-Query-Router)** | Production LLM gateway that routes queries across a 3-tier model ladder by complexity. Provider fallback, 40–60% cache hit rate, sub-20ms on cached repeats, Kafka analytics. | `FastAPI` `Groq` `Kafka` `Redis` |
| **[Respiratory Sound Diagnostic Engine](https://github.com/Nikhiljai03/Respiratory-Sound-Diagnostic-Engine)** | Classifies 8 lung conditions from cough audio. MFCC feature pipeline turning 1D signals into spectral tensors, fed to a CNN classifier. | `TensorFlow` `Librosa` `NumPy` |
| **[ShareSpace](https://github.com/Nikhiljai03/ShareSpcae)** | Full-stack social platform — auth, posts, media uploads, threaded discussion. [Live →](https://share-spcae.vercel.app/) | `Next.js` `Prisma` `Neon` `Clerk` |

---

### `~/ stack`

| | |
|:--|:--|
| **Languages** | Python · TypeScript · JavaScript · Java · SQL |
| **AI / ML** | TensorFlow · Keras · Librosa · RAG + vector search (Qdrant) · Groq · Together AI |
| **Backend** | FastAPI · Node.js · Prisma · PostgreSQL · MongoDB · Redis · Kafka |
| **Frontend** | Next.js · React · Tailwind · shadcn/ui |
| **Infra** | Docker · AWS · Vercel · GitHub Actions |

---

### `~/ signals`

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=Nikhiljai03&show_icons=true&hide_border=true&hide_title=true&bg_color=00000000&text_color=94A3B8&icon_color=22D3EE&ring_color=A78BFA">
    <img src="https://github-readme-stats.vercel.app/api?username=Nikhiljai03&show_icons=true&hide_border=true&hide_title=true&bg_color=00000000&text_color=475569&icon_color=0891B2&ring_color=7C3AED" alt="GitHub stats" height="150">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=Nikhiljai03&layout=compact&hide_border=true&hide_title=true&bg_color=00000000&text_color=94A3B8&langs_count=6">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Nikhiljai03&layout=compact&hide_border=true&hide_title=true&bg_color=00000000&text_color=475569&langs_count=6" alt="Top languages" height="150">
  </picture>
</div>

---

### `~/ currently`

```console
$ nikhil --status
▸ shipping   agentic dev-tooling — issue triage, sandboxed repro, auto-PR
▸ learning   distributed systems, eval harnesses for LLM pipelines
▸ open to    backend / AI-infra internships and open-source collaboration
```

<div align="center">
  <br>
  <sub><i>"In the game of algorithms, I compete to dominate and conquer to win."</i></sub>
  <br><br>
  <a href="https://kolanikhiljai.vercel.app/"><b>Portfolio</b></a> ·
  <a href="https://linkedin.com/in/nikhil-jai"><b>LinkedIn</b></a> ·
  <a href="mailto:nikhilraina95@gmail.com"><b>Email</b></a> ·
  <a href="https://github.com/Nikhiljai03?tab=repositories"><b>All repos</b></a>
</div>
