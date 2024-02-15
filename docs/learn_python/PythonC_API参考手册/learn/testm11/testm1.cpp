#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* my_add(PyObject* self, PyObject* args) {
    int x, y;
    if (!PyArg_ParseTuple(args, "ii", &x, &y)) {
        return NULL;
    }
    return PyLong_FromLong(x + y);
}

PyMODINIT_FUNC initmy_module(void) {
    static struct PyMethodDef my_methods[] = {
        {"add", my_add, METH_VARARGS, "Add two numbers"},
        {NULL, NULL, 0, NULL}
    };
    static struct PyModuleDef my_module = {
        PyModuleDef_HEAD_INIT,
        "my_module",
        NULL,
        -1,
        my_methods,
        NULL,
        NULL,
        NULL,
        NULL
    };
    return PyModule_Create(&my_module);
}