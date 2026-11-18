# Começa aqui — FolderPilot

Criaste um projeto novo: um organizador de ficheiros com pré-visualização,
histórico e opção de desfazer. Esta versão funciona por regras de extensão;
não usa inteligência artificial nem precisa de uma subscrição.

## Abrir no Windows

1. Descarrega o ZIP no computador e escolhe **Extrair tudo**.
2. Instala Python 3.11 ou superior de <https://www.python.org/downloads/> se
   ainda não estiver instalado. Não abras apenas um ficheiro dentro do ZIP.
3. Abre a pasta extraída e faz duplo clique em **START_WINDOWS.bat**.
4. Na janela, escolhe uma pasta de teste ou a tua pasta Transferências.
5. Clica em **Pré-visualizar**. Vê os ficheiros e os destinos propostos.
6. Clica em **Organizar** e confirma quando estiver tudo correto.
7. Para voltar atrás, seleciona a mesma pasta e usa **Desfazer última organização**.

Para começar sem mexer nos teus documentos, abre o PowerShell na pasta do
projeto e executa:

```powershell
py -3 make_demo.py
```

Depois seleciona a pasta **demo-sandbox** na aplicação. O script não altera uma
pasta de demonstração que já exista.

## Se não abrir

Na pasta do projeto, testa no PowerShell:

```powershell
py -3 --version
py -3 -m tkinter
py -3 -m folderpilot gui
```

Se `py` não existir, tenta `python` no lugar de `py -3`. O segundo comando deve
abrir uma pequena janela de teste do Python. O código precisa de Python 3.11 ou
superior; o ZIP não contém um instalador nem um executável autónomo.

## O que acontece aos ficheiros

- Documentos, imagens, áudio, vídeos e arquivos compactados vão para pastas
  com nomes em inglês: Documents, Images, Audio, Videos e Archives.
- Subpastas, ficheiros ocultos, programas e extensões desconhecidas são ignorados.
- Um nome repetido recebe um sufixo como `(2)`; um ficheiro existente não é substituído.
- Ao desfazer, ficheiros editados ou nomes ocupados ficam preservados e são
  apresentados como conflitos.
- As pastas vazias criadas pela organização podem permanecer.
- O histórico fica na pasta `.folderpilot`. Guarda-o se quiseres desfazer.

Usa uma pasta local. O disco precisa de suportar ligações físicas (hard links).
Se não suportar, a aplicação apresenta um erro e mantém o original. Evita
editar os ficheiros, executar outra organização ou sincronizar essa pasta
durante a operação. O histórico não substitui uma cópia de segurança.

## Publicar e candidatar-te

Segue [PUBLICAR_NO_GITHUB.md](PUBLICAR_NO_GITHUB.md). O projeto entregue ainda
não está publicado na tua conta. A publicação e os commits devem corresponder
ao teu trabalho real, sem datas ou estatísticas inventadas.

Os textos atualizados para o formulário estão em
[CANDIDATURA_CLAUDE.md](CANDIDATURA_CLAUDE.md). Eles descrevem este projeto e a
sua fase inicial. Uma publicação nova não garante elegibilidade nem aprovação.
