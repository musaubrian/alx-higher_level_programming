#include <Python.h>

/**
 * print_python-list_info - prints infomation about a python list
 *
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, idx;
	PyObject *obj;

	size = Py_SIZE(P);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (idx = 0; idx < size; idx++)
	{
		printf("Element %d: ", idx);

		obj = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
