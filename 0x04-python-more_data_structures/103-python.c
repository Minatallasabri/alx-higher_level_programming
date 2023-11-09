#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyObject_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("  Size of the Python List = %ld\n", size);
    printf("  Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("  Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyObject_Size(p);
    Py_ssize_t i;

    printf("[*] Python bytes info\n");
    printf("  Size of the bytes: %ld\n", size);
    printf("  First %ld bytes: ", size > 10 ? 10 : size);

    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
        if (i < size - 1 && i < 9) {
            printf(" ");
        }
    }

    printf("\n");
}

int main(void) {
    Py_Initialize();

    PyObject *list = Py_BuildValue("[isO]", 1, "hello", Py_None);
    print_python_list(list);

    PyObject *bytes = Py_BuildValue("y", "example bytes");
    print_python_bytes(bytes);

    Py_Finalize();

    return 0;
}

