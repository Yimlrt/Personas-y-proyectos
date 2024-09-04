from flask import Flask, jsonify, request, abort

app = Flask(__name__)



# Datos simulados para las entidades
personas = [
    {'id': 1, 'nombre': 'Juan', 'edad': 30},
    {'id': 2, 'nombre': 'Ana', 'edad': 25}
]

proyectos = [
    {'id': 1, 'nombre': 'Proyecto A', 'presupuesto': 1000},
    {'id': 2, 'nombre': 'Proyecto B', 'presupuesto': 2000}
]

# Funciones auxiliares
def find_persona(persona_id):
    for persona in personas:
        if persona['id'] == persona_id:
            return persona
    return None

def find_proyecto(proyecto_id):
    for proyecto in proyectos:
        if proyecto['id'] == proyecto_id:
            return proyecto
    return None

# Rutas para Personas
@app.route('/personas', methods=['GET'])
def get_personas():
    return jsonify({'personas': personas})

@app.route('/personas/<int:persona_id>', methods=['GET'])
def get_persona(persona_id):
    persona = find_persona(persona_id)
    if persona is None:
        abort(404)
    return jsonify(persona)

@app.route('/personas', methods=['POST'])
def create_persona():
    if not request.json or 'nombre' not in request.json or 'edad' not in request.json:
        abort(400)
    persona = {
        'id': personas[-1]['id'] + 1 if personas else 1,
        'nombre': request.json['nombre'],
        'edad': request.json['edad']
    }
    personas.append(persona)
    return jsonify(persona), 201

@app.route('/personas/<int:persona_id>', methods=['PUT'])
def update_persona(persona_id):
    persona = find_persona(persona_id)
    if persona is None:
        abort(404)
    if not request.json:
        abort(400)
    persona['nombre'] = request.json.get('nombre', persona['nombre'])
    persona['edad'] = request.json.get('edad', persona['edad'])
    return jsonify(persona)

@app.route('/personas/<int:persona_id>', methods=['DELETE'])
def delete_persona(persona_id):
    persona = find_persona(persona_id)
    if persona is None:
        abort(404)
    personas.remove(persona)
    return jsonify({'result': True})

# Rutas para Proyectos
@app.route('/proyectos', methods=['GET'])
def get_proyectos():
    return jsonify({'proyectos': proyectos})

@app.route('/proyectos/<int:proyecto_id>', methods=['GET'])
def get_proyecto(proyecto_id):
    proyecto = find_proyecto(proyecto_id)
    if proyecto is None:
        abort(404)
    return jsonify(proyecto)

@app.route('/proyectos', methods=['POST'])
def create_proyecto():
    if not request.json or 'nombre' not in request.json or 'presupuesto' not in request.json:
        abort(400)
    proyecto = {
        'id': proyectos[-1]['id'] + 1 if proyectos else 1,
        'nombre': request.json['nombre'],
        'presupuesto': request.json['presupuesto']
    }
    proyectos.append(proyecto)
    return jsonify(proyecto), 201

@app.route('/proyectos/<int:proyecto_id>', methods=['PUT'])
def update_proyecto(proyecto_id):
    proyecto = find_proyecto(proyecto_id)
    if proyecto is None:
        abort(404)
    if not request.json:
        abort(400)
    proyecto['nombre'] = request.json.get('nombre', proyecto['nombre'])
    proyecto['presupuesto'] = request.json.get('presupuesto', proyecto['presupuesto'])
    return jsonify(proyecto)

@app.route('/proyectos/<int:proyecto_id>', methods=['DELETE'])
def delete_proyecto(proyecto_id):
    proyecto = find_proyecto(proyecto_id)
    if proyecto is None:
        abort(404)
    proyectos.remove(proyecto)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
