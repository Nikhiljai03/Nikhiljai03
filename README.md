<div align="center">
  <img src="assets/banner.svg" alt="Nikhil Jai — AI Engineer · Agents · LLM Infrastructure" width="100%">
</div>

<p align="center">
  <a href="https://kolanikhiljai.vercel.app/"><img alt="Portfolio" src="https://img.shields.io/badge/portfolio-kolanikhiljai.vercel.app-0B0E14?style=flat-square&labelColor=0B0E14&color=22D3EE"></a>
  <a href="https://linkedin.com/in/nikhil-jai"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-nikhil--jai-0B0E14?style=flat-square&labelColor=0B0E14&color=A78BFA"></a>
  <a href="mailto:nikhilraina95@gmail.com"><img alt="Email" src="https://img.shields.io/badge/email-nikhilraina95@gmail.com-0B0E14?style=flat-square&labelColor=0B0E14&color=38BDF8"></a>
  <img alt="Location" src="https://img.shields.io/badge/base-Hyderabad,%20IN-0B0E14?style=flat-square&labelColor=0B0E14&color=64748B">
</p>

<div align="center">
  <img src="assets/terminal.svg" alt="whoami — Nikhil Jai, AI Engineer Intern @ Intants" width="840">
</div>

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
  <img src="assets/stats.svg" alt="GitHub statistics — contributions, repos, languages, code shipped" width="840">
  <br><br>
  <sub>Rendered straight from the GitHub API by a <a href="https://github.com/Nikhiljai03/Nikhiljai03/actions/workflows/stats.yml">scheduled Action</a> — self-hosted, no third-party widgets.</sub>
</div>

<div align="center">
  <br>
  <sub><i>"In the game of algorithms, I compete to dominate and conquer to win."</i></sub>
  <br><br>
  <a href="https://kolanikhiljai.vercel.app/"><b>Portfolio</b></a> ·
  <a href="https://linkedin.com/in/nikhil-jai"><b>LinkedIn</b></a> ·
  <a href="mailto:nikhilraina95@gmail.com"><b>Email</b></a> ·
  <a href="https://github.com/Nikhiljai03?tab=repositories"><b>All repos</b></a>
</div>
