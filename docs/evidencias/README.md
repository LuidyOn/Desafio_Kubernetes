# Evidências da atividade

As quatro imagens abaixo são cópias integrais dos anexos fornecidos na atualização das Fases 1 e 2. Elas registram a execução manual anterior; nenhuma execução de AWS ou EKS está documentada aqui.

| Arquivo | Conteúdo comprovado pela captura |
|---|---|
| [01-aplicacao-local.png](01-aplicacao-local.png) | Resposta de `GET /` em `localhost:5000`, ambiente local e indicação de Secret configurado |
| [02-health-check.png](02-health-check.png) | Resposta de `GET /health` com `status: ok` |
| [03-docker-images-ps-push.png](03-docker-images-ps-push.png) | `docker images`, `docker ps`, criação da tag e `docker push` concluído para `luidyon/desafio-kubernetes:v1` |
| [04-docker-hub-v1.png](04-docker-hub-v1.png) | Repositório `luidyon/desafio-kubernetes` no Docker Hub com a tag `v1` |

A evidência 03 reúne imagens, container e push no mesmo terminal. Não foram criadas capturas separadas ou duplicadas para essas ações.

## Complementos locais ainda não fornecidos

- Saída da construção com `docker build`.
- Comando e saída inicial de `docker run`.
- Consultas dos dois endpoints que exibam explicitamente o status HTTP 200.

Essas validações foram informadas como concluídas pelo autor. As capturas do navegador mostram o corpo JSON, sem os cabeçalhos HTTP; a captura do terminal mostra a imagem resultante e o container em execução, sem as saídas de build e run.

## Evidências da Fase 3 — PENDENTES

- Nós do cluster (`kubectl get nodes`).
- Deployment aplicado e 2 Pods em execução no EKS.
- Service LoadBalancer e endereço externo disponível.
- Respostas de `GET /` e `GET /health` pela Internet, incluindo o status HTTP.
- ConfigMap validado por `ambiente: demonstracao` e Secret validado pela indicação booleana, sem expor seu conteúdo.
- Pod antes da exclusão, exclusão manual e novo Pod criado automaticamente, com retorno a 2 réplicas prontas.
- Remoção dos recursos AWS e verificação de custos ao final.

Adicionar somente capturas reais, após cada etapa ser executada. Registrar a data, o comando ou ação e uma legenda, omitindo credenciais. Atualizar o [README principal](../../README.md) e o [roteiro acadêmico](../roteiro-documentacao.md) ao incorporar novas evidências.
