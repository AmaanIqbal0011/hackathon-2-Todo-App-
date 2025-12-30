# Data Model: Phase I Todo CLI

## Task Entity

| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| id | int | Unique recurring identifier | Auto-generated, positive integer |
| title | string | Task summary | Required, non-empty |
| description | string | Detailed notes | Optional |
| completed | boolean | Status | Default: False |

## State Transitions

- **Pending** (default) -> **Completed** (via Mark Task as Complete)
- **Completed** -> **Pending** (via Mark Task as Complete)
- **Any** -> **Deleted** (via Delete Task)
