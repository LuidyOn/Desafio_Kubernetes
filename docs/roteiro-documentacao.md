# Roteiro para a documentação acadêmica final

Esqueleto para preenchimento com dados reais da atividade. Usar o [README principal](../README.md) como fonte para as Fases 1 e 2 e o [índice de evidências](evidencias/README.md) para localizar as capturas.

**Fase 3 — Amazon EKS: PENDENTE.** Preencher seus resultados somente depois da implantação e dos testes reais. Os campos abaixo são orientações de preenchimento, não relatos de execução.

## 1. Introdução

- [Preencher] Contexto da disciplina, objetivo do desafio e escopo do trabalho.
- [Preencher] Identificação acadêmica solicitada pelo roteiro da disciplina.

## 2. Aplicação desenvolvida

- [Preencher] Descrição da API Python/Flask, endpoints e porta.
- [Preencher] Variáveis de ambiente e tratamento do Secret sem exposição de conteúdo.
- [Preencher] Limitações da aplicação didática.

## 3. Conteinerização com Docker

- [Preencher] Papel do Dockerfile e das dependências.
- [Preencher] Comandos de build e run, resultados observados e evidências disponíveis.

## 4. Publicação no Docker Hub

- [Preencher] Imagem local, imagem publicada, repositório e tag registrados no README.
- [Preencher] Comandos de tag e push e evidências da publicação.

## 5. Implantação no Amazon EKS

**PENDENTE.**

- [Preencher após executar] Preparação das ferramentas, região, cluster e validação dos nós, sem credenciais.
- [Preencher após executar] Comandos de implantação e estado real do Deployment e dos 2 Pods.
- [Preencher] Diagrama de arquitetura; usar o diagrama planejado do README como base e ajustar ao ambiente efetivamente implantado.

## 6. ConfigMap e Secret

**Validação no Kubernetes: PENDENTE.**

- [Preencher] Finalidade dos manifestos e referências do Deployment.
- [Preencher após executar] Evidência do ambiente recebido e da indicação de Secret configurado; não registrar seu conteúdo.

## 7. Service e acesso externo

**PENDENTE.**

- [Preencher após executar] Service, portas, endereço externo e comandos de consulta.
- [Preencher após executar] Status HTTP e respostas reais de ambos os endpoints pela Internet.

## 8. Recuperação automática dos Pods

**PENDENTE.**

- [Preencher após executar] Nomes e estados dos Pods antes e depois da exclusão manual.
- [Preencher após executar] Evidências do novo Pod e do retorno a 2 réplicas prontas.

## 9. Dificuldades encontradas

- [Preencher] Problema efetivamente encontrado, mensagem observada, tentativa de solução e resultado.
- [Preencher] Pendências ainda não resolvidas, se houver.

## 10. Aprendizados

- [Preencher] Conceitos compreendidos durante cada fase, vinculados a exemplos reais da execução.

## 11. Custos e remoção dos recursos

**Execução e verificação na AWS: PENDENTES.**

- [Preencher após executar] Recursos utilizados, período de uso e custos efetivamente observados.
- [Preencher após executar] Ações de remoção e evidências da conferência de recursos remanescentes.

## 12. Conclusão

- [Preencher] Objetivos efetivamente atingidos e resultados sustentados pelas evidências.
- [Preencher] Limitações e etapas ainda pendentes na data da entrega.

## 13. Evidências

- [Preencher] Relacionar cada etapa ao arquivo correspondente em `docs/evidencias/`.
- [Preencher] Para cada captura, registrar data, ação ou comando, resultado e legenda.
- [Preencher] Identificar lacunas de evidência sem inventar capturas ou resultados.
