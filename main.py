from webScrapingAndProcess import choice
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/processNaturalLanguage/LowestPrice', methods=['POST'])
def pnllp():
    try:
        data = request.json
        res = choice(data["product"], data["option"])
        return jsonify(res), 200  # Retornar a resposta da função choice()
    except Exception as e:
        # Em caso de erro, retorne uma resposta de erro com uma mensagem explicativa
        error_message = str(e)
        return jsonify({'error': error_message}), 500

# def main():
#     product = str(input("Digite o produto que deseja procurar: "))
#     print("Você deseja o maior custo benefício (Usamos IA para te ajudar!) ou menor preço ? ")
#     option = int(input("Digite 0 para Custo Benefício ou 1 para Menor preço: "))
#     choice(product, option)

if __name__ == '__main__':
    app.run(debug=True)
