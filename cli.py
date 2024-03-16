# cli.py
import shutil
import subprocess
import sys

def check_gh_installed():
    return shutil.which("gh") is not None

def check_gh_logged_in():
    try:
        subprocess.run(["gh", "auth", "status"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False
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

def teste():
    print("Hello, world!")

def main():
    if not check_gh_installed():
        print("GitHub CLI (gh) não está instalado. Por favor, instale-o e tente novamente.")
        sys.exit(1)

    if not check_gh_logged_in():
        print("Você não está logado no GitHub CLI (gh). Por favor, faça login e tente novamente.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Uso: ic <comando>")
        sys.exit(1)

    comando = sys.argv[1]

    if comando == "fixsnyk":
        fix_snyk()
    elif comando == "teste":
        teste()
    else:
        print("Comando não reconhecido")
        sys.exit(1)

if __name__ == "__main__":
    main()
