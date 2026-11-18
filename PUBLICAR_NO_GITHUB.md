# Publicar o FolderPilot no GitHub

O projeto está pronto para ser publicado, mas nenhum repositório foi criado
automaticamente na tua conta. O nome sugerido é **folderpilot**.

## Pelo navegador no computador

1. Extrai o ZIP e entra na tua conta em <https://github.com>.
2. Abre <https://github.com/new>.
3. Usa `folderpilot` como nome, ou outro nome se já existir na tua conta.
4. Descrição sugerida: `Offline file organiser with preview, undo, and a lightweight desktop interface.`
5. Escolhe **Public** para disponibilizar este código como open source.
6. Deixa desmarcadas as opções de criar README, licença e `.gitignore`: esses
   ficheiros já estão incluídos. Cria o repositório.
7. Abre **uploading an existing file** ou **Add file → Upload files**.
8. Arrasta o **conteúdo da pasta extraída**, incluindo as pastas `folderpilot`,
   `tests` e `.github`, e todos os documentos. Não envies apenas o ZIP e não
   acrescentes um nível extra de pasta acima do README.
9. Confirma que `README.md`, `LICENSE`, `pyproject.toml` e `folderpilot/core.py`
   aparecem nas posições corretas. Inclui `.gitignore` e `.gitattributes`.
10. Mensagem de commit sugerida: `Add FolderPilot initial implementation`.
    Confirma o envio usando a tua conta.
11. Abre **Actions** e verifica o resultado dos testes. O ficheiro do workflow
    tem de estar em `.github/workflows/tests.yml` para ser reconhecido.

Se o navegador omitir os ficheiros que começam por ponto, podes usar **Add file
→ Create new file** e copiar o respetivo conteúdo para o caminho exato. Por
exemplo: `.github/workflows/tests.yml`. Não partilhes `.env`, tokens, chaves,
dados pessoais ou o histórico `.folderpilot` de uma pasta tua.

No telemóvel, o envio de pastas pode ser limitado. É mais simples publicar pelo
computador. O ZIP entregue não contém os teus ficheiros pessoais.

## Verificações depois da publicação

- O README deve aparecer na página inicial do repositório.
- A visibilidade deve indicar **Public**.
- Os ficheiros `.py` devem estar navegáveis, não apenas dentro de um ZIP.
- Executa a aplicação, resolve problemas reais e regista as tuas melhorias.
- O link do repositório terá o utilizador da tua conta e o nome que escolheste.

## Sobre o formulário do Claude

Volta ao formulário e liga a mesma conta GitHub. Tenta selecionar o repositório.
Não há garantia de que um repositório novo apareça imediatamente, seja elegível
ou obtenha aprovação. A seleção técnica e a avaliação do programa são etapas
diferentes. O programa considera contribuições e impacto no ecossistema.

O texto em `CANDIDATURA_CLAUDE.md` descreve a situação de um projeto novo sem
inventar utilizadores, downloads, estrelas ou contribuições de terceiros.
Mantém-o atualizado se a situação mudar.

Referências oficiais consultadas em 18 de novembro de 2026:

- <https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository>
- <https://claude.com/contact-sales/claude-for-oss>
