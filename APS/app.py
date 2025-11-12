from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    carbonoEletricidade = "0"
    carbonoGasolina = "0"
    carbonoDiesel = "0"
    carbonoGasNatural = "0"
    carbonoOnibus = "0"
    carbonoMetro = "0"
    carbonoTotal = "0"

    if request.method == "POST":
        # Obter valores do formulário (com tratamento para campos vazios)
        eletricidade = float(request.form.get("eletricidade") or 0)
        carbonoEletricidade = eletricidade * 0.233

        gasolina = float(request.form.get("gasolina") or 0)
        carbonoGasolina = gasolina * 2.31

        diesel = float(request.form.get("diesel") or 0)
        carbonoDiesel = diesel * 2.68

        gasNatural = float(request.form.get("gasNatural") or 0)
        carbonoGasNatural = gasNatural * 2.03

        onibus = float(request.form.get("onibus") or 0)
        carbonoOnibus = onibus * 0.105

        metro = float(request.form.get("metro") or 0)
        carbonoMetro = metro * 0.056

        carbonoTotal = (carbonoEletricidade + carbonoGasolina + carbonoDiesel + 
                       carbonoGasNatural + carbonoOnibus + carbonoMetro)

        # Formatar todos os valores para 2 casas decimais
        carbonoEletricidade = f"{carbonoEletricidade:.3f}"
        carbonoGasolina = f"{carbonoGasolina:.3f}"
        carbonoDiesel = f"{carbonoDiesel:.3f}"
        carbonoGasNatural = f"{carbonoGasNatural:.3f}"
        carbonoOnibus = f"{carbonoOnibus:.3f}"
        carbonoMetro = f"{carbonoMetro:.3f}"
        carbonoTotal = f"{carbonoTotal:.3f}"

    return render_template("index.html", 
                         carbonoEletricidade=carbonoEletricidade, 
                         carbonoGasolina=carbonoGasolina, 
                         carbonoDiesel=carbonoDiesel, 
                         carbonoGasNatural=carbonoGasNatural, 
                         carbonoOnibus=carbonoOnibus, 
                         carbonoMetro=carbonoMetro, 
                         carbonoTotal=carbonoTotal)

if __name__ == "__main__":
    app.run(debug=True)