from flask import Flask, request, render_template
from Arbol import Nodo
from DFS_rec import buscar_solucion_dfs_rec
from BFS import buscar_solucion_BFS
from DFS import buscar_solucion_DFS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        
        estado_inicial = list(map(int, request.form['estado_inicial'].split(',')))
        solucion = list(map(int, request.form['solucion'].split(',')))
    except ValueError:
        return "Los valores de 'estado_inicial' y 'solucion' deben ser números separados por comas.", 400

    resultados = {}

    resultado_dfs = []
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_dfs = buscar_solucion_dfs_rec(nodo_inicial, solucion, visitados)
    if nodo_dfs:
        nodo_actual = nodo_dfs
        while nodo_actual.get_padre() is not None:
            resultado_dfs.append(nodo_actual.get_datos())
            nodo_actual = nodo_actual.get_padre()
        resultado_dfs.append(nodo_actual.get_datos())
        resultado_dfs.reverse()
    resultados['DFS_recursivo'] = resultado_dfs

    resultado_BFS = []
    nodo_puzzle = buscar_solucion_BFS(estado_inicial, solucion)
    if nodo_puzzle:
        nodo_actual = nodo_puzzle
        while nodo_actual.get_padre() is not None:
            resultado_BFS.append(nodo_actual.get_datos())
            nodo_actual = nodo_actual.get_padre()
        resultado_BFS.append(nodo_actual.get_datos())
        resultado_BFS.reverse()
    resultados['BFS'] = resultado_BFS

    resultado_DFS = []
    nodo_puzzle1 = buscar_solucion_DFS(estado_inicial, solucion)
    if nodo_puzzle1:
        nodo_actual = nodo_puzzle1
        while nodo_actual.get_padre() is not None:
            resultado_DFS.append(nodo_actual.get_datos())
            nodo_actual = nodo_actual.get_padre()
        resultado_DFS.append(nodo_actual.get_datos())
        resultado_DFS.reverse()
    resultados['DFS'] = resultado_DFS

    return render_template('index.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)