# Conferência dos critérios da entrega acadêmica

Documento principal: [Desafio_Kubernetes.pdf](../entrega/Desafio_Kubernetes.pdf), com 7 páginas de conteúdo e 4 de anexos. Identificação: Universidade Salesiano Espírito Santo; Luiz Gabriel de Oliveira Ferreira (6924106557), Yahn de Freitas Santos (6924106421) e Davi dos Santos (6924106679).

A conferência considera os critérios informados na solicitação da atividade. O repositório não contém uma cópia separada do enunciado integral com pesos ou rubrica adicional; portanto, não se presume uma pontuação não fornecida.

| Critério | Comprovação real | Cobertura no PDF | Situação |
|---|---|---|---|
| Aplicação e teste local | app/app.py e capturas 01/02: endpoints e corpos JSON | p. 1; anexo A | Comprovado com ressalva: HTTP 200 local sem cabeçalhos visíveis |
| Docker: build, imagem e run | Captura 03: imagem, container e porta publicada; README registra build/run | p. 2; anexo B | Comprovado com ressalva: saídas integrais de build/run ausentes |
| Docker Hub | Capturas 03/04: push concluído, repositório e tag v1 | p. 2; anexos A/B | Comprovado |
| Amazon EKS e node Ready | Captura 05: ACTIVE; fase3-comandos.txt, seções 1/8: node Ready, tipo e grupo | p. 3; anexo B | Comprovado |
| Deployment com duas réplicas | Captura 06 e registro textual: 2/2, AVAILABLE 2 e dois Pods Running | p. 3 e 5; anexo C | Comprovado |
| ConfigMap e Secret | Manifestos; registro seção 2: existência; captura 07 e seção 8: variáveis nos dois Pods | p. 4; anexo C | Comprovado sem exposição do segredo |
| Service LoadBalancer | Captura 08 e registro seções 4/8: tipo, hostname, portas e endpoints | p. 4; anexo D | Comprovado |
| Acesso externo GET / | Registro seções 5/8: HTTP 200 e JSON antes/depois do teste | p. 4 | Comprovado por saída real |
| Acesso externo GET /health | Registro seções 6/8: HTTP 200 e status ok antes/depois | p. 4 | Comprovado por saída real |
| Recuperação automática | Registro seção 7: nomes antes, exclusão única, novo Pod, tempos e estado final | p. 5 | Comprovado por documentação textual, sem screenshots artificiais |
| Arquitetura | Manifestos e recursos observados; diagrama explicativo no PDF | p. 3 | Documentado |
| Dificuldades | Relatos registrados da atividade, sem causas ou soluções inventadas | p. 6 | Documentado como relato |
| Aprendizados | Análise dos conceitos demonstrados pela execução | p. 6 | Documentado |
| Custos e cuidados | Encerramento após os testes e conferência da remoção registrados | p. 6 | Comprovado |
| Limpeza dos recursos | `eksctl delete cluster` concluído; nenhum cluster, EC2 ou Load Balancer remanescente; credenciais temporárias removidas | p. 6/7 | Concluído |
| Conclusão e limitações | Síntese sustentada pelos resultados e ressalvas | p. 6 | Documentado |

## Itens ainda não comprovados diretamente

1. Saídas integrais dos comandos docker build e docker run, embora seus resultados estejam visíveis na captura 03.
2. Cabeçalhos HTTP 200 dos testes locais anteriores; as capturas comprovam os corpos JSON e o acesso local.
3. Valor financeiro detalhado dos custos AWS não foi quantificado neste relatório.

Os resultados técnicos de HTTP externo e self-healing estão comprovados no arquivo de comandos. A falta de screenshots próprios não foi tratada como falha desses testes, pois a entrega aceita documentação textual real.

## Preservação das evidências e backup

As oito imagens e fase3-comandos.txt foram mantidos sem alteração de conteúdo. O ZIP de backup inclui o PDF, app/, Dockerfile, os quatro YAMLs e a documentação com as evidências originais. Foram excluídos metadados Git, ambientes virtuais, caches, arquivos temporários, kubeconfig e credenciais reais. O manifesto k8s/secret.yaml usa exclusivamente o valor fictício de demonstração.

**Recursos AWS foram removidos após os testes.** Nenhum commit ou push foi executado na preparação da entrega.
