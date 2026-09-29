# AI-Powered Criminal Network Analysis System

**Smart India Hackathon 2026 | Problem Statement 26189 | Team POLICE**

Police in India already have a lot of data: FIRs, call records, bank transactions, surveillance reports, criminal histories. What they don't have is an easy way to connect all of it. This project is our attempt to fix that. It's an AI layer that sits on top of existing systems, pulls scattered clues together, and shows investigators how a criminal network actually fits together, in hours or days instead of months.

| | |
|---|---|
| Problem Statement ID | 26189 |
| Title | AI-Powered Criminal Network Analysis System |
| Theme | Blockchain & Cybersecurity |
| Category | Software |
| Team Name | POLICE |
| Team ID | _add your Team ID_ |

---

## Contents

- [Why we built this](#why-we-built-this)
- [A real example: the Jaffer Sadiq case](#a-real-example-the-jaffer-sadiq-case)
- [What we're building](#what-were-building)
- [How it works](#how-it-works)
- [Tech stack](#tech-stack)
- [Where our data comes from](#where-our-data-comes-from)
- [Is this realistic?](#is-this-realistic)
- [Risks and how we handle them](#risks-and-how-we-handle-them)
- [Expected impact](#expected-impact)
- [Getting started](#getting-started)
- [Project structure](#project-structure)
- [Roadmap](#roadmap)
- [References](#references)
- [Team](#team)
- [Disclaimer](#disclaimer)

---

## Why we built this

The way we see it, the problem isn't a lack of data. Systems like CCTNS and ICJS have done a good job of digitizing and integrating criminal records. The problem is that the useful part is buried inside all that data.

- A key clue might be one line in a FIR, one bank transfer, or one phone call out of thousands.
- Evidence about the same person often sits in different places, under slightly different names.
- Investigators end up connecting the dots by hand, which takes months.
- Meanwhile, criminal networks keep evolving faster than anyone can analyse them.

Tools like COPLINK and IBM i2 do help find connections, but they stop short in three ways:

1. They don't automatically validate or prioritise the links they find.
2. They don't tell you how confident they are in a match.
3. They can't trace a link back to the original record it came from.

That last one matters a lot. A lead you can't verify isn't much use in a real investigation.

---

## A real example: the Jaffer Sadiq case

In 2024, a Tamil Nadu film financier was found to be running a drug-trafficking and money-laundering network, using film and real-estate businesses as a front.

Mapping the whole thing took investigators about **9 months**. By the end they had uncovered:

- 45 consignments
- 6 front companies
- 9 overseas entities
- 56 bank accounts
- ₹30 Cr+ in deposits

Our goal is to reconstruct that same network in **hours or days**, with every finding checked by an investigator. We use this case as our benchmark for whether the system actually works.

---

## What we're building

Think of it as an intelligence layer over the data police already have. It does four main things.

**1. Combines data from many sources.**
FIRs, call records, financial records, surveillance reports, social media and intelligence inputs get pulled together, so a clue in one place can be connected to a clue in another.

**2. Maps who is connected to whom, and how.**
It doesn't just say "A is linked to B." It records the type of relationship (father, business partner, financier, intermediary), and it can predict hidden links that aren't obvious in the raw records.

**3. Spots things that don't add up.**
By analysing time, location and activity, it flags impossible travel, such as someone appearing in two far-apart places too close together in time, as well as other suspicious movements.

**4. Ranks leads and shows the proof.**
It picks out the most important leads, ranks them, and links each one to the records that support it. It can also suggest what evidence to look for next to move someone up to primary suspect.

Two principles run through all of this:

- **Privacy first.** Agencies can train shared models together using federated learning, so raw data never has to leave its owner. A blockchain-backed audit trail keeps the evidence record tamper-proof.
- **The investigator always decides.** The AI suggests, the human validates.

### Main features

| Feature | What it does |
|---|---|
| Impossible travel detection | Flags location and time contradictions and checks whether the travel was even feasible |
| Unified entity profiles | Merges mentions of the same person or company from different sources into one profile |
| Next-best-evidence | Suggests which evidence to pursue next, in priority order |
| Criminal history linkage | Connects a person to past cases, associates and related networks |
| Hypothesis engine | Proposes explanations, ranks them, explains its reasoning and gives a confidence score |
| Federated learning + blockchain | Lets agencies learn together securely, with a tamper-proof audit trail |
| Source traceability | Every lead points back to the original record |

---

## How it works

```
 DATA SOURCES
 FIRs · CDRs · Social media · Financial records · Surveillance · Criminal history
        │
        ▼
 MULTIMODAL + AGENTIC AI  ──────────►  TEMPORAL NETWORK
 (fuses data, reasons across sources,   (time-aware analysis, sequence
  plans and uses tools)                  and anomaly detection)
        │                                        │
        ├──────────────┐                         │
        ▼              ▼                         │
 GRAPH NETWORK     EVENT & ENTITY                │
 ANALYSIS          EXTRACTION                    │
 (relationships,   (NLP + vision + speech,       │
  communities,      structured data,             │
  key players,      cross-document linking)      │
  hidden links)          │                       │
        │                ▼                       │
        └────────►  FINE-TUNED LLM  ◄────────────┘
                    (domain-adapted, grounded in evidence)
                         │
                         ▼
                  HYPOTHESIS ENGINE
                  (generate, rank, explain, score confidence)
                         │
                         ▼
                      OUTPUTS
     Impossible travel · Entity profiles · Next-best-evidence
     Federated learning + blockchain · Criminal history linkage
```

### What each part does

- **Multimodal + agentic AI** is the coordinator. It handles different kinds of data (text, images, audio), correlates clues across sources, and decides which tools to use.
- **Event and entity extraction** turns messy documents into structured facts. It uses NLP for text, vision for images and speech recognition for audio, then links the same person or event across documents.
- **Graph network analysis** builds the relationship map. It finds clusters (gangs or groups), identifies central figures, and predicts links that aren't recorded anywhere.
- **Temporal network** adds the time dimension. It's what makes impossible-travel detection possible.
- **Fine-tuned LLM** is a language model adapted to this domain. It has to ground its answers in retrieved evidence.
- **Hypothesis engine** turns everything above into ranked hypotheses, each with an explanation and a confidence score.

### The processing pipeline

**OCR → RAG → Knowledge Graph → Graph ML → LLM**

Each step is an independent module. The LLM never has to read the whole dataset. It only sees the relevant part of the graph, pulled in through selective retrieval.

---

## Tech stack

| Purpose | Tools |
|---|---|
| Core language | Python |
| Machine learning | PyTorch |
| Graph database | Neo4j |
| Data and statistics | Pandas, NumPy, SciPy |
| Blockchain | Ethereum |
| Agentic AI | LangChain |
| Retrieval | RAG (retrieval-augmented generation) |
| Models | Fine-tuned LLM / SLM |
| Document processing | OCR, NLP, vision, speech recognition |

---

## Where our data comes from

Real investigation data is sensitive, so we can't use it for a prototype. Instead we use:

- Web scraping from verified sources
- Publicly available FIRs
- Public court hearing records (e-Courts / NJDG)
- Synthetic data to fill the gaps

---

## Is this realistic?

We think so, for two reasons.

**It's buildable step by step.** Because OCR, RAG, the knowledge graph, graph ML and the LLM are independent modules, we can build and test them one at a time. Selective retrieval keeps the LLM workload manageable.

**It fits what already exists.** The system is designed to work on top of CCTNS and ICJS, so agencies don't have to replace anything. Human validation, evidence provenance and privacy protections are built in, which matters for sensitive cases.

---

## Risks and how we handle them

| Risk | What we plan to do |
|---|---|
| Real-world data is hard to get | Use public and synthetic data for the prototype |
| FIRs come in many languages and scripts | Use OCR and NLP built for multilingual documents |
| Evidence is sensitive | Use federated learning and blockchain to protect data and provenance |
| AI can be wrong | Keep a human in the loop; investigators validate every finding |
| Evidence is spread across sources | Link entities across sources so the data connects |

---

## Expected impact

A note before the numbers: **everything below is a projection.** These are our estimates based on how the system is designed. They aren't results from a live deployment, and they'd need to be tested in real pilots.

### Who benefits and how

**Narcotics enforcement** (seizures, drug networks, supply chains)
- 3 to 6 months earlier detection of networks
- 30 to 40% higher seizure rate and coverage
- 40 to 60% less investigation time and cost

**Women safety and anti-human trafficking units (AHTUs)**
- 25 to 35% more hidden links found between victims, traffickers and safe houses
- 40 to 60% faster victim identification and rescue
- 50 to 70% less manual data analysis

**Ministry of Home Affairs (state and centre coordination)**
- 3 to 6 months faster action on emerging threats
- 30 to 40% better cross-state link coverage
- 2 to 3x stronger inter-agency collaboration

**Frontline police**
- 40 to 60% less manual effort
- 2 to 4x more linked entities per case
- 50 to 70% less time to get actionable leads

### The current picture: narcotics enforcement in India

Data cited from the Narcotics Control Bureau (MHA, Government of India):

| Year | Cases registered | Arrests made | Quantity seized (kg) |
|---|---:|---:|---:|
| 2020 | 58,620 | 73,871 | 123,311 |
| 2021 | 66,590 | 91,799 | 158,012 |
| 2022 | 78,204 | 105,476 | 132,845 |
| 2023 | 89,467 | 121,701 | 158,751 |
| 2024 | 84,061 | 110,369 | 153,349 |

### Where we think this could lead by 2030

If the system were widely adopted, we estimate roughly **40% fewer cases** and about **50% less drug quantity in circulation** compared with the current trend. The reasoning is that catching networks earlier disrupts supply before it reaches the market. Again, this is a modelled estimate, not an observed outcome.

---

## Getting started

_These steps are a template. Update them as the code takes shape._

**You'll need:**
- Python 3.10 or newer
- Neo4j (Desktop or Docker)
- Node.js and a local Ethereum dev chain (Hardhat or Ganache) for the blockchain module
- An OCR engine such as Tesseract, with multilingual language packs
- Optionally, a GPU for fine-tuning


## Project structure

_A suggested layout. Adjust it to match your code._

```
.
├── data/
│   ├── raw/          # public FIRs, court hearings, scraped data
│   └── synthetic/    # synthetic datasets
├── src/
│   ├── ingestion/    # OCR, speech recognition, scrapers
│   ├── extraction/   # entity and event extraction
│   ├── graph/        # Neo4j schema, relationships, graph ML
│   ├── temporal/     # timelines and impossible-travel detection
│   ├── llm/          # fine-tuned LLM, RAG, hypothesis engine
│   ├── federated/    # federated learning
│   ├── blockchain/   # smart contracts and audit trail
│   └── app/          # API and investigator dashboard
├── notebooks/
├── tests/
├── requirements.txt
└── README.md
```

---

## Roadmap

- [ ] Multilingual OCR and NLP for FIRs
- [ ] Entity and event extraction with cross-document linking
- [ ] Knowledge graph in Neo4j with typed relationships
- [ ] Graph ML: communities, key players, hidden-link prediction
- [ ] Temporal analysis and impossible-travel detection
- [ ] RAG and fine-tuned LLM with evidence grounding
- [ ] Hypothesis engine with confidence scoring
- [ ] Next-best-evidence recommender
- [ ] Federated learning across simulated agencies
- [ ] Blockchain audit trail
- [ ] Investigator dashboard with human validation
- [ ] Pilot integration with CCTNS / ICJS

---

## References

- [Ministry of Home Affairs](https://www.mha.gov.in/en): drug trafficking measures
- [Enforcement Directorate](https://www.enforcementdirectorate.gov.in): Jaffer Sadiq case
- [data.gov.in](https://data.gov.in): open government data
- [National Judicial Data Grid](https://www.doj.gov.in/the-national-judicial-data-grid-njdg): e-Courts data
- [Narcotics Control Bureau](https://ncb.gov.in): narcotics statistics
- [IEEE Xplore](https://ieeexplore.ieee.org): research papers

## Disclaimer

This is a hackathon prototype built on public and synthetic data. It's meant to support investigators, not replace them. Every link, hypothesis and recommendation it produces must be checked by a human before anyone acts on it. The impact figures are projections, not guaranteed outcomes.

Licensed under the MIT License (change this if you prefer another). See `LICENSE`.
