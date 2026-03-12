#!/usr/bin/env python3
"""
Skill Compliance Checker

Validates SKILL.md files against skill_building_standards.md requirements.
Returns compliance report with pass/fail for each criterion.

Usage:
    python check_skill_compliance.py path/to/SKILL.md
    python check_skill_compliance.py --all  # Check all skills in pm-skills-arsenal
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


class SkillComplianceChecker:
    """Validates skill files against structural requirements."""

    REQUIRED_YAML_FIELDS = [
        'name', 'description', 'version', 'type', 'tags',
        'created', 'valid_until', 'derived_from', 'tested_with', 'license'
    ]

    REQUIRED_SECTIONS = [
        '## Purpose',
        '## When to Use / When NOT to Use',
        '## Format Rules',
        '## Output Template',
        '## Executive Summary',
        '## How to Read This Document',
        '## Notation Key',
        '## Step 0: Context Fitness Check',
        '## Step 0b: Framework Selection',
        '## Domain Frameworks',
        '## Evidence Standards',
        '## Application Method',
        '## Quality Gradients',
        '## Failure Modes',
        "## What's Next",
        '## Appendix: Quick-Reference Checklist'
    ]

    MIN_FRAMEWORKS = 6
    MIN_FAILURE_MODES = 7
    MIN_FORMAT_RULES = 9
    TARGET_LINE_RANGE = (800, 1300)

    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.content = skill_path.read_text(encoding='utf-8')
        self.lines = self.content.split('\n')
        self.line_count = len(self.lines)

    def check_yaml_front_matter(self) -> Tuple[bool, List[str]]:
        """Check if YAML front matter has all required fields."""
        missing = []

        # Extract YAML block (between --- delimiters)
        if not self.content.startswith('---'):
            return False, ['No YAML front matter found']

        yaml_end = self.content.find('---', 3)
        if yaml_end == -1:
            return False, ['YAML front matter not properly closed']

        yaml_block = self.content[3:yaml_end]

        for field in self.REQUIRED_YAML_FIELDS:
            if f'{field}:' not in yaml_block and f'"{field}":' not in yaml_block:
                missing.append(field)

        return len(missing) == 0, missing

    def check_required_sections(self) -> Tuple[int, List[str]]:
        """Check which required sections are present."""
        missing = []
        found = 0

        for section in self.REQUIRED_SECTIONS:
            if section in self.content:
                found += 1
            else:
                missing.append(section)

        return found, missing

    def count_frameworks(self) -> int:
        """Count domain frameworks (looking for Framework N: patterns)."""
        # Look for patterns like "### Framework 1:" or "**Framework 1:**"
        framework_patterns = [
            r'###\s+Framework\s+\d+:',
            r'\*\*Framework\s+\d+:\*\*',
            r'###\s+F\d+:',
            r'## \d+\.',  # Numbered sections under Domain Frameworks
        ]

        frameworks = set()
        for pattern in framework_patterns:
            matches = re.findall(pattern, self.content)
            frameworks.update(matches)

        return len(frameworks)

    def count_failure_modes(self) -> int:
        """Count failure modes (looking for FM-N patterns)."""
        # Look for patterns like "**FM-1:" or "### FM-1:"
        fm_pattern = r'(?:###|\*\*)\s*FM-\d+'
        matches = re.findall(fm_pattern, self.content)
        return len(set(matches))

    def count_format_rules(self) -> int:
        """Count format rules in Format Rules section."""
        # Find Format Rules section
        fr_start = self.content.find('## Format Rules')
        if fr_start == -1:
            return 0

        # Find next ## section
        next_section = self.content.find('\n## ', fr_start + 1)
        if next_section == -1:
            fr_section = self.content[fr_start:]
        else:
            fr_section = self.content[fr_start:next_section]

        # Count rules in multiple formats:
        # Format 1: "### Rule N:"
        # Format 2: "N. **"
        rule_patterns = [
            r'###\s+Rule\s+\d+:',
            r'^\d+\.\s+\*\*'
        ]

        rules = set()
        for pattern in rule_patterns:
            matches = re.findall(pattern, fr_section, re.MULTILINE)
            rules.update(matches)

        return len(rules)

    def check_framework_quality(self) -> Tuple[int, List[str]]:
        """Check if frameworks have scoring rubrics or decision tables."""
        # Look for tables (| ... |) and rubric keywords
        framework_section_start = self.content.find('## Domain Frameworks')
        if framework_section_start == -1:
            return 0, ['Domain Frameworks section not found']

        evidence_section_start = self.content.find('## Evidence Standards')
        if evidence_section_start == -1:
            framework_section = self.content[framework_section_start:]
        else:
            framework_section = self.content[framework_section_start:evidence_section_start]

        # Count tables (rough heuristic: lines with |...| pattern)
        table_lines = [line for line in framework_section.split('\n') if line.strip().startswith('|') and line.strip().endswith('|')]
        has_tables = len(table_lines) > 10  # At least some substantial tables

        # Look for rubric/decision table keywords
        rubric_keywords = ['rubric', 'decision table', 'scoring', 'rating', 'assessment']
        has_rubrics = any(keyword in framework_section.lower() for keyword in rubric_keywords)

        if has_tables and has_rubrics:
            return 1, []
        else:
            issues = []
            if not has_tables:
                issues.append('Few or no tables found in Domain Frameworks section')
            if not has_rubrics:
                issues.append('No rubric/scoring language found')
            return 0, issues

    def check_line_count(self) -> Tuple[bool, str]:
        """Check if line count is in target range."""
        in_range = self.TARGET_LINE_RANGE[0] <= self.line_count <= self.TARGET_LINE_RANGE[1]
        status = f"{self.line_count} / {self.TARGET_LINE_RANGE[0]}-{self.TARGET_LINE_RANGE[1]}"
        return in_range, status

    def run_full_check(self) -> Dict:
        """Run all compliance checks and return report."""
        yaml_pass, yaml_missing = self.check_yaml_front_matter()
        sections_found, sections_missing = self.check_required_sections()
        frameworks_count = self.count_frameworks()
        failure_modes_count = self.count_failure_modes()
        format_rules_count = self.count_format_rules()
        framework_quality, framework_issues = self.check_framework_quality()
        line_count_pass, line_count_status = self.check_line_count()

        return {
            'skill_path': str(self.skill_path),
            'line_count': self.line_count,
            'line_count_status': line_count_status,
            'line_count_pass': line_count_pass,
            'yaml_pass': yaml_pass,
            'yaml_missing': yaml_missing,
            'sections_found': sections_found,
            'sections_total': len(self.REQUIRED_SECTIONS),
            'sections_missing': sections_missing,
            'frameworks_count': frameworks_count,
            'frameworks_min': self.MIN_FRAMEWORKS,
            'frameworks_pass': frameworks_count >= self.MIN_FRAMEWORKS,
            'failure_modes_count': failure_modes_count,
            'failure_modes_min': self.MIN_FAILURE_MODES,
            'failure_modes_pass': failure_modes_count >= self.MIN_FAILURE_MODES,
            'format_rules_count': format_rules_count,
            'format_rules_min': self.MIN_FORMAT_RULES,
            'format_rules_pass': format_rules_count >= self.MIN_FORMAT_RULES,
            'framework_quality_pass': framework_quality == 1,
            'framework_quality_issues': framework_issues,
        }

    def print_report(self, report: Dict):
        """Print compliance report to console."""
        print(f"\n{'='*60}")
        print(f"Skill Compliance Report: {self.skill_path.name}")
        print(f"{'='*60}\n")

        # Line count
        status = '✅' if report['line_count_pass'] else '⚠️'
        print(f"{status} Line count: {report['line_count_status']}")

        # YAML
        status = '✅' if report['yaml_pass'] else '❌'
        yaml_msg = 'All fields present' if report['yaml_pass'] else f"Missing: {report['yaml_missing']}"
        print(f"{status} YAML front matter: {yaml_msg}")

        # Sections
        status = '✅' if len(report['sections_missing']) == 0 else '❌'
        print(f"{status} Required sections: {report['sections_found']}/{report['sections_total']}")
        if report['sections_missing']:
            print(f"   Missing: {', '.join(report['sections_missing'][:3])}{'...' if len(report['sections_missing']) > 3 else ''}")

        # Frameworks
        status = '✅' if report['frameworks_pass'] else '❌'
        print(f"{status} Domain frameworks: {report['frameworks_count']}/{report['frameworks_min']} minimum")

        # Failure modes
        status = '✅' if report['failure_modes_pass'] else '❌'
        print(f"{status} Failure modes: {report['failure_modes_count']}/{report['failure_modes_min']} minimum")

        # Format rules
        status = '✅' if report['format_rules_pass'] else '❌'
        print(f"{status} Format rules: {report['format_rules_count']}/{report['format_rules_min']} minimum")

        # Framework quality
        status = '✅' if report['framework_quality_pass'] else '⚠️'
        fq_msg = 'Rubrics/tables present' if report['framework_quality_pass'] else 'Check manually'
        print(f"{status} Framework quality: {fq_msg}")
        if report['framework_quality_issues']:
            for issue in report['framework_quality_issues']:
                print(f"   - {issue}")

        # Overall
        all_critical_pass = (
            report['yaml_pass'] and
            len(report['sections_missing']) == 0 and
            report['frameworks_pass'] and
            report['failure_modes_pass'] and
            report['format_rules_pass']
        )

        print(f"\n{'='*60}")
        if all_critical_pass:
            print("✅ PASS: All critical requirements met")
        else:
            print("❌ FAIL: Some requirements not met")
        print(f"{'='*60}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_skill_compliance.py path/to/SKILL.md")
        print("       python check_skill_compliance.py --all")
        sys.exit(1)

    if sys.argv[1] == '--all':
        # Check all skills in pm-skills-arsenal
        # Try both Second Brain path and direct repos path
        skills_dir_paths = [
            Path(__file__).parent.parent.parent / 'repos' / 'pm-skills-arsenal' / 'skills',
            Path.home() / 'repos' / 'pm-skills-arsenal' / 'skills',
        ]

        skills_dir = None
        for path in skills_dir_paths:
            if path.exists():
                skills_dir = path
                break

        if skills_dir is None:
            print(f"Skills directory not found. Tried:")
            for path in skills_dir_paths:
                print(f"  - {path}")
            sys.exit(1)

        skill_files = list(skills_dir.glob('*/SKILL.md'))
        if not skill_files:
            print("No SKILL.md files found")
            sys.exit(1)

        print(f"\nChecking {len(skill_files)} skills...\n")

        all_pass = True
        for skill_file in sorted(skill_files):
            checker = SkillComplianceChecker(skill_file)
            report = checker.run_full_check()

            # Quick summary
            critical_pass = (
                report['yaml_pass'] and
                len(report['sections_missing']) == 0 and
                report['frameworks_pass'] and
                report['failure_modes_pass'] and
                report['format_rules_pass']
            )

            status = '✅' if critical_pass else '❌'
            print(f"{status} {skill_file.parent.name}: {report['sections_found']}/{ report['sections_total']} sections, {report['frameworks_count']} frameworks, {report['failure_modes_count']} FMs")

            if not critical_pass:
                all_pass = False

        print(f"\n{'='*60}")
        if all_pass:
            print("✅ All skills pass compliance checks")
        else:
            print("❌ Some skills have issues (run individually for details)")
        print(f"{'='*60}\n")

    else:
        # Check single skill
        skill_path = Path(sys.argv[1])
        if not skill_path.exists():
            print(f"File not found: {skill_path}")
            sys.exit(1)

        checker = SkillComplianceChecker(skill_path)
        report = checker.run_full_check()
        checker.print_report(report)


if __name__ == '__main__':
    main()
