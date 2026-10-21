import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sast_tool.ast_analyzer import ASTAnalyzer
from sast_tool.vuln_pattern_matcher import VulnPatternMatcher
from sast_tool.security_rule_engine import SecurityRuleEngine
from sast_tool.code_quality_checker import CodeQualityChecker
from sast_tool.sarif_reporter import SarifReporter

def main(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    ast_issues = ASTAnalyzer().analyze(code)
    pattern_issues = VulnPatternMatcher().match(code)
    quality_issues = CodeQualityChecker().check(file_path)

    rules_path = "rules/default_rules.json"
    if not os.path.exists(rules_path):
        rules_path = os.path.join(os.path.dirname(__file__), '..', 'rules', 'default_rules.json')

    rule_engine = SecurityRuleEngine(rules_path)
    final_issues = rule_engine.evaluate(ast_issues, pattern_issues) + quality_issues

    SarifReporter().generate_report(final_issues, analyzed_file=file_path)
    print(f"Analysis complete. Report saved to report.sarif with {len(final_issues)} issues.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m sast_tool.main <file.py>")
        sys.exit(1)
    main(sys.argv[1])
