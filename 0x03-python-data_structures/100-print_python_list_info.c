#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: Python object (list)
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *listobj;
	int j;

	if (!p)
		return;
	listobj = (PyListObject *) p;
	printf("[*] Size of the Python List = %d\n", (int)PyList_Size(p));
	printf("[*] Allocated = %d\n", (int)listobj->allocated);
	for (j = 0; j < Py_SIZE(p); j++)
		printf("Element %d: %s\n", j, listobj->ob_item[j]->ob_type->tp_name);
}
