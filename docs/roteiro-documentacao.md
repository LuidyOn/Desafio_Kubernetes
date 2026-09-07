# Documentação acadêmica consolidada

Resultados técnicos verificados em **07/09/2026**, no cluster `desafio-kubernetes`, região `us-east-1`, namespace `default`. Usar o [README principal](../README.md) e as [evidências textuais](evidencias/fase3-comandos.txt) como fontes. Os registros da Fase 3 incluem horários com fuso UTC−03:00.

**Situação:** Fases 1 e 2 concluídas; validação técnica da Fase 3 concluída. A entrega principal é o [PDF acadêmico](../entrega/Desafio_Kubernetes.pdf), com 7 páginas de conteúdo e 4 de anexos. As oito capturas existentes foram incorporadas, e HTTP externo e self-healing foram documentados por saídas reais de comandos. A limpeza AWS foi concluída após os testes.

**Instituição:** Universidade Salesiano Espírito Santo.

| Identificador | Integrante |
|---|---|
| 6924106557 | Luiz Gabriel de Oliveira Ferreira |
| 6924106421 | Yahn de Freitas Santos |
| 6924106679 | Davi dos Santos |

## 1. Introdução

Trabalho do Desafio Modular da disciplina **Computação em Nuvem e Orquestração com Kubernetes**, envolvendo uma aplicação Flask, Docker, Docker Hub e Amazon EKS.

## 2. Objetivo

Demonstrar o fluxo **Aplicação → Docker → Docker Hub → Amazon EKS → Deployment → Service → Acesso externo**, incluindo configuração por variáveis de ambiente, execução de duas réplicas e recuperação automática após a exclusão de um Pod.

## 3. Aplicação desenvolvida

A API **Materiais Hospitalares** usa Python e Flask e escuta na porta 5000. `GET /` retorna o nome da aplicação, o status, o ambiente e a indicação de Secret configurado. `GET /health` retorna `{"status":"ok"}`.

A variável `AMBIENTE` tem padrão `local` e recebe `demonstracao` pelo ConfigMap no EKS. `APP_SECRET` é recebido em tempo de execução; seu conteúdo não é exposto pelas respostas. Os manifestos locais contêm somente um valor fictício de demonstração.

## 4. Docker

O Dockerfile usa `python:3.12-slim`, instala as dependências de `app/requirements.txt` e inicia a aplicação com `python app.py`. A imagem local é `desafio-kubernetes:v1`.

O build e a execução local foram concluídos manualmente. Os comandos e as respostas locais estão no README; a captura [03-docker-images-ps-push.png](evidencias/03-docker-images-ps-push.png) mostra a imagem resultante e o container em execução. As saídas próprias de build e run ainda não foram fornecidas como capturas.

## 5. Docker Hub

A imagem foi publicada como **`luidyon/desafio-kubernetes:v1`**, no repositório público `luidyon/desafio-kubernetes`, tag `v1`. A publicação está documentada na captura do terminal e em [04-docker-hub-v1.png](evidencias/04-docker-hub-v1.png). Não houve novo push nesta execução.

## 6. Amazon EKS

| Item | Resultado verificado |
|---|---|
| Cluster | `desafio-kubernetes`, `ACTIVE` |
| Região | `us-east-1` |
| Node group | `workers` |
| Node | `ip-192-168-33-60.ec2.internal`, `Ready` |
| Quantidade e tipo | 1 node `t3.small` |
| Namespace | `default` |
| Autenticação | AWS CLI autenticada como `desafio-kubernetes-admin`; conta omitida |
| kubectl | Contexto do cluster confirmado e consultas executadas com sucesso |

A infraestrutura já havia sido provisionada pelo autor. Nesta execução, foram realizadas consultas de estado e validações. A seção 1 e a seção 8 da evidência textual registram o node e a confirmação final do cluster.

Usar o diagrama Mermaid do README, que representa a arquitetura implantada. O AWS Load Balancer encaminha ao Service, que seleciona os Pods gerenciados pelo Deployment. O Deployment define as réplicas e não atua como intermediário HTTP.

## 7. Deployment e réplicas

O Deployment `materiais-app` referencia `luidyon/desafio-kubernetes:v1` e define `replicas: 2`. Foi encontrado e confirmado ao final com **READY 2/2** e **AVAILABLE 2**.

Os Pods finais eram:

- `materiais-app-86c5fbbcc9-prtkp` — `1/1 Running`, IP `192.168.60.154`.
- `materiais-app-86c5fbbcc9-r4s2l` — `1/1 Running`, IP `192.168.60.179`.

Ambos estavam no único node do cluster. Nomes e IPs são os observados na coleta e podem mudar em execuções posteriores.

## 8. ConfigMap e Secret

O ConfigMap `materiais-config` e o Secret `materiais-secret` foram encontrados no namespace `default`. O Secret foi listado somente por metadados, sem consulta ao seu conteúdo.

A execução de comandos dentro do container confirmou `AMBIENTE=demonstracao` e `APP_SECRET=configurado`. A validação foi repetida individualmente nos dois Pods finais, incluindo o novo Pod. As seções 2 e 8 da evidência textual registram essas verificações sem imprimir o valor do Secret.

## 9. Service LoadBalancer

O Service `materiais-service` é do tipo **LoadBalancer**, seleciona `app: materiais-app` e expõe a porta **80**, direcionada à porta **5000** dos Pods. O hostname foi obtido diretamente do estado do Service:

```text
a22cf95f8f7a14db285c7655db7b1447-1519761716.us-east-1.elb.amazonaws.com
```

Após o self-healing, o EndpointSlice registrou `192.168.60.154` e `192.168.60.179`, ambos na porta 5000. A atualização substituiu o endpoint do Pod excluído.

## 10. Acesso externo

As consultas externas antes e depois do self-healing retornaram **HTTP 200 OK** para ambos os endpoints.

`GET /`:

```json
{
  "ambiente": "demonstracao",
  "aplicacao": "Materiais Hospitalares",
  "secret_configurado": true,
  "status": "online"
}
```

`GET /health`:

```json
{
  "status": "ok"
}
```

As seções 5 e 6 da evidência textual contêm a primeira validação, e a seção 8 contém a repetição após a recuperação. O endereço foi consultado no Kubernetes, sem assumir um hostname fixo.

## 11. Recuperação automática

O teste começou às **16:58:12 (UTC−03:00)**. Foram confirmados dois Pods `1/1 Running` e sua propriedade pelo ReplicaSet do Deployment `materiais-app`.

| Etapa | Registro real |
|---|---|
| Antes | `materiais-app-86c5fbbcc9-mpvpb` e `materiais-app-86c5fbbcc9-r4s2l` |
| Único Pod excluído | `materiais-app-86c5fbbcc9-mpvpb` |
| Pod preservado | `materiais-app-86c5fbbcc9-r4s2l` |
| Novo Pod | `materiais-app-86c5fbbcc9-prtkp` |
| Dois Pods ativos prontos observados | Aproximadamente 4,6 segundos após iniciar a exclusão |
| Exatamente dois Pods totais, sem o excluído | Aproximadamente 34,2 segundos após iniciar a exclusão |
| Estado final | Deployment `2/2`, `AVAILABLE 2`; dois Pods `1/1 Running` |

O Pod excluído permaneceu brevemente como `Terminating` enquanto o substituto já estava pronto. Os tempos incluem a latência das consultas e esperas de 2 segundos; são aproximações da observação, não medidas exatas da transição.

O comportamento ocorreu porque `replicas: 2` define o estado desejado. O ReplicaSet gerenciado pelo Deployment criou outro Pod para recompor essa quantidade. Somente um Pod foi excluído, sem alteração de Deployment, réplicas ou YAMLs. O registro completo está na seção 7 da evidência textual.

## 12. Dificuldades encontradas

**Dificuldades reais relatadas pelo autor**, sem atribuir detalhes que não foram registrados:

- Configuração inicial do Docker Desktop/WSL2.
- Autenticação da AWS CLI.
- Preparação do IAM.
- Tempo de provisionamento do EKS.
- Pequeno intervalo até o Load Balancer responder externamente.

## 13. Aprendizados

A execução demonstrou o uso da mesma imagem publicada no Docker Hub pelo Deployment, a separação da configuração em ConfigMap e Secret, a associação do Service aos Pods por labels e a reposição automática de uma réplica excluída.

Também permitiu distinguir a presença de dois Pods no mesmo node da tolerância a falhas de nodes, e a prontidão do substituto do encerramento completo do Pod anterior.

## 14. Custos e cuidados

**Limpeza AWS concluída.** Após os testes, `eksctl delete cluster` terminou com `all cluster resources were deleted`; `eksctl get cluster --region us-east-1` retornou `No clusters found`. Não restaram EC2, Classic Load Balancers ou ELBv2. A Access Key temporária e o usuário/perfil IAM temporário do laboratório foram removidos.

O encerramento e a remoção dos recursos foram conferidos após os testes. Nenhum valor de custo foi necessário para a comprovação da limpeza.

Os recursos removidos e a conferência de recursos remanescentes estão registrados acima.

As evidências não contêm Access Keys, senhas ou o conteúdo do Secret. O identificador da conta na verificação de identidade foi mascarado como `<ACCOUNT_ID>`.

## 15. Limitações

- Aplicação didática, sem regras de negócio nem persistência de dados.
- Um único node hospeda as duas réplicas; o exercício não demonstra recuperação de falha desse node.
- Foram feitos testes pontuais de HTTP e exclusão de um Pod, sem ensaio de carga ou medição contínua de disponibilidade.
- Os testes HTTP externos e o self-healing têm comprovação textual real, sem capturas próprias; foram apresentados nesse formato no PDF.
- O custo financeiro detalhado não foi quantificado neste relatório.

## 16. Conclusão

As validações técnicas demonstraram o fluxo da aplicação local até o acesso externo no Amazon EKS, com duas réplicas, configurações recebidas pelos Pods e substituição automática de um Pod excluído. Ambos os endpoints responderam HTTP 200 antes e depois desse teste.

A entrega acadêmica está consolidada no PDF com as evidências existentes, e a limpeza AWS foi concluída após os testes.

## 17. Evidências e conferência

- [Índice de evidências](evidencias/README.md): oito capturas originais analisadas e mapeadas aos anexos.
- [Registro textual da Fase 3](evidencias/fase3-comandos.txt): consultas, status HTTP, configurações, self-healing e estado final, preservados sem alteração.
- [Conferência dos critérios](conferencia-criterios.md): fonte de comprovação e situação de cada requisito.
- [PDF acadêmico](../entrega/Desafio_Kubernetes.pdf): entrega principal com legendas, arquitetura e discussão objetiva.
- [README principal](../README.md): comandos e checklist atualizado.

As capturas 05 e 07 foram descritas pelo que efetivamente mostram: a primeira comprova o cluster ACTIVE; a segunda comprova variáveis nos Pods. Node Ready e existência dos objetos ConfigMap/Secret estão comprovados no registro textual. Não foram criadas, recriadas ou simuladas capturas.
