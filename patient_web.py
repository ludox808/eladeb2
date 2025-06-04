from flask import Flask, request, render_template_string

app = Flask(__name__)

DOMAINS = [
    "Lieu de vie", "Finances", "Travail", "Droit & justice",
    "Temps libre", "Tâches administratives", "Entretien du ménage", "Déplacements",
    "Fréquentation des lieux publics", "Connaissances et amitiés", "Famille",
    "Enfants", "Relations sentimentales", "Alimentation", "Hygiène personnelle",
    "Santé physique", "Santé psychique", "Addiction", "Traitement",
    "Spiritualité & croyances", "Sexualité"
]

FORM_HTML = """
<!doctype html>
<title>ELADEB-R Web</title>
<h1>Auto-évaluation ELADEB-R</h1>
<form method=post>
<p>Quel est pour vous le problème le plus important actuellement ?<br>
<input type=text name=free_question required></p>
<h2>Difficultés</h2>
{% for name in domains %}
<label>{{name}}</label>
<select name="diff_{{loop.index0}}">
<option value=0>Aucun</option>
<option value=1>Peu important</option>
<option value=2>Important</option>
<option value=3>Très important</option>
</select><br>
{% endfor %}
<h2>Besoins d'aide supplémentaire</h2>
{% for name in domains %}
<label>{{name}}</label>
<select name="need_{{loop.index0}}">
<option value=0>Aucun</option>
<option value=1>Non urgent (&gt;3 mois)</option>
<option value=2>Moyennement urgent (1-3 mois)</option>
<option value=3>Urgent (&lt;30 jours)</option>
</select>
Origine (P/F/E/?)<input type=text name="orig_{{loop.index0}}" size=1><br>
{% endfor %}
<p>Si on ne pouvait faire qu’une seule chose pour vous, laquelle choisiriez-vous ?<br>
<input type=text name=priority required></p>
<input type=submit value="Envoyer">
</form>
"""

RESULT_HTML = """
<!doctype html>
<title>ELADEB-R Résultats</title>
<h1>Résultats</h1>
<p>Réponse initiale : {{free_question}}</p>
<table border=1>
<tr><th>Domaine</th><th>Difficulté</th><th>Besoin</th><th>Origine</th></tr>
{% for row in rows %}
<tr><td>{{row.name}}</td><td>{{row.diff}}</td><td>{{row.need}}</td><td>{{row.orig}}</td></tr>
{% endfor %}
</table>
<p>Besoin prioritaire : {{priority}}</p>
<p>Score total difficultés : {{total_diff}}</p>
<p>Score total besoins : {{total_need}}</p>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        free_question = request.form['free_question']
        priority = request.form['priority']
        rows = []
        total_diff = 0
        total_need = 0
        for i, name in enumerate(DOMAINS):
            diff = int(request.form.get(f'diff_{i}', 0))
            need = int(request.form.get(f'need_{i}', 0))
            orig = request.form.get(f'orig_{i}', '')
            rows.append({'name': name, 'diff': diff, 'need': need, 'orig': orig})
            total_diff += diff
            total_need += need
        return render_template_string(RESULT_HTML, free_question=free_question,
                                      priority=priority, rows=rows,
                                      total_diff=total_diff, total_need=total_need)
    return render_template_string(FORM_HTML, domains=DOMAINS)

if __name__ == '__main__':
    app.run(debug=True)
