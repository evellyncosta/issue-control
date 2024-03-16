#!/bin/bash

# Adicione aqui a lógica da sua CLI
# Por exemplo, a lógica da função fix_snyk()

# Bash ## FIX SNYK AUTOMATION
function fix_snyk() {
    echo "Iniciando criação da issue..."

    # Executa o comando e captura a saída em uma variável
    output=$(gh issue create --title "Fix Snyk" --body "$(cat .github/ISSUE_TEMPLATE/snyk.md)" --assignee @me)
    echo "Issue criada: $output"

    # Extrai o número da issue a partir da saída
    issue_number=$(echo "$output" | awk -F/ '{print $NF}')
    echo "Número da issue: $issue_number"

    echo "Iniciando desenvolvimento da issue..."

    # Nome da branch seguindo o padrão fix/{issue_number}-fix-snyk
    branch_name="fix/$issue_number-fix-snyk"

    # Executa o comando para desenvolvimento da issue e faz o checkout do branch
    gh issue develop "$issue_number" --base fix-snyk --name "$branch_name" --checkout

    echo "Desenvolvimento da issue finalizado."

    echo "Fazendo commit das alterações..."

    # Faz o commit vazio com a mensagem especificada
    git commit -m "fix(app): fix vulnerabilities" --allow-empty

    echo "Commit realizado."

    echo "Enviando alterações para o repositório remoto..."

    # Faz o push das alterações para o repositório remoto
    git push

    echo "Alterações enviadas para o repositório remoto."

    echo "Criando pull request..."

    # Cria um pull request com os detalhes fornecidos
    gh pr create --title "[FIX]: fix snyk vulnerabilities" --body "$(cat .github/pull_request_template.md)" --draft --head "$branch_name" \
		--reviewer GuillaumeFalourd \
		--reviewer RodrigoCuryZup \
		--reviewer diogokykutaz \
		--reviewer tiagodolphine

    echo "Pull request criado."
}

# Verifica se foi passado um argumento
if [ $# -eq 0 ]; then
    echo "Uso: ic <comando>"
    exit 1
fi

# Verifica qual comando foi passado
case "$1" in
    fixsnyk)
        fix_snyk
        ;;
    *)
        echo "Comando não reconhecido"
        exit 1
        ;;
esac
