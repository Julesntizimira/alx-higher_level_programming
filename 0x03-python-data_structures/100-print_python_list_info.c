#include <Python.h>
/**
 * print_python_list_info - basic info of lists.
 * @p: PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size;
	int alloc;
	int i = 0;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	while (i < size)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		i++;
	}
}
