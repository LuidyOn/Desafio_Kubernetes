# Evidências analisadas e incorporadas à entrega

As oito capturas originais e o arquivo `fase3-comandos.txt` foram analisados. O [PDF acadêmico](../../entrega/Desafio_Kubernetes.pdf) contém 7 páginas de conteúdo e 4 páginas de anexos. Cada imagem é reproduzida uma única vez; HTTP externo e self-healing são documentados por saídas de comandos reais, sem screenshots artificiais.

## Capturas reais disponíveis

| Fonte | Arquivo | Conteúdo efetivamente visível | Local no PDF |
|---|---|---|---|
| E1 | [01-aplicacao-local.png](01-aplicacao-local.png) | GET / em localhost:5000; ambiente local, aplicação online e Secret configurado | Anexo A, figura A1, p. 8 |
| E2 | [02-health-check.png](02-health-check.png) | GET /health local com status: ok | Anexo A, figura A2, p. 8 |
| E3 | [03-docker-images-ps-push.png](03-docker-images-ps-push.png) | Imagem, container em execução, porta publicada, tag e push concluído | Anexo B, figura B1, p. 9 |
| E4 | [04-docker-hub-v1.png](04-docker-hub-v1.png) | Repositório luidyon/desafio-kubernetes com tag v1 | Anexo A, figura A3, p. 8 |
| E5 | [05-eks-node-ready.png](05-eks-node-ready.png) | DescribeCluster: desafio-kubernetes ACTIVE; não mostra o node Ready | Anexo B, figura B2, p. 9 |
| E6 | [06-deployment-dois-pods.png](06-deployment-dois-pods.png) | Deployment 2/2, AVAILABLE 2 e dois Pods 1/1 Running | Anexo C, figura C1, p. 10 |
| E7 | [07-configmap-secret-pods.png](07-configmap-secret-pods.png) | AMBIENTE=demonstracao e APP_SECRET=configurado nos dois Pods, sem conteúdo do segredo | Anexo C, figura C2, p. 10 |
| E8 | [08-loadbalancer.png](08-loadbalancer.png) | Service LoadBalancer, hostname, porta 80, targetPort 5000 e endpoints finais | Anexo D, figura D1, p. 11 |

Os nomes dos arquivos foram preservados. As legendas descrevem o conteúdo real, inclusive quando o nome sugere mais do que a imagem mostra. Nenhuma captura foi editada ou simulada.

## Registro textual real

O arquivo [fase3-comandos.txt](fase3-comandos.txt) foi preservado integralmente. Ele registra a validação de 07/09/2026, entre 16:54 e 17:00 (UTC-03:00):

1. Node Ready, tipo t3.small e node group workers.
2. Existência de ConfigMap/Secret e validação segura das variáveis.
3. Deployment e Pods no estado inicial.
4. Service, hostname, portas e endpoints iniciais.
5. GET / externo: HTTP 200 e JSON.
6. GET /health externo: HTTP 200 e JSON.
7. Self-healing: dois Pods antes, exclusão única, substituto e tempos de recuperação.
8. Estado final, autenticação/cluster, dois Pods, endpoints atualizados, variáveis e repetição dos testes HTTP.

O PDF apresenta os resultados HTTP na página 4 e os excertos literais do self-healing na página 5. O antes/depois está documentado como texto, sem criar uma captura de terminal. A observação histórica de documentação pendente no final do arquivo permanece intacta; essa pendência foi resolvida com a presente consolidação.

## Limites da comprovação

- Os cabeçalhos HTTP 200 locais não aparecem nas capturas; o status consta do histórico informado.
- Não há saídas integrais próprias de docker build e docker run; a imagem resultante e o container são visíveis em E3.
- Node Ready e existência dos objetos ConfigMap/Secret estão comprovados no registro textual, não nas capturas E5/E7.
- HTTP externo e self-healing têm comprovação textual; não dependem de imagens inexistentes nesta entrega.
- Limpeza AWS concluída após os testes: `eksctl delete cluster` terminou com `all cluster resources were deleted`; `eksctl get cluster --region us-east-1` retornou `No clusters found`; não restaram EC2, Classic Load Balancers ou ELBv2; Access Key e usuário/perfil IAM temporários foram removidos.

Consultar a [conferência dos critérios](../conferencia-criterios.md) para o mapeamento completo e o [README principal](../../README.md) para os comandos e o estado documentado.

**Recursos AWS foram removidos após os testes.**
