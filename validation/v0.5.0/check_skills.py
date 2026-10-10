#!/usr/bin/env python3
"""Static integrity tests for Academic AI Learning System v0.5.0 Skill sources.

This validates source structure, references, distinct ownership, and invariants.
It does NOT measure LLM automatic Skill invocation or runtime Intelligent UI.
"""
from __future__ import annotations
import hashlib
import re
import sys
from pathlib import Path
import yaml

BASE = Path(__file__).resolve().parents[2] / 'skills'
EXPECTED = [
    'course-tutor-builder', 'rigorous-math-tutor',
    'statistics-quant-lab', 'computer-ai-tutor',
    'interactive-learning-designer', 'learning-progress-coordinator',
    'obsidian-academic-kb'
]

def run():
    errors = []
    records = {}
    for name in EXPECTED:
        folder = BASE / name
        path = folder / 'SKILL.md'
        if not path.is_file():
            errors.append(f'missing {path}')
            continue
        source = path.read_text(encoding='utf-8')
        m = re.match(r'^---\n(.*?)\n---\n', source, re.S)
        if not m:
            errors.append(f'{name}: invalid frontmatter')
            continue
        meta = yaml.safe_load(m.group(1))
        if set(meta) != {'name', 'description'} or meta['name'] != name:
            errors.append(f'{name}: wrong frontmatter identity/fields')
        if not (30 <= len(meta['description']) <= 1024):
            errors.append(f'{name}: insufficient/oversized description')
        agents = folder / 'agents/openai.yaml'
        if not agents.is_file():
            errors.append(f'{name}: no agents/openai.yaml')
        else:
            data = yaml.safe_load(agents.read_text(encoding='utf-8'))
            if not data.get('interface', {}).get('display_name'):
                errors.append(f'{name}: no UI display name')
            for key in ['icon_small', 'icon_large']:
                icon = data.get('interface', {}).get(key)
                if icon and not (folder / icon).is_file():
                    errors.append(f'{name}: missing {key}={icon}')
        if re.search(r'\bTODO\b|example_asset|scripts/example.py', source):
            errors.append(f'{name}: leftover template content')
        for ref in re.findall(r'`(references/[\w-]+\.md)`', source):
            if not (folder / ref).is_file():
                errors.append(f'{name}: dangling ref {ref}')
        records[name] = source
    if len(records) == len(EXPECTED):
        mapping = {
            'interactive-learning-designer': [
                'Learning Intent', 'Interactive Observation', 'interaction-qa.md',
                'learning-progress-coordinator', 'Tutor', 'Evidence'],
            'learning-progress-coordinator': [
                'Review Queue', 'Learning Debt', 'Evidence',
                'review-policy.md', 'Obsidian', 'Course Learning Profile'],
        }
        for name, required in mapping.items():
            for token in required:
                if token not in records[name]:
                    errors.append(f'{name}: missing contract token {token}')
        descs = [yaml.safe_load(re.match(r'^---\n(.*?)\n---', records[n], re.S).group(1))['description'] for n in EXPECTED]
        if len(set(descs)) != len(descs):
            errors.append('duplicate Skill descriptions')
        if 'post-hoc power' not in records['statistics-quant-lab']:
            errors.append('statistical evidence invariant missing')
        if 'WebCodex' not in records['computer-ai-tutor']:
            errors.append('code validation invariant missing')
        if 'Obsidian' not in records['obsidian-academic-kb']:
            errors.append('Obsidian invariant missing')
        if 'Stage' not in records['course-tutor-builder']:
            errors.append('CLP Stage invariant missing')
    print(f'CHECKED {len(records)} skills (expected {len(EXPECTED)})')
    print('FAIL' if errors else 'PASS - source integrity and expected contract anchors')
    for e in errors:
        print('ERROR:', e)
    return int(bool(errors))

if __name__ == '__main__':
    sys.exit(run())
