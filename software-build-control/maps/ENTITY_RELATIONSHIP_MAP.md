# ENTITY_RELATIONSHIP_MAP

## Purpose
Map entities, tables, keys, relationships, and tenant linkage.

## When to use
Before schema, import/export, report, or backend changes.

## Owner/tool
Data/backend owner.

## Inputs
Schema, migrations, runtime map, data table spec.

## Activities or fields
Entity; table; key; relationship; tenant key; RLS; evidence.

## Outputs/records
ERD/data map.

## Gate controlled
No ERD/data map → no schema change.

## PASS/HOLD/BLOCKED rules
PASS if relationships and tenant keys are clear. HOLD if incomplete. BLOCKED if schema change lacks map.

## Update trigger
Schema/data model change.
