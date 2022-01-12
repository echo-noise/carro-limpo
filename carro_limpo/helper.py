ADD = "Adicionar: "
EDIT = "Editar: "
DELETE = "Deletar: "
SUCCESS = "sucesso"
FAIL = "erro"

def default_response(obj, msg):
    return  { 
                "id": obj.id,
                "error": False,
                "message": msg + SUCCESS
            }

def error_response(form_errors, msg):
    error_string = ' '.join([' '.join(x for x in l) for l in list(form_errors.values())])
    return {
        "error": True,
        "message": msg + FAIL,
        "user_alert": error_string
    }