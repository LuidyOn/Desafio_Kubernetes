import os

from flask import Flask, jsonify

app = Flask(__name__)

# Configurações recebidas por variáveis de ambiente.
# AMBIENTE vem do ConfigMap; APP_SECRET vem do Secret (valor fictício).
AMBIENTE = os.environ.get("AMBIENTE", "local")
APP_SECRET = os.environ.get("APP_SECRET")


@app.route("/")
def index():
    return jsonify(
        {
            "aplicacao": "Materiais Hospitalares",
            "status": "online",
            "ambiente": AMBIENTE,
            # Nunca expor o valor do segredo, apenas se ele foi configurado.
            "secret_configurado": APP_SECRET is not None,
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # 0.0.0.0 permite acesso de fora do container.
    app.run(host="0.0.0.0", port=5000)
