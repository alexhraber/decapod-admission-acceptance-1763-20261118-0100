# Interfaces

## Project Purpose
Exercise the accepted required native-call path, actual failure and fresh repair in an isolated local fixture; admit only the exact fixture head and independently accepted base; never merge.

## Authoring Scope and Evidence
Project: Native path acceptance. This is an initial authoring scaffold, not an implementation attestation.

Describe the configured project from purpose to architecture to implementation depth. Start with the whole product: its users, problem, outcomes, and boundaries; then explain the system and its components, interfaces, state, operations, security, and proof. Ground factual prose in the repository's config, README/product documentation, source paths and symbols, contracts, and tests. Distinguish implemented behavior, intended behavior, assumptions, and unresolved gaps. A narrow task changes the relevant part of this whole-project account; it must not replace project-wide identity with the latest task, release workflow, or tooling. Record task-specific scope and evidence in the current change's governance record. Templates and declared capabilities are authoring/proof obligations, not evidence that a runtime guarantee exists. Preserve authored prose during generated refreshes. If configured metadata and explicit project-level sections are absent, leave project identity unknown and ask for or author grounded context rather than promoting an arbitrary legacy/task line.

Use the seeded context below as a starting point to verify against repository sources. Replace example diagrams, suggested controls, targets, tables, and blank fields with source-grounded prose; mark non-applicable topics with a reason. Do not adopt a store, queue, server, CI provider, replay guarantee, or service level merely because it appears in a template.

## Contract Principles
- Prefer explicit schemas over implicit behavior.
- Every mutating interface defines idempotency semantics.
- Every failure path maps to a typed, documented error code.

## Generated Contract Depth
Generated interface specs should include:
- API/CLI contracts with request/response schemas.
- Read/write ownership for each storage path.
- Idempotency and retry behavior for mutations.
- Typed failure classes and recovery instructions.

## API / RPC Contracts
| Interface | Method | Request Schema | Response Schema | Errors | Idempotency |
|---|---|---|---|---|---|
| `TODO` | `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |

## Event Consumers
| Consumer | Event | Ordering Requirement | Retry Policy | DLQ Policy |
|---|---|---|---|---|
| `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |

## Outbound Dependencies
| Dependency | Purpose | SLA | Timeout | Circuit-Breaker |
|---|---|---|---|---|
| `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |

## Inbound Contracts
- API / RPC entrypoints:
- CLI surfaces:
- Event/webhook consumers:
- Repository-detected surfaces: not detected yet

## Data Ownership
- Source-of-truth tables/collections:
- Cross-boundary read models:
- Consistency expectations:

## Error Taxonomy Example (service_or_library)
```ts
export enum ApiErrorCode {
  Validation = "validation_failed",
  UpstreamTimeout = "upstream_timeout",
  Conflict = "conflict"
}
```

## Failure Semantics
| Failure Class | Retry/Backoff | Client Contract | Observability |
|---|---|---|---|
| Validation | No retry | 4xx typed error | warn log + metric |
| Dependency timeout | Exponential backoff | 503 with retryable code | error log + alert |
| Conflict | Conditional retry | 409 with conflict detail | info log + metric |

## Timeout Budget
| Hop | Budget (ms) | Notes |
|---|---|---|
| Client -> Edge/API | 500 | Includes auth + routing |
| API -> Domain | 300 | Includes validation |
| Domain -> Store/Dependency | 200 | Includes retry overhead |

## Interface Versioning
- Version strategy (`v1`, date-based, semver):
- Backward-compatibility guarantees:
- Deprecation window and removal policy:

## CLI and Machine-Readable Contract
| Surface | Invocation/Shape | Reads | Writes | Output Stability | Proof |
|---|---|---|---|---|---|
| Human CLI | | | | | |
| JSON/automation | | | | | |
| RPC/plugin | | | | | |
| Event/file boundary | | | | | |

## Compatibility Matrix
| Contract | Current Version | Consumers | Additive Changes | Breaking Changes | Migration Trigger |
|---|---|---|---|---|---|
| Request/input | | | | | |
| Response/output | | | | | |
| Persisted data | | | | | |
| Events/artifacts | | | | | |

## Observability Contract
- Correlation/request identity:
- Structured fields required on success:
- Structured fields required on failure:
- Audit events for sensitive mutations:
- Metrics and traces that prove latency, retries, and outcomes:

## Interface Change Review
- [ ] The owner and source of truth are named for every changed field.
- [ ] Retry, idempotency, timeout, and conflict behavior are explicit.
- [ ] Consumers can distinguish validation, authorization, conflict,
  dependency, and internal failures.
- [ ] Backward compatibility or migration instructions are published.

<!-- decapod:codebase-attestation:start -->

## Codebase Attestation

- Repository signal fingerprint: `12cecd65977b1a5063def3b3ff0a19ded94d1552be887de8a0ddcc3fda7662ec`
- Significant implementation surfaces: `src/` (2 files)
- Refreshed from the current codebase by `decapod rpc --op specs.refresh`
<!-- decapod:codebase-attestation:end -->

## Native path acceptance

The separately accepted target requires the guard to remain required and payload to be ready. Both literal checks must execute through native authorization under the current task, plan, instruction, policy and lease. A successful native path has bounded kernel coverage, with full-host observation unknown. Configured PR admission requires matching proof and final independent GitHub readback; merge remains unauthorized.

The current measured v0.148.10 candidate reexecutes this accepted native contract after supported release regeneration. Original recorded source, provider revisions, failed attempts, external non-admitted control and current task custody remain preserved. A caller-declared PASS cannot replace actual accepted checks; a source failure refuses publication, and exact repair requires fresh native proof and independent current GitHub head/base readback. Human authentication, full-host observation and merge authorization remain unproven.
