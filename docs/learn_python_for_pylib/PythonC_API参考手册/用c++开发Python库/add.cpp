#include <Python.h>

// 定义一个Python函数
static PyObject* add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong((long)(a + b));
}

// 模块方法初始化表
static PyMethodDef AddMethods[] = {
    {"add", add, METH_VARARGS, "Adds two integers"},
    {NULL, NULL, 0, NULL}
};

// 模块定义
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "add_module",       // Name of module
    NULL,               // Docstring of module (can be NULL)
    -1,                 // Size of per-interpreter state of the module, or -1 if the module keeps state in global variables only.
    AddMethods,         // Method table
};

// Initialization function for the module
PyMODINIT_FUNC PyInit_add_module(void) {
    return PyModule_Create(&moduledef);
}