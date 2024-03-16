#!/usr/bin/env python3
import subprocess
import sys

def fix_snyk():
    print("Iniciando criação da issue...")

    output = subprocess.check_output(["gh", "issue", "create", "--title", "Fix Snyk", "--body", "$(cat .github/ISSUE_TEMPLATE/snyk.md)", "--assignee", "@me"], text=True)
    print("Issue criada:", output.strip())

    issue_number = output.split("/")[-1].strip()
    print("Número da issue:", issue_number)

    print("Iniciando desenvolvimento da issue...")

    branch_name = f"fix/{issue_number}-fix-snyk"
    print(f"{branch_name}")

    subprocess.run(["gh", "issue", "develop", issue_number, "--base", "fix-snyk", "--name", branch_name, "--checkout"])

    print("Desenvolvimento da issue finalizado.")

    print("Fazendo commit das alterações...")

    subprocess.run(["git", "commit", "-m", "fix(app): fix vulnerabilities", "--allow-empty"])

    print("Commit realizado.")

    print("Enviando alterações para o repositório remoto...")

    subprocess.run(["git", "push"])

    print("Alterações enviadas para o repositório remoto.")

    print("Criando pull request...")

    subprocess.run(["gh", "pr", "create", "--title", "[FIX]: fix snyk vulnerabilities", "--body", "$(cat .github/pull_request_template.md)", "--draft", "--head", branch_name, "--reviewer", "GuillaumeFalourd", "--reviewer", "RodrigoCuryZup", "--reviewer", "diogokykutaz", "--reviewer", "tiagodolphine"])

    print("Pull request criado.")

def main():
    if len(sys.argv) < 2:
        print("Uso: python ic.py <comando>")
        sys.exit(1)

    comando = sys.argv[1]

    if comando == "fixsnyk":
        fix_snyk()
    else:
        print("Comando não reconhecido")
        sys.exit(1)

if __name__ == "__main__":
    main()
