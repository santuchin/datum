#include <Python.h>

// Función que suma dos enteros
static PyObject* suma(PyObject *self, PyObject *args) {
    
    int a, b;

    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;

    return PyLong_FromLong(a + b);
}

// Tabla de métodos del módulo
static PyMethodDef ModuleMethods[] = {
    {"suma", suma, METH_VARARGS, "Suma dos enteros."},
    {NULL, NULL, 0, NULL}
};

// Definición del módulo
static struct PyModuleDef mimodulomodule = {
    PyModuleDef_HEAD_INIT,
    "datum",  // nombre del módulo
    NULL,        // documentación
    -1,          // estado del módulo
    ModuleMethods
};

// Inicialización del módulo
PyMODINIT_FUNC PyInit_mimodulo(void) {
    return PyModule_Create(&mimodulomodule);
}
