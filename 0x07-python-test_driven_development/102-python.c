#include <Python.h>
#include <object.h>
#include <unicodeobject.h>
#include <stdio.h>

/**
 * print_python_string - Print a python string.
 * @p: Python string as PyObject type
 */
void print_python_string(PyObject *p)
{
	char *type;
	wchar_t *str;
	Py_ssize_t len = 0;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	else
		type = "compact unicode object";

	str = PyUnicode_AsWideCharString(p, &len);

	printf("  type: %s\n", type);
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", str);
}
