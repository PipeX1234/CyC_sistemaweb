$("#idPresupuesto").validate(
    { 
        "rules": 
            {
                "nombreCliente":
                    {
                        required: true,
                        minlength: 2,
                        maxlength: 150
                    },
                "telefonoCliente":
                    {
                        required: true,
                        maxlength: 9,
                        minlength: 9
                    },
                "correoCliente":
                    {
                        required: true,
                        maxlength: 150,
                        email: true
                    },
                "direccionCliente": 
                    {
                        required: true,
                        minlength: 10,
                        maxlength: 300
                    },
                "descripcionPresupuesto":
                    {
                        required: true,
                        minlength: 20,
                        maxlength: 500
                    }
            }, // --> Fin de reglas
        messages: 
            {
                "nombreCliente":
                {
                    required: 'Este es un campo obligatorio',
                    minlength: 'Debe ingresar un nombre válido',
                    maxlength: 'Debe ingresar un nombre válido'
                },
                "telefonoCliente":
                {
                    required: 'Este es un campo obligatorio',
                    maxlength: 'Ingrese su número telefónico agregando el 9',
                    minlength: 'Ingrese su número telefónico agregando el 9'
                },
                "correoCliente":
                {
                    required: 'Este es un campo obligatorio',
                    maxlength: 'Debe ingresar un correo que contenga como máximo 150 letras',
                    email: 'Debe ingresar un correo en formato válido'
                },
                "direccionCliente": 
                {
                    required: 'Este es un campo obligatorio',
                    minlength: 'Debe ingresar su dirección con un mínimo de 10 letras',
                    maxlength: 'Debe ingresar su dirección con un máximo de 300 letras'
                },
                "descripcionPresupuesto":
                {
                    required: 'Este es un campo obligatorio',
                    minlength: 'Debe ingresar una descripción más larga, intente explayarse más',
                    maxlength: 'Debe ingresar la descripción en menos de 500 caracteres'
                }
            },
    }
);



$("#idLogin").validate(
    { 
        "rules": 
            {
                "txtEmail": 
                    {
                        required: true,
                        email: true,
                        minlength:1
                    },
                "txtContrasena":
                    {
                        required: true,
                        minlength: 8
                    }
            }, // --> Fin de reglas
        messages: 
            {
                "txtEmail": 
                    {
                        required: 'El email es un campo requerido',
                        email: 'El email no cumple el formato de un correo',
                        minlength: 'Debe tener como mínimo 1 caracteres'
                    },
                "txtContrasena":
                    {
                        required: 'Debe ingresar su contraseña',
                        minlength: 'Debe tener como mínimo 8 caracteres'
                    }
            },
    }
);